import os
import time
from flask import request, jsonify
from werkzeug.utils import secure_filename

import utils.files as file_util

import services.ranker as ranker

from __main__ import app


@app.route('/ranker/demo', methods=['POST'])
def demo():
    consider_emoji = request.json['consider_emoji']
    consider_emphasized_text = request.json['consider_emphasized_text']
    data = ranker.demo('product_id', 'review_body', 15,
                       consider_emoji, consider_emphasized_text)

    return jsonify({
        'status': True,
        'message': 'Demo ranked products',
        'data': data
    })


@app.route('/ranker/demo/<product_id>/reviews/sentiments', methods=['POST'])
def demo_reviews_sentiments(product_id):

    data = ranker.demo_reviews_sentiments(
        product_id, 'product_id', 'review_body', 15)

    return jsonify({
        'status': True,
        'message': 'Demo products reviews sentiments',
        'data': data
    })


@app.route('/ranker/process-csv', methods=['POST'])
def rank_custom_csv():

    file = request.files['csv_file']
    filename = str(time.time()) + secure_filename(file.filename)
    file_path = os.path.join(file_util.get_upoad_path(), filename)
    file.save(file_path)

    product_id_column = request.form["product_id_column"]
    review_text_column = request.form["review_text_column"]
    max_products_amount = int(request.form["max_products_amount"])
    consider_emoji = bool(int(request.form["consider_emoji"]))
    consider_emph_text = bool(int(request.form["consider_emph_text"]))

    data = ranker.rank_custom_csv(file_path, product_id_column, review_text_column,
                                  max_products_amount, consider_emoji, consider_emph_text)

    return jsonify({
        'status': True,
        'message': 'Ranked Custom CSV',
        "data": data,
        "file_name": filename
    })


@app.route('/ranker/custom-csv/<product_id>/reviews/sentiments', methods=['POST'])
def custom_csv_reviews_sentiments(product_id):
   
    max_products_amount = request.json['max_products_amount']
    file_name = request.json['file_name']

    data = ranker.custom_csv_reviews_sentiments(
        os.path.join(file_util.get_upoad_path(), file_name),
        product_id,
        'product_id',
        'review_body',
        max_products_amount
    )

    return jsonify({
        'status': True,
        'message': 'Custom CSV products reviews sentiments',
        'data': data
    })
