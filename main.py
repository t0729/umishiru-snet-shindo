import time
import threading
from flask import Flask, jsonify
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

# 初期化
URL = "https://www.msil.go.jp/msil/htm/main.html?centerx%3D140.17192920491166%26centery%3D38.990471955010314%26cacheLevel%3D6%26BaseMap%3D1%26VisibleLayers%3Dm293_1_100_1_1%26Lang%3D0%26BaseMap2%3D1%26VisibleLayers2%3D%26active%3D0%26polarId%3D1"
TEMP_PATH = "temp.png"
PIXEL_CSV = "pixels.csv"
SHINDO_CSV = "shindo_colors.csv"
latest_shindo = []

# 座標の読み込み
pixels = []
with open(PIXEL_CSV, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        pixels.append((int(row["x"]), int(row["y"])))

# 震度テーブルの読み込み
shindo_colors = []
with open(SHINDO_CSV, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        val, r, g, b = row
        shindo_colors.append((float(val), (int(r), int(g), int(b))))

# 色から震度へ変換
def rgb_to_shindo(r, g, b):
    min_dist = float("inf")
    best_val = None
    for val, (rr, gg, bb) in shindo_colors:
        dist = ((r-rr)**2 + (g-gg)**2 + (b-bb)**2)**0.5
        if dist < min_dist:
            min_dist = dist
            best_val = val
    return best_val

# スクリーンショットの撮影
def capture_screenshot():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get(URL)
    time.sleep(5)
    driver.save_screenshot(TEMP_PATH)
    driver.quit()

# 自動更新
def update_shindo():
    global latest_shindo
    capture_screenshot()
    img = Image.open(TEMP_PATH).convert("RGB")
    latest_shindo = [rgb_to_shindo(*img.getpixel((x, y))) for x, y in pixels]

    while True:
        now = time.localtime()
        wait_sec = ((60 - now.tm_sec + 10) % 60)
        time.sleep(wait_sec)

        capture_screenshot()
        img = Image.open(TEMP_PATH).convert("RGB")
        latest_shindo = [rgb_to_shindo(*img.getpixel((x, y))) for x, y in pixels]

# Flask
app = Flask(__name__)

@app.route("/shindo")
def get_shindo():
    return jsonify(latest_shindo)

if __name__ == "__main__":
    # バックグラウンドで自動更新を開始
    t = threading.Thread(target=update_shindo, daemon=True)
    t.start()
    # Flask起動
    app.run(port=5000)
