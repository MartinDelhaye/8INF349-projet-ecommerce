from flask import Blueprint, jsonify
from playhouse.shortcuts import model_to_dict

from ..models import Product

products_bp = Blueprint("products", __name__)

@products_bp.route('/', methods=['GET'])
def products():
    products = [
        model_to_dict(a) 
        for a in Product.select()
    ]
    response = {
        "products": products
    }
    return jsonify(response)
