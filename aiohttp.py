import aiohttp
import asyncio
import ssl

async def main(loop):
    options = {
        "headers":{"User-Agent": "aloha123"},
        "cookies" : {'cookies_are': 'working'}
    }
    
    url_list = ['https://api.pushshift.io/reddit/search/comment/?q=Nestle&size=30&after=1530396000&before=1530436000',
                'https://api.pushshift.io/reddit/search/comment/?q=Nestle&size=30&after=1530436000&before=1530476000']
    
    async def fetch_all(urls, loop):
        # method to make requests
        async def fetch(session, url):
            async with session.get(url, ssl=ssl.SSLContext()) as response:
                return await response.json()

        async with aiohttp.ClientSession(loop=loop, **options) as session:
            results = await asyncio.gather(*[fetch(session, url) for url in urls], return_exceptions=True)
            return results

    html = await fetch_all(url_list, loop)
    print(html)

    # async with aiohttp.ClientSession(**options) as session:
    #     async with session.get('http://ns559501.ip-54-39-51.net:7097/echo.php') as response:

    #         print("Status:", response.status)
    #         print("Content-type:", response.headers['content-type'])

    #         html = await response.text()
    #         print("Body:", html[:], "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
