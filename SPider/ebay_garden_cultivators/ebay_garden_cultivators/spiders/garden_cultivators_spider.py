import scrapy
import json


class GardenCultivatorsSpider(scrapy.Spider):
    name = 'garden_cultivators_spider'
    allowed_domains = ['ebay.com']
    start_urls = [f'https://www.ebay.com/sch/i.html?_nkw=garden+cultivators&_pgn={page}' for page in range(1, 9)]

    def start_requests(self):
        self.product_list = []
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        products = response.css('div.s-item__wrapper.clearfix')

        for product in products:
            title = product.css('span[role="heading"][aria-level="3"]::text').get()
            if not title:
                continue
            title = title.strip()

            price = product.css('span.s-item__price::text').get()
            if price:
                price = price.strip()
            else:
                price = None

            image_url = product.css('div.s-item__image-wrapper img::attr(src)').get()

            self.product_list.append({
                'Title': title,
                'Price': price,
                'Image URL': image_url
            })

        if len(self.product_list) > 0 and response.url == self.start_urls[-1]:
            with open('garden_cultivators.json', 'w') as f:
                json.dump(self.product_list, f, indent=4)

            print('Scraped eBay garden cultivators and saved to garden_cultivators.json')
