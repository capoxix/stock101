import requests

url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/get-full"

querystring = {"id":"adsmi:ind,aex:ind,co1:com,gc1:com"}

headers = {
    'x-rapidapi-key': "ed85df5751mshfb21ab5d9a644fcp1a74abjsnb84e74b991d9",
    'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)