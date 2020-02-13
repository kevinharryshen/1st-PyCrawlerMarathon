import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import sys

def main(target_board):
    #target_board = ['Gossiping', 'Stock']
    #target_board = ['Gossiping']
    print("target_board=",target_board)
    process = CrawlerProcess(get_project_settings())
    for board in target_board:
        process.crawl('PTTCrawler', board=board)
        process.start()

if __name__ == '__main__':
    main(sys.argv[1:])
