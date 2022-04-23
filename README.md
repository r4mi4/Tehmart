# Tehmart scraping by Scrapy

I made this project by [Scrapy](https://scrapy.org/).

product :

    {
        "name": "پاد سیستم VAPORESSO مدل ZERO نقره ای",
        "price": "5,350,000ریال", 
        "price_before_discount": "6,800,000ریال",
        "image_link": "https://www.tehmart.ir/media/uploads/catalog/default/product_154_1628600412_14505.jpg",
        "page_link": "https://www.tehmart.ir/product-154/%D9%BE%D8%A7%D8%AF-%D8%B3%DB%8C%D8%B3%D8%AA%D9%85-smok-%D9%85%D8%AF%D9%84-novo-%D8%B3%D9%81%DB%8C%D8%AF",
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

## Save inside specific file

    scrapy crawl tehmart -O filename.json
    or
    scrapy crawl tehmart -O filename.csv
    or
    scrapy crawl tehmart -O filename.xml

#### There is another way to save file like json file 
    scrapy crawl tehmart -O filename.jl
This format better than json ...