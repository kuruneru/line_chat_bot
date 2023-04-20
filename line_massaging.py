import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

#jsonファイルの読み込み
file = open('info.json', 'r')
info = json.load(file)

#LINE BOTの作成
CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

#関数
def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text="なにかご用ですか？")
    line_bot_api.push_message(USER_ID,messages=messages)
    
if __name__ == "__main__":
    main()