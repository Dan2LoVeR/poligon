import undetected_chromedriver
import time

try:
    driver = undetected_chromedriver.Chrome()
    driver.get('https://byrutgame.org/favorites/')
    time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()