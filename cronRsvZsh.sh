#!/bin/zsh

# 実行日を取得
EXECUTION_DATE=$(date +%Y-%m-%d)

# 2ヶ月後の日時を取得
TARGET_DATE=$(date -v+2m +%Y-%m-%d)
TARGET_DAY_OF_WEEK=$(date -v+2m +%u)  # 1=月曜, 2=火曜...7=日曜

# 曜日の名前を取得（1=月曜, 2=火曜, ..., 7=日曜）
case $TARGET_DAY_OF_WEEK in
    1) TARGET_DAY_NAME="月曜日" ;;
    2) TARGET_DAY_NAME="火曜日" ;;
    3) TARGET_DAY_NAME="水曜日" ;;
    4) TARGET_DAY_NAME="木曜日" ;;
    5) TARGET_DAY_NAME="金曜日" ;;
    6) TARGET_DAY_NAME="土曜日" ;;
    7) TARGET_DAY_NAME="日曜日" ;;
esac

# ログファイルへのパス
LOG_FILE="/path/to/cron.log"

# ログの区切り
echo "------------------------------------" >> $LOG_FILE
echo "実行日: $EXECUTION_DATE" >> $LOG_FILE
echo "対象日: $TARGET_DATE" >> $LOG_FILE
echo "対象日の曜日: $TARGET_DAY_NAME" >> $LOG_FILE

# 水曜日(3)と木曜日(4)であれば実行
if [[ "$TARGET_DAY_OF_WEEK" == "3" || "$TARGET_DAY_OF_WEEK" == "4" ]]; then
    echo ">>> 指定曜日（$TARGET_DAY_NAME）のため、Pythonスクリプトを実行しました。" >> $LOG_FILE
    source /path/to//venv/bin/activate

    /path/to/python /path/to/reservationBySelenium.py >> /path/to/logfile.log 2>> /path/to/Error.log  >> $LOG_FILE 2>&1

    deactivate
else
    echo ">>> 対象日の曜日は $TARGET_DAY_NAME です。指定された曜日（水曜日または木曜日）ではないため、スクリプトは実行されませんでした。" >> $LOG_FILE
fi

echo "------------------------------------" >> $LOG_FILE