import requests;
import json;
from lxml import etree;
def gets_by(_id,pswd):
    s=requests.session();
    html=etree.HTML(requests.get("http://bdfz-cas.pkuschool.edu.cn/cas/login").text);
    lt=html.xpath('//*[@id="lt"]/@value');
    data={
        "lt":lt,
        "service":"https://passport.seiue.com/sso/cas/login?school_id=3",
        "username":_id,
        "password":pswd
    };
    headers={"Content-Type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
    r=s.post("http://bdfz-cas.pkuschool.edu.cn/cas/login",data=data,headers=headers);
    data={"client_id":"GpxvnjhVKt56qTmnPWH1sA","response_type":"token"};
    res=json.loads(s.post("https://passport.seiue.com/authorize",data=data).text);
    return res["token_type"]+" "+res["access_token"];