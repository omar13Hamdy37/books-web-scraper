import scrapy

# To go to many pages
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import BooksItem
# for making a list of items
from scrapy.loader import ItemLoader

class ProductsSpider(CrawlSpider):
    name = "Products"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    rules = (
        Rule(LinkExtractor(allow=(r"/catalogue/page-\d+\.html",))),
        # Callback for extracting data it will call parseItem function
        Rule(LinkExtractor(allow=(r"/catalogue/[^/]+_\d+/index\.html$")), callback="parseItem"),

    )

    def parseItem(self, response):

        loader = ItemLoader(item = BooksItem(), response = response) #second response is in func param
        # add css because we use css selectors
        loader.add_css("title", "div.col-sm-6.product_main h1")
        loader.add_css("price", "p.price_color")
        loader.add_xpath("Available", "normalize-space(//p[@class='instock availability'])")
        loader.add_css("UPC", "table.table.table-striped tr:nth-child(1) td")

        return loader.load_item()
