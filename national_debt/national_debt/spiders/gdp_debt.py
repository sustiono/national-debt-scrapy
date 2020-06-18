# -*- coding: utf-8 -*-
import logging

import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath('//tbody/tr')
        for row in rows:
            yield {
                'country_name': row.xpath('.//td[1]/a/text()').get(),
                'gdp_debt': row.xpath('.//td[2]/text()').get(),
                'population': row.xpath('.//td[3]/text()').get()
            }
