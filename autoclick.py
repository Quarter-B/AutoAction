# 方便延时加载
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 模拟浏览器打开网站
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
#window电脑本地
# browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
succeed = False


def scut():
    browser.get('https://sso.scut.edu.cn/cas/login?service=https%3A%2F%2Fiamok.scut.edu.cn%2Fcas%2Flogin')
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath(
        "//*[@id='un']").send_keys(os.environ['SCUT_USER'])
    browser.find_element_by_xpath(
        "//*[@id='pd']").send_keys(os.environ['SCUT_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("//*[@id='index_login_btn']").click()
    time.sleep(10)
    try:
    #     if(is_element_exist("#app > div > div > div:nth-child(2) > div.reportPeaceDiv > div:nth-child(1) > span") and ):
    #         succeed = True
    #     else:
        browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
        print("华工申报成功")
        succeed = True
        time.sleep(3)
        saveFile("华工健康申报签到成功！")
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        # js = 'document.getElementById("btn").click();'
        # browser.execute_script(js)
        saveFile(str(e))
    finally:
        saveFile("华工签到代码存在异常")

def is_element_exist(css):
    s = browser.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        print("元素未找到:%s"%css)
        return False
    elif len(s) == 1:
        print("元素找到:%s"%css)
        return True
    else:
        print("找到%s个元素：%s"%(len(s),css))
        return False

def saveFile(message):
    # 保存email内容
    with open("email.txt", 'a+', encoding="utf-8") as email:
        email.write(message+'\n')


def situyun():
    browser.get('http://situcloud.xyz/auth/login')
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath(
        "//*[@id='email']").send_keys(os.environ['SITUYUN_USER'])
    browser.find_element_by_xpath(
        "//*[@id='password']").send_keys(os.environ['SITUYUN_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("//*[@id='app']/section/div/div/div/div[2]/form/div/div[5]/button").click()
    time.sleep(10)
    try:
        if("明日再来" in browser.find_element_by_xpath("//*[@id='checkin-div']").text):
            succeed = True
            saveFile("明日再来!")
        else:
            # browser.find_element_by_xpath("//*[@id='checkin-div']/a").send_keys(Keys.ENTER)
            js = 'document.getElementById("checkin-div").children[0].click();'
            browser.execute_script(js)
            succeed = True
            print("司徒云打卡成功")
        time.sleep(3)
        saveFile("司徒云签到成功！")
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        saveFile(str(e))
    finally:
        saveFile("司徒云签到代码存在异常")
if __name__ == '__main__':
    scut()
    # 脚本运行成功,退出浏览器
    browser.quit()
