from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def main():
    webdriver_path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(webdriver_path)
    url = "https://tradingeconomics.com/country-list/inflation-rate?continent=world"
    driver.get(url)
    
    table = driver.find_element(By.CLASS_NAME, "table-responsive")
    rows = table.find_elements(By.TAG_NAME, "tr")
    
    data = []
    for row in rows[1:]:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells]
        data.append(row_data)
    
    df = pd.DataFrame(data)
    df.to_csv("inflation.csv", index=False)
    
    return

if __name__ == "__main__":
    main()
