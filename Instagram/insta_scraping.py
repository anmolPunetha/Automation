from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Program Files (x86)/chromedriver.exe")
driver.implicitly_wait(15)

driver.get('https://www.instagram.com/')
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
login.send_keys('account here')
time.sleep(1)

pswd = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pswd.send_keys('password here')
time.sleep(2)

button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
button.click()
time.sleep(4)

driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys('account to be searched')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]').click()


followers_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
followers_button.click()
time.sleep(2)


def get_followers():
    num_of_followers = 239
    followers = []
    last = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[11]')
    driver.execute_script("arguments[0].scrollIntoView(true);", last)

    for i in range(24, num_of_followers + 1, 6):
        last = driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]')
        time.sleep(0.6)
        driver.execute_script("arguments[0].scrollIntoView(true);", last)
        time.sleep(1.2)

    patch = driver.find_elements_by_class_name('d7ByH')
    print(len(patch))
    for i in patch:
        followers.append(i.text)

    print(followers)
    return followers


followers = get_followers()
time.sleep(2)
driver.get('https://www.instagram.com/appu.2280/')
following_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
following_button.click()
time.sleep(2)


def get_following():
    num_of_following = 257
    following = []
    last = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[11]')
    driver.execute_script("arguments[0].scrollIntoView(true);", last)

    for i in range(24, num_of_following + 1, 6):
        last = driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]')
        time.sleep(0.5)
        driver.execute_script("arguments[0].scrollIntoView(true);", last)
        time.sleep(0.5)

    patch = driver.find_elements_by_class_name('d7ByH')
    print(len(patch))
    for i in patch:
        following.append(i.text)

    print(following)
    return following


following = get_following()

for person in following:
    if person in followers:
        pass
    else:
        print(person)
