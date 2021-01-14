import requests
import json
# 上传文件
url = 'https://www.imooc.com/user/postpic'
# 上传图片参数
file = {
    "fileField":("qq.png",open(r"C:\Users\Administrator\Desktop\qq.png",'rb'),"image/png")
}
# 登陆cookies值
cookie = {"apsid":"BkNDQ4ZTM3NjNjY2IyYmM5YmMyM2JmY2M3ZGUxYWMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODIwMDA4NQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADI4Njg2ODNiMjUyYWYwYWZlZGY0NTQ4N2NjNGMwZmNjpkX9X3FxAF8%3DYj"
}
res = requests.post(url,files=file,verify=False,cookies=cookie).json()
print(json.dumps(res,indent=4,ensure_ascii=False))