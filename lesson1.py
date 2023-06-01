import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import numpy as np

driver = webdriver.Chrome(r'C:\Users\apiwut\Downloads\chromedriver_win32\chromedriver.exe')
actions = ActionChains(driver)
driver.get('https://www.google.co.th/')
driver.maximize_window()
driver.find_element(by=By.CLASS_NAME, value='gLFyf').send_keys('SET50')
time.sleep(2)
driver.find_element(by=By.CLASS_NAME, value='gLFyf').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(by=By.XPATH, value="//*[text()='ภาพรวมดัชนี SET50 - ตลาดหลักทรัพย์แห่งประเทศไทย']").click()

time.sleep(2)
i = 1
n = 51
# df = pd.DataFrame(index=np.arange(0, n), columns=('Name', 'Price') )
columns=["",'Name', 'Price']
rows = []

for i in range(1,n) :
    NameCompany = driver.find_element(by=By.XPATH, value='//*[@class="table b-table table-custom-field table-custom-field--cnc table-hover-underline b-table-no-border-collapse b-table-selectable b-table-select-multi"]/tbody/tr['+str(i)+']/td[1]/div/div/a/div').text
    price = driver.find_element(by=By.XPATH, value='//*[@class="table b-table table-custom-field table-custom-field--cnc table-hover-underline b-table-no-border-collapse b-table-selectable b-table-select-multi"]/tbody/tr['+str(i)+']/td[5]').text
    print(str(i) +':'+ NameCompany +':'+ price)
    row = [i, NameCompany, price]
    rows.append(row)

    dff = pd.DataFrame(rows, columns=columns)
    # df.loc[i] = [NameCompany + str(price)]
    # ---------------------------------
print(dff)
dff.to_csv(r'C:\Users\apiwut\OneDrive\Desktop\stock.csv',index=False)  