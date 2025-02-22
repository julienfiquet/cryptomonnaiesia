import os
from flask import Flask, jsonify
from flask_cors import CORS  # Importer CORS pour éviter les erreurs de requêtes bloquées

app = Flask(__name__)
CORS(app)  # Active CORS

@app.route('/')
def home():
    return "Bienvenue sur l'API de Cryptomonnaies !"

@app.route('/recommend', methods=['GET'])
def recommend_cryptos():
    data = [
        {"name": "Bitcoin", "symbol": "BTC", "current_price": 50000},
        {"name": "Ethereum", "symbol": "ETH", "current_price": 3000},
        {"name": "Solana", "symbol": "SOL", "current_price": 150},
    ]
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Utiliser le port défini par Railway
    app.run(debug=True, host="0.0.0.0", port=port)
