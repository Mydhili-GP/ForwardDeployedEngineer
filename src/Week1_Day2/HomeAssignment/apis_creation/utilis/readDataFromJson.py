import json

json_path = "../data/InvoiceDataFile.json"
def read_data_from_json():
    with open(json_path) as input_file:
        data = json.load(input_file)        
    return data

def write_data_to_json(data):
    with open (json_path,'w') as output_file:
        json.dump(data,output_file,indent=4)