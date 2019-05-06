import requests        
def post_seu(a,b):
        post_addr="https://xxxxxxxxxxxxxxxxxxxxxxxxx"
        post_header={
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate,br',
                'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3',
                'Connection': 'keep-alive',
                'Content-Length': '56',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'xxxxxxxxxxxxxxxxxxxxxxxxx',
                'Origin': 'https://xxxxxxxxxxxxxxxxxxxxxxxxx',
                'Referer': 'https://xxxxxxxxxxxxxxxxxxxxxxxxx',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
                'X-Requested-With': 'XMLHttpRequest',
                'Cookie': 'think_language=zh-Hans-CN; sunriseUsername='+a+'', 
                'Cache-Control': 'max-age=0'
                }

        post_data ={
                'username': a,
                'password': b,
                'enablemacauth': '0'
                }
        requests.post(post_addr, data=post_data, headers=post_header,verify=False)

if __name__ == '__main__':
    connect_seu('xxxxxxx',b'xxxxxxxxx')
