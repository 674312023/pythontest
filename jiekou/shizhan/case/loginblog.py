# coding:utf-8
import requests,sys
sys.path.append('..')
from common.logger import Log

# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Blog():
    # s = requests.session()  # 全局参数
    log = Log()

    def __init__(self, s):
        self.s = s

    def login(self):
        url = "https://passport.cnblogs.com/user/signin"
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           "Accept-Language": 'zh-CN,zh;q=0.8',
           "Accept-Encoding": 'gzip, deflate, br',
           "Content-Type":  'application/json; charset=UTF-8',
           "X-Requested-With": 'XMLHttpRequest',
           "Cookie": '__gads=ID=b37919386478dba9:T=1497232460:S=ALNI_MaViCeDh5X-pbkCg8RcDs5DJ9U3BA; pgv_pvi=323950592; UM_distinctid=160d514d75d2e7-056d5b5d5d58cf-6b1b1279-13c680-160d514d75e7c5; Hm_lvt_444ece9ccd5b847838a56c93a0975a8b=1520407355; __utma=226521935.214876567.1491875711.1521793673.1524213886.5; __utmz=226521935.1524213886.5.2.utmcsr=so.com|utmccn=(organic)|utmcmd=organic|utmctr=python%20pickle%E6%A8%A1%E5%9D%97; __guid=162291773.3264445550285863000.1524644067956.6982; _ga=GA1.2.214876567.1491875711; ASP.NET_SessionId=01uikgwjczpijbn5aq2l4jfk; monitor_count=1; SERVERID=34e1ee01aa40e94e2474dffd938824db|1529378011|1529377966',
           'Connection': 'keep-alive'
            }
        json_data = {"input1":"这里是抓包后获取的加密账号",
                "input2":"这里是抓包后获取的加密密码",
                "remember": False}


        res = self.s.post(url, headers=header, json=json_data, verify=False)
        result1 = res.content  # 字节输出
        self.log.info(u"调用登录方法，获取结果：%s"%(result1.decode('utf-8')))
        return res.json()

    def save(self, title, body):
        url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
        d = {"__VIEWSTATE": "",
            "__VIEWSTATEGENERATOR":"FE27D343",
            "Editor$Edit$txbTitle":title,
            "Editor$Edit$EditorBody":"<p>%s</p>"%body,
            "Editor$Edit$Advanced$ckbPublished":"on",
            "Editor$Edit$Advanced$chkDisplayHomePage":"on",
            "Editor$Edit$Advanced$chkComments":"on",
            "Editor$Edit$Advanced$chkMainSyndication":"on",
            "Editor$Edit$lkbDraft":"存为草稿",
             }
        r2 = self.s.post(url2, data=d, verify=False)  #保存草稿箱
        self.log.info(u"调用保存草稿箱方法，获取结果：%s"%r2)
        return r2.url

    def get_postid(self, r2_url):
        # 正则表达式提取
        import re
        postid = re.findall(r"postid=(.+?)&", r2_url)  # 这里是list []
        self.log.info(u"正则提取postid，获取结果：%s"%postid)
        return postid[0]

    def del_tie(self, postid):
        del_json = {"postId": postid}
        del_url = "https://i.cnblogs.com/post/delete"
        r3 = self.s.post(del_url, json=del_json, verify=False)
        self.log.info(u"删除草稿箱，获取结果：%s"%r3.json()["isSuccess"])
        return r3.json()

if __name__ == "__main__":
    import requests
    s = requests.session()
    Blog(s).login()
