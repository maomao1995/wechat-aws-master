#coding=utf8
from werobot import WeRoBot


import logging

logging.basicConfig()

wechat = WeRoBot(enable_session=False,
                token='awswechat',
                APP_ID='wx354be169ddce26e2',
                APP_SECRET='6e1138ffb0f1e79a433e15f42da5c90f')

client = wechat.client


# 通过修饰符添加handler
@wechat.handler
def echo(message):
    return 'Hello World!'

#text 修饰的 Handler 只处理文本消息
@wechat.text
def echo(message):
    print('Recive Text:' + message.content)

    return message.content


#image 修饰的 Handler 只处理图片消息
@wechat.image
def image(message):
    print('Recive Image:' + message.img)
    return message.img


#voice 修饰的 Handler 只处理语音消息
@wechat.voice
def voice(message):
    print('Recive Voice:' + message.media_id)
    return message.recognition

    
#location 修饰的 Handler 只处理语音消息
@wechat.location
def location(message):
    print('Recive Location:')
    return 'Hello My Friend!Location' + message.label


#subscribe 被关注 (Event)
@wechat.subscribe
def subscribe(message):
    return 'Hello My Friend!'


#location_event 修饰的 Handler 只处理上报位置 (Event)
@wechat.location_event
def location_event(message):
    print('Recive Location Event:')
    return 'Location Success!' 


#click 修饰的 Handler 只处理自定义菜单事件 (Event)
@wechat.click
def click(message):
    print('Recive Menu Event:' + message.key)
    if message.key == "V1001_TODAY_WARNING":
        return "Please Uploading Picture..."
    if message.key == "V1001_TODAY_WEATHER":
        return "Waiting For Weather Report..."




