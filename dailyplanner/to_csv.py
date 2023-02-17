from get_seiue_schedule import gets
import pathlib
import csv
import requests
import os
from urllib import parse
import json

p_ = str(pathlib.Path(__file__).parent)


def change(cloud=0, path=p_, seiue_id="", seiue_pswd=""):
    f = open(path + "/temp/user_dairy.csv", "w", encoding="utf-8")
    wt = csv.writer(f)
    if cloud:
        url = "https://passport.seiue.com/login?school_id=3&type=account&force=1"
        s = requests.session()
        if (s.post(url, data={"email": seiue_id, "password": seiue_pswd, "school_id": 3,
                              "submit": "提交"}).status_code != 200):
            return 401
        else:
            url = "https://passport.seiue.com/authorize"
            data = {
                "response_type": "token",
                "client_id": "GpxvnjhVKt56qTmnPWH1sA"
            }
            payload = parse.urlencode(data)
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69',
            }
            data = json.loads(s.request("POST", url, headers=headers, data=payload).text)
            files = gets(token=data["token_type"] + " " + data["access_token"], email=seiue_id)
            for j in files:
                i = files[j]
                wt.writerow([i["id"], i["title"], i["ddl"], i["type"], i["indispensable"], "", "",
                             "", "", i["predict_time"], i["emergency"], "", i["start_time"], i["stop_time"]])
    ls1 = os.listdir(p_ + "/events/seiue_")
    ls2 = os.listdir(p_ + "/events/user_")
    files = []
    for i in ls1:
        with open(p_ + "/events/seiue_/" + i, "r", encoding="utf-8") as g:
            if os.path.splitext(i)[1] == ".json":
                files.append(json.load(g))
    for i in ls2:
        with open(p_ + "/events/user_/" + i, "r", encoding="utf-8") as g:
            if os.path.splitext(i)[1] == ".json":
                files.append(json.load(g))
    with open(p_ + "/options/importance_basis.json", "r", encoding="utf-8") as f:
        basis = json.load(f)
    for i in files:
        a = i["ddl"]
        wt.writerow([i["id"], i["title"], a, i["type"], i["indispensable"], basis[i["tag"]],
                     str(float((int(i["indispensable"]) * 7 + int(basis[i["tag"]])) / 10)),
                     i["emergency"], "", i["predict_time"], "", "", i["start_time"], i["stop_time"]])
    f.close()


if __name__ == "__main__":
    change()
