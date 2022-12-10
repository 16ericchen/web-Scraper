from playwright.async_api import async_playwright
import asyncio


 
async def main():
    async with async_playwright() as pw:
        browser = await pw.firefox.launch()
        # browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.findchips.com/search/5PB1106CMGI")
 
        all_items = await page.query_selector_all('tbody')
        books = []
        distributor = await page.query_selector_all('.distributor-results')
        for x in distributor:
            distributorName = await x.query_selector('.distributor-title')
            name = await distributorName.query_selector('a')
            subtract = await distributorName.query_selector('.other-disti-details')
            z = await name.inner_text()
            w = await subtract.inner_text()
            print(z,w)
            z = z.replace(w,'')
            print(z)
        await browser.close()
 
if __name__ == '__main__':
    asyncio.run(main())



# url = "https://www.findchips.com/search/5PB1106CMGI"
# driver.get(url)


# soup = BeautifulSoup(driver.page_source, "html.parser")
# x = soup.findAll('div', class_='distributor-results')
# for y in x:
#     if y.get('data-distributor_name') in distributors:
#         z=[]
#         print(y.get('data-distributor_name'))
#         tdStock = y.find('td',class_='td-stock')
#         tdPrice = y.find('td',class_='td-price')
#         tdMNF = y.find('td',class_='td-mfg')
#         tdPN = y.find('div',class_="part-name").find('a',class_='onclick').get_text().strip()
#         stock = re.sub("[^0-9]", "", tdStock.get_text().replace("\n", ""))
#         test = tdPrice.findAll('li')
#         # print(tdPN)
#         for x in test:
#             z.append(x.get_text().replace("\n",'').strip().replace(' ','').split('$'))
#         print(tdPN,stock,z,y.get('data-distributor_name'),tdMNF.get_text().strip())




# async def main():
#     async with async_playwright() as pw:
#         browser = await pw.firefox.launch()
#         # browser = await pw.chromium.launch()
#         page = await browser.new_page()
#         await page.goto('https://books.toscrape.com')
 
#         all_items = await page.query_selector_all('.product_pod')
#         books = []
#         for item in all_items:
#             book = {}
#             name_el = await item.query_selector('h3')
#             book['name'] = await name_el.inner_text()
#             price_el = await item.query_selector('.price_color')
#             book['price'] = await price_el.inner_text()
#             stock_el = await item.query_selector('.availability')
#             book['stock'] = await stock_el.inner_text()
#             books.append(book)
#         print(books)
#         await browser.close()
 
# if __name__ == '__main__':
#     asyncio.run(main())