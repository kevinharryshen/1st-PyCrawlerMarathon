import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main():
    target_urls = [
        'https://www.ptt.cc/bbs/Stock/M.1579757620.A.54A.html',
        'https://www.ptt.cc/bbs/Stock/M.1579757999.A.E75.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('PTTStockCrawler', start_urls=target_urls, filename='test.json')
    process.start()

if __name__ == '__main__':
    main()
    