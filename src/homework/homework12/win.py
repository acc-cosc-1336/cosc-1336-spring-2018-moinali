from tkinter import Tk, Label, Button
from src.homework.homework12.converter import Converter
#src.homework.homework12.

class Win(Tk):

    def __init__(self):

        self.miles = Converter()
        Tk.__init__(self, None, None)

        self.button_quit = Button(self,text='Quit', command=self.destroy)
        self.button_quit.grid(row=2,column=3)
        
        self.display_conversion_button = Button(self, text='Display Conversion',command=self.display_labels)
        self.display_conversion_button.grid(row=2,column=1)


        self.mainloop()

    def display_labels(self):
        km = 100
        self.label = Label(self, text='Km:' + str(km)).grid(row=0, column=1)
        self.label = Label(self, text='Miles:' + str(self.miles.get_miles_from_km(km))).grid(row=1, column=1)

