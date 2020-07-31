import requests
import json

url = 'https://www.instagram.com/graphql/query/'

short_code = input('Please enter a short code post instagram : ')

var = {
        #"shortcode": "CC0rB2rDKkX",
        "shortcode": short_code,
        "include_reel": True,
        "first": 50
}

params = {
    'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
    'variables': json.dumps(var)
}

response = requests.get(url, params).json()

users = response['data']['shortcode_media']['edge_liked_by']['edges']

count = 0

for user in users:
    username = user['node']['username']
    fullname = user['node']['full_name']
    profile_pic = user['node']['profile_pic_url']
    print(username, fullname, profile_pic)
    count += 1
    print(count)
