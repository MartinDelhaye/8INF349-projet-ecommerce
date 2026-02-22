from flask import Blueprint, jsonify, request, abort, redirect, url_for
from playhouse.shortcuts import model_to_dict, dict_to_model
import peewee as p

from ..models import Account

accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route('/accounts', methods=['GET'])
def accounts():
    accounts = [model_to_dict(a) for a in Account.select()]
    return jsonify(accounts)


@accounts_bp.route('/accounts/<int:id>', methods=['GET'])
def accounts_get(id):
    account = Account.get_or_none(id)
    if account is None:
        return abort(404)
    return jsonify(model_to_dict(account))


@accounts_bp.route('/accounts', methods=['POST'])
def accounts_create():
    if not request.is_json:
        return abort(400)

    json_payload = request.json['account']
    json_payload['id'] = None

    new_account = dict_to_model(Account, json_payload)

    try:
        new_account.save()
    except p.IntegrityError:
        return jsonify({
            "error": "Un compte avec le même propriétaire existe déjà"
        }), 422

    return redirect(url_for("accounts.accounts_get", id=new_account.id))