class car:
    def __init__(selfi,window,door,engine):
        selfi.window=window
        selfi.door=door
        selfi.engine=engine


    def self_driving(self):
        print("This is  car with {} engine ".format(self.engine))

car1=car(2,4,"petrol")
print(car1.door)

car1.self_driving()

