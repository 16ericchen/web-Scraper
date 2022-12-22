from playwright.async_api import async_playwright
import time,re,asyncio
start_time = time.time()
validDistributors = ["Digi-Key",'Arrow Electronics','Future Electronics','Verical','Newark','Mouser Electronics','Mouser','Master','Rochester','Master Electronics']
 

async def main():
    async with async_playwright() as pw:
        browser = await pw.firefox.launch()
        page = await browser.new_page()
        await page.goto("https://octopart.com/search?q=GRM188R6YA106MA73&currency=USD&specs=0")
        distributor = await page.query_selector('//div[contains(@class, "prices-view")]')
        distributorTest = await distributor.query_selector_all('//div[contains(@class, "part")]')
        for x in distributorTest:
            footer = await x.query_selector('//div[contains(@class, "footer")]')
            button = await footer.query_selector('//button[contains(@type, "button")]')
            await button.click()
            test = await x.query_selector_all('//a[contains(@class, "expander")]')
            for m in test:
                await m.click()
            table = await x.query_selector('tbody')
            tableRow = await table.query_selector_all('tr')
            for y in tableRow:
                test2 = await y.query_selector_all('td')
                valid = await test2[1].inner_text()
                valid = re.sub("[0-9]", "", valid.replace('\n',''))
                if valid in validDistributors:
                    for z in test2:
                        print(await z.inner_text())
                else:
                    continue
        await browser.close()





# Octopath with expander in for loop
# async def main():
#     async with async_playwright() as pw:
#         browser = await pw.firefox.launch()
#         page = await browser.new_page()
#         await page.goto("https://octopart.com/search?q=GRM188R6YA106MA73&currency=USD&specs=0")
#         distributor = await page.query_selector('//div[contains(@class, "prices-view")]')
#         distributorTest = await distributor.query_selector_all('//div[contains(@class, "part")]')
#         for x in distributorTest:
#             footer = await x.query_selector('//div[contains(@class, "footer")]')
#             button = await footer.query_selector('//button[contains(@type, "button")]')
#             await button.click()
#             table = await x.query_selector('tbody')
#             tableRow = await table.query_selector_all('tr')
#             for y in tableRow:
#                 test2 = await y.query_selector_all('td')
#                 for z in range(len(test2)):
#                     # if z == 1:
#                     #     expander = await test2[z].query_selector('//a[contains(@class, "expander")]')
#                     #     if expander:
#                     #         print('expander text: ',await expander.inner_text())
#                     #         await expander.click()
#                     print(await test2[z].inner_text())
#         await browser.close()






# OEMTrades
# async def main():
#     async with async_playwright() as pw:
#         browser = await pw.firefox.launch()
#         page = await browser.new_page()
#         await page.goto("https://www.oemstrade.com/search/GRM0225C1C221JA02")
#         distributor = await page.query_selector_all('.distributor-results')
#         for x in distributor:
#             distributorName = await x.query_selector('.distributor-title')
#             subtract = await distributorName.query_selector('span')
#             z = await distributorName.inner_text()
#             w = await subtract.inner_text()
#             # distributor
#             z = z.replace(w,'')
#             if z.strip() in validDistributors:
#                 getInfo = await x.query_selector('tbody')
#                 stock = await getInfo.query_selector('.td-stock')
#                 stockk = await stock.inner_text()
#                 stockk = re.sub("[^0-9]", "", stockk.replace("\n", ""))
#                 # instock value
#                 if int(stockk) > 0:
#                     prices = await getInfo.query_selector('.td-price')
#                     click = await prices.query_selector(".show-more")
#                     await click.click()
#                     mnf = await getInfo.query_selector('.td-part-number')
#                     mnfValue = await mnf.query_selector('a')
#                     manufacturer = await getInfo.query_selector('.td-distributor-name')
#                     # manufacturer
#                     print(await manufacturer.inner_text())
#                     # part number
#                     print(await mnfValue.inner_text())
#                     # prices
#                     print(await prices.inner_text())
#         await browser.close()

# FindChips
# async def main():
#     async with async_playwright() as pw:
#         browser = await pw.firefox.launch()
#         page = await browser.new_page()
#         await page.goto("https://www.findchips.com/search/5PB1106CMGI")
#         distributor = await page.query_selector_all('.distributor-results')
#         for x in distributor:
#             distributorName = await x.query_selector('.distributor-title')
#             name = await distributorName.query_selector('a')
#             subtract = await distributorName.query_selector('.other-disti-details')
#             z = await name.inner_text()
#             w = await subtract.inner_text()
#             # distributor name
#             z = z.replace(w,'')
#             if z.strip() in validDistributors:
#                 getInfo = await x.query_selector('tbody')
#                 stock = await getInfo.query_selector('.row')
#                 # instock value
#                 stockk =await stock.get_attribute('data-instock')
#                 if int(stockk) > 0:
#                     prices = await getInfo.query_selector('.td-price')
#                     click = await prices.query_selector(".hyperlink")
#                     await click.click()
#                     # prices
#                     mnf = await getInfo.query_selector('.td-mfg')
#                     # part number
#                     pn = await stock.get_attribute('data-mfrpartnumber')
#                     print(await mnf.inner_text())
#                     print(await prices.inner_text())
#                     print(pn)
#         await browser.close()
 
if __name__ == '__main__':
    asyncio.run(main())
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    # checks the stock and distributor
    # async with async_playwright() as pw:
    #     browser = await pw.firefox.launch()
    #     # browser = await pw.chromium.launch()
    #     page = await browser.new_page()
    #     await page.goto("https://www.findchips.com/search/5PB1106CMGI")
 
    #     all_items = await page.query_selector_all('tbody')
    #     books = []
    #     distributor = await page.query_selector_all('.distributor-results')
    #     for x in distributor:
    #         distributorName = await x.query_selector('.distributor-title')
    #         name = await distributorName.query_selector('a')
    #         subtract = await distributorName.query_selector('.other-disti-details')
    #         z = await name.inner_text()
    #         w = await subtract.inner_text()
    #         z = z.replace(w,'')
    #         if z.strip() in validDistributors:
    #             getInfo = await x.query_selector('tbody')
    #             stock = await getInfo.query_selector_all('.row')
    #             for x in stock:
    #                 getStock = await x.query_selector('.td-stock')
    #                 try: 
    #                     if int(await getStock.inner_text()) > 0:
    #                         print(await getStock.inner_text())
    #                 except:
    #                     pass

# ------gets the distributor name------
    # async with async_playwright() as pw:
    #     browser = await pw.firefox.launch()
    #     # browser = await pw.chromium.launch()
    #     page = await browser.new_page()
    #     await page.goto("https://www.findchips.com/search/5PB1106CMGI")
 
    #     all_items = await page.query_selector_all('tbody')
    #     books = []
    #     distributor = await page.query_selector_all('.distributor-results')
    #     for x in distributor:
    #         distributorName = await x.query_selector('.distributor-title')
    #         name = await distributorName.query_selector('a')
    #         subtract = await distributorName.query_selector('.other-disti-details')
    #         z = await name.inner_text()
    #         w = await subtract.inner_text()
    #         print(z,w)
    #         z = z.replace(w,'')
    #         print(z)
    #     await browser.close()




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