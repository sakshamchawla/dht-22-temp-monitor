import time
import adafruit_dht
import board
import threading
from services.database import *
from services.api import *

dht_device = adafruit_dht.DHT22(board.D23)

def temps():
    conn = set_up_db()
    go()
    while True:
        try:
            temperature_c = dht_device.temperature
            temperature_f = temperature_c * (9 / 5) + 32

            humidity = dht_device.humidity

            save_data(conn, temperature_c, temperature_f, humidity, 1)
        except RuntimeError as err:
            print(err.args[0])

        time.sleep(60.0)

def main():
    threading.Thread(target=go,
                    daemon=False).start()    

    threading.Thread(target=temps,
                    daemon=False).start()    

if __name__ == '__main__':
    main()