import scrapy


class CareersPageScraperItem(scrapy.Item):
    job_title = scrapy.Field()
    location = scrapy.Field()
    duties_and_responsibilities = scrapy.Field()
    requirements = scrapy.Field()

