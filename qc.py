from selenium import webdriver
import selenium.webdriver.support.ui as ui
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import datetime
import time

edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument('--disable-blink-features=AutomationControlled')

driver = Edge(executable_path='C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/MicrosoftWebDriver.exe', options=edge_options)
data = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
data = str(data)
print(data)
url = 'http://www.koksoft.com/weixinordernewv7.aspx?wxkey=153DC84BBF7CABBB49618F7ED48D5A310A30AB1DF70AD3A9D56E06C4361FE6E3A7257A467D56E248AB776CEFF445264D618B4CBC82AED3FDA1BF65E52E21239214900E6959D0178A6F43F133A18724422EE19A24CDE8D2929D141458590A907CFEC5A5357032FEE4B5677F755E27BBA9&lxbh=Y&orderdate='
url = url + data
driver.get(url)

n = 0
x = 0
while(1):
    while(1):
        start = time.clock()
        try:
            #8-9点主馆场地6为/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/table/tbody/tr[15]/td[6]/span
            button1 = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/a[4]/span[2]')
            print('已定位到元素')
            end = time.clock()
            break
        except:
            print("还未定位到元素!")
            n += 1
            if n > 5:
                driver.refresh()
                x += 1
                n = 0
    print('定位耗费时间：' + str(end - start))
    print('已刷新次数：' + str(x))
    try:
        button1.click()
    except:
        print("场地未选取成功！")
    #提交订单
    buttonTi = driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div/a[3]/p')
    buttonTi.click()

    #确认付款
    buttonFu = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[4]/a[1]')
    try:
        buttonFu.click()
        print('支付成功！')
        break
    except:
        print("支付未成功！")
        driver.refresh()
        x += 1
        print('已刷新次数：' + str(x))
