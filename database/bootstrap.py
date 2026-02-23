from pathlib import Path
from app.models import db, Product
import os

def suppr_db():
    db_path = Path(db.database)
    print(f"Chemin de la base de données : {db_path}")
    if db_path.exists():
        os.remove(db_path)
        print(f"Suppression de l'ancienne base de données : {db_path}")
    
def create_tables():
    db.connect()
    db.create_tables([Product])
    db.close()
    print("Tables créées avec succès.")

def main():
    print("------------ Database Bootstrapping ------------")
    suppr_db()
    create_tables()
    print(f"Base de données crée : {db.database}")

if __name__ == "__main__":
    main()