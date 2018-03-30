#Write import statements for classes invoice and invoice_item
from src.assignments.assignment9.invoice import Invoice
from src.assignments.assignment9.invoice_item import InvoiceItem
'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object
In the loop:
Create a new InvoiceItem
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''


invoice = Invoice('ABC Company', '03282018')
loop = 'y'
while loop == 'y':
    description = input('enter description')
    quantity = int(input('enter quantity'))
    cost = float(input('enter cost'))
    
    invoice_item = InvoiceItem(description, quantity, cost)
    invoice.add_invoice_item(invoice_item)
    
    loop = input('enter y to cont.')

    if loop != 'y':
        invoice.print_invoice()
