import csv
from itertools import count

with open('src\\FDE_Week1_Day1\\data\\homework_invoices.csv', mode='r') as inputfile ,\
     open('src\\FDE_Week1_Day1\\data\\homework_invoices_output.csv', mode='w', newline='') as outputfile:
    csv_reader = csv.DictReader(inputfile)  
    writer = csv.DictWriter(outputfile, fieldnames=csv_reader.fieldnames)
    writer.writeheader()

    for row in csv_reader:
        try:
            invoice_Amt=float(row['amount'])
            if invoice_Amt> 100000:
                        writer.writerow(row)
                        print(invoice_Amt)
                       
        except ValueError:
            print(f"Invalid amount found for row: {row}")
           
       