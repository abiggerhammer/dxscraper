import json
from scrapy.spider import BaseSpider

class RbeaconSpider(BaseSpider):
    name = "reversebeacon.net"
    allowed_domains = ["reversebeacon.net"]
    start_urls = ["http://www.reversebeacon.net/dxsd1/sk.php?s=0&r=15&fid=506&x=234&ng=1"]
    
    def parse(self, response):
        j = json.loads(response.body)
        f = open(self.name, 'wb')
        for contact in j['s']:
            for x in range(len(j['s'][contact])):
                if x in [0,1,2,5]:
                    f.write(j['s'][contact][x])
                elif 3==x:
                    f.write(j['s'][contact][x] + ' dB')
                elif 4==x:
                    f.write(j['s'][contact][x] + ' wpm')
                f.write('     ')
            f.write('\n')


        
