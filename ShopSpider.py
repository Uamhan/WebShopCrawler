from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyderman as dr

#template for product object
class Product:
    name = ""
    buyprice = ""

#instals chrome driver for selenium iif not present
path = dr.install(browser=dr.chrome, file_directory='./lib/', verbose=True, chmod=True, overwrite=False, version=None, filename=None, return_info=False)
print("installed chrome driver to path: %s" % path)
driver = webdriver.Chrome(path)
#loads the webpage to be crawled
driver.get("https://ie.webuy.com/search?categoryIds=977")

#list containing products
products = []

#Waits for page script to load needed items.
loaded=""
while not loaded:
    try:
        loaded=driver.find_element_by_class_name('searchRcrd')
    except:continue

#list = driver.find_element_by_class_name('desc')

#creates product object and apends to list from items pull from website
for item in driver.find_elements_by_class_name('desc'):
    product = Product()
    #takes product name from h1 tag
    product.name = item.find_element_by_tag_name('h1').tex
    #takes price from class 'priceTxt' and takes the value after the € symbol
    product.buyprice = item.find_element_by_class_name('priceTxt').text
    product.buyprice = product.buyprice.partition('€')[2]
    #adds product to product list
    products.append(product)
#prints product names
for item in products:
    print(item.name + " | " + item.buyprice)

