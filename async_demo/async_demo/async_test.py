import asyncio
import aiohttp
import time
from lxml import etree

urls=['https://www.baidu.com','http://www.taobao.com','http://www.jd.com','https://www.sogou.com']
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

#特殊函数
async def get_request(url):
    async with aiohttp.ClientSession() as s:
        async with await s.get(url,headers=headers) as response:
            print('正在下载',url)
            page_text=await response.text()
            return page_text


#回调函数
def parse(task):
    page_text=task.result()
    tree=etree.HTML(page_text)
    div=tree.xpath('//a/@href')
    print(div)

start_time=time.time()
tasks=[]    #存放多任务
for url in urls:
    func=get_request(url)
    task=asyncio.ensure_future(func)
    task.add_done_callback(parse)
    tasks.append(task)


loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

print(f'总耗时：{time.time()-start_time}')

    
