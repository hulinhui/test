import asyncio
import aiohttp

async def getch():
	async with aiohttp.ClientSession() as session:
		async with session.get('http://httpbin.org/get') as response:
			print(response.status)
			print (await response.text()) 

getch()





'''
async def fetch(session,url):
	async with session.get(url) as response:
		return await response.text()
		

async def main():
	async with aiohttp.ClientSession() as session:
		html=await fetch(session,'http://python.org')
		print(html)



if __name__ == '__main__':
	loop=asyncio.get_event_loop()
	loop.run_until_complete(main())
'''
#连接器
conn=aiohttp.TCPConnector()
session=aiohttp.ClientSession(connector=conn)

#限制连接池大小
conn=aiohttp.TCPConnector(limit=30)