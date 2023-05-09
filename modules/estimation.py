
from selenium import webdriver
from selenium.webdriver import  ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import json

# Selenium Configuration
options=ChromeOptions()
options.headless=True
options.add_argument('--log-level=1')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

class EstimatePrice:
    
    def __init__(self):
        self.driver = webdriver.Chrome()

    def Daraz(self,slug):
        try:
            self.driver.get(f"https://www.daraz.pk/catalog/?q={slug}&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e34937C0KdMd")
            product_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.title--wFj93')
            productNames = [element.text for element in product_elements]
            product_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.price--NVB62')
            productPrice = [element.text for element in product_elements]
            print(productNames)
            print(productPrice)
            return {'Product':'title', 'Price':'price'}
        except:
            return 0

    def OLX(self):
        try:
            self.driver.get(f"https://www.olx.com.pk/items/q-Iphone-14")
           
            product_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.a5112ca8')
            productNames = [element.text for element in product_elements]
            product_elements = self.driver.find_elements(By.CSS_SELECTOR, 'span._95eae7db')
            productPrices = [element.text for element in product_elements]
            print(productNames)
            print(productPrices)

            return {'Product':'title', 'Price':f"Rs. "}
        except:
            return 0
        
   
    
    def Scrape(self,slug):
        try:
            return {
            'Amazon':self.Amazon(slug),
            'Daraz':self.Daraz(slug),
            # 'AliExpress':self.AliExpress(slug),
        }
        except:
            return 0

