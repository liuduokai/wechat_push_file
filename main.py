#coding=utf-8

from wxpy import *
import os
import time
import logging
import threading
import configparser
import shutil

# 日志配置
ticks = time.time()
log_file_name = str(ticks)+'logging.info'
logging.basicConfig(filename=log_file_name, level=logging.INFO, format='%(asctime)s %(levelname)s  %(message)s %(pathname)s')

#配置文件
config_path  = "./default.cfg"
config_raw = configparser.RawConfigParser()
config_raw.read(config_path, encoding="utf-8")

group_name = config_raw.get('default', 'group')
wait_time = config_raw.get('default', 'wait_time')
file_action = config_raw.get('default', 'file_action')
keep_alive_interval = config_raw.get('default', 'keep_alive_interval')


# print(group_name+'::'+wait_time+'::'+file_action);

try:
    # bot = Bot(console_qr=2)
    bot = Bot()
except:
    logging.error('wechat login fail')
else:
    logging.info('wechat login success')

try:
    my_friend = bot.groups().search(group_name)[0];
except:
    logging.error('find group fali')
    print("获取失败")
else:
    logging.info('find group success')


def send_file_func():
    for root, dirs, files in os.walk("./file/"):
        for file in files:
            try:
                my_friend.send_file('./file/'+file)
            except:
              logging.error("send file fail")
            else:
                logging.info("send file:"+file+'success')
            if int(file_action) == 1:
                try:
                    os.remove('./file/'+file)
                except:
                    logging.error("remove file fail")
                else:
                    logging.info("remove file success")
            elif int(file_action) == 2:
                try:
                    shutil.move('./file/'+file, './file_backup/'+file)
                except:
                    logging.error("move file "+file+"fail")
                else:
                    logging.info("move file"+file+"success")
    timer_send_func = threading.Timer(int(wait_time), send_file_func)
    timer_send_func.start()


def keep_alive():
    bot.file_helper.send('啊')
    timer_keep_alive = threading.Timer(int(keep_alive_interval), keep_alive)
    timer_keep_alive.start()


timer_send_func = threading.Timer(int(wait_time), send_file_func)
timer_send_func.start()

timer_keep_alive = threading.Timer(int(keep_alive_interval), keep_alive);
timer_keep_alive.start()
