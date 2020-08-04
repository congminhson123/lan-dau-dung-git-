import scrapy


class ZingSpider(scrapy.Spider):
    name = "bim"
    start_urls = ['https://zingnews.vn/thu-tuong-phai-khong-che-toc-do-lay-nhiem-covid-19-post1112768.html',]
    list_link = []



    def parse(self, response):
        id = response.css('div.page-wrapper article::attr(article-id)').get()
        f = open(
            'C:/Users/acer/PycharmProjects/crawl zingnews/crawlzingnews/crawlzingnews/spiders/Output/title.txt',
            'a+', encoding="utf-8")
        title = response.css('header.the-article-header h1.the-article-title::text').get()

        f.write('TIÊU ĐỀ: '+title + '\n')
        f.write('NỘI DUNG:' +'\n')
        for i in response.css('div.the-article-body p::text'):
            p_body = i.get()
            f.write(p_body + '\n')

        # get context of article
        next_link = response.css('p.article-title a::attr(href)').getall()
        for link in next_link:
            if link and (link not in self.list_link) and len(self.list_link) < 3:
                self.list_link.append(link)

                yield scrapy.Request(
                    response.urljoin(link),callback=self.parse
                )

