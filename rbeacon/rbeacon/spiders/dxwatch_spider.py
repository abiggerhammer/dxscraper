import json
from scrapy.spider import BaseSpider

class DxwatchSpider(BaseSpider):
    name = "dxwatch.com"
    allowed_domains = ["dxwatch.com"]
    start_urls = ["http://www.dxwatch.com/dxsd1/s.php?s=0&r=15&fid=506&x=234"]
    
    def parse(self, response):
        j = json.loads(response.body)
        f = open(self.name, 'wb')
        for contact in j['s']:
            for x in range(len(j['s'][contact])):
                if x in [0,1,2,4]:
                    f.write(j['s'][contact][x])
                f.write('     ')
            f.write('\n')


        
