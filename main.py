from wxpy import *
import os
import time
import logging
import threading

ticks = time.time()
log_file_name = str(ticks)+'logging.info'
logging.basicConfig(filename=log_file_name, level=logging.INFO, format='%(asctime)s %(levelname)s  %(message)s %(pathname)s')

try:
    # bot = Bot(console_qr=2)
    bot = Bot()
except:
    logging.error('wechat login fail')
else:
    logging.info('wechat login success')

my_friend = bot.groups().search('测试群聊')[0];

def send_file_func():
    for root, dirs, files in os.walk("./file/"):
        for file in files:
            try:
                my_friend.send_file('./file/'+file)
            except:
              logging.error("send file fail")
            else:
                logging.info("send file:"+file+'success')
            try:
                os.remove('./file/'+file)
            except:
                logging.error("remove file fail")
            else:
                logging.info("remove file success")
    timer = threading.Timer(5, send_file_func)
    timer.start()

timer = threading.Timer(5,send_file_func)
timer.start()