# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: file.py
@time: 17:20
"""


# import requests


# a = random.random(1, 99)
# print(a)


# output: __getattribute__:('b',){}


#
# filename = "a.txt"
# try:
#     with open(filename, "r") as f_obj:
#         contents = f_obj.read()
# except Exception as e:
#     print(e.message)
# else:
#     word = contents.split()
#     num_words = len(word)
#     print(num_words)
class Init(object):
    def __init__(self, value):
        self.val = value


class Add2(Init):
    def __init__(self, val):
        super(Add2, self).__init__(val)
        self.val += 2


class Mul5(Init):
    def __init__(self, val):
        super(Mul5, self).__init__(val)
        self.val *= 5


class Pro(Mul5, Add2):
    pass


class Incr(Pro):
    csup = super(Pro)

    def __init__(self, val):
        self.csup.__init__(val)
        self.val += 1


# p = Incr(5)
# print(p.val)
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    # r = requests.get(url="http://bbs.ngacn.cc/", headers=headers)
    # print(r.status_code)
    # r.encoding = "gbk"
    # print(r.text.encode("utf-8"))
    # with open("a.html", "w") as fp:
    #     fp.write(r.text)
    import urllib2
    url="http://bbs.ngacn.cc/"
    request=urllib2.Request(url)
    request.add_header('User-Agent',"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")
    response=urllib2.urlopen(request)
    with open("b.html","w") as fp:
        fp.write(response.read().decode("GBK").encode("UTF-8"))
