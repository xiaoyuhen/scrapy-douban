# -*- coding: utf-8 -*-
import re
from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy import Request

from douban.items import DoubanItem


class DoubanSpider(Spider):
  name = 'douban'

  def start_requests(self):
    url = 'https://movie.douban.com/top250'
    yield Request(url)

  def parse(self, response):
    sites = response.xpath('//div[@id="wrapper"]//ol[@class="grid_view"]/li')
    if sites:
      for site in sites:

        item = DoubanItem()
        item_ele = site.xpath('./div[@class="item"]')
        item_info_ele = item_ele.xpath('./div[@class="info"]')
        item_info_star = item_info_ele.xpath('./div[@class="bd"]/div')

        item['poster'] = item_ele.xpath('./div[@class="pic"]//img/@src').extract()
        item['ranking'] = item_ele.xpath('./div[@class="pic"]/em/text()').extract()
        item['film_name'] = item_info_ele.xpath('./div[@class="hd"]/a/span[1]/text()').extract()
        item['film_eng_name'] = item_info_ele.xpath('./div[@class="hd"]/a/span[2]/text()').extract()
        item['direct'] = item_info_ele.xpath('./div[@class="bd"]/p[1]/text()').extract()
        item['star'] = item_info_star.xpath('./span[@class="rating_num"]/text()').extract()
        item['comment_num'] = item_info_star.xpath('./span[4]/text()').extract()
        item['quote'] = item_info_ele.xpath('./div[@class="bd"]/p[@class="quote"]/span/text()').extract()
        yield item

      page_num = 0
      url = response.url
      if re.search(r'start=(\d+)', url):
        page_num = re.search(r'start=(\d+)', response.url).group(1)
      else:
        url = url + '?start=0'

      page_num = 'start=' + str(int(page_num)+25)
      next_url = re.sub(r'start=\d+', page_num, url)
      yield Request(next_url)

