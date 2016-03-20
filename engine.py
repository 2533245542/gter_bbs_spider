import gevent.monkey
gevent.monkey.patch_socket()

import gevent

import crawler

start_url="http://bbs.gter.net/forum.php?mod=forumdisplay&fid=49&typeid=158&filter=typeid&typeid=158&page=2"

def asyn_fetch(url_list):
    greenlets=[]
    for url in url_list:
        greenlets.append(gevent.spawn(crawler.get_personal_data,url))
    gevent.joinall(greenlets)

if __name__=="__main__":

    url_list=crawler.get_link(start_url)
    asyn_fetch(url_list)
