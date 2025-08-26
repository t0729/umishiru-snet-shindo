# Umishiru to Shindo
## 概要
海しるの強震動情報レイヤーからS-netの観測震度を抽出します。  
抽出した情報はhttpでリクエストすることにより配列として取得できます。
## 使用方法
1. main.pyを実行します
2. 20秒ほど待ちます
3. [ここ](http://127.0.0.1:5000/shindo)にアクセスします  

APIとして使用する場合は、GETメソッドを使用します。  
また、毎分10秒に自動更新されます。
## レスポンス
レスポンスは配列です。  
```
[-2.5,-2.3,-1.0,-0.9,-0.6,-1.3,-1.8,-2.3,-3.0, (省略) ]
```
配列の順番は[ここ](https://github.com/t0729/umishiru-snet-shindo/blob/main/station_code.md)に記載されています。
## その他
### 使用について
このツールを使用する場合、クレジットを記載してください。  
使用の許可は必要はありません。  
リポジトリ内にあるファイルについては[クレジット](https://github.com/t0729/umishiru-snet-shindo/edit/main/README.md#%E3%82%AF%E3%83%AC%E3%82%B8%E3%83%83%E3%83%88)に記載されています。
### 安定性について
動作の安定性や信頼性は、一切保証できません。  
**自己責任**で使用してください。  
>[!WARNING]
>更新頻度を変更する場合は、情報元の負荷を考慮して変更してください。
## クレジット
### リポジトリ内のファイル
#### shindo_colors.csv
ingen084様
https://github.com/ingen084/KyoshinShindoColorMap/blob/master/KyoshinShindoColorMap.csv
#### pixels.csv
t0729が作成しました。  
使用に許可は必要ありませんが、ライセンスを記述してください。
