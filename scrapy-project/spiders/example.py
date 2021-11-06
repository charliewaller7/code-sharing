"""
Example Spider

This script is an example of how to build a web scraper using the Scrapy framework.

This auction uses the example of a car auction site.
"""

from datetime import datetime

import scrapy

# Custom functions
# from src.transformers import BasicTransformers
# ...


class ExampleSpider(scrapy.Spider):

    # TODO - Required spider metadata
    name = 'example'
    BASE_URL = 'https://example.com'

    # Each spider must record it's start time
    start_time = int(datetime.now().strftime('%Y%m%d%H%M%S'))

    def start_requests(self):
        """
        Required scrapy method to initiate scrape.
        """
        yield scrapy.Request(
            url=f'{self.BASE_URL}/results',
            callback=self.parse_pages
        )

    def parse_pages(self, response):
        """
        Scrape links to each auction page
        """
        pages = response.css('div.some-example-pages a::attr(href)').getall()

        # Other custom logic
        # ...
        # ...

        for page in pages:
            yield scrapy.Request(
                url=page,
                callback=self.parse_auctions
            )

    def parse_auctions(self, response):
        """
        Scrape links to each auction page
        """
        auctions = response.css('div.all-auctions a::attr(href)').getall()

        # Other custom logic
        # ...
        # ...

        for auction in auctions:
            yield scrapy.Request(
                url=auction,
                callback=self.parse_listings
            )

    def parse_listings(self, response):
        """
        Parse links for individual listings
        """
        listings = response.css('div.all-listings a::attr(href)').getall()

        # Other custom logic
        # ...
        # ...

        for listing in listings:
            yield scrapy.Request(
                url=listing,
                callback=self.parse_details
            )

    def parse_details(self, response):
        """
        Parse car information for each listing
        """

        item = {
            # TODO - Required fields for each listing
            'auction_name': response.css('...').get(),
            'auction_date': response.css('...').get(),
            'lot_name': response.css('...').get(),
            'name': response.css('...').get(),
            'price_string': response.css('...').get(),
            'link': response.css('...').get(),
            'image': response.css('...').get(),
            'all_images': response.css('...').get(),
            'description': response.css('...').get(),

            # Any additional available metadata
            'chassis_number': response.css('...').get(),
            'licence_plate': response.css('...').get(),
            # ...
        }

        yield item

