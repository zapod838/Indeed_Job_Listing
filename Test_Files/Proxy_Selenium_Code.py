from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver 
import time


proxy_ip_port = 'https://175.106.10.98:3128'
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilties = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilties)   

ser = Service(r"C:\Users\LastC\Downloads\chromedriver_win32")

driver = webdriver.Chrome(service=ser, desired_capabilities = capabilties) 

# Send the request 
driver.get('http://whatismyipaddress.com')

time.sleep(5)

driver.quit()