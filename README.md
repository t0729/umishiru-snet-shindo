# Umishiru to Shindo
## 概要
海しるの強震動情報レイヤーからS-netの観測震度を抽出します。  
抽出した情報はhttpでリクエストすることにより配列として取得できます。  
コードは99%がAIによるものです。Pythonなんて書けません。  
(ツール名があまりにも適当なのでいい案があればください)
## リリースノート
### v0.3(最新のバージョン)
取得座標の更新
### [v0.2](https://github.com/t0729/umishiru-snet-shindo/tree/4c5e7799dc045601b93b20a7061100df251b765f)
解析方法の変更  
[0Quake様のSnet_Points](https://github.com/0Quake/Zero-Quake/blob/main/src/Resource/Snet_Points.json)を取得座標として使用
### [v0.1](https://github.com/t0729/umishiru-snet-shindo/tree/c01c4ba50242311ca269c08ffd168a8b4d561031)
公開
## 必要なもの
- Python
### 必要なパッケージ
- flask
- Pillow
- selenium
- chromedriver_autoinstaller
- csv
### パッケージのインストール
```
pip install flask pillow selenium chromedriver-autoinstaller
```
pipコマンドを使用し、必要なパッケージをインストールします  
## 使用方法
1. [ダウンロード](https://github.com/t0729/umishiru-snet-shindo/archive/refs/heads/main.zip)します
2. 解凍して、main.pyを実行します
3. 20秒ほど待ちます
4. [ここ](http://127.0.0.1:5000/shindo)にアクセスします  

APIとして使用する場合は、GETメソッドを使用します。  
また、毎分10秒に自動更新されます。
## レスポンス
レスポンスは配列です。  
```
[-2.5,-2.3,-1.0,-0.9,-0.6,-1.3,-1.8,-2.3,-3.0, (省略) ]
```
配列の順番は[ここ](https://github.com/t0729/umishiru-snet-shindo/blob/main/pixels.csv)を確認してください。　　
7.0は解析の失敗によるものか無効になっている観測点です。表示しないように対策を行ってください。
## その他
### 使用について
このツールを使用する場合、クレジットを記載してください。  
使用の許可は必要はありません。  
>[!CAUTION]
>[海洋状況表示システム利用規約](https://www.msil.go.jp/msil/Data/kiyaku_ja.pdf)に従い、出典を必ず記載してください。  
>例: 海洋状況表示システム ( https://www.msil.go.jp/ )

リポジトリ内にあるファイルについては[クレジット](https://github.com/t0729/umishiru-snet-shindo/edit/main/README.md#%E3%82%AF%E3%83%AC%E3%82%B8%E3%83%83%E3%83%88)に記載されています。
### 安定性について
動作の安定性や信頼性は、一切保証できません。  
**自己責任**で使用してください。  
### 問い合わせ先
- [Discordサーバー](https://discord.gg/R6QeB53AdK)
- [X(非推奨)](https://x.com/cat_t0729)
>[!WARNING]
>更新頻度を変更する場合は、情報元の負荷を考慮して変更してください。
## クレジット
### 情報元
海しる 強震動情報レイヤー  
https://www.msil.go.jp/msil/htm/main.html
### リポジトリ内のファイル
#### shindo_colors.csv
ingen084様  
https://github.com/ingen084/KyoshinShindoColorMap/blob/master/KyoshinShindoColorMap.csv
#### pixels.csv(v0.2)
0Quake様  
https://github.com/0Quake/Zero-Quake/blob/main/src/Resource/Snet_Points.json
#### pixels.csv(v0.1とv0.3)
t0729が作成しました。  
使用に許可は必要ありません。
