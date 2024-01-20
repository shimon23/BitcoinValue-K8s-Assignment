import threading
import time
from flask import Flask
import requests
from datetime import datetime, timedelta



app = Flask(__name__)
@app.route("/")
def home():
    return f"Service A, bitcoin value is {get_bitcoin_rate()}$ for {timestamp()}"



def get_bitcoin_rate():
    api_url ="https://blockchain.info/tobtc?currency=USD&value=1"
    response  = requests.get(api_url)
    btc_to_usd = 1/float(response.text)
    return btc_to_usd

def bitcoin_thread():
    avarage_10 = [ ]
    minutes = 0

    while True:
        bitcoin_value = get_bitcoin_rate()
        print(f"Bitcoin value is {bitcoin_value}$ for {timestamp()}")
        avarage_10.append(bitcoin_value)
        # Sleep for 1 minute
        time.sleep(60)
        minutes = minutes + 1
        # Calculate and print average every 10 minutes
        if minutes == 10:            
            print(f"Average Bitcon rate for the last 10 minutes: {list_verage(avarage_10)}$")
            minutes = 0
            avarage_10 = [ ]


def timestamp():
        return datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

def list_verage(lst):
    return sum(lst) / len(lst) 

if __name__ == "__main__":
    bitcoin_thread = threading.Thread(target=bitcoin_thread)
    bitcoin_thread.daemon = True
    bitcoin_thread.start()

    # Run the Flask application
    app.run(debug=True)

