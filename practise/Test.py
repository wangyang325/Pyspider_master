from selenium import webdriver

driver = webdriver.PhantomJS(executable_path="C:\\Users\\phantomjs-2.1.1\\bin\\phantomjs.exe")
driver.get("http://www.baidu.com")
data = driver.title
print(data)