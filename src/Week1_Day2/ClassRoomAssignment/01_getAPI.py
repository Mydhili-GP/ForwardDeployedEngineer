import requests
URL="https://jsonplaceholder.typicode.com/users"
reposnse=requests.get(URL)
print(reposnse.status_code)
# print(reposnse.json())
users=reposnse.json()
for user in users:
    name=user['name']
    company=user['company']['name']
    phone_extension=user['phone'].split('x')
    if len(phone_extension)>1:
        phone_extension=phone_extension[1]
    else:
        phone_extension="No extension"
    print(f"{name}, {company}, {phone_extension}")
   
