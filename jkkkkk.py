#需要用到谷歌浏览器，以及浏览器相应的版本驱动
#将驱动放到python程序的同级目录下
#亦可以使用火狐浏览器，但也要下载相应版本的驱动，如上
#程序中所有的time延时2秒可以去掉，跟网路快慢无关
#学号 密码 为必填项目
#如果害怕脚本在服务器上没有执行可以设置一个邮箱提醒
#有服务器的朋友可以把程序仍服务器上运行，用crontab模块设置定时任务，解放双手，没有服务器的话用自己电脑添加一个定时运行程序，
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

uname = '8888888'  #####设置学号
passwd = '123456'    #####设置密码
Temperature = ['36.8', '37', '36.6', '36.5', '36.9'] #####设置温度（利用列表，利用随机数索引传入保证每天的温度不一样，避免辅导员约茶）
a = random.randint(0, 4)#与温度列表的个数相对应
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
    message['From'] = Header('你的邮箱小助手吖', 'utf-8')
    # 收件人名字 ，可以自由填写
    message['To'] = Header('坏狗i', 'utf-8')

    # 邮件标题
    subject = '健康填报接送通知！'
    message['Subject'] = Header(subject, 'utf-8')

    # 发送方地址
    sender = '77******@qq.com'
    # 接收方地址，可以是多个地址
    receivers = ['**********@qq.com']

    # 使用qq邮箱的服务，发送邮件
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtpObj.login(sender, 'sbp***********')  # 登录 地址 授权码 在发送方到邮箱设置里开启pop3服务会生成授权码
    smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
    smtpObj.quit()  # 关闭
    print('邮件发送成功')



def jitb(uname, passwd, Temperature):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')  #由于我使用的是centos无gui服务器 ，设置的无沙盒模式
    start_url = 'http://hmgr.sec.lit.edu.cn/web/#/login'
    brower = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_options) #调用谷歌浏览器的驱动备注第二条所述的复制到的安装目录下（可以使用火狐，调用驱动的绝对路径）
    brower.get(start_url)
    login_input = brower.find_element_by_xpath("//input[@placeholder='请输入密码']") #利用xpath获取选中框，键入，密码
    login_input.click()
    login_input.send_keys(passwd)
    time.sleep(2)
    login_input = brower.find_element_by_xpath("//input[@placeholder='请输入账号']")#利用xpath选中用户框
    login_input.click()
    login_input.send_keys(uname)
    login_click = brower.find_element_by_xpath("//button[contains(@class,'van-button van-button--default')]") #登录
    login_click.click()
    time.sleep(2)
    login_click = brower.find_element_by_xpath("//p[text()='单位个人每日健康状况一键上报，快速收集']") #进入页面
    login_click.click()
    time.sleep(2)
    temperature = Temperature[a]
    try:
        login_click = brower.find_element_by_xpath("//button[contains(@class,'bottom_btn van-button')]") #于昨日无差别 点击完成
        login_click.click()
        time.sleep(2)
        login_click = brower.find_element_by_xpath("//input[@placeholder='腋下温度(小数或整数)']") #输入度数
        login_click.send_keys(Temperature[a])  #确保随机生成温度值在字典范围中
        time.sleep(2)
        login_click = brower.find_element_by_xpath("//button[contains(@class,'ensure_button van-button')]") #输入度数
        login_click.click()
        print('今日份健康填报已经完成')
        state = '今天首次填报'
        emailtx(temperature, state)
        print(temperature)
        time.sleep(2)
    except:
        print('已经填报过了，请明天再来')
        state = '重复填报'
        emailtx(temperature, state)
    brower.quit()
jitb(uname,passwd,Temperature)

#作者:坏狗i
