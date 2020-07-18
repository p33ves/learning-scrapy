# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import json
from datetime import datetime

from itemadapter import ItemAdapter
from flixable.items import FlixableListItem, FlixableNetflixItem

import pymongo


class FlixablePipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        db = self.conn['flixableDB']
        self.collection = db['netflix_collection']

    def process_item(self, item, spider):
        if isinstance(item, FlixableNetflixItem):
            self.collection.insert(dict(item))
        elif isinstance(item, FlixableListItem):
            list_file = open("data/netflix_list.json")
            list_data = json.load(list_file)
            list_file.close()
            if 'extract_date' not in list_data.keys() or list_data['extract_date'] != datetime.today().strftime('%Y-%m-%d'):
                with open("data/netflix_list.json", 'w') as list_json:
                    json.dump(
                        {'extract_date': datetime.today().strftime('%Y-%m-%d')}, list_json)
            with open("data/netflix_list.json", 'a') as list_json:
                json.dump({item['title_url']: item}, list_json)
        return item
