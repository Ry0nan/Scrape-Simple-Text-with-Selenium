from selenium import webdriver

def get_driver():
  #Set options to make browsing Easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",
                                 ["enable-automation"])
  options.add_argument("disable-blink-feaututes=AutomationControlled")
  
  driver = webdriver.Chrome(options)
  driver.get(https://automated.pythonanywhere.com/)
  return driver

def_main():
  driver = get_driver
  element = driver.find_element_by_xpath("/html/body/div[1]/div/h1[1]")
  return element

print(main())