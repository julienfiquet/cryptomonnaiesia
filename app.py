from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Active CORS pour autoriser les requêtes depuis un site web

@app.route('/recommend', methods=['GET'])
def recommend_cryptos():
    data = [
        {"name": "Bitcoin", "symbol": "BTC", "current_price": 50000},
        {"name": "Ethereum", "symbol": "ETH", "current_price": 3000},
        {"name": "Solana", "symbol": "SOL", "current_price": 150},
    ]
    return jsonify(data)  # Retourne les cryptos en JSON

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Assure-toi que le port est bien
def recommend_cryptos():
    data = [
        {"name": "Bitcoin", "symbol": "BTC", "current_price": 50000, "change": "+3%", "volume": "35B"},
        {"name": "Ethereum", "symbol": "ETH", "current_price": 3000, "change": "-1.2%", "volume": "15B"},
        {"name": "Solana", "symbol": "SOL", "current_price": 150, "change": "+5%", "volume": "3B"},
    ]
    return jsonify(data)
