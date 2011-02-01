# Scrapy settings for rbeacon project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'rbeacon'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['rbeacon.spiders']
NEWSPIDER_MODULE = 'rbeacon.spiders'
DEFAULT_ITEM_CLASS = 'rbeacon.items.RbeaconItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

