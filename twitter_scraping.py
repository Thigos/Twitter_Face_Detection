import time
from seleniumwire import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import urllib.parse

MAX_TRY = 10
URL = "https://twitter.com/search?q={}&src=typed_query&f=video"


def load_browser():
    global driver
    binary = FirefoxBinary('downloads/firefox/firefox.exe')
    driver = webdriver.Firefox(executable_path=r"downloads/geckodriver.exe", firefox_binary=binary)
    driver.implicitly_wait(10)


def start(path):
    load_browser()
    list_videos = {}
    with open(path, 'r', encoding="UTF-8") as querys:
        for line in querys.readlines():
            driver.get(URL.format(line))
            load = driver.execute_script('return document.readyState;')
            print("Page", load)
            time.sleep(2)
            count = 0
            arm_videos = []
            for i in range(0, MAX_TRY):
                for request in driver.requests:
                    if request.response:
                        link_video = request.url
                        if 'fmp4' in link_video and 'variant_version=1' in link_video and link_video not in arm_videos:
                            print(link_video)
                            count += 1
                            list_videos[line + '-vid-' + str(count)] = link_video
                            arm_videos.append(link_video)
                            driver.execute_script("window.scroll(0,window.innerWidth*{})".format(str(i/2)))
    driver.close()
    return list_videos
