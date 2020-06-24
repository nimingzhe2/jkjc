import time
from selenium import webdriver


start_url = 'http://hmgr.sec.lit.edu.cn/web/#/login'
brower = webdriver.Chrome("d:/guge/chromedriver.exe")
brower.get(start_url)
login_input = brower.find_element_by_xpath("//input[@placeholder='请输入密码']") #利用xpath获取选中框，键入，密码
login_input.click()
login_input.send_keys('123456')      #默认密码123456
time.sleep(2)
login_input = brower.find_element_by_xpath("//input[@placeholder='请输入账号']") #键定，键入账号
login_input.click()
login_input.send_keys('Z18035536')    #键入学号

login_click = brower.find_element_by_xpath("//button[contains(@class,'van-button van-button--default')]") #魔力浏览器确定
login_click.click()
time.sleep(2)
login_click = brower.find_element_by_xpath("//p[text()='单位个人每日健康状况一键上报，快速收集']") #进入页面
login_click.click()
time.sleep(2)
login_click = brower.find_element_by_xpath("//button[contains(@class,'bottom_btn van-button')]") #于昨日无差别 点击完成
login_click.click()
time.sleep(2)
login_click = brower.find_element_by_xpath("//input[@placeholder='腋下温度(小数或整数)']") #输入度数
login_click.send_keys('36.8')
time.sleep(2)
login_click = brower.find_element_by_xpath("//button[contains(@class,'ensure_button van-button')]") #输入度数
login_click.click()
time.sleep(2)

brower.quit()
