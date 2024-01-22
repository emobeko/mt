from flask import Flask, request, jsonify
import json, inspect

app = Flask(__name__)

# Endpoint to handle signals
@app.route('/send_signal', methods=['POST'])
def send_signal():
    data = request.form if request.form else request.json

    action = data.get('action')
    symbol = data.get('symbol')
    quantity = data.get('quantity')

    # Assuming you have a trading module or logic
    # Implement your trading logic here based on the received signal

    if action == 'BUY':
        print(f"Received BUY signal for {symbol} with quantity {quantity}")
        # Place buy order or execute buy logic here
    elif action == 'SELL':
        print(f"Received SELL signal for {symbol} with quantity {quantity}")
        # Place sell order or execute sell logic here
    else:
        print(f"Invalid action: {action}")

    # Send a response back to the client (you can customize this based on your needs)
    return jsonify({'status': 'success', 'message': 'Signal received successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80, debug=True)
