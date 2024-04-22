import csv
import requests

def scrape_product_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['page_product_analytics']

        with open('productos.csv', mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['item_brand', 'item_category','item_category2', 'item_id', 'item_name', 'price'])
            
            # Escribir las cabeceras solo si el archivo está vacío
            if csvfile.tell() == 0:
                writer.writeheader()
            
            # Escribir los datos de cada producto
            for product in data.values():
                writer.writerow({
                    'item_brand': product.get('item_brand', ''),
                    'item_category': product.get('item_category', ''),
                    'item_category2': product.get('item_category2', ''),
                    'item_id': product.get('item_id', ''), 
                    'item_name': product.get('item_name', ''), 
                    'price': product.get('price', '')
                })
    else: 
        print(f'Error {response.status_code}')

# Leer las URLs desde el archivo CSV

with open('urls.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    urls = [row['url'] for row in reader]

# Procesar cada URL
for url in urls:
    scrape_product_data(url)

