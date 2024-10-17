from machine import UART
import time
from gps.location import Location
class GpsMoule:
    
    def __init__(self,bau=38400):
        self.uart = UART(2, baudrate=bau)
        
    def readline(self):
            try:
                gpsInfo = buff.decode('utf-8').strip()
            except Exception as e:
                return None
            if gpsInfo.startswith('$GPGGA'):
                location=Location.strToLocation(gpsInfo)
                if location  is not None:
                    print(location)
                    return location
            return None