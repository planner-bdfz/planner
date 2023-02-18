import requests;
import json;
from urllib import parse
def gets(email,password):
    s = requests.session()
    url = "https://passport.seiue.com/login?force=1&school_id=3&type=account"
    data = {
            "email":email,
            "password":password,
            "school_id": 3,
            "submit": "提交"
            }
    payload = parse.urlencode(data)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69',
    }
    res=s.request("POST", url, headers=headers, data=payload)
    if(res.status_code==401):
        return -1;
    url = "https://passport.seiue.com/authorize"
    data = {
        "response_type": "token",
        "client_id": "GpxvnjhVKt56qTmnPWH1sA"
    }
    payload = parse.urlencode(data)
    data = json.loads(s.request("POST", url, headers=headers, data=payload).text)
    return data["token_type"]+" "+data["access_token"];

