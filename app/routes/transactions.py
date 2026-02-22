from flask import Blueprint, jsonify, request, abort, redirect, url_for
from playhouse.shortcuts import model_to_dict, dict_to_model
import peewee as p

from ..models import Transaction, Account, db

transactions_bp = Blueprint("transactions", __name__)

@transactions_bp.route('/transactions', methods=['POST'])
def transactions_create():
    if not request.is_json:
        return abort(400)

    json_payload = request.json['transaction']
    json_payload['id'] = None

    new_transaction = dict_to_model(Transaction, json_payload)

    with db.atomic() as transaction:
        try:
            new_transaction.save()

            Account.update(
                current_balance=Account.current_balance - new_transaction.amount
            ).where(Account.id == new_transaction.from_account.id).execute()

            Account.update(
                current_balance=Account.current_balance + new_transaction.amount
            ).where(Account.id == new_transaction.to_account.id).execute()

            transaction.commit()
        except p.IntegrityError:
            transaction.rollback()
            return jsonify({"error": "Fonds insuffisants"}), 422
        except:
            transaction.rollback()
            return abort(400)

    return redirect(url_for("transactions.transactions_get", id=new_transaction.id))


@transactions_bp.route('/transactions/<int:id>', methods=['GET'])
def transactions_get(id):
    transaction = Transaction.get_or_none(id)
    if transaction is None:
        return abort(404)

    return jsonify(model_to_dict(transaction))