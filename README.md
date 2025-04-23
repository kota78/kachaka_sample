# 導入方法
pythonが実行できる環境(anaconda prompt等)で以下を実行
```
pip install -r requirements.txt
```

# テストプレイ時メモ
- DLはgithubからzipで行なった。授業ではboxでよさそう
- pythonの環境はanacondaを使用
- 学生がanacondaを使用したのは2年前なので現在使用可能かどうかは不明
- 現在のanacondaの環境を壊してしまう可能性も。
- 今回はPCのできる2人だったためpythonファイルから実行できたが、kachakaに直接繋ぐ方が簡単


# 各ファイルの説明
### kachaka_api_client.ipynb
- [公式サンプル](https://github.com/pf-robotics/kachaka-api/blob/main/docs/kachaka_api_client.ipynb)そのまま
- JupytarNotebook形式でさまざまなサンプルを実行可能
### move_sample.py
- 前進するためのサンプルコード
- 1行目：そのまま
- 2行目：IPアドレスを書き換える
	- アプリ→設定→アプリ情報→IPアドレスを参照
- 3行目：client.〇〇を書き換えることで様々な動作が可能

# grpcioがインストールできなかった場合
→python3.10.12をインストール

以下pyenvを用いたコマンドを記載
```
pyenv install 3.10.12
pyenv global 3.10.12
python -m venv .venv
source .venv/bin/activate
```