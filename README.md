# 導入方法
1. kachaka_sampleディレクトリに移動
2. pyenvのインストール　[Windows](https://github.com/pyenv-win/pyenv-win) / [mac](https://github.com/pyenv/pyenv?tab=readme-ov-file#macos)
3. python 3.10.12(or3.10.11)のインストール
	```
	pyenv install 3.10.12
	pyenv local 3.10.12
	python -m venv .venv
 	(windows) .venv\Scripts\activate.bat
 	(mac) source .venv/bin/activate
	pip install -r requirements.txt
	```

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
