class Laptop: 

#add some attributes of a Laptop
    # make = None
    # model = None
    # year = None
    # color = None
#We need a constructor to enclose all our attributes together
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
#add methods. This could be how the Laptop operate

    def touchscreen(self):
        print("This Laptop has a touchscreen")
    
    def shut(self):
        print("This Laptop shuts down after 15 seconds")

