# -*- coding: utf-8 -*-
'''
通过输入[Enter]触发唤醒状态
'''
import logging
from sdk.dueros_core import DuerOS

from app.framework.mic import Audio
from app.framework.player import Player
from app.utils.prompt_tone import PromptTone
import json
logging.basicConfig(level=logging.ERROR)


def directive_listener(directive_content):
    '''
    云端下发directive监听器
    :param directive_content:云端下发directive内容
    :return:
    '''
    content = u'云端下发directive:%s' % (directive_content)
    logging.info(content)
    print '[DerOS 网络数据]云端下发directive:'
    print json.dumps(directive_content, sort_keys=True, indent=4, separators=(',', ': '))

def main():
    # 创建录音设备（平台相关）
    audio = Audio()
    # 创建播放器（平台相关）
    player = Player()

    dueros = DuerOS(player)
    dueros.set_directive_listener(directive_listener)

    audio.link(dueros)

    dueros.start() #主线程
    audio.start()  #开始录音，应该是流开始把

    prompt_tone_player = PromptTone(player) #设置来电铃声，放到播放器

    while True:
        try:
            try:
                print '\n'
                input('单击[Enter]建，然后发起对话\n')
            except SyntaxError:
                pass
            # 唤醒态提示音
            prompt_tone_player.play()  #播放提示音
            dueros.listen()      #监听
        except KeyboardInterrupt:
            break

    dueros.stop()
    audio.stop()


if __name__ == '__main__':
    main()
