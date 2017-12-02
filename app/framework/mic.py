# -*- coding: utf-8 -*-
import pyaudio
import logging

import app.app_config as app_config
import wave
import time
import control
logging.basicConfig(level=app_config.LOGGER_LEVEL)
logger = logging.getLogger(__file__)


class Audio(object):
    '''
    录音类(基于pyaudio)
    '''

    def __init__(self, rate=16000, frames_size=None, channels=None, device_index=None):
        '''
        录音类初始化
        :param rate:采样率
        :param frames_size:数据帧大小
        :param channels:通道数
        :param device_index:录音设备id
        '''
        self.sample_rate = rate
        self.frames_size = frames_size if frames_size else rate / 100
        self.channels = channels if channels else 1

        self.pyaudio_instance = pyaudio.PyAudio()

        self.record=False
        self.recorddata=[]
        self.ctl=control.control()

        if device_index is None:
            if channels:
                for i in range(self.pyaudio_instance.get_device_count()):
                    dev = self.pyaudio_instance.get_device_info_by_index(i)
                    name = dev['name'].encode('utf-8')
                    logger.info('{}:{} with {} input channels'.format(i, name, dev['maxInputChannels']))
                    if dev['maxInputChannels'] == channels:
                        logger.info('Use {}'.format(name))
                        device_index = i
                        break
            else:
                device_index = self.pyaudio_instance.get_default_input_device_info()['index']

            if device_index is None:
                raise Exception('Can not find an input device with {} channel(s)'.format(channels))

        self.stream = self.pyaudio_instance.open(
            start=False,
            format=pyaudio.paInt16,
            input_device_index=device_index,
            channels=self.channels,
            rate=int(self.sample_rate),
            frames_per_buffer=int(self.frames_size),
            stream_callback=self.__callback,
            input=True
        )

        self.sinks = []

    def start(self):
        '''
        开始录音
        :return:
        '''
        self.stream.start_stream()

    def stop(self):
        '''
        结束录音
        :return:
        '''
        self.stream.stop_stream()

    def link(self, sink):
        '''
        绑定录音接收实体
        :param sink: 录音接收实体
        :return:
        '''
        if hasattr(sink, 'put') and callable(sink.put):
            self.sinks.append(sink)
        else:
            raise ValueError('Not implement put() method')

    def unlink(self, sink):
        '''
        录音实体解除绑定
        :param sink: 录音接收实体
        :return:
        '''
        self.sinks.remove(sink)

    def __callback(self, in_data, frame_count, time_info, status):
        '''
        录音数据(pmc)回调
        :param in_data:录音数据
        :param frame_count:
        :param time_info:
        :param status:
        :return:
        '''
        for sink in self.sinks:
            sink.put(in_data)
        if self.record:
            self.recorddata.append(in_data)
        return None, pyaudio.paContinue

    def recode(self):
        # frames=[]
        # for i in range(0, int(self.sample_rate / int(self.frames_size) * 5)):
        #     data = self.stream.read(1024)
        #     frames.append(data)
        self.record=True
        time.sleep(5)
        self.record=False
        wf = wave.open("test.wav", 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.pyaudio_instance.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.recorddata))
        wf.close()
        self.recorddata.reverse()
        self.ctl.recognize()