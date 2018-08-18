# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from  scrapy.exporters import JsonLinesItemExporter
class ShanghaifangPipeline(object):

    def __init__(self):
        self.fp=open('newhouse.json','wb')
        self.exporter=JsonLinesItemExporter(self.fp,encoding='utf-8',ensure_ascii=False)

    def process_item(self, item, spider):
        self.exporter.export_item(item)

        return item

    def close(self,spider):
        self.fp.close()
