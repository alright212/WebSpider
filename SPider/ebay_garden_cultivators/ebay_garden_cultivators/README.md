# Garden Cultivators Scraper

Tegemist on Scrapy projektiga, mille eesmärk on koguda eBayst aiakultivaatorite nimekiri. Saadud andmed sisaldavad iga kuulutuse pealkirja, hinda ja pildi URL-i. Väljund salvestatakse JSON-faili nimega garden_cultivators.json.

## Prerequisites

- Python 3.6 or higher
- Scrapy

## Scrapy Paigaldamine

Scrapy installimiseks kirjutage käsureale järgmine käsk:

```
pip install scrapy
```

## Spider jooksutamine

Ämbliku käivitamiseks ja scrapingu alustamiseks navigeerige projekti juurkataloogi ja käivitage:

```
scrapy crawl garden_cultivators_spider
```

Kui ämblik on crawli lõpetanud, luuakse projekti kataloogis fail nimega garden_cultivators.json. See fail sisaldab kogutud andmeid JSON-vormingus.

## Andmestruktuur

JSON-fail sisaldab objektide massiivi, kus iga objekt esindab aiakultivaatorite loetelu. Igal objektil on järgmised omadused:

- Pealkiri: Aiakultivaatorite pealkiri.
- Hind: Aiakultivaatori hind, kui see on olemas.
- Pildi URL: Aiakultivaatori pildi URL.


### Näidisandmed:
```json
[{
        "Title": "Petrol Cordless Cultivator Rotavator Tiller Garden Soil Vegetable Patch 52cc",
        "Price": "$199.85",
        "Image URL": "https://i.ebayimg.com/thumbs/images/g/PhgAAOSwNNVguzMc/s-l225.jpg"
    },
    {
        "Title": "Fiskars Ergo Cultivator Garden Tool with Aluminum Head and Ergonomic Handle",
        "Price": "$17.88",
        "Image URL": "https://i.ebayimg.com/thumbs/images/g/v14AAOSwGB9kN31u/s-l225.jpg"
    }]
```