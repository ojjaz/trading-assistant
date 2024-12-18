from flask import Flask, jsonify, request

app = Flask(__name__)

# Заглушка для данных о ценах акций
mock_data = {
    "AAPL": {"price": 189.50, "change": 1.2},
    "MSFT": {"price": 345.10, "change": -0.5},
    "GOOGL": {"price": 2765.00, "change": 0.3}
}

@app.route('/')
def home():
    return "Trading Assistant is running!"

@app.route('/get-price/<ticker>', methods=['GET'])
def get_price(ticker):
    stock = mock_data.get(ticker.upper())
    if stock:
        return jsonify({"ticker": ticker.upper(), "price": stock["price"], "change": stock["change"]})
    return jsonify({"error": "Ticker not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
