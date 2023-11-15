import scrapy
from ..items import CareersPageScraperItem

class CareersSpider(scrapy.Spider):
    name = 'careers'
    start_urls = [
        'https://www.awsys-i.com/en/careers.php'
    ]

    def parse(self, response) :

        items = CareersPageScraperItem()

        all_div_careers = response.css("div.panel.box")

        for careers in all_div_careers:
            job_title = careers.css("div.career-text::text").extract()
            duties_and_responsibilities = careers.css("div.car-dnr").css("div.dnr-cont").css("li::text").extract()        
            requirements = careers.css("div.car-rqmt").css("div.rqmt-cont").css("li::text").extract()
            location = careers.css("div.loc-cont::text").extract()
           
            items['job_title'] = job_title
            items['duties_and_responsibilities'] = duties_and_responsibilities if duties_and_responsibilities else careers.css("div.car-dnr").css("div.dnr-cont2::text").extract()  
            items['requirements'] = requirements
            items['location'] = location

            yield items