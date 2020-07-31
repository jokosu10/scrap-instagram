import requests
import json
import time

url = 'https://www.instagram.com/graphql/query/'
end_cursor = ''
count = 0

short_code = input('Please enter a short code post instagram : ')

while 1:

    var = {
        # "shortcode": "CDL_c7Mj-ie",
        "shortcode": short_code,
        "include_reel": True,
        "first": 50,
        "after": end_cursor
    }

    params = {
        'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
        'variables': json.dumps(var)
    }

    response = requests.get(url, params).json()

    try:
        users = response['data']['shortcode_media']['edge_liked_by']['edges']
    except:
        print('Waiting for 30 seconds...')
        time.sleep(30)
        continue

    for user in users:
        username = user['node']['username']
        fullname = user['node']['full_name']
        profile_pic = user['node']['profile_pic_url']
        count += 1
        print(count, username, fullname, profile_pic)

    end_cursor = response['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    has_next_page = response['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']

    if has_next_page == False:
        break

    time.sleep(2)
