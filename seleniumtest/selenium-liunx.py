from pyvirtualdisplay import Display
from selenium import webdriver
display = Display(visible=0, size=(900, 800))
display.start()

driver = webdriver.Firefox()

driver.get('http://www.cnblogs.com')
browser.get(url)
time.sleep(3)
bt = browser.find_element_by_id('see_all')
bt.click()
print(browser.page_source)

driver.quit()

display.stop()