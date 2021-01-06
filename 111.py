from selenium import webdriver  # 导入浏览器的驱动
import time
import datetime

driver=webdriver.chrome# 打开一个谷歌浏览器


def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            for i in range(1, 21):#每隔0.2秒抢购一次，尝试抢购20次
                webdriver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/input").click()
                webdriver.find_element_by_link_text("去结算").click()
                print(now.strftime('%Y-%m-%d %H:%M:%S'))
                print("第%d次抢购" % i)
                time.sleep(0.2)
            time.sleep(3)
            print('purchase success')
        time.sleep(0.5)
webdriver.get("https://cart.jd.com/cart?rd=0.6242487242726857")  # 此为购物车网站 https://cart.jd.com/cart?rd=0.6242487242726857
time.sleep(3)
webdriver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div/ul/li[2]/a[1]").click()   # 一般需要登录，此处点击的是去登录按钮
time.sleep(50)  # 为了避免输入校验码绕过了输入登录账户密码的步骤，此处打开的是二维码页面，请在50秒内用手机app扫描登录。
buy_on_time("2020-02-15 09:50:00")#开始抢购时间
