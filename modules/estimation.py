
from selenium import webdriver
from selenium.webdriver import  ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Selenium Configuration
options=ChromeOptions()
options.headless=True
options.add_argument('--log-level=1')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')


c=['Haier -8.5kg/ Quick Wash Series/Fully Automatic/ Top Loading Washing Machine/ HWM 85-826 (Pillow Drum/Memory Backup/Dual Lint Filters/Fuzzy Quick) 10 Years Warranty.', 'Haier -8 kg/ Hand Wash Series/ Fully Automatic/ Top Loading Washing Machine/ HWM 80-1269Y (Hand Wash Technology/ Pillow Drum/ Memory Backup/ Dual Lint Filters)- 10 Years Warranty.', 'Haier Washing Machine -7.5kg/ Twin Tub / Semi Automatic/ HWM 75-AS / 10 Years Brand Warranty.', 'Haier -8 kg/ Hand Wash Series/ Fully Automatic/ Top Loading Washing Machine/ HWM 80-1708Y (Hand Wash Technology/ Pillow Drum/ Memory Backup/ Dual Lint Filters)- 10 Years Warranty.', 'Haier -09kg/Fully Automatic/ Top Loading Washing Machine/ HWM 90-826Y/10 Years Brand Warranty.', 'Haier -10kg/ Twin Tub / Semi Automatic/ HWM 100-AS/10 Years Brand Warranty.', 'Mini Washing Machine Portable Ultrasonic Turbine Washer, Portable Washing Machine with USB for Travel Business Trip or College Rooms', 'Dawlance 8.5 KG Top Load Fully Automatic Washing Machine-DWT 255-C/ 10 Years Brand Warranty Included', 'Haier Washing Machine - HWM 150-826 - 15 kg Top Loading Fully Automatic 10 Years Brand Warranty.', 'Dawlance 10 KG Top Load Fully Automatic Washing Machine DWT 260 ES/ 10 Years Brand Warranty', 'Mini washing machine portable lazy turbo washing machine school season student dormitory portable socks washing machine', 'Haier -12kg/ Twin Tub / Semi Automatic/ HWM 120-AS (Gear System/ Virgin Plastic/Overheating Sensor/ High RPM) 10 Years Warranty.', 'Haier -15kg/ Hand Wash Series/ Fully Automatic/ Top Loading Washing Machine/ HWM 150-1708- 10 Years Brand Warranty.', 'Haier -09kg/ 3D Wash Series/ Fully Automatic/ Top Loading Washing Machine/ HWM 90-1789 (3D Wash Technology/ Memory Backup/ Pillow Drum/ Double Lint Filters) 10 Years Warranty.', 'Haier -08kg Washing Machine / Single Tub Washer/ Semi Automatic/ HWM 80-35 (Gear System/ Virgin Plastic/Compact Design/ Wide Voltage Range) 10 Years Warranty.', 'Haier -12kg/ Quick Wash Series/Fully Automatic/ Top Loading Washing Machine/ HWM 120-826/ 10 Years Brand Warranty.', 'EsoGoal Mini Washing Machine Ultrasonic Turbo Washing Machine Portable Lazy Laundry Travel USB Washer Mini Dishwashers for Cleaning Sock Underwear Small Rags', 'Dawlance 10 KG Top Load Fully Automatic Washing Machine DWT 11467 ES/Auto matic', 'Super Asia 8 KG-Twin Tub Semi Automatic Washing Machine-SA-244- 1 Year Brand Warranty', 'Haier -9.5kg/ 3D Wash Series/ Fully Automatic/ Top Loading Washing Machine/ HWM 95-1678 (3D Wash Technology/ Knob Control/ Pillow Drum/Memory Backup) 10 Years Warranty.', 'Dawlance 8KG Spinner DS-6010 / 10 Years Brand Warranty', 'Haier 8.5 kg/1708 Series/Fully Automatic/Top Load/HWM 85-1708/Washing Machine/10 Years Warranty', 'Haier -12kg/ 3D Wash Series/ Fully Automatic/ Top Loading Washing Machine/ HWM 120-1789 (3D Wash Technology/ Memory Backup/ Pillow Drum/ Double Lint Filters) 10 Years Warranty.', 'Haier Washing Machine HWM 120-35 FF (12KG) Single Tub Jumbo - 100% Copper', 'Haier -09kg/Fully Automatic/ Top Loading Washing Machine/ HWM 90-826S5 (Pillow Drum/Memory Backup/Dual Lint Filters/Fuzzy Quick) 10 Years Brand Warranty.', 'Haier -15kg/ 3D Wash Series/ Fully Automatic/ Top Loading Washing Machine/ HWM 150-1678 (3D Wash Technology/ Knob Control/ Pillow Drum/ Memory Backup) 10 Years Warranty.', 'Gaba National 12 Kg Single Tub Washer GNW-1208 STD/ 1 Year Brand Warranty', 'Dawlance 12 KG Top Load Fully Automatic Washing Machine-DWT 270ES/ 10 Years Brand Warranty', 'Haier -15kg/ 3D Wash Series/ Fully Automatic/ Top Loading Washing Machine/ HWM 150-1789 (3D Wash Technology/ Memory Backup/ Pillow Drum/ Double Lint Filters) 10 Years Warranty.', 'HWM 100-BS - Semi-Automatic Twin Tub Washing Machine - 10 Kg - White', 'Haier Washing Machine - HWM 120-826E - 12 kg Top Loading Fully Automatic 10 Years Brand Warranty.', 'Dawlance 12 KG Top Load Fully Automatic Washing Machine DWT 270 C LVS+ / Auto matic', 'Dawlance 8 kg Single Tub Washer Washing Machine DW 6100W White/ 10 Years Brand Warranty', 'Super Asia SA-210 Semi Automatic Washing Machine 4 Kg - Grey', 'National Washing Mashine Top Load Capacity: 8 Kg (Double Layer Body) Brand Warranty', 'Dawlance 8 kg Twin Tub Washing Machine Semi Automatic DW 6550W White Color', 'Boss K.E-3000-N-15-BS Single Washing Machine - Grey', 'ROYAL WASHING MACHINE RW-1014(SKIN TRANSPARENT)', 'Haier -12kg/ 3D Wash Series/ Fully Automatic/ Top Loading Washing Machine/ HWM 120-1678 (3D Wash Technology/ Memory Backup/ Pillow Drum/ Double Lint Filters) 10 Years Warranty.', 'Dawlance 7 KG Front Load Fully Automatic Washing Machine DWF 7120 / Auto matic / Inverter']
b=['Rs. 71,999', 'Rs. 66,799', 'Rs. 30,999', 'Rs. 70,099', 'Rs. 77,999', 'Rs. 37,499', 'Rs. 2,150', 'Rs. 65,999', 'Rs. 109,999', 'Rs. 86,000', 'Rs. 2,260', 'Rs. 46,499', 'Rs. 111,499', 'Rs. 82,999', 'Rs. 24,699', 'Rs. 101,999', 'Rs. 3,160', 'Rs. 82,900', 'Rs. 29,999', 'Rs. 95,999', 'Rs. 21,999', 'Rs. 75,999', 'Rs. 105,999', 'Rs. 29,499', 'Rs. 79,899', 'Rs. 131,999', 'Rs. 19,799', 'Rs. 91,999', 'Rs. 111,999', 'Rs. 38,999', 'Rs. 86,999', 'Rs. 107,700', 'Rs. 28,600', 'Rs. 12,800', 'Rs. 14,399', 'Rs. 41,000', 'Rs. 20,450', 'Rs. 23,300', 'Rs. 122,999', 'Rs. 146,500']

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
            res=self.calculate(slug,productNames,productPrice)
            array_int = [int(i.replace(',','')) for i in res]
            average = sum(array_int) / len(array_int)
            return {'average':average}
        except Exception as error:
            print(error)
            return 0

    def OLX(self,slug):
        try:
            self.driver.get(f"https://www.olx.com.pk/items/q-{slug.replace(' ','-')}")
            product_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.a5112ca8')
            productNames = [element.text for element in product_elements]
            product_elements = self.driver.find_elements(By.CSS_SELECTOR, 'span._95eae7db')
            productPrices = [element.text for element in product_elements]
            res=self.calculate(slug,productNames,productPrices)
            print(res)
            # array_int = [int(i.replace(',','')) for i in res]
            # average = sum(array_int) / len(array_int)
            return {'average':'average'}
        except Exception as error:
            print(error)
            return 0
        
    def calculate(self, slug, nameList, priceList):
        targetStr = slug.split(' ')
        newList = []
        
        for index, name in enumerate(nameList):
            
            found_all = True
            for str in targetStr:
                if str not in name:
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

