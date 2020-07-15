#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
comment: 百度网盘爬虫分析

@author: GanAH  2020/5/12.
@version 1.0.
@contact: dinggan@whu.edu.cn
"""
import csv
import os
import urllib.request
import time

from bs4 import BeautifulSoup


class BaiduNetdisk(object):

    def __init__(self):
        pass

    def disabledLink(self, link):
        """
        链接有效性判断
        :param link: baiduNetdisk download Link
        :return: 0-False / html-True
        """
        try:
            print("url", link)

            headers = {
                'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
            }

            req = urllib.request.Request(url=link, headers=headers, method='POST')
            response = urllib.request.urlopen(req, None, 8)  # 在这里应该加入代理
            html = response.read()
            return {"code": 1, "status": html}
        except Exception as e:
            return {"code": 0, "status": e.__str__()}

    def anylies(self, link):
        resultDict = self.disabledLink(link)
        if resultDict["code"] == 0:
            print("异常错误！")
            print(resultDict.get("status"))
        else:
            try:
                # print(resultDict.get("status").decode('utf-8'))
                # ak = str(resultDict.get("status"),encoding = "utf8")
                # print(type(resultDict.get("status")))
                # for i in range(len(ak)):
                #     print(ak[i])
                soup = BeautifulSoup(resultDict.get("status"), 'html.parser')  # 文档对象

                # 类名为xxx而且文本内容为hahaha的div
                count = 0
                # 查找是否有share-error标签，有则无效
                print("查找是否有share-error标签，有则无效")
                for k in soup.find_all('div', class_='share-error-left'):  # ,string='更多'
                    print(k)
                    count += 1
                if count == 0:
                    print("链接有效")
                    return True
                else:
                    print("链接无效")
                    return False

            except Exception as e:
                print("异常错误-302：", e.__str__())


if __name__ == "__main__":

    try:
        link = input("输入链接:")
        BaiduNetdisk().anylies(link)

    except Exception as e:
        print("异常错误-301：", e.__str__())
