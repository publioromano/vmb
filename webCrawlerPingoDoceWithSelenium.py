from pyvirtualdisplay import Display
from selenium import webdriver
import time
import urllib.request
from lxml import html
import product
import dbInterface


originName = "Pingo Doce"
urls = ["https://www.pingodoce.pt/produtos/categoria/alimentacao-especial/"
       ,"https://www.pingodoce.pt/produtos/categoria/animais/"
       ,"https://www.pingodoce.pt/produtos/categoria/bebe/"
       ,"https://www.pingodoce.pt/produtos/categoria/bebidas/"
       ,"https://www.pingodoce.pt/produtos/categoria/casa/"
       ,"https://www.pingodoce.pt/produtos/categoria/charcutaria/"
       ,"https://www.pingodoce.pt/produtos/categoria/chef-express/"
       ,"https://www.pingodoce.pt/produtos/categoria/congelados/"
       ,"https://www.pingodoce.pt/produtos/categoria/electrodomesticos/"
       ,"https://www.pingodoce.pt/produtos/categoria/frescos/"
       ,"https://www.pingodoce.pt/produtos/categoria/higiene/"
       ,"https://www.pingodoce.pt/produtos/categoria/lacticinios/"
       ,"https://www.pingodoce.pt/produtos/categoria/limpeza/"
       ,"https://www.pingodoce.pt/produtos/categoria/maquina-cafe/"
       ,"https://www.pingodoce.pt/produtos/categoria/mercearia/"
       ,"https://www.pingodoce.pt/produtos/categoria/pre-cozinhados/"
       ,"https://www.pingodoce.pt/produtos/categoria/vinhos-e-espumantes/"]

total = 0
products = 0
dbInterface.deleteAllByOrigin(originName)
print("Todas as informaçõs de {} foram excluídas.".format(originName))
for url in urls:
    display = Display(visible=0, size=(800, 600))
    display.start()
    browser = webdriver.Firefox()
    browser.get(url)
    total = total + 1
    try:
        button = browser.find_element_by_id("catapultCookie")
        button.click()
        element = browser.find_element_by_class_name("view-more")
    except:
        continue
    while element.is_displayed():
        element.click()
        time.sleep(2)
    i = 0
    articles = len(browser.find_elements_by_xpath("//article[contains(@class,'cf')]"))
    for x in range(articles):
        product.Product.category = browser.find_elements_by_xpath("//div[@class='categoria-produto']")[i].text
        product.Product.origin = originName
        product.Product.price = browser.find_elements_by_xpath("//span[@class='price']")[i].text
        product.Product.productName = browser.find_elements_by_xpath("//div[@class='product-box-title']")[i].text
        product.Product.price = browser.find_elements_by_xpath("//span[@class='price']")[i].text
        product.Product.unit = browser.find_elements_by_xpath("//span[@class='units']")[i].text
        product.Product.url = url 
        print("Product", products + 1)
        i = i + 1
        products = products + 1
        o = dbInterface.insertProduct(product.Product)
    browser.quit()
    display.stop()