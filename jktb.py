#需要用到谷歌浏览器，以及浏览器相应的版本驱动
#将驱动放到python安装目录下的srict目录下，并且复制一份到谷歌浏览器的安装目录下
#亦可以使用火狐浏览器，但也要下载相应版本的驱动，如上
#学号 密码 为必填项目
import time
from selenium import webdriver
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header
uname = '*******'  #####设置学号
passwd = '********'    #####设置密码
Temperature = ['36.8', '37', '36.6', '36.5', '36.9', '36.6'] #####设置温度（利用列表，利用随机数索引传入保证每天的温度不一样，避免辅导员约茶）
a = random.randint(0, 5)#与温度列表的个数相对应
print(a)


def emailtx(temperature, state):
    # 邮件的内容
    mail_msg = """
           <h2 style="color:#f00"> 健康填报系统提示你：</h2>
           <p>""" + state + """
         <p>今日分健康填报已经完成：你所填写的的温度值是：""" + temperature +""""</p>
         <p>祝你生活愉快</p>
                  """
    message = MIMEText(mail_msg, 'html', 'utf-8')

    # 发件人名字，可以自由填写
    message['From'] = Header('坏狗邮箱小助手', 'utf-8')
    # 收件人名字 ，可以自由填写
    message['To'] = Header('坏狗i', 'utf-8')

    # 邮件标题
    subject = '健康填报接送通知！'
    message['Subject'] = Header(subject, 'utf-8')

    # 发送方地址
    sender = '********@qq.com'
    # 接收方地址，可以是多个地址
    receivers = ['2*********@qq.com']

    # 使用qq邮箱的服务，发送邮件
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtpObj.login(sender, '********')  # 登录 地址 授权码 ：授权码是发送方开启pop3 服务，在邮箱的设置中可以找到，开启后生成授权码
    smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
    smtpObj.quit()  # 关闭
    print('邮件发送成功')

def jitb(uname, passwd, Temperature):
    url = 'http://hmgr.sec.lit.edu.cn/web/#/login'
    brower = webdriver.Chrome('d:\guge\chromedriver.exe')  #####这里的路径是你的谷歌驱动程序所放置的路径(需要设置)
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
    temperature = Temperature[a]
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
        state = '今天首次填报'
        emailtx(temperature, state)
        time.sleep(2)
    except:
        state = '重复填报，请你明天再来'
        temperature = '(二次填报值不给予显示)'
        emailtx(temperature, state)
        print('已经填报过了，请明天再来')
    brower.quit()    #关闭浏览器
jitb(uname,passwd,Temperature)

#作者:坏狗i
