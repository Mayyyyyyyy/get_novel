
import requests,base64

home_url = 'https://webapi.gongzicp.com/home/initPcIndex'

header = {
    'User-Agent': 'Mozilla/5.0 (Macintoshntel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

home_res = requests.get(home_url,headers=header).json()

# print(home_res)

novel_id_list = home_res['data']['recList']['finishbookslt']['list']
# print(novel_id_list)

for item in novel_id_list:
    # novel_id = item['novel_id']
    novel_id = 537773
    # print(novel_id)
    novel_url = f'https://www.gongzicp.com/novel-{novel_id}.html'
    novel_res = requests.get(novel_url,headers=header).text

    novel_info_url = f'https://webapi.gongzicp.com/novel/novelInfo?id={novel_id}'
    novel_info_res = requests.get(novel_info_url,headers=header).json()
    author_nickname = novel_info_res['data']['author_nickname']
    novel_name = novel_info_res['data']['novel_name']
    file_name = f'{novel_name}-{author_nickname}'

    chapter_list_url = f'https://webapi.gongzicp.com/novel/chapterGetList?nid={novel_id}'
    chapter_list_res = requests.get(chapter_list_url,headers=header).json()
    # print(chapter_list_res)
    chapter_list = chapter_list_res['data']['list']
    # print(chapter_list)

    for item in chapter_list:
        # print(item)
        if item['type'] == 'item':
            chapter_name = item['name']
            chapter_id = item['id']
            
            chapter_content_url = f'https://webapi.gongzicp.com/novel/chapterGetInfo?cid={chapter_id}&server=0'
            chapter_content_res = requests.get(chapter_content_url,headers=header).json()
            chapter_content = chapter_content_res['data']['chapterInfo']['content']
            # print(chapter_content)
            with open(f'{file_name}.txt',mode='a+') as file:
               file.write(chapter_name)
               file.write('\n')
               file.write(chapter_content)
               file.write('\n')
               print('spider is running, please wait~')
print('over~')

