from gui.main_gui import *
import settings
from scrapy import cmdline
import os 

dirpath=os.path.dirname(os.path.abspath(__file__)) # 获取当前路径
 
os.chdir(dirpath)         # 切换到当前目录


def crawl_by_query(query, output_path='../output', document_type='Article', output_format='bibtex', sid=''):
    cmdline.execute(
        r'scrapy crawl wos_advanced_query_spider -a output_path={} -a output_format={}'.format(
            output_path, output_format).split() +
        ['-a', 'query={}'.format(query), '-a', 'document_type={}'.format(document_type), '-a', 'sid={}'.format(sid)])

def crawl_by_journal(journal_list_path, output_path='../output', document_type='Article', output_format='bibtex'):
    """
    Crawl Web of Science by journal list
    :param journal_list_path: journal list file path
    :param output_path: output file path
    :param document_type: document type, e.g. Article
    :param output_format: output format, e.g. bibtex
    """
    cmdline.execute(
        r'scrapy crawl wos_journal_10k_spider -a journal_list_path={} -a output_path={} -a output_format={}'.format(
            journal_list_path, output_path, output_format).split() + ['-a', 'document_type={}'.format(
            document_type)])


def crawl_by_gui():
    gui_crawler = GuiCrawler()
    gui_crawler.show()
    reactor.run()


if __name__ == '__main__':
    # 按期刊下载
    # crawl_by_journal(journal_list_path=r'C:\Users\Tom\PycharmProjects\wos_crawler\input\journal_list_test.txt',
    #                  output_path=r'E:\wos爬取结果', output_format='fieldtagged', document_type='')

    # 按检索式下载
    crawl_by_query(query='TS=(solid waste polution) AND PY=(2024-2024)', output_path='../output', output_format='fieldtagged', document_type='Article', sid='USW2EC0AB9EaPHF2PyvPrTIntRQHc')

    # 使用GUI下载
    #crawl_by_gui()
    pass
