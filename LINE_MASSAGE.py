# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:11:32 2023

@author: takay
"""
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Ak0Vsic8OJy73v9e1syakIGIvJ+Prkrepdi4HfzAaEyxcM51vYo1xBpOn4miyt29B8p5oUT7eqKIJ0hW1siIdASH+esLteMeAuADYkLoLYqRvXoDP+lMMwzyOqxd21pscE5dYRMZRSlZZ7fkzCLYdgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('95a10f8a3b93448356a50191cdfad7b0')

@app.route("/")
def test():
    return "ok"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
