import json 

def load():
    with open('D:\\FDE\\Workspace\\ForwardDeployedEngineer\\src\\Week1\\Day2\\HomeAssignment\\data\\Invoices.json','r') as inputFile:
        data = json.load(inputFile)       
    return data
def writeData(data):
    with open('D:\\FDE\\Workspace\\ForwardDeployedEngineer\\src\\Week1\\Day2\\HomeAssignment\\data\\Invoices.json','w') as outputFile:
        json.dump(data, outputFile, indent=4)