import json
import os
from random import randint
from datetime import datetime

def translate_date(date, s=True):
    if date == "unplanned":
        if not s:
            return str(datetime.now().day + 1) + "-" + str(datetime.now().month) + "-" + str(datetime.now().year)
        return str(datetime.now().day) + "-" + str(datetime.now().month) + "-" + str(datetime.now().year)
    return date[8:10] + "-" + date[5:7] + "-" + date[0:4]

def list_allfile(path, all_files=[]):    
    if os.path.exists(path):
        files=os.listdir(path)
    else:
        print('this path not exist')
    for file in files:
        if os.path.isdir(os.path.join(path,file)):
            list_allfile(os.path.join(path,file),all_files)
        else:
            if file.endswith('.json'):
                all_files.append(os.path.join(path,file))
    return all_files

def get_json_data():
    path = os.path.dirname(os.path.realpath(__file__)) + "/" + "events"
    all_json = list_allfile(path)

    """
    for items in all_json:
        if "system_/course.gef" in items:
            all_json.remove(items)
    """

    rec = []

    for j in all_json:
        try:
            f = open(j, encoding="utf-8")
            k = json.load(f)

            tmpd = [
                dict(
                    Task=k["title"],
                    Start=translate_date(k["start_time"]),
                    Finish=translate_date(k["stop_time"], s=False),
                    Completion_pct=0,
                    Category="Title",
                    Note=''
                ),
                dict(
                    Task=k["title"],
                    Start=translate_date(k["start_time"]),
                    Finish=translate_date(k["stop_time"], s=False),
                    Completion_pct=0,
                    Category="Category "+ str(randint(1,5)),
                    Note=k["info"]
                )]

            rec += tmpd

            print("Successfully loaded json:"+j)
        except:
            print("Failed loaded json:" + j)

    return rec