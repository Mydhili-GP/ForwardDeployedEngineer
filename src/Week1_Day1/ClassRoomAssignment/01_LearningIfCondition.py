invoice_amount=1000000
invoice_approver=["Manager","Director","Supervisor"]

if invoice_amount>50000:
    print(invoice_approver[1],invoice_approver[0],"can approve the invoice")
elif invoice_amount> 25000:
    print(invoice_approver[0],"can approve the invoice")
elif invoice_amount< 1000:
    print(invoice_approver[2],"can approve the invoice")

   