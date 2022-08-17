import requests


endpoint = "http://localhost:8080/register/newuser/"
endpoint2 = "http://localhost:8083/scraper/newinfo/"


data = {
    'email_address': 'newtest2_gmail22',
    'keyword': "apple22"
}

data2 = {
    'time': "08-07-202211111",
    'page': "google22",
    'info': "duke22"
}
get_response = requests.post(endpoint2, json=data2)

get_response = requests.post(endpoint, json=data)


# print(get_response.json())
