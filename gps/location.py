class Location:
    #                      0         1          2
    #     _statusArr = ['未定位','非差分定位','差分定位']
    def __init__(self,status = 0, longitude =0.00, latitude =0.00,time = ' ',satelliteNum = 0):
        self.status = status
        self.longitude = longitude
        self.latitude = latitude
        self.time = time
        self.satelliteNum = satelliteNum

    def __str__(self):
        return "Location(status={}, longitude={}, latitude={},time={}, satelliteNum={})".format(
            self.status, self.longitude, self.latitude, self.time, self.satelliteNum)
    
    @property
    def __dict__(self):
        return {
            "status": self.status,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "time": self.time,
            "satelliteNum": self.satelliteNum
        }
    
    @staticmethod
    def strToLocation(info):
        def lonOrlatToFloat(dms):
             arr=dms.split(".")
             integer=arr[0]
             decimals=float(dms)%1
             integerLen=len(integer)
             degrees=float(integer[:integerLen-2])
             minutes=float(integer[integerLen-2:integerLen])
             seconds=(decimals*60) 
             return degrees + minutes / 60 + seconds / 3600
        
        try:
            infoArr=info.split(',')
            if len(infoArr) == 15 and infoArr[6] != "0" :
                timeStr=infoArr[1]
                latStr=infoArr[2]
                lonStr=infoArr[4]
                statusNum=int(infoArr[6])
                satelliteNum=int(infoArr[7])

                hour = int(timeStr[:2])
                minute = timeStr[2:4]
                second = timeStr[4:6]
                hour += 8
                if hour >= 24:
                   hour -= 24
                timeStr= str(hour) +':'+minute+':'+second
                return Location(statusNum,lonOrlatToFloat(lonStr),lonOrlatToFloat(latStr),timeStr,satelliteNum)
            return None
        except Exception as e:
            print("error: {}",e)
            return None
    



