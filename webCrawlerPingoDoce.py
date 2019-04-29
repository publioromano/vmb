import urllib.request
from lxml import html

urls = ["https://www.pingodoce.pt/produtos/"
       ,"https://www.pingodoce.pt/produtos/categoria/alimentacao-especial/"
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
       ,"https://www.pingodoce.pt/produtos/categoria/vinhos-e-espumantes/"
       ]

total = 0
for url in urls:
    request = urllib.request.Request(url)
    result = urllib.request.urlopen(request)
    resulttext = result.read()
    htmlForm = html.fromstring(resulttext)
    i = 0
    for article in htmlForm.xpath("//article[contains(@class,'cf')]"): #("//div[@class='product-box-title']"):
        product = article.xpath("//div[@class='product-box-title']")[i]
        price = article.xpath("//span[@class='price']")[i]
        units = article.xpath("//span[@class='units']")[i]
        category = article.xpath("//div[@class='categoria-produto']")[i]
        print("Product", total + 1, category.text.strip(), price.text.strip(), units.text.strip(), product.text.strip())
        i = i + 1
        total = total + 1

