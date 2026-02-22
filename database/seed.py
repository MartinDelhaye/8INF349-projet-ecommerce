from app.models import db, Account, Transaction
from peewee import IntegrityError
import datetime


def clear_database():
    db.connect()
    db.atomic()
    Account.delete().execute()
    print("Base de données vidée.")


def seed_accounts():
    accounts = [
        {"owner": "Alztztice", "current_balance": 1000},
        {"owner": "Bob", "current_balance": 500},
        {"owner": "Charlie", "current_balance": 750},
    ]
    for data in accounts:
        Account.create(**data)
    print("Comptes créés.")


def main():
    print("------------ Seeding Database ------------")

    try:
        clear_database()
        with db.atomic():
            seed_accounts()
        print("Seeding terminé avec succès.")

    except IntegrityError as e:
        print("Erreur lors du seeding :", e)

    finally:
        db.close()


if __name__ == "__main__":
    main()