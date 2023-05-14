
from selenium import webdriver
from selenium.webdriver import  ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Selenium Configuration
options=ChromeOptions()
options.headless=False
options.add_argument('--log-level=1')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')


class EstimatePrice:
    
    def __init__(self):
        self.driver = webdriver.Chrome()

    def computeAvg(self,res):
        try:
            array_int = [int(i.replace(',','')) for i in res]
            average = sum(array_int) / len(array_int)
            return average
        except Exception as error:
            return 0
        
    def Daraz(self,slug):
        try:
            self.driver.get(f"https://www.daraz.pk/catalog/?q={slug}&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e34937C0KdMd")
            product_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.title--wFj93')
            productNames = [element.text for element in product_elements]
            product_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.price--NVB62')
            productPrice = [element.text for element in product_elements]
            res=self.calculate(slug,productNames,productPrice)
            return self.computeAvg(res)
        except Exception as error:
            # print(error)
            return 0

    def OLX(self,slug):
        try:
            self.driver.get(f"https://www.olx.com.pk/items/q-{slug.replace(' ','-')}")
            product_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.a5112ca8')
            productNames = [element.text for element in product_elements]
            product_elements = self.driver.find_elements(By.CSS_SELECTOR, 'span._95eae7db')
            productPrices = [element.text for element in product_elements]
            res=self.calculate(slug,productNames,productPrices)
            return self.computeAvg(res)
        except Exception as error:
            # print(error)
            return 0
        
    def calculate(self, slug, nameList, priceList):
        targetStr = slug.split(' ')
        newList = []
        for index, name in enumerate(nameList):
            found_all = True
            for str in targetStr:
                if str.lower() not in name.lower():
                    found_all = False
                    break
            if found_all:
                newList.append(priceList[index].split(' ')[1])
        return newList

    def Scrape(self,slug):
        try:
            return {
            'OLX':self.OLX(slug),
            'Daraz':self.Daraz(slug),
        }
        except Exception as e:
            print(e)
            return 0

