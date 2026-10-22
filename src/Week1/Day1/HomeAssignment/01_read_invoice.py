import csv
total_invoice =0
total_invoice_above=0
invalid_invoice=0


with open('D:\\FDE\\Workspace\\ForwardDeployedEngineer\\src\\Week1\\Day1\\data\\homework_invoices.csv', mode='r') as inputFile:
    DataReadFromCSV=csv.DictReader(inputFile)
    for row in DataReadFromCSV:
        # print("Vendor:", row['vendor'], "Amount:", row['amount'], "Status:", row['status'])
       total_invoice +=1
       try:
            invoice_amount= float(row['amount'])
            if invoice_amount>100000:     
                        total_invoice_above +=1
                        print("number of invoice greater than 100000 is:", row)
       except ValueError:
             invalid_invoice +=1
             print("Invalid invoice amount:", row['amount'], "for vendor:", row['vendor'])  


    print("Total number of invoices:", total_invoice)
    print("Total number of invoices greater than 100000:", total_invoice_above)
    print("Total number of invalid invoices:", invalid_invoice) 
                      