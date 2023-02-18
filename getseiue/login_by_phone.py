import requests;
import json;
def phone_login(phone="",code="",id_=""):
    s = requests.session();
    if(code==""):
        url="https://passport.seiue.com/login/generate-code";
        phone=phone;
        data={"identity": phone};
        res=json.loads(s.post(url,data=data).text);
        if(res["ok"]==False):
            return res;
        id__=res["reminder_id"];
        yield id__;
    code=code.strip();
    url="https://passport.seiue.com/login?school_id=3&type=code";
    data={"phone":phone,
          "code":code,
          "school_id":3,
          "reminder_id":id_,
          "submit":"提交"}
    s.post(url,data=data);
    #print(s.status_code)
    url="https://passport.seiue.com/authorize";
    data={
        "client_id":"GpxvnjhVKt56qTmnPWH1sA",
        "response_type":"token"
    }
    res=json.loads(s.post(url,data=data).text)
    try:
        return res["token_type"]+" "+res["access_token"];
    except KeyError:
        return "-1";
#print(next(phone_login("jjj")))
