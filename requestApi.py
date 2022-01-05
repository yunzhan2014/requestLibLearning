import requests
##import json
##import rest_client 
## Get 方法
r = requests.get('https://simple-books-api.glitch.me/status')

params_book_type = {'type':'fiction'}

r = requests.get('https://simple-books-api.glitch.me/books', params=params_book_type) 

## Post 方法
book_data = {'bookId':'1', 'customerName':'Vivian Schowalter'}
r_post = requests.post('https://simple-books-api.glitch.me/orders', data=book_data)

base_url = 'https://reqres.in'
reqesIn_api = {'1': '/api/users',
               '2': '/api/user/2'}

s = requests.session()
api1 = base_url + reqesIn_api['1'] 
nr = s.get(api1)

def get_api1():
    return s.get(api1)