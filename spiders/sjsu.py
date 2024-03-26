import scrapy
from UniversityChatbot.items import FAQ #importing our model to map the data from website to database

class sjsuSpdier(scrapy.Spider):
    name = 'sjsu' #just naming the scraoer
    allowed_domains = ['www.sjsu.edu/'] # only scraping the websites that start with
    start_url = ['https://www.sjsu.edu/professional/openuniversity/faq.php'] # array of the urls that we are scraping
    custom_settings = {
        'FEED_URI' : 'tmp/sjsu.csv' #stores the data in temp file in a csv // make this file in any folder and specify the path
    }
    def parse(self, respone): #self is a reference to this class and response is the response we get from scrapy
        for item in respone.xpath("//div[@class='content column small-12 large-7 large-push-5 xlarge-8 xlarge-push-4']//div[@class='accordions component']"): # we loop through the parent div class found using inspect on website
            yield {
                'question': item.xpath(".//accordions__label/text()"),
                'answer': item.xpath(".//accordions__content//p/text()")
            }