# -*- coding: utf-8 -*-
import re
from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy import Request

from douban250.items import DoubanItem


class DoubanPosterSpider(Spider):
  name = 'douban250_poster'

  def start_requests(self):
    url = 'https://movie.douban.com/top250'
    yield Request(url)


  def parse(self, response):
    sites = response.xpath('//div[@id="wrapper"]//ol[@class="grid_view"]/li')
    if sites:
      for site in sites:

        item = DoubanItem()
        item_ele = site.xpath('./div[@class="item"]')

        item['image_urls'] = item_ele.xpath('./div[@class="pic"]//img/@src').extract()
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

