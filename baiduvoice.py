# -*- coding: utf-8 -*-
#参考资料： http://yuyin.baidu.com/docs/asr/190
from aip import AipSpeech
import pyaudio
import wave
import json

# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 16000
# RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
#
# p = pyaudio.PyAudio()
#
# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)
#
# print("* recording")
#
# frames = []
#
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)
#
# print("* done recording")
#
# stream.stop_stream()
# stream.close()
# p.terminate()
#
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()
#
#
APP_ID = '10306241'
API_KEY = '6DFOb0hwY1qaLBY5o1mTj8AoTmRCYoZc'
SECRET_KEY = 'DFFsiQzVSmBOXyUrUg9k5LXqKYGDkhwP'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
res=aipSpeech.asr(get_file_content(WAVE_OUTPUT_FILENAME), 'wav', 16000, {
    'lan': 'zh',
})
print res
for word in  res['result']:
    print word

# # 从URL获取文件识别
# print aipSpeech.asr('', 'wav', 16000, {
#     'url': 'http://121.40.195.233/res/16k_test.pcm',
#     'callback': 'http://xxx.com/receive',
# })