#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: debugtalk.py
# @time: 2020/11/4 8:30 下午
import random
import requests

def get_search_word():
    word_list = ['newdream','12306','火车票','新梦想软测教育']
    num = random.randint(0,len(word_list)-1)
    return word_list[num]

def s():
    print( '测试用例开始执行' )
def t():
    print('测试用例结束执行')

def s1(step_name):
    print( '测试步骤 [%s] 开始执行'%step_name )
def t1(step_name):
    print('测试步骤 [%s] 结束执行'%step_name)

def get_true():
    return None

def get_access_token():
    p_dict = {
        'grant_type': 'client_credential',
        'appid': 'wx55614004f367f8',
        'secret': '65515b46dd758dfdb09420bb7db2c67f'
    }
    try:
        response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token',
                                params=p_dict)
        token = response.json()['access_token']
    except KeyError as e:
        token = None
    return token
# 参数实战：
def get_params01():
    return ['newdream','12306','火车票']
def get_params02():
    return [['newdream','newdream_百度搜索'],['12306','12306_百度搜索'],['火车票','火车票_百度搜索']]
def get_random_int(min,max,count=3):
    num_list = []
    for i in range(count):
        num_list.append( random.randint(min,max) )
    return num_list

def get_random_string(base_str,str_len,count=3):
    string_list = []
    for i in range(count):
        string = ''
        for j in range(int(str_len)):
            string = string + base_str[random.randint(0,len(base_str)-1)]
        string_list.append(string)
    return string_list

def get_random_phonenum(*mobile_num,count=3):
    phonenum_list = []
    for i in range(count):
        phone_start = random.choice(mobile_num)
        phone_end = ''.join( random.sample('0123456789',8) )
        phonenum_list.append( phone_start + phone_end )
    return phonenum_list

if __name__=='__main__':
    # print( get_random_phonenum(['131','132','133'])  )
    print( get_random_phonenum('131','132')  )
    # str1 = '1234567890abcdefghi中国我们'
    # # 需求：上述的字符串为底，用它们的字母组合生成随机字符串
    # # print(len(str1))
    # # print( str1[random.randint(0,len(str1)-1)] )
    # str2 = ''
    # for i in range(10):
    #     str2 = str2 + str1[random.randint(0,len(str1)-1)]
    # print(str2)
    # 需求：实现随机手机号 131  132  133
    # mobile_num = ['131','132','133']
    # print( random.choice(mobile_num) )
    # # 131 0123456789 == 8
    # print( random.sample('0123456789',8) )
    # a = ['5', '0', '8', '6', '4', '3', '7', '2']
    # print( random.choice(mobile_num) + ''.join( a ) )

