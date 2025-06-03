# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# To make items be only text
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags # remove html tags

# function I made
def clean_data(value: str) -> str:
    if not value:
        return ""
    chars_to_remove = ["£"]
    for char in chars_to_remove:
        value = value.replace(char, "")
    return value.strip()


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(
        input_processor = MapCompose(remove_tags, clean_data),
        output_processor = TakeFirst(), # zy css_first
    )
    price = scrapy.Field(
        input_processor = MapCompose(remove_tags, clean_data),
        output_processor = TakeFirst(),
    )
    Available = scrapy.Field(
        input_processor = MapCompose(remove_tags, clean_data),
        output_processor = TakeFirst(),
    )
    UPC = scrapy.Field(
        input_processor = MapCompose(remove_tags, clean_data),
        output_processor = TakeFirst(),
    )
    
