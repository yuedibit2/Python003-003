import time
import requests
from fake_useragent import UserAgent
from selenium import webdriver

def login_request():
    ua = UserAgent(verify_ssl=False)
    headers = {
    'User-Agent' : ua.random,
    'Referer' : 'https://shimo.im/login?from=home'
    }

    s = requests.Session()
    # 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie，
    # 期间使用 urllib3 的 connection pooling 功能。
    # 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
    #login_url = 'https://shimo.im/login?from=home'
    login_url ='https://shimo.im/lizard-api/auth/password/login'
    form_data = {
    'mobile':'134xxxxxxxx',
    'password':'xxxxx'
    }

    response = s.post(login_url, data=form_data, headers=headers, cookies=s.cookies)
    print(response.cookies)
    visit_url='https://shimo.im/docs/GDvcyh3PPDt8Dh3J/read'
    content=s.get(visit_url,headers=headers, cookies=s.cookies)
    print(content.text)

def login_webdriver():
    try :
        browser = webdriver.Chrome()
        # 需要安装chrome driver, 和浏览器版本保持一致
        # http://chromedriver.storage.googleapis.com/index.html

        browser.get('https://shimo.im/login?from=home')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@name="mobileOrEmail"]').send_keys('134xxxxxxxx')
        browser.find_element_by_xpath('//*[@name="password"]').send_keys('xxxxx')
        time.sleep(1)
        browser.find_element_by_xpath('//button[contains(@class,"sm-button submit")]').click()

        cookies = browser.get_cookies()  # 获取cookies
        print(cookies)
        time.sleep(3)
        browser.find_element_by_xpath('//a[@href="/inbox"]').click()
        time.sleep(5)

    except Exception as e:
        print(e)
    finally:
        browser.close()

if __name__=='__main__':
    login_webdriver()
    #login_request()