import requests
from lxml import etree
import time


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
    "cookie":"JSESSIONID=4ED48ECBC8A4E525C623FB22158DC79E; route=07dacd5bc2376948165d308313275d36;"
}
form_data = {
    "xnm": "2026",
    "xqm": "3"
}

url="https://jw1.hustwenhua.net/jwglxt/kbcx/xskbcx_cxXsgrkb.html?gnmkdm=N253508"
resp = requests.post(url=url, headers=headers, data=form_data)
resp.encoding = resp.apparent_encoding

with open("result.html", "w", encoding="utf-8") as f:
    f.write(resp.text)
print("执行完成，已经生成 result.html 文件")

