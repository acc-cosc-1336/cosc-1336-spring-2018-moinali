'''
Create a customer class
Add a constructor with parameters first_name, last_name, and phone_number
Create public attributes for first_name, last_name, and phone_number

STUDENT MUST ALSO MODIFY INVOICE CLASS TO USE THIS CLASS
SEE INVOICE file FOR INSTRUCTIONS
'''

class Customer:

    def __init__(self, first_name, last_name, phone_number,discount=0):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.discount = discount

    def get_discount_rate(self):
        return self.discount
        #ASSIGNMENT11: add discount class attribute and set value to 0

    #ASSIGNMENT11: create a method named get_discount_rate that returns the discount class attribute

