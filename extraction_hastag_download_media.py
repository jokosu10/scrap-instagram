import requests

count = 0
end_cursor = ''
while True:

    url_1 = 'https://www.instagram.com/explore/tags/baksokuahkiller/?__a=1&max_id={}'.format(end_cursor)
    res_1 = requests.get(url_1).json()
    short_codes = res_1['graphql']['hashtag']['edge_hashtag_to_media']['edges']

    for sc in short_codes:
        short_code = sc['node']['shortcode']
        url_2 = 'https://www.instagram.com/p/{}/?__a=1'.format(short_code)
        res_2 = requests.get(url_2).json()
        username = res_2['graphql']['shortcode_media']['owner']['username']

        count += 1
        file_name_media_image = '{} {}.jpg'.format(count, username)
        file_name_media_video = '{} {}.mp4'.format(count, username)
        path_image = 'result_media_download/{}'.format(file_name_media_image)
        path_video = 'result_media_download/{}'.format(file_name_media_video)

        is_video = res_2['graphql']['shortcode_media']['is_video']

        if is_video == True:
            url_media_video_download = res_2['graphql']['shortcode_media']['video_url']
            res_url_media_video_download = requests.get(url_media_video_download).content
            open(path_video, 'wb').write(res_url_media_video_download)

        if is_video == False:
            url_media_image_download = res_2['graphql']['shortcode_media']['display_url']
            res_url_media_image_download = requests.get(url_media_image_download).content
            open(path_image, 'wb').write(res_url_media_image_download)

        print(count, short_code, username)

    end_cursor = res_1['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
    has_next_page = res_1['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']

    if has_next_page == False:
        break