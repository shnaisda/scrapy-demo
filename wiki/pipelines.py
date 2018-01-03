# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import re

class WikiPipeline(object):
    def process_item(self, item, spider):
        list_of_age = []
        if None in ([item[k] for k,v in item.items()]):
            raise DropItem("Missing value in %s" % item)
        else:
            data_in_text = item['record']
            for data in data_in_text:
                res = re.search(r'( \d\d, .*)', data)
                if res:
                    detail = res.group(1).replace(',',' ').strip().split()
                    list_of_age.append( detail )
        if list_of_age:
            logging.info( item['year'] )
            logging.info( ' '.join( min(list_of_age, key=(lambda x: x[0])) ) )