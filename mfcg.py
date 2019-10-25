from selenium import webdriver

def webthing(url):
    DRIVER = 'C:\Program Files (x86)\Google\chromedriver.exe'
    driver = webdriver.Chrome(DRIVER)
    driver.get(url)
    screenshot = driver.save_screenshot('output/my_screenshot.png')
    driver.quit()