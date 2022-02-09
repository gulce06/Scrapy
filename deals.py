import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.groupon.com']
    start_urls = ['https://www.groupon.com/landing/deal-of-the-day']

    def parse(self, response):
        for product in response.xpath("//div[@class='grpn-dc-caption']"):
            yield{
                "title" : product.xpath(".//div[@class='grpn-dc-title']/text()").get(),
                "first_price" : product.xpath(".//s[@class='wh-dc-price-original']/text()").get(),
                "price" : product.xpath(".//span[@class='wh-dc-price-discount c-txt-price']/text()").get(),
                "discount_rate" : product.xpath(".//div[@class='wh-dc-discount']/text()").get(),
                "product_rating" : product.xpath(".//div[@class='grpn-rating']/text()").get(),
                "total_ratings" : product.xpath(".//div[@class='grpn-total-ratings']/text()").get()
            }
