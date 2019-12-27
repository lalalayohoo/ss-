#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import sys
import csv

'''
目前改需求，读取同一IP内的用户信息进行配置（修改）
'''
def getcsv(os_version):    #读取ss.csv脚本
    filename = 'ss.csv'   #用户配置信息

    with open(filename,"r") as f:   #尝试打开文件
        try:
            reader = csv.reader(f)
        except:
            print("can't open .csv")
        for row in reader:     #逐行读取
            if reader.line_num == 1:    #舍弃首行信息
                continue
            if row[0] == os_version:      #根据系统选择配置（这里需要根据需求改）
                config = [row[7], row[5], row[6]]    #对应pwd,port,encrypt
                return config #对应pwd,port,encrypt



'''
命令行都是Linux语句,不知道是否会出错。
注：Ubuntu，centos，Debian百度了大多采用Linux内核
'''
def getip():
    cmd = "ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1 -d '/'"   #shell执行语句，grep匹配服务器IP，根据最新需求可省略
    result = os.popen(cmd).read()
    return(result)

def getos():
    cmd = "uname"      #简易获取系统，不带版本
    '''
    仅获取操作系统，未获取版本号
    lsb_release -a     #获取详细系统版本，未编写grep提取信息
    '''
    result = os.popen(cmd).read()
    res=result.replace("\n","")    #去掉换行符
    return (res)

