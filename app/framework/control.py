# -*- coding: utf-8 -*-
#参考资料： http://yuyin.baidu.com/docs/asr/190
from aip import AipSpeech
import light
APP_ID = '10306241'
API_KEY = '6DFOb0hwY1qaLBY5o1mTj8AoTmRCYoZc'
SECRET_KEY = 'DFFsiQzVSmBOXyUrUg9k5LXqKYGDkhwP'
WAVE_OUTPUT_FILENAME="/home/lj/PycharmProjects/DuerOS-Python-Client/test.wav"
dircmd=[u"打开电视",        #0
        u"关电视",          #1
        u"开灯",            #2
        u"关灯",
        u"凤凰台",
        u"换台",
        u"声音大点",
        u"声言小点",
        u"看b站"]
# 读取文件
class control(object):
    def __init__(self):
        iscmd=False;
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    def recognize(self):
        aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # 识别本地文件
        res=aipSpeech.asr(self.get_file_content(WAVE_OUTPUT_FILENAME), 'wav', 16000, {
            'lan': 'zh',
        })
        print res
        print dircmd
        for word in  res['result']:
            print word
            if word[:-1] in dircmd:
                iscmd=True
                print "开始打开电视请稍等"
            if word[:-1] == dircmd[1]:
                pass
            elif word[:-1] == dircmd[2]:
                light.on()
            elif word[:-1] == dircmd[3]:
                light.off()