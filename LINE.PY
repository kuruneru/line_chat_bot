from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import json

app = Flask(__name__)

# LINE botのアクセストークンとChannel Secretを設定
line_bot_api = LineBotApi('a2198dba9aca8b6f33928d0cf75771d6')
handler = WebhookHandler('U0c7c717a93f894ef4ee7d8e4a9bade94')

# Webhookを受け取るエンドポイントの設定
@app.route('/callback', methods=['POST'])
def callback():
    # リクエストヘッダーから署名検証のための値を取得
    signature = request.headers['X-Line-Signature']
    # リクエストボディを取得
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        # 署名の検証を行い、問題があれば例外を発生
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# メッセージを受け取るハンドラーの設定
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == '明日の教科は？':
        # JSONファイルから教科を読み取る
        with open('subjects.json') as f:
            subjects = json.load(f)
        # 明日の教科を取得する
        tomorrow = 'math' # 仮の値を設定
        for day in subjects:
            if day['day'] == 'tomorrow':
                tomorrow = day['subject']
                break
        # LINEにメッセージを送信する
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"明日の教科は{tomorrow}です。")
        )

if __name__ == "__main__":
    app.run()
