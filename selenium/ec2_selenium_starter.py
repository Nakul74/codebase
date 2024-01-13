from selenium import webdriver
from chromedriver_py import binary_path

#https://pypi.org/project/chromedriver-py/
svc = webdriver.ChromeService(executable_path=binary_path)

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9230")
driver = webdriver.Chrome(service=svc,options=options)
print(driver.current_url)
print(driver.title)
driver.stop_client()
driver.close()
driver.quit()
