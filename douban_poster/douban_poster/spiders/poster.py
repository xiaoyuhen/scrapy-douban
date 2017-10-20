# -*- coding: utf-8 -*-
import re
from scrapy.spiders import Spider
from scrapy import Request

from douban_poster.items import DoubanPosterItem


class DoubanPosterSpider(Spider):
  name = 'douban_poster'

  def start_requests(self):
    url = 'https://movie.douban.com/subject/25864085/photos?start=0'
    yield Request(url)


  def parse(self, response):
    sites = response.xpath('//div[@id="wrapper"]//div[@class="article"]/ul/li')
    if sites:
      for site in sites:

        item = DoubanPosterItem()
        item_src = site.xpath('./div[@class="cover"]/a/img/@src')

        item['image_urls'] = item_src.extract()
        yield item

      page_num = re.search(r'start=(\d+)', response.url).group(1)
      page_num = 'start=' + str(int(page_num) + 30)
      next_url = re.sub(r'start=\d+', page_num, response.url)
      yield Request(next_url)

