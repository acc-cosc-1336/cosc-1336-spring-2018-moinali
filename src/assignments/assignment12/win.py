from tkinter import Tk, Label
from src.assignments.assignment12.converter import Converter

class Win(Tk):


    def __init__(self):
        Tk.__init__(self, None, None)
        self.km = 100
        self.km_to_miles = Converter.get_miles_from_km(self.km)
        
        self.label1 = Label(self, text='Km:' +str(self.km)).grid(row=0)
        
        self.label2 = Label(self, text='Miles: ' + str(format(self.km_to_miles,'.2f'))).grid(row=1)

        self.mainloop()



