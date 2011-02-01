# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class RbeaconItem(Item):
    # define the fields for your item here like:
    dx = Field()
    de = Field()
    freq = Field()
    snr = Field()
    speed = Field()
    time = Field()


