import psycopg2
import product

connectionString = "host=localhost dbname=vmb_db user=vmbUser password=vmbUser"

def insertProduct(product):
        conn = psycopg2.connect(connectionString)
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

def deleteAllByOrigin(originName):
        conn =psycopg2.connect(connectionString)
        cur = conn.cursor()
        deleteCommand = 'delete from "vmbSchema"."ResultadoCrawler" where origin like {}'.format("'" + originName + "'")
        cur.execute(deleteCommand)
        conn.commit()


