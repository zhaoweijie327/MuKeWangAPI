import requests
# 下载文件
url = 'http://file.mukewang.com/apk/app/125/1609297863/imooc_8.0.0_10102001_android.apk?version=1609297867'
# 登陆cookies值
cookie = {"apsid":"BkNDQ4ZTM3NjNjY2IyYmM5YmMyM2JmY2M3ZGUxYWMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODIwMDA4NQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADI4Njg2ODNiMjUyYWYwYWZlZGY0NTQ4N2NjNGMwZmNjpkX9X3FxAF8%3DYj"
}
res = requests.get(url,verify=False,cookies=cookie)
with open("./mukewang.apk",'wb') as f:
    f.write(res.content)
