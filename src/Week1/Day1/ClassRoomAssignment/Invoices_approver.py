from unittest import case


invoice_amount=50000
invoices_approver=["Manager","Director","CEO"]
if invoice_amount>50000:
    print("invoices amount is appoved by:" + invoices_approver[2],invoices_approver[1])
elif invoice_amount>25000:
    print("invoices amount is appoved by:" + invoices_approver[1])
elif invoice_amount<1000:
    print("invoices amount is appoved by:" + invoices_approver[0])
else:
    print("not valid invoice amount")

# dont use matcg case when we have conditional checks like greater than or less than. 
# Use match case when we have exact values to check.
match invoice_amount:
    case amount if amount>50000:
        print("invoices amount is appoved by:" + invoices_approver[2],invoices_approver[1])
    case amount if amount>25000:
        print("invoices amount is appoved by:" + invoices_approver[1])
    case amount if amount<1000:
        print("invoices amount is appoved by:" + invoices_approver[0])
    case _:
        print("not valid invoice amount")