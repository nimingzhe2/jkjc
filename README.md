# jkjc
#由于比较懒，早上不能早起床，经常延误健康填报就很烦！！！！
#用python 模拟浏览器访问健康填报的网站，扔到服务器上让他自己跑解决了辅导员催促的问题，岂不美哉！！！
#是个新手，大佬们别喷。
#非计算机专业
#给了linux 和 win  版本不同代码

jkkkkk.py 用于linux服务器，设置的是无沙盒模式  如果你的linux有GUI你可以修改（非必要）
jktb.py 用于win 系统
############需要安装python3 
############需要下载selenium   (pip install selenium)
############必须下载谷歌浏览器和相应版本的谷歌驱动（当然你也可以使用火狐，及驱动）
############linux 下谷歌驱动 放在与代码运行的同级目录下  
############win 下的谷歌驱动放在谷歌安装目录，并且复制一份到python安装目录下的scrpict目录下，程序中的调用路径也要相应修改
############ 必填项目  学号，密码，邮件发送方地址 邮件接受方地址 ，以及发送方的授权码（当然 你看懂代码，可以把邮件发送给取消，省去不必要麻烦）
#可以将项目放在服务器上运行，彻底解放双手  linux服务器 需要安装crontab  设置定时任务 
#没有服务器的话，用自己的电脑设置定时任务