from cmath import inf
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#intializes bot
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://orteil.dashnet.org/cookieclicker/')
actions = ActionChains(driver)
productList = ['product0','product1','product2']

#selects English to start game
language = WebDriverWait(driver, timeout=15).until(lambda d: d.find_element(By.ID, "langSelect-EN"))
print(language)
actions.click(language)
actions.perform()

cookie = WebDriverWait(driver, timeout=15).until(lambda d: d.find_element(By.ID, "bigCookie"))
sleep(8)

#continuously clicks cookie and upgrades by minimum priced item
while 1 != 0:
    WebDriverWait(driver, timeout=15).until(EC.presence_of_element_located((By.ID, "bigCookie")))
    actions.click(cookie)
    actions.perform()

    numCookies = driver.find_element(By.ID, "cookies")
    count = numCookies.text.split(" ")[0]

    products = driver.find_element(By.ID, "products")
    minPricedUpgrade = float(inf)
    upgradeClick = productList[0]
    if(count != ''):
        if int(count) > 15:
            for item in productList:
                price = int(products.find_element(By.ID, item).find_element(By.CLASS_NAME, 'content').find_element(By.CLASS_NAME, 'price').text.replace(',',''))
                if price < minPricedUpgrade:
                    minPricedUpgrade = price
                    upgradeClick = item
            
            if int(count) >= minPricedUpgrade:
                actions.click(products.find_element(By.ID, upgradeClick))
                actions.perform()
