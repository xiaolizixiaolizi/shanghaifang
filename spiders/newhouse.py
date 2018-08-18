# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import re
from ..items import NewHouseItem


class NewhouseSpider(CrawlSpider):
    name = 'newhouse'
    allowed_domains = ['newhouse.sh.fang.com']
    start_urls = ['http://newhouse.sh.fang.com/house/s/b91/?ctm=1.sh.xf_search.page.2']

    rules = (
        Rule(LinkExtractor(allow=r'.+/house/s/b.*'), callback='parse_newhouse', follow=True),
    )

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

    def parse_newhouse(self, response):
        lis = response.xpath('//div[contains(@class,"nl_con")]//li')
        for li in lis:
            pictr = li.xpath('.//div[@class="pictr"]')  # 找不到就是空 空就是假
            if pictr:
                pass
            else:

                name = li.xpath('.//div[@class="nlcd_name"]/a/text()').get().strip()
                rooms_list = li.xpath('.//div[contains(@class,"house_type")]/a/text()').getall()
                # rooms_list=list(map(lambda x:x.strip(),rooms_list))
                rooms_list = list(map(lambda x: re.sub(r"\s", '', x), rooms_list))
                rooms = list(filter(lambda x: x.endswith("居"), rooms_list))  # 过滤掉居结尾的列表之前先去除结尾空格
                rooms = "".join(rooms).strip()

                area = li.xpath('.//div[contains(@class,"house_type")]/text()').getall()
                area = list(map(lambda x: re.sub(r"[\s/－]", "", x), area))
                area = "".join(area).strip()

                address = li.xpath('.//div[@class="address"]/a/@title').get()

                district = li.xpath('.//div[@class="address"]/a//text()').getall()
                # district="".join(district)
                # district=re.sub(r"\s",'',district)
                # district=re.search(r".*\[(.+)\].*",district).group(1)
                district = list(map(lambda x: re.sub(r"\s", "", x), district))
                district = "".join(district)
                district = re.search(r".*\[(.*)\].*", district).group(1)

                sale = li.xpath('.//div[contains(@class,"fangyuan")]/span/text()').get()
                desc = li.xpath('.//div[contains(@class,"fangyuan")]/a/text()').getall()
                desc = ";".join(desc)
                unit_price = li.xpath('.//div[@class="nhouse_price"]//text()').getall()
                unit_price = list(map(lambda x: re.sub(r"[\s广告]", "", x), unit_price))
                unit_price = "".join(unit_price)
                original_url = li.xpath('.//div[@class="nlcd_name"]/a/@href').get()
                item = NewHouseItem(
                    name=name, rooms=rooms, area=area,
                    district=district, address=address, sale=sale, desc=desc, unit_price=unit_price,
                    original_url=original_url
                )
                yield item
