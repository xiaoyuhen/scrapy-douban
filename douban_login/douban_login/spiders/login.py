# -*- coding: utf-8 -*-

import scrapy
import json
from urllib import urlretrieve
from scrapy.http import  Request, FormRequest

class login(scrapy.Spider):
    name = 'douban_login'
    allowed_domains = ['accounts.douban.com', 'douban.com']
    start_urls = [
        'https://www.douban.com/'
    ]
    url = 'https://accounts.douban.com/login'

    data = {
        'form_email': 'your email',
        'form_password': 'your password',
        'redir': 'https://www.douban.com'
    }

    headers = {
        'Host': 'accounts.douban.com',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    }


    def start_requests(self):
        return [
            scrapy.Request(
                self.url,
                headers=self.headers,
                meta={'cookiejar': 1},
                callback=self.post_login
            )
        ]

    def post_login(self, response):
        captcha = response.xpath('//img[@id="captcha_image"]/@src').extract_first()

        if captcha:
            local_path = 'captcha.png'
            urlretrieve(captcha, local_path)

            print 'please enter verification code'
            code = input()

            self.data['captcha-solution'] = code


        return [
            FormRequest(
                self.url,
                method='POST',
                # headers=self.headers,
                meta={'cookiejar': response.meta['cookiejar']},
                formdata=self.data,
                callback=self.after_login
            )
        ]

    def after_login(self, response):
        print '登录成功'
        print response
        print response.body


