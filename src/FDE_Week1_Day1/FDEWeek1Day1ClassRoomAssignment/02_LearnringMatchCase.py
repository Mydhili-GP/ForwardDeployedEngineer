invoices=1000
invoices_approver=["Manager","Director","Supervisor"]

match invoices:
    case invoices if invoices>50000:
        print("Invoice requires Director approval")
    case invoices if invoices>10000:
        print("Invoice requires Supervisor approval")
    case _:
        print("Invoice requires Manager approval")  