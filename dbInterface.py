import psycopg2
import product

def insertProduct(product):
    conn = psycopg2.connect("host=localhost dbname=vmb_db user=vmbUser password=vmbUser")
    cur = conn.cursor()
    insertCommand = 'INSERT INTO "vmbSchema"."ResultadoCrawler" ' + \
                    '(url, product, origin, price, unit, category) VALUES {}' \
                   .format("('" + product.url + \
                           "','" + product.productName + \
                           "','" + product.origin + \
                           "','" + product.price + \
                           "','" + product.unit + \
                           "','" + product.category + "')")
    cur.execute(insertCommand)
    conn.commit()
