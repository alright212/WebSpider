import requests
from bs4 import BeautifulSoup
import json


class EbayGardenTractorsScraper:

    def __init__(self):
        self.url_base = 'https://www.ebay.com/sch/i.html?_nkw=garden+tractors&_pgn='
        self.product_list = []

    def scrape(self):
        for page_number in range(1, 9):
            url = self.url_base + str(page_number)
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            products = soup.find_all('div', class_='s-item__wrapper clearfix')

            for product in products:
                title = product.find('span', {'role': 'heading', 'aria-level': '3'})
                if title:
                    title = title.text.strip()
                else:
                    continue

                price = product.find('span', class_='s-item__price')
                if price:
                    price = price.text.strip()
                else:
                    price = None

                image_wrapper = product.find('div', class_='s-item__image-wrapper')
                if image_wrapper:
                    image = image_wrapper.find('img')
                    if image and 'src' in image.attrs:
                        image_url = image['src']
                    else:
                        image_url = None
                else:
                    image_url = None

                self.product_list.append({
                    'Title': title,
                    'Price': price,
                    'Image URL': image_url
                })

    def save_to_json(self):
        with open('ebay_garden_tractors.json', 'w') as f:
            json.dump(self.product_list, f, indent=4)
        print('Scraped eBay garden tractors and saved to ebay_garden_tractors.json')


if __name__ == '__main__':
    scraper = EbayGardenTractorsScraper()
    scraper.scrape()
    scraper.save_to_json()
