import websocket, json, pprint, talib, numpy
import config
from binance.client import Client
from binance.enums import *


SOCKET = 'wss://stream.binance.com:9443/ws/ethusdt@kline_1m'

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'ETHUSDT'
TRADE_QUANTITY = 0.05

closes = []
in_position = False

# client = Client(config.API_KEY , config.config.API_SECRET , testnet=True)

def buy(symbol, quantity, side, order_type=ORDER_TYPE_MARKET):
    order = client.create_test_order(
    symbol=symbol,
    side=side,
    type=order_type,
    quantity=quantity)

def on_open(ws):
    print('opened connection')

def on_close():
    print('closed connection')

def on_message(ws, message):
    global closes

    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']


    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)

        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print('All RSIs calculated so far:')
            print(rsi)
            last_rsi = rsi[-1]
            print("the last RSI is {}".format(last_rsi))

            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print('OVERBOUGHT, SELL! SELL ! SELL! ')
                    # put binance sell order here 
                    
                else:
                    print('It is OVERBOUGHT but already in the trade, nothing to do.')
            
            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print('It is OVERSOLD but already in the trade, nothing to do.')
                else:
                    print('OVERSOLD, BUY! BUY! BUY!')
                    # put binance buy order here 




#ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
#ws.run_forever()
on_close()
on_close()
on_close()
on_close()
on_close()