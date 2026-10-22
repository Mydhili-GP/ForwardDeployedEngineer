import requests
URL="https://jsonplaceholder.typicode.com/users"

request=requests.get(URL)
response=request.json()
try:
    
    for i in response:
        name=i["name"]
        company=i["company"]["name"]
        email=i["email"]
        phone_extension=i["phone"].split("x")
        if len(phone_extension)>1:
            phone_extension=phone_extension[1]            
        else:
            phone_extension=""      
        print(f"{name} | {email} | {company} | {phone_extension}")     
    

except requests.exceptions.RequestException as err:
    print(f"Invalid Phone number: {err}")

# print(response)
