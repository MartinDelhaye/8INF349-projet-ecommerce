import os
import peewee as p

DATABASE_PATH = os.getenv("DATABASE_PATH", "app/db.sqlite")

db = p.SqliteDatabase(DATABASE_PATH)

class BaseModel(p.Model):
    class Meta:
        database = db


class Product(BaseModel):
    id = p.AutoField(primary_key=True)
    name = p.CharField(unique=True, null=False)
    in_stock = p.BooleanField(null=False)
    description = p.TextField(null=True)
    price = p.IntegerField(null=False, constraints=[
        p.Check('price >= 0')
    ])
    weight = p.IntegerField(null=False, constraints=[
        p.Check('weight >= 0')
    ])
    image = p.CharField(null=True)