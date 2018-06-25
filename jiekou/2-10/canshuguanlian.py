# coding:utf -8
import requests,re
# 先打开登录首页，获取部分 cookie
url = 'https://passport.cnblogs.com/user/signin'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
s = requests.session()
r = s.get(url, headers=headers, verify=False)
print(s.cookies)
# 添加登录需要的两个 cooki
c = requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie', '2FD7F4FEA62D1BDA74321C2C0B1BAB0C35AEA8FC119DF2EC5CEBBEDF9D9E8C31C805A0CBEBDDE8F12243673C1B1E0F6C94FB4EB18CECE7292156974987EDE8DD3973FF7BF881459D4C4308769DE0C2E1D7E7023F10D524988C308EA202BF144370250E0A')
c.set('.Cnblogs.AspNetCore.Cookies', 'CfDJ8FHXRRtkJWRFtU30nh_M9mAIoGWQ-dsJ1fB3L4VPvlO5ZKuKeVWo1yTMJnBV3YhXclGeJMEOEDIlyq9QPzKiBgaaeJ63f_67VNJhMmGk_xuYCRR8hbu1ScYJItxWYYYPRnSswbVRJPGyNAOmEgmp8K7FGeZV6IM3GMGCMjAbrWYAJSnhUB01i2l9QEZQCs8Ww0FTMuqR1R9ijXdtBMt211Og_SMuq4JOkizOhrBFXSQHxQY1v8pSLlb8PoQD3kENFN5bV2GcB85Lzh2ONUUigdtYR7KPPZHbT_y12ISFPWCy')
s.cookies.update(c)
print(s.cookies)
# 登录成功后保存编辑内容
r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers,
verify=False)
# 第二步：保存草稿
url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR":"FE27D343",
        "Editor$Edit$txbTitle":"这是测试删除2",
        "Editor$Edit$EditorBody":"<p>这里111：http://www.cnblogs.com/yoyoketang/</p>11",
        "Editor$Edit$Advanced$ckbPublished":"on",
        "Editor$Edit$Advanced$chkDisplayHomePage":"on",
        "Editor$Edit$Advanced$chkComments":"on",
        "Editor$Edit$Advanced$chkMainSyndication":"on",
        "Editor$Edit$Advanced$txbEntryName":"",
        "Editor$Edit$Advanced$txbExcerpt":"",
        "Editor$Edit$Advanced$tbEnryPassword":"",
        "Editor$Edit$lkbDraft":"存为草稿",
         }
r2 = s.post(url2, data=body, verify=False)
print(r2.url)
# 第三步：正则提取需要的参数值
postid = re.findall(r'postid=(.+?)&', r2.url)
print(postid)
# 提取为字符串
print(postid[0])

# 第四步：删除草稿箱
url3 = "https://i.cnblogs.com/post/delete"
json3 = {"postId": postid[0]}
r3 = s.post(url3, json=json3, verify=False)
print(r3.json())

