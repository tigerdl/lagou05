# -*- coding: utf-8 -*-
# @Time : 2021/1/15 22:46
# @author :lidong

import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWorkWeixin:

    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)
        # self.driver = webdriver.Chrome()
        url = "https://work.weixin.qq.com/"
        self.driver.get(url)
        self.driver.find_element(By.LINK_TEXT,"企业登录").click()
        #休眠10s，手动扫码登录
        sleep(10)
        # 获取登录的cookie
        cookies = self.driver.get_cookies()
        with open("cookie.json","w") as f:
            json.dump(cookies,f)


    def test_weixin(self):
        with open("cookie.json","r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        main_url = "https://work.weixin.qq.com/wework_admin/frame"
        self.driver.get(main_url)
        self.driver.find_element(By.ID,"menu_customer").click()
        sleep(3)


    def teardown_method(self):
        self.driver.quit()
