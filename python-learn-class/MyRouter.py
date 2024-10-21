class MyRouter(object) :
    "This is class describe about router"
    def __init__(self, routername, model, serialno, ios) :
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
    def print_router(self, manuf_date) :
        print("Router Name : ", self.routername)
        print("Model : ", self.model)
        print("Serial No : ", self.serialno)
        print("IOS : ", self.ios)
        print("Manufacture Date : ", manuf_date)    