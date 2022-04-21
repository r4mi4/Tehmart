# Tehmart scraping by Scrapy

I made this project to try [Scrapy](https://scrapy.org/).

product :

    {
        "name": "پاد سیستم VAPORESSO مدل ZERO نقره ای",
        "price": "5,350,000ریال", 
        "price_before_discount": "6,800,000ریال",
        "description": "\nپاد سیستم VAPORESSO  مدل ZERO ...",
        "specifications": {"توان خروجی": "9 , 10.5 , 12.5 وات", "جنس": "سری(Pod) PCTG"}
    }

# Run

## Create and activate virtual env

    python3 -m venv venv
    . ./venv/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Check spiders contracts

    scrapy check tehmart

## Scrap

    scrapy crawl tehmart