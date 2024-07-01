import requests
from bs4 import BeautifulSoup
import json
import scrapper
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/training-data', methods=['GET'])
def get_training_data():
    competency_id = request.args.get('competency_id')
    if not competency_id:
        return jsonify({"error": "Competency ID parameter is required"}), 400

    data = scrapper.scrape_training_data(competency_id)
    if not data:
        return jsonify({"error": "Failed to retrieve data for the provided competency ID"}), 404

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
