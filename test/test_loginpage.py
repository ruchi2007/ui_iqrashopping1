from selenium import webdriver
import time
def test_setup():
    global driver
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver_path = "C:\\Users\\takia\\Documents\\workspace\\ui_iqrashopping1\\chromedriver.exe"
    driver = webdriver.Chrome(driver_path)
    driver.get(url)
    driver.implicitly_wait(10)

def test_login():
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    time.sleep(3)
    driver.find_element_by_xpath(username).send_keys("Admin")
    time.sleep(3)
    driver.find_element_by_xpath(password).send_keys("admin123")
    time.sleep(3)
    driver.find_element_by_xpath(login).click()
    time.sleep(3)
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    actual_url = driver.current_url
    driver.save_screenshot("image.png")
    assert expected_url == actual_url
    print(driver.current_url)
    title = driver.title

    assert title == "OrangeHRM"
