#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
from GetMessage import *

#处理端口冲突
def kill_process():
    port = getcsv(os_version)[1]                #获取csv中填写的端口
    cmd = 'netstat -tunlp | grep ' + str(port)  #检测端口占用情况
    result = os.popen(cmd).read()
    print(result) 
    
    if len(result) == 0:                        #对输出结果判空
        pass
    else:
        os.popen('kill -9 $(lsof -i:'+str(port)+')').read() #kill进程
        





class SsServer:
    def __init__(self, config):    #SsServer(config)调用
        self.sspath = 'git clone -b master https://github.com/shadowsocks/shadowsocks.git'    #git clone -b 指定分支
        self.config = config       #对象赋值
    

    
    def ssserver(self):
        cmd = 'cd shadowsocks/shadowsocks && python server.py -p ' + str(self.config[1]) + ' -k ' + str(
            self.config[0]) + ' -m ' + str(self.config[2]) + ' -d start '  #命令拼接，注意空格/使用数组接收值
        #print(cmd)
        print("服务器ss简易部署(...)")
        try:
            result = os.popen(self.sspath).read()
            print(result)     #输出终端信息
            result = os.popen(cmd).read()
            print(result)     #输出终端信息

        except Exception as e:
            raise e


if __name__ == '__main__':
    ip = getip()             #获取当前服务器IP，目前似乎不需要
    os_version = getos()     #获取服务器系统配置
    config = getcsv(os_version)   #接收list，对应pwd,port,encrypt
    
    ssserver = SsServer(config)   #启动
    kill_process()           #检测端口情况
    ssserver.ssserver()      #执行类方法

    print('服务器IP : %s服务器系统 : %s\n端口 : %s\n密码 : %s\n加密方式 : %s\n'
          % (str(ip), str(os_version), str(config[1]), str(config[0]), str(config[2])))



