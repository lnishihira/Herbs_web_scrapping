import scrapy

from herb.items import HerbItem


class HerbSpider(scrapy.Spider):
    name = 'herbspider'
    allowed_domains = ['anniesremedy.com']
    handle_httpstatus_list = [302,301]
    

    def start_requests(self):
        start_urls = ['https://www.anniesremedy.com/chart.php?alpha={0}'.format(alpha) for alpha in list(map(chr, range(97, 123)))]
        #print('&'*50 ,'\n',scrapy.Request('https://www.anniesremedy.com/chart.php?alpha=a', self.parse))
        for urls in start_urls:
            yield scrapy.Request(urls, callback = self.parse)
        # yield scrapy.Request('https://www.anniesremedy.com/chart.php?alpha=a', callback = self.parse)
        # yield scrapy.Request('https://www.anniesremedy.com/chart.php?alpha=b', callback = self.parse)
        # yield scrapy.Request('https://www.anniesremedy.com/chart.php?alpha=c', callback = self.parse)




    def parse(self, response):
        

        path = response.xpath('//ul[@class = "chart"]//tr[@class = "left"]//td[@class = "herbprops"]')

        for paths in path:
            #common_name = paths.xpath('./a/text()').extract()
            #botanical_name = paths.xpath('.//em/text()').extract()
            links = path.xpath('./a[@class = "sitelist"]/@href').extract()

             
            
            # for botanical_name in response.xpath('//ul[@class = "chart"]//tr[@class = "left"]//td[@class = "herbprops"]//em/text()').getall():
    #         #     item['botanical_name'] = botanical_name
            for link in links:
                

                
                link = "https://www.anniesremedy.com/" + link
                

                yield scrapy.Request(link, callback = self.parse_list_page)
                #yield scrapy.Request(link, callback = self.parse_list_page, meta = {'common_name':common_name, 'botanical_name': botanical_name})


    def parse_list_page(self, response):

        print('&'*50 ,'\n' , response)

        medicinal_uses = response.xpath('//ul[@class = "nobullets"]//li//a[@class = "tag"]/text()').extract()
        print('#'*50 ,'\n' , medicinal_uses)
        properties = response.xpath('//ul[@class = "nobullets"]//li//a[@class = "chartID"]/text()').extract()
        common_name = response.xpath('//div[@class = "herbbox"]//h2[2][@class = "colheader"]/text()').extract()
        #folklore = response.xpath('//div[@class = "history"]//text()')[3].extract() 
        tags = response.xpath('//div[@id = "centercontent"]//a[@class = "tag"]/text()').extract()
        origins =  response.xpath('//div[@class = "plant_desc"]//a/text()').extract()

        try:
            description = response.xpath('//*[@id="centercontent"]/div[1]/div[3]/p/text()').extract()
        except:
            if type(description) == float:
                description = "TRY SOMETHING ELSE!"

        try:
            folklore = response.xpath('//div[@class = "history"]//text()')[3].extract() 
        except:
            if type(description) == float:
                folklore = "TRY SOMETHING ELSE!"

   
        #family = response.xpath('//div[@class = "med_desc_herb"]//li[7]/text()').extract()

        # print("RESPONSE \n " , response)
        # print("REQUEST \n " , request)



        #parts_used = response.xpath('//ul[@class = "nobullets"]//li/text()').extract()  


        item = HerbItem()
        item['common_name'] = common_name
        item['origins'] = origins
        item['medicinal_uses'] = medicinal_uses
        item['properties'] = properties
        item['description'] = description
        item['folklore'] = folklore
        item['link'] = response
        item['tags'] = tags
       # item['family'] = family
        yield item



        # for common_name in response.xpath('//ul[@class = "chart"]//tr[@class = "left"]//td[@class = "herbprops"]/a/text()').getall():
        #     yield scrapy.Request(response.urljoin(common_name), self.parse)

        

        # for b_name in response.xpath('//ul[@class = "chart"]//tr[@class = "left"]//td[@class = "herbprops"]//em/text()').getall():
        #     yield scrapy.Request(response.urljoin(b_name), self.parse)
    



    # start_urls = ['https://www.anniesremedy.com/chart.php']

    # def start_requests( self ):
    #     next_urls = ['https://www.anniesremedy.com/chart.php?alpha={0}'.format(alpha) for alpha in list(map(chr, range(97, 123)))]


    #     for url in next_urls[:3]:


    #         print("#" * 50 + '\n', response, url)
    #         yield scrapy.Request(url, self.parse)
    

    # def parse(self, response):


    #     div_table = response.xpath('//ul[@class = "chart"]//tr[@class = "left"]//td[@class = "herbprops"]')

    #     for el in div_table:
    #         print("*"*50, "\n", el)

    #         common_name = el.xpath('/a/text()').get()
    #         print("*"*50, "\n", common_name)
            
    #         link = el.xpath('/a[@class = "sitelist"]/a/@href').get() 
    #         print("*"*50, "\n", link)
            
              
    #         botanical_name =  el.xpath('//em/text()').get()
    #         print("*"*50, "\n", botanical_name)

    #         item = HerbItem()
    #         item['link'] = link
    #         item['common_name'] = common_name
    #         item['botanical_name'] = botanical_name
    #         print(item)

    #         yield item




    # def parse_list_page(self, response):
    #         print("%" * 50 + '\n', response)

    #         ul = response.xpath('//ul[@class = "chart"]//tr')
    #     #   if !urls:
    #     #       continue # x and z links do not exist

          



    #         print("*"*50, "\n", ul)
    #         link = ul.xpath('//@href').extract_first() 
    #         print("*"*50, "\n", link)
    #         common_name = ul.xpath('//@alt').extract_first().strip()
    #         botanical_name =  ul.xpath('//em/text()').extract_first().strip()

    #         item = HerbItem()
    #         item['link'] = link
    #         item['common_name'] = common_name
    #         item['botanical_name'] = botanical_name
    #         print(item)

    #         yield item



