# itoshima_rsv
*糸島市体育館自動予約のために開発したプログラム*

## cron用の記法
### シェルスクリプト
/path/to/python3.10 /path/to/itoshima_rsv/reservationBySelenium.py >> /path/to/itoshima_rsv/logfile.log 2>> /path/to/itoshima_rsv/Error.log

### 時間指定
#### 水曜日予約分
30 8 * * 3 /path/to/cron/itoshimaRsv.sh

#### 木曜日予約分
30 8 * * 4 /path/to/cron/itoshimaRsv.sh


### 環境変数
- USERNAME: ログインID
- PASSWORD: パスワード
- LINE_ACCESS_TOKEN: プログラムの可否通知用のアクセストークン


### 必要ライブラリ
- Selenium
    プログラム全体の根幹
- requests
    LINE Notify使用のため
- python-dotenv
    .envファイルに格納してある環境変数を読み込む

### note
Seleniumによる自動化のため、UI上操作となる。
スリープ中の実行ができないため、Requestsを用いた自動予約システムに書き換えたいところ。
