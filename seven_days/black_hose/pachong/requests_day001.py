import requests


class spider_tieba(object):

    def __init__(self, tieba_name,):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"}


    def get_url_list(self): # 构建url列表
        # url_list = []
        # for i in range(0, 101, 50):
        #     url_list.append(self.url_temp.format(i))
        # return url_list
        return [self.url_temp.format(i) for i in range(0, 101, 50)]


    def pase_url(self, url): # 获取url，发送请求，获取响应
        response = requests.get(url, headers = self.headers)
        return response.content.decode()


    def save_html(self, page_num, htmlstr):
        filepath = "{}吧-第{}页".format(self.tieba_name, page_num)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(htmlstr)

    def run(self):
        # 构建url列表
        url_list = self.get_url_list()
        # 遍历、发送请求，获取响应
        for i in url_list:
            htmlstr = self.pase_url(i)
            page_num = url_list.index(i) + 1

            # 保存页面
            self.save_html(page_num, htmlstr)



# 运行
if __name__ == "__main__":
    tieba_spider = spider_tieba("lol")
    tieba_spider.run()
