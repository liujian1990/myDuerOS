# -*- coding: utf-8 -*-
'''
OAuth2.0认证
'''
import sdk.auth as auth

# 开发者注册信息
CLIENT_ID = '6DFOb0hwY1qaLBY5o1mTj8AoTmRCYoZc'
CLIENT_SECRET = 'DFFsiQzVSmBOXyUrUg9k5LXqKYGDkhwP'

def main():
    # 使用开发者注册信息
    auth.auth_request(CLIENT_ID, CLIENT_SECRET)

    # 使用默认的CLIENT_ID和CLIENT_SECRET
    #auth.auth_request()


if __name__ == '__main__':
    main()
