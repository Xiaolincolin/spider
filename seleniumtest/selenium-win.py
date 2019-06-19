    from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
#这个是一个用来控制chrome以无界面模式打开的浏览器
#创建一个参数对象，用来控制chrome以无界面的方式打开
chrome_options = Options()
#后面的两个是固定写法 必须这么写
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#驱动路径 谷歌的驱动存放路径
path = 'D:\chromedriver\chromedriver.exe'

#创建浏览器对象

browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)

url ='http://wanfangdata.com.cn/details/detail.do?_type=perio&id=jkdsy-xsb201819344#'

browser.get(url)
time.sleep(3)
bt = browser.find_element_by_id('see_all')
bt.click()
print(browser.page_source)
browser.quit()