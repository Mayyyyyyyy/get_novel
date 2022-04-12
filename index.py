import requests,parsel
from random import randint

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
# proxy = {'https': '106.46.136.112:808'}


url = 'https://www.qbiqu.com/95_95628/'
res = requests.get(url, headers=headers).text.encode('iso-8859-1').decode('gbk')
# print(res)

selector = parsel.Selector(res)
novel_name = selector.css('#info h1::text').get()
# print(novel_name)
chapter_name = selector.css('#list dd a::attr(href)').getall()
# print(chapter_name)
for chapter in chapter_name:
#    print(chapter)
   link_url = 'https://www.qbiqu.com'+chapter
  #  print(link_url)
   chapter_data = requests.get(
       link_url, headers=headers).text.encode('iso-8859-1').decode('gbk')
  #  print(chapter_data)
   chapterSelector = parsel.Selector(chapter_data)
   chapter_title = chapterSelector.css('.bookname h1::text').get()
   chapter_content = chapterSelector.css('#content::text').getall()
   content = '\n'.join(chapter_content)
  #  print(content)
   with open(f'{novel_name}.txt', mode='a', encoding='utf-8') as file:
     file.write(chapter_title)
     file.write('\n')
     file.write(content)
     file.write('\n')
  #  break
   


