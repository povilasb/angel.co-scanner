import scrapy
from scrapy.utils.project import get_project_settings


class AngelCoSpider(scrapy.Spider):
    """angel.co spider"""
    name = 'angel.co Spider'
    start_urls = ['https://angel.co']


    def __init__(self):
        settings = get_project_settings()
        self.investors = settings.get('INVESTORS')


    def parse(self, response):
        yield scrapy.Request(
            self.investor_url(response),
            meta={
                'investor_nr': self.investor_nr(response),
            },
            callback=self.scrape_investor
        )


    def scrape_investor(self, response):
        yield self.make_investor_data(response)

        if self.have_more_investors(response):
            yield scrapy.Request(
                self.next_investor_url(response),
                meta={
                    'investor_nr': self.investor_nr(response) + 1,
                },
                callback=self.scrape_investor
            )


    def scrape_social_links(self, response):
        return response.css('a.link_el::attr(href)').extract()


    def make_investor_data(self, response):
        return {
            'nickname': self.investor_nickname(response),
            'social_links': self.scrape_social_links(response),
        }


    def have_more_investors(self, response):
        """
        Returns:
            bool: True if there are more investors to scrape, False
                otherwise.
        """
        return self.investor_nr(response) < (len(self.investors) - 1)


    def investor_url(self, response):
        """
        Returns:
            str: url to investor page.
        """
        return response.urljoin(self.investors[self.investor_nr(response)])


    def next_investor_url(self, response):
        """
        Returns:
            str: url to next investor page.
        """
        return response.urljoin(self.investors[self.investor_nr(response) + 1])


    def investor_nr(self, response):
        investor_nr = 0
        try:
            investor_nr = response.meta['investor_nr']
        except KeyError:
            pass

        return investor_nr


    def investor_nickname(self, response):
        return self.investors[response.meta['investor_nr']]
