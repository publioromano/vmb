import product
import dbInterface

product.Product.origin = "pingo doce"
product.Product.price = "1.98"
product.Product.productName = "Producto nome"
product.Product.unit = "kg"
product.Product.url = "www"
product.Product.category = "cat"

db = dbInterface.insertProduct(product.Product)


