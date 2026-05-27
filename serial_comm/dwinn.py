import serial
import threading
import time

from config import SERIAL_PORT, BAUDRATE

class DWIN:

    def __init__(self):

        self.touch_event = False

        try:

            self.ser = serial.Serial(
                SERIAL_PORT,
                BAUDRATE,
                timeout=0.1
            )

            threading.Thread(
                target=self.listen,
                daemon=True
            ).start()

        except:

            self.ser = None

    def listen(self):

        while True:

            if self.ser.in_waiting:

                data = self.ser.read()

                self.touch_event = True

            time.sleep(0.01)

    def read_touch(self):

        if self.touch_event:

            self.touch_event = False

            return True

        return False
