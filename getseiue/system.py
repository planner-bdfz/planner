import os
import oss2;
from itertools import islice
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)
sys.path.append("../../../Downloads")
auth = oss2.Auth("[OssAuthKey]","[OssSecret]")
bucket = oss2.Bucket(auth, 'http://oss-cn-qingdao.aliyuncs.com', 'dckong-114514')
import authorizationgets as aug;
import gettoken_by_bdfz as gt;
import time;
import json;
import shutil;
def run(id=None,pswd=None,mode=0):
    token=None;
    if(token==None):
        try:
            bucket.get_object_to_file("whitelist/%s.txt"%id,os.path.dirname(__file__)+"/tmp.txt");
        except oss2.exceptions.NoSuchKey:
            yield -8;
        except oss2.exceptions.RequestError:
            yield -2;
        else:
            os.remove(os.path.dirname(__file__)+"/tmp.txt")
        while 1:
            if(mode):
                token=gt.gets_by(id,pswd);
            else:
                token=aug.gets(id,pswd);
            if(type(token)==int):
                if(token==-1):#数据错误
                    yield -1;
            else:
                break;
    return token;








