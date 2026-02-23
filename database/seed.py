from app.models import db, Product
from peewee import IntegrityError
import datetime


def clear_database():
    db.connect()
    db.atomic()
    Product.delete().execute()
    print("Base de données vidée.")


def seed_products():
    products = [
        {
            "name" : "Brown eggs",
            "id" : 1,
            "in_stock" : True,
            "description" : "Raw organic brown eggs in a basket",
            "price" : 28.1, "weight": 400, "image": "0.jpg"
            },
        { 
         "description": "Sweet fresh stawberry on the wooden table",
         "image": "1.jpg",
         "in_stock" : True,
         "weight": 299,
         "id" : 2,
         "name" : "Sweet fresh stawberry",
         "price" : 29.45
         }
    ]
    for data in products:
        Product.create(**data)
    print("Produits créés.")


def main():
    print("------------ Seeding Database ------------")

    try:
        clear_database()
        with db.atomic():
            seed_products()
        print("Seeding terminé avec succès.")

    except IntegrityError as e:
        print("Erreur lors du seeding :", e)

    finally:
        db.close()


if __name__ == "__main__":
    main()