#coding=utf8
from werobot import WeRoBot
from werobot import utils
from werobot import parser
#from urllib import urlretrieve
#from werobot.replies import ImageReply
#from qrcode import models as qrcode_models
#import json
import logging

logging.basicConfig()

TAKEN = 'awswechat'
APP_ID = 'wx354be169ddce26e2'
APP_SECRET = '6e1138ffb0f1e79a433e15f42da5c90f'

#enable_session=False,
robot = WeRoBot(token=TAKEN,
                APP_ID=APP_ID,
                APP_SECRET=APP_SECRET)

client = robot.client
client.create_menu({
   "button":[
       {
           "type":"click",
           "name":"Warning",
           "key":"V1001_TODAY_WARNING"
       },
       {
           "type":"click",
           "name":"Weather",
           "key":"V1001_TODAY_WEATHER"
       },
       {
           "name":"Help",
           "sub_button":[
               {
                   "type":"view",
                   "name":"Home",
                   "url":"http://www.shipxy.com"
               },
               {
                   "type":"view",
                   "name":"Service",
                   "url":"http://www.cetc.com.cn"
               }
           ]
      }]
})


# 通过修饰符添加handler
@robot.handler
def handler(message):
    print('Hello World!')
    return 'Hello World!'

#text 修饰的 Handler 只处理文本消息
@robot.text
def text(message, session):
    print('Recive Text:' + message.content)
    count = session.get("count", 0) + 1
    session["count"] = count
    return "Hello! You have sent %s messages to me" % count
    #return message.content


    #msg_obj = qrcode_models.RequestMessage.objects.create(
    #msg_id   = message.message_id,
    #msg_type = message.type,
    #msg_src  = message.source,
    #msg_data = message.content,
    #msg_url  = '')
    #msg_obj.save()
    #return 'Text['+message.content+'] Processing ...'

#image 修饰的 Handler 只处理图片消息
@robot.image
def image(message):
    print('Recive Image:' + message.img)
    return message.img
    #下载文件并上传资源，重新返回
    #urlretrieve(message.img,'/home/ubuntu/wechat-aws/wechat/media_file.jpg') 
    #media_file = open('/home/ubuntu/wechat-aws/wechat/media_file.jpg')
    #print 'Download image as /home/ubuntu/wechat-aws/wechat/media_file for upload'   
    #media_resp = client.upload_media('image', media_file)
    #print 'Upload media id is '+media_resp['media_id'] 
    
    #应答格式{"type":"TYPE","media_id":"MEDIA_ID","created_at":123456789}
    #media_dict = json.loads(media_resp)
    #print 'Return media:'+media_dict
    #reply = ImageReply(message=message, media_id=media_resp['media_id'])
    #return reply 

    #msg_obj = qrcode_models.RequestMessage.objects.create(
    #msg_id   = message.message_id,
    #msg_type = message.type,
    #msg_src  = message.source,
    #msg_data = message.img,
    #msg_url  = message.img)
    #msg_obj.save()
    #return 'Image[' + message.img + '] Processing ...'

     
#voice 修饰的 Handler 只处理语音消息
@robot.voice
def voice(message):
    print('Recive Voice:' + message.media_id)
    return message.recognition

    #msg_obj = qrcode_models.RequestMessage.objects.create(
    #msg_id   = message.message_id,
    #msg_type = message.type,
    #msg_src  = message.source,
    #msg_data = message.recognition,
    #msg_url  = message.media_id)
    #msg_obj.save()
    #return 'Voice[' + message.recognition + '] Processing...'
    
#location 修饰的 Handler 只处理语音消息
@robot.location
def location(message):
    print('Recive Location:')
    return 'Hello My Friend!Location' + message.label
    
#subscribe 被关注 (Event)
@robot.subscribe
def subscribe(message):
    return '(@^o^@)'

#location_event 修饰的 Handler 只处理上报位置 (Event)
@robot.location_event
def location_event(message):
    print('Recive Location Event:')
    return 'Location Success!' 

#click 修饰的 Handler 只处理自定义菜单事件 (Event)
@robot.click
def click(message):
    print('Recive Menu Event:' + message.key)
    if message.key == "V1001_TODAY_WARNING":
        return "Please Uploading Picture..."
    if message.key == "V1001_TODAY_WEATHER":
        return "Waiting For Weather Report..."


def check_signature(timestamp, nonce, signature):
    if not (TAKEN and timestamp and nonce and signature):
        return False
    sign = utils.get_signature(TAKEN, timestamp, nonce)
    print(sign)
    return sign

def parse_message(body, timestamp, nonce, msg_signature):
    print(1)
    message_dict = parser.parse_xml(body)
    return parser.process_message(message_dict)

def get_encrypted_reply(message):
    print(2)
    return message

