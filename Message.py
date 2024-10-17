class Message:
    def __init__(self,code,data):
        self.code=code
        self.data=data
    
    def __str__(self):
        return "Message(code:{},data:{})".format(self.code,self.data)
    
    @property
    def __dict__(self):
        return {
            "code": self.code,
            "data": self.data
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d['code'], d['data'])

