from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# SELENIUM CSS SELECTOR
CSS_LOAD_MORE = "a._8imhp._glz1g"
CSS_RIGHT_ARROW = "a[class='_de018 coreSpriteRightPaginationArrow']"
FIREFOX_FIRST_POST_PATH = "//a[contains(@class, '_8mlbc _vbtk2 _t5r8b')]"
TIME_TO_CAPTION_PATH = "../../following-sibling::ul/*/*/span"

# FOLLOWERS/FOLLOWING RELATED
CSS_EXPLORE = "a[href='/explore/']"
CSS_LOGIN = "a[href='/accounts/login/']"
CSS_FOLLOWERS = "a[href='/{}/followers/']"
CSS_FOLLOWING = "a[href='/{}/following/']"
FOLLOWER_PATH = "//div[contains(text(), 'Followers')]"
FOLLOWING_PATH = "//div[contains(text(), 'Following')]"


username=""
password=""
time.sleep(3)
driver=webdriver.Firefox()

'''
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/accounts/login/")

driver.find_element_by_xpath("//div/input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//div/input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//span/button").click()
'''

# driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys('kyliejenner')
# driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.RETURN)

driver.get("https://www.instagram.com/kyliejenner/")
driver.find_element_by_xpath(FIREFOX_FIRST_POST_PATH).click()


