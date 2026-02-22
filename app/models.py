import os
import datetime
import peewee as p

DATABASE_PATH = os.getenv("DATABASE_PATH", "app/db.sqlite")

db = p.SqliteDatabase(DATABASE_PATH)

class BaseModel(p.Model):
    class Meta:
        database = db


class Account(BaseModel):
    id = p.AutoField(primary_key=True)
    owner = p.CharField(unique=True, null=False)
    current_balance = p.IntegerField(default=0, constraints=[
        p.Check('current_balance >= 0')
    ])


class Transaction(BaseModel):
    id = p.AutoField(primary_key=True)
    from_account = p.ForeignKeyField(Account, backref="transactions_from", null=False)
    to_account = p.ForeignKeyField(Account, backref="transactions_to", null=False)
    timestamp = p.DateTimeField(default=datetime.datetime.now)
    amount = p.IntegerField(constraints=[
        p.Check('amount > 0')
    ])