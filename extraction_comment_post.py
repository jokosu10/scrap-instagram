import time
import requests
import json
import csv

url = 'https://www.instagram.com/graphql/query/'
#short_code = 'CDL_c7Mj-ie'

end_cursor = ''
count = 0
counter_file = 1
sum_page_file = 100

short_code = input('Please enter a short code post instagram : ')

writer = csv.writer(open('result_comment/{} {}.csv'.format(short_code, counter_file), 'w', newline=''))
headers = ['No', 'User Name', 'Comment']
writer.writerow(headers)

while 1:

    var = {
            #"shortcode": "CDL_c7Mj-ie",
            "shortcode": short_code,
            "first": 50,
            "after": end_cursor
    }

    params = {
        'query_hash': 'bc3296d1ce80a24b1b6e40b1e72903f5',
        'variables': json.dumps(var)
    }

    response = requests.get(url, params).json()

    comments = response['data']['shortcode_media']['edge_media_to_parent_comment']['edges']

    try:
        comments = response['data']['shortcode_media']['edge_media_to_parent_comment']['edges']
    except:
        print('Waiting for 30 seconds...')
        time.sleep(30)
        continue

    for comment in comments:
        if count % sum_page_file == 0 and count != 0:
            counter_file += 1
            writer = csv.writer(open('result_comment/{} {}.csv'.format(short_code, counter_file), 'w', newline=''))
            headers = ['No', 'User Name', 'Comment']
            writer.writerow(headers)

        username = comment['node']['owner']['username']
        text = comment['node']['text']
        count += 1
        print(count, username, text)
        writer = csv.writer(open('result_comment/{} {}.csv'.format(short_code, counter_file), 'a', newline='', encoding='utf-8'))
        datas = [count, username, text]
        writer.writerow(datas)

    end_cursor = response['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['end_cursor']
    has_next_page = response['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['has_next_page']

    if has_next_page == False:
        break

    time.sleep(3)