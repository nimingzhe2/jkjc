#需要用到谷歌浏览器，以及浏览器相应的版本驱动
#将驱动放到python安装目录下的srict目录下，并且复制一份到谷歌浏览器的安装目录下
#亦可以使用火狐浏览器，但也要下载相应版本的驱动，如上
#学号 密码 为必填项目
#如果害怕脚本在服务器上没有执行可以设置一个邮箱提醒
#有服务器的朋友可以把程序仍服务器上运行，用crontab模块设置定时任务，解放双手，没有服务器的话用自己电脑添加一个定时运行程序，
import time
from selenium import webdriver
import random
uname = 'Z1803****'  #####设置学号
passwd = '123456'    #####设置密码
Temperature = ['36.8', '37', '36.6', '36.5', '36.9'] #####设置温度（利用列表，利用随机数索引传入保证每天的温度不一样，避免辅导员约茶）
a = random.randint(0, 4)#与温度列表的个数相对应
print(a)
def jitb(uname, passwd, Temperature):
    url = 'http://hmgr.sec.lit.edu.cn/web/#/login'
    brower = webdriver.Chrome("d:/guge/chromedriver.exe")  #####这里的路径是你的谷歌驱动程序所放置的路径(需要设置)
    brower.get(url)
    pw_input = brower.find_element_by_xpath("//input[@placeholder='请输入密码']") #利用xpath获取选中框，键入，密码
    pw_input.click()
    pw_input.send_keys(passwd)
    time.sleep(2)
    login_input = brower.find_element_by_xpath("//input[@placeholder='请输入账号']")#利用xpath选中用户框
    login_input.click()
    login_input.send_keys(uname)
    login_click = brower.find_element_by_xpath("//button[contains(@class,'van-button van-button--default')]") #登录
    login_click.click()
    time.sleep(2)
    entrance_click = brower.find_element_by_xpath("//p[text()='单位个人每日健康状况一键上报，快速收集']") #进入页面
    entrance_click.click()
    time.sleep(2)
    try:
        seleceted_click = brower.find_element_by_xpath("//button[contains(@class,'bottom_btn van-button')]") #于昨日无差别 点击完成
        seleceted_click.click()
        time.sleep(2)
        key_click = brower.find_element_by_xpath("//input[@placeholder='腋下温度(小数或整数)']") #输入度数
        key_click.send_keys(Temperature[a])
        time.sleep(2)
        complete_click = brower.find_element_by_xpath("//button[contains(@class,'ensure_button van-button')]") #输入度数
        complete_click.click()
        print('今日份健康填报已经完成')
        time.sleep(2)
    except:
        print('已经填报过了，请明天再来')
    brower.quit()    #关闭浏览器
jitb(uname,passwd,Temperature[a])

#作者:坏狗i
