import time
import threading
import requests
from flask import Flask, jsonify
from PIL import Image
import csv

# 設定
QUERY_URL = "https://www.msil.go.jp/arcgis/rest/services/Msil/DisasterPrevImg1/ImageServer/query?f=json&returnGeometry=false&outFields=msilstarttime,msilendtime"
IMAGE_URL = "https://www.msil.go.jp/arcgis/rest/services/Msil/DisasterPrevImg1/ImageServer/exportImage"
TEMP_PATH = "temp.png"
PIXEL_CSV = "pixels.csv"
SHINDO_CSV = "shindo_colors.csv"

latest_shindo = []

# 座標読み込み
pixels = []
with open(PIXEL_CSV, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        pixels.append((int(row["x"]), int(row["y"])))

# 震度テーブル読み込み
shindo_colors = []
with open(SHINDO_CSV, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        val, r, g, b = row
        shindo_colors.append((float(val), (int(r), int(g), int(b))))

def rgb_to_shindo(r, g, b):
    min_dist = float("inf")
    best_val = None
    for val, (rr, gg, bb) in shindo_colors:
        dist = ((r - rr) ** 2 + (g - gg) ** 2 + (b - bb) ** 2) ** 0.5
        if dist < min_dist:
            min_dist = dist
            best_val = val
    return best_val

def fetch_latest_msilstarttime():
    try:
        r = requests.get(QUERY_URL, verify=False, timeout=10)
        r.raise_for_status()
        data = r.json()
        features = data.get("features", [])
        if not features:
            return None
        latest_time = max(
            int(elm["attributes"]["msilstarttime"])
            for elm in features
            if elm["attributes"].get("msilstarttime")
        )
        return latest_time
    except Exception as e:
        print("msilstarttime取得エラー:", e)
        return None

def fetch_image(dateTime):
    params = {
        "f": "image",
        "time": f"{dateTime}%2C{dateTime}",
        "bbox": "13409547.546603577,2713376.239114911,16907305.960932314,5966536.162931148",
        "size": "400,400",
    }
    r = requests.get(IMAGE_URL, params=params, verify=False)
    r.raise_for_status()
    with open(TEMP_PATH, "wb") as f:
        f.write(r.content)

def update_shindo_loop():
    global latest_shindo
    while True:
        dateTime = fetch_latest_msilstarttime()
        if dateTime:
            try:
                fetch_image(dateTime)
                img = Image.open(TEMP_PATH).convert("RGB")
                latest_shindo = [rgb_to_shindo(*img.getpixel((x, y))) for x, y in pixels]
                print("更新成功:", dateTime)
            except Exception as e:
                print("画像取得/解析エラー:", e)
        else:
            print("最新時間取得できず")
        time.sleep(60)  # 1分ごとに更新

# Flask
app = Flask(__name__)

@app.route("/shindo")
def get_shindo():
    return jsonify(latest_shindo)

if __name__ == "__main__":
    t = threading.Thread(target=update_shindo_loop, daemon=True)
    t.start()
    app.run(port=5000)
