import oss2
import json
import time


def gets(token="", email=""):
    auth = oss2.Auth("[OssAuthKey]", "[OssAuthSecret]")
    bucket = oss2.Bucket(auth, 'http://oss-cn-qingdao.aliyuncs.com', 'dckong-114514')
    data = json.dumps({"time": str(int(time.time())), "accept": token})
    bucket.put_object("Keys/getfile_%s.json" % email, data)
    while 1:
        try:
            fl = bucket.get_object("Keys/acceptgets_%s.json" % email)
        except oss2.exceptions.NoSuchKey:
            pass
        else:
            file = json.loads(fl.read())
            break
    if file["status"] == 200:
        file = file["token"]
        auth = oss2.StsAuth(file["AccessKeyId"], file['AccessKeySecret'], file['SecurityToken'])
        bucket = oss2.Bucket(auth, 'http://oss-cn-qingdao.aliyuncs.com', 'dckong-114514')
        _ = bucket.get_object("Keys/allfile_%s.json" % email)
        fl = json.loads(_.read())
        # _就是所有日程的总和的json文件，设想是一个字典每个key是任务ID，value是任务详细信息那些东西
        return fl
    if file["status"] == 404:
        return -1
    if file["status"] == 400:
        return -2
