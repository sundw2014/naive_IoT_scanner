import scrapy
import ips
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class WebCameraXPSpider(scrapy.Spider):
    name = "WebCameraXP"
    custom_settings = {
        'CONCURRENT_ITEMS': 1000,
	'CONCURRENT_REQUESTS' : 1000,
	'DOWNLOAD_TIMEOUT' : 1.0,
	'RETRY_TIMES' : 0,
	'DEPTH_PRIORITY' : 1,
	'SCHEDULER_DISK_QUEUE' : 'scrapy.squeue.PickleFifoDiskQueue',
	'SCHEDULER_MEMORY_QUEUE' : 'scrapy.squeue.FifoMemoryQueue'
    }
    # from IPython import embed; embed()
    #ip_g = ips.ips('1.1.1.1','255.255.255.255')
    url_g = ips.urls_fromFile('8080.txt')

    def start_requests(self):
	for url in self.url_g:
            url = 'http://'+next(self.url_g)+':8080'
	    #print url
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log('up host no WebCameraXP : ' + response.url)
    def handle_error(self, failure):
        self.log("Request failed: %s" % failure.request)

