#!/usr/bin/env python3
# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'arcticapi.settings'
import django
django.setup()
# regular imports
from api.models import Category, Product
import json
# main script
def main():
    dbcat1 = Category.objects.create(title='Ducks')
    dbcat1.save()
    dbcat2 = Category.objects.create(title='Household')
    dbcat2.save()
    dbcat3 = Category.objects.create(title='Food')
    dbcat3.save()
    dbcat4 = Category.objects.create(title='Clothes')
    dbcat4.save()
    dbcat5 = Category.objects.create(title='Office')
    dbcat5.save()
    dbcat6 = Category.objects.create(title='Other')
    dbcat6.save()
    with open('products.json') as json_file:
        data = json.load(json_file)
    products = data['products']
    # print(products)
    for prod in products:
        dbprod = Product()
        print(prod)
        dbprod.id = prod['id']
        dbprod.category = Category.objects.get(title=prod['category'])
        dbprod.filename = prod['filename']
        dbprod.name = prod['name']
        dbprod.description = prod['description']
        dbprod.price = prod['price']
        #dbprod = Product.objects.create(product_id=prod['product_id'], name=prod['name'], category=Category.objects.get(title=prod['category'], filename=prod['filename'], description=prod['description'], price=prod['price'])
        dbprod.save()
    for p in Product.objects.all():
        print(p.name)
        
    
# bootstrap
if __name__ == '__main__':
    main()