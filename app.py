from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS pour éviter les erreurs navigateur

app = Flask(__name__)
CORS(app)  # Active CORS pour permettre l'accès depuis ton site web

@app.route('/')  # Page d'accueil pour vérifier que l'API tourne bien
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
    app.run(debug=True, port=5000)  # Port 5000 par défaut

