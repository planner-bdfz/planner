import os
import sys
import time
import tkinter as tk

from tkcalendar import DateEntry
from datetime import datetime
from tkinter import scrolledtext, messagebox
from PIL import Image, ImageTk

import pygame

import json

import re

import run_it

change = int(0)

try:
    with open("temp/data_event.json") as f_load:
        filename = dict(json.load(f_load))
        filename = filename["filename"]
        print(filename)
except:
    filename = "New"
else:
    os.remove("temp/data_event.json")


def load():
    global change
    if filename == "New":
        change = 0
        return
    else:
        change = 1
        root_edit.title("修改事件")
        with open(filename) as loading:
            load_json = dict(json.load(loading))
            title = load_json["title"]
            title = str(title)
            root_edit.title("修改事件-" + title)
            name_entry.insert(tk.INSERT, title)
            info = load_json["info"]
            info_scroll_text.insert(tk.INSERT, info)
            type_event = load_json["type"]
            event_y.set(type_event)
            type_update()
            indispensable = load_json["indispensable"]
            indispensable_scale.set(indispensable)
            emergency = load_json["emergency"]
            emergency_scale.set(emergency)
            location = load_json["location"]
            location_entry.insert(tk.INSERT, location)
            tag = load_json["tag"]
            type_e.set(tag)
            if type_event == "route":
                start_time = load_json["start_time"]
                start_date_load = start_time[0: 10]
                start_date_load = re.sub("-", "/", start_date_load)
                start_date.set_date(start_date_load)
                start_hour_load = str(start_time[11:13])
                start_hour.set(start_hour_load)
                start_min_load = str(start_time[14:16])
                start_min.set(start_min_load)
                start_sec_load = str(start_time[17:19])
                start_sec.set(start_sec_load)
                stop_time = load_json["stop_time"]
                stop_date_load = stop_time[0: 10]
                stop_date_load = re.sub("-", "/", stop_date_load)
                stop_date.set_date(stop_date_load)
                stop_hour_load = str(stop_time[11:13])
                stop_hour.set(stop_hour_load)
                stop_min_load = str(stop_time[14:16])
                stop_min.set(stop_min_load)
                stop_sec_load = str(stop_time[17:19])
                stop_sec.set(stop_sec_load)
            elif type_event == "ddl":
                ddl_time = load_json["ddl"]
                ddl_date_load = ddl_time[0: 10]
                ddl_date_load = re.sub("-", "/", ddl_date_load)
                ddl_date.set_date(ddl_date_load)
                ddl_hour_load = str(ddl_time[11:13])
                ddl_hour.set(ddl_hour_load)
                ddl_min_load = str(ddl_time[14:16])
                ddl_min.set(ddl_min_load)
                ddl_sec_load = str(ddl_time[17:19])
                ddl_sec.set(ddl_sec_load)
                predict_time = int(load_json["predict_time"])
                predict_day = predict_time // 86400
                predict_time %= 86400
                predict_hour = predict_time // 3600
                predict_time %= 3600
                predict_min = predict_time // 60
                predict_sec = predict_time % 60
                predict_time_d_entry.insert(tk.INSERT, predict_day)
                predict_time_h_entry.insert(tk.INSERT, predict_hour)
                predict_time_m_entry.insert(tk.INSERT, predict_min)
                predict_time_s_entry.insert(tk.INSERT, predict_sec)


def save():
    code = "user-"+str(int(time.time()))
    title = str(name_entry.get())
    info = str(info_scroll_text.get("1.0", "end-1c"))
    location = location_entry.get()
    tag = type_e.get()
    type_c = event_y.get()
    if type_c == "ddl":
        try:
            predict_time_d = int(predict_time_d_entry.get())
            predict_time_h = int(predict_time_h_entry.get())
            predict_time_m = int(predict_time_m_entry.get())
            predict_time_s = int(predict_time_s_entry.get())
        except:
            messagebox.showerror(title="日程预计时间非法", message="日程预计时间必须为正整数或零，\n即预计时间∈N")
            raise ValueError("The predict time can only be integer")
        else:
            predict_time = predict_time_s + int(predict_time_m * 60) + int(predict_time_h * 60 * 60)
            predict_time = predict_time + int(predict_time_d * 60 * 60 * 24)
            predict_time = str(predict_time)
            if int(predict_time) < 0:
                messagebox.showerror(title="预计时间不能为负", message="你是一个一个一个时间机器（恼）")
    else:
        predict_time = "None"

    if title == "":
        messagebox.showerror(title="标题不能为空", message="日程标题不能为空")
        raise ValueError("The title can't be empty")

    if " " in title:
        detect = 0
        for i_detect in title:
            if i_detect != " ":
                detect = 1
            else:
                pass
        if detect == 0:
            messagebox.showerror(title="标题不能仅含有空格", message="日程标题不能仅含有空格")
            raise ValueError("The title can't only have " + '"' + " " + '"')

    if "'" in title or '"' in title:
        messagebox.showerror(title="标题不能含有引号", message="日程标题不能含有引号")
        raise ValueError("The title can't have " + '"""' + "or"''"")

    if type_c == "unsetted":
        messagebox.showerror(title="未设置时间", message="不能没有时间设置")
        raise ValueError("Event without time")

    if change == 1:
        file_name = filename
    else:
        file_name = "events/user_/" + code + ".json"
    print(str(change), "change")
    print(file_name, "filename")
    type_of_event = event_y.get()
    print(type_of_event)
    d_ddl = ddl_date.get_date()
    h_ddl = ddl_hour.get()
    m_ddl = ddl_min.get()
    s_ddl = ddl_sec.get()
    if type_of_event == "ddl":
        ddl = str(d_ddl) + "-" + str(h_ddl) + "-" + str(m_ddl) + "-" + str(s_ddl)
    else:
        ddl = "None"
    if type_of_event == "long":
        long = "True"
    else:
        long = "False"
    print("long=" + long)

    if type_c == "route":
        start_time = str(start_date.get_date()) + "-" + start_hour.get() + "-" + start_min.get() + "-" + start_sec.get()
        stop_time = str(stop_date.get_date()) + "-" + stop_hour.get() + "-" + stop_min.get() + "-" + stop_sec.get()
    elif type_c == "ddl":
        start_time = "unplanned"
        stop_time = "unplanned"
    else:
        start_time = "None"
        stop_time = "None"

    indispensable = str(indispensable_scale.get())

    emergency = str(emergency_scale.get())

    if change == 1:
        with open(file_name, "r", encoding="utf-8") as loading_ic:
            load_ic = dict(json.load(loading_ic))
            ic = load_ic["id"]
            ic = str(ic)

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump({"id": "id_code", "title": "title_tag", "info": "info_tag", "location": "location_tag",
                   "tag": "tag_tag", "type": "type_tag", "ddl": "ddl_tag", "long": "long_tag",
                   "predict_time": "predict_time_tag", "start_time": "start_time_tag", "stop_time": "stop_time_tag",
                   "indispensable": "indispensable_tag", "emergency": "emergency_tag"}, f)
    # -- ID --
    if change == 0:
        with open(file_name, "r", encoding="utf-8") as f:
            id_code = dict(json.load(f))
            id_code["id"] = code
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(id_code, f)
            id_code.clear()
    else:
        with open(file_name, "r", encoding="utf-8") as f:
            id_code = dict(json.load(f))
            id_code["id"] = ic
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(id_code, f)
            id_code.clear()
    # -- title --
    with open(file_name, "r", encoding="utf-8") as f:
        title_code = dict(json.load(f))
        title_code["title"] = title
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(title_code, f)
        title_code.clear()
    # -- info --
    with open(file_name, "r", encoding="utf-8") as f:
        info_code = dict(json.load(f))
        info_code["info"] = info
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(info_code, f)
        info_code.clear()
    # -- location --
    with open(file_name, "r", encoding="utf-8") as f:
        location_code = dict(json.load(f))
        location_code["location"] = location
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(location_code, f)
        location_code.clear()
    # -- tag --
    with open(file_name, "r", encoding="utf-8") as f:
        tag_code = dict(json.load(f))
        tag_code["tag"] = tag
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(tag_code, f)
        tag_code.clear()
    # -- type --
    with open(file_name, "r", encoding="utf-8") as f:
        type_code = dict(json.load(f))
        type_code["type"] = type_c
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(type_code, f)
        type_code.clear()
    # -- ddl --
    with open(file_name, "r", encoding="utf-8") as f:
        ddl_code = dict(json.load(f))
        ddl_code["ddl"] = ddl
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(ddl_code, f)
        ddl_code.clear()
    # -- long --
    with open(file_name, "r", encoding="utf-8") as f:
        long_code = dict(json.load(f))
        long_code["long"] = long
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(long_code, f)
        long_code.clear()
    # -- predict_time --
    with open(file_name, "r", encoding="utf-8") as f:
        predict_time_code = dict(json.load(f))
        predict_time_code["predict_time"] = predict_time
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(predict_time_code, f)
        predict_time_code.clear()
    # -- start_time --
    with open(file_name, "r", encoding="utf-8") as f:
        start_time_code = dict(json.load(f))
        start_time_code["start_time"] = start_time
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(start_time_code, f)
        start_time_code.clear()
    # -- stop_time --
    with open(file_name, "r", encoding="utf-8") as f:
        stop_time_code = dict(json.load(f))
        stop_time_code["stop_time"] = stop_time
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(stop_time_code, f)
        stop_time_code.clear()
    # -- indispensable --
    with open(file_name, "r", encoding="utf-8") as f:
        indispensable_code = dict(json.load(f))
        indispensable_code["indispensable"] = indispensable
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(indispensable_code, f)
        indispensable_code.clear()
    # -- emergency --
    with open(file_name, "r", encoding="utf-8") as f:
        emergency_code = dict(json.load(f))
        emergency_code["emergency"] = emergency
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(emergency_code, f)
        emergency_code.clear()
    root_edit.destroy()
    sys.exit()


def cancel():
    msg_box_close = messagebox.askokcancel(title="数据未保存", message="数据未保存，请确定是否关闭")
    if msg_box_close:
        root_edit.destroy()
        sys.exit()
    else:
        pass


current_year = datetime.now().year
current_month = datetime.now().month
current_date = datetime.now().day
current_hour = datetime.now().hour
current_min = datetime.now().minute
current_sec = datetime.now().second
root_edit = tk.Tk()
root_edit.title("创建事件")
Icon = tk.PhotoImage(file="assets/ico/events_editor/events_editor_ico.png")
Icon_New = tk.PhotoImage(file="assets/ico/events_editor/events_editor_new_ico.png")
Icon_ddl = tk.PhotoImage(file="assets/ico/events_editor/events_editor_ddl_ico.png")
Icon_route = tk.PhotoImage(file="assets/ico/events_editor/events_editor_route_ico.png")
Icon_Long = tk.PhotoImage(file="assets/ico/events_editor/events_editor_long_ico.png")
root_edit.iconphoto(False, Icon)
root_edit.geometry("600x455")
root_edit.resizable(width=False, height=False)


def on_closing():
    msg_box_close = messagebox.askokcancel(title="数据未保存", message="数据未保存，请确定是否关闭")
    if msg_box_close:
        root_edit.destroy()
    else:
        pass


root_edit.protocol("WM_DELETE_WINDOW", on_closing)
win1 = tk.Frame(root_edit, width=600, height=150)
win1.place(x=0, y=0)
name_lbl = tk.Label(win1, text="日程名称：")
name_lbl.place(x=0, y=0)
name_entry = tk.Entry(win1, width=55)
name_entry.place(x=75, y=0)
info_lbl = tk.Label(win1, text="日程描述：")
info_lbl.place(x=0, y=30)
info_scroll_text = scrolledtext.ScrolledText(win1, width=70, height=8)
info_scroll_text.place(x=75, y=30)
win3 = tk.Frame(root_edit, width=600, height=90)
win3.place(x=0, y=330)
location_lbl = tk.Label(win3, text="地点信息：")
location_lbl.place(x=0, y=0)
location_entry = tk.Entry(win3, width=55)
location_entry.place(x=75, y=0)
tag_lbl = tk.Label(win3, text="日程标签：")
tag_lbl.place(x=0, y=30)


def type_u():
    e = type_e.get()
    print(e)


type_e = tk.StringVar()
type_e.set("unsetted")
work_type_rad_btn = tk.Radiobutton(win3, text="工作", command=type_u, variable=type_e, value='work',
                                   foreground="#ff8800")
work_type_rad_btn.place(x=75, y=30)
study_type_rad_btn = tk.Radiobutton(win3, text="休息", command=type_u, variable=type_e, value='relax',
                                    foreground="#dddd00")
study_type_rad_btn.place(x=150, y=30)
sport_type_rad_btn = tk.Radiobutton(win3, text="运动", command=type_u, variable=type_e, value='sport',
                                    foreground="#88ff00")
sport_type_rad_btn.place(x=225, y=30)
read_type_rad_btn = tk.Radiobutton(win3, text="阅读", command=type_u, variable=type_e, value='read',
                                   foreground="#00a4bb")
read_type_rad_btn.place(x=300, y=30)
study_type_rad_btn = tk.Radiobutton(win3, text="学习", command=type_u, variable=type_e, value='study',
                                    foreground="#0000ff")
study_type_rad_btn.place(x=375, y=30)
communicate_type_rad_btn = tk.Radiobutton(win3, text="社交", command=type_u, variable=type_e, value='communicate',
                                          foreground="#cc00ff")
communicate_type_rad_btn.place(x=450, y=30)
play_type_rad_btn = tk.Radiobutton(win3, text="娱乐", command=type_u, variable=type_e, value='play',
                                   foreground="#aaaaaa")
play_type_rad_btn.place(x=525, y=30)
others_type_rad_btn = tk.Radiobutton(win3, text="其它", command=type_u, variable=type_e, value='others',
                                     foreground="#000000")
others_type_rad_btn.place(x=75, y=60)
unsetted_type_rad_btn = tk.Radiobutton(win3, text="未设置", command=type_u, variable=type_e, value='unsetted',
                                       foreground="#dd3d6c")
unsetted_type_rad_btn.place(x=150, y=60)
win4 = tk.Frame(root_edit, width=600, height=30)
win4.place(x=0, y=420)
save_btn = tk.Button(win4, text="保存", command=save)
save_btn.place(x=120, y=0)
cancel_btn = tk.Button(win4, text="取消", command=cancel)
cancel_btn.place(x=410, y=0)
win2 = tk.Frame(root_edit, width=600, height=180)
win2.place(x=0, y=150)
event_y = tk.StringVar()
ddl_type_frame = tk.Frame(win2, width=600, height=60)
ddl_time_label = tk.Label(ddl_type_frame, text="DDL：", font=("黑体.ttf", 13))

ddl_hour = tk.StringVar()
ddl_hour.set(str(current_hour))
ddl_h_opt_menu = tk.OptionMenu(ddl_type_frame, ddl_hour, "00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
                               "10",
                               "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                               "24")
ddl_h_opt_menu.config(width=2)
ddl_time_label1 = tk.Label(ddl_type_frame, text=":", font=("黑体.ttf", 13))
ddl_min = tk.StringVar()
ddl_min.set(str(current_min))
ddl_m_opt_menu = tk.OptionMenu(ddl_type_frame, ddl_min, "00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
                               "10",
                               "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                               "24",
                               "25", "26", "27", "28", "29", "30", "30", "31", "32", "33", "34", "35", "36",
                               "37",
                               "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                               "51",
                               "55", "53", "54", "55", "56", "57", "58", "59")
ddl_m_opt_menu.config(width=2)
ddl_time_label2 = tk.Label(ddl_type_frame, text=":", font=("黑体.ttf", 13))
ddl_sec = tk.StringVar()
ddl_sec.set(str(current_sec))
ddl_s_opt_menu = tk.OptionMenu(ddl_type_frame, ddl_sec, "00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
                               "10",
                               "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                               "24",
                               "25", "26", "27", "28", "29", "30", "30", "31", "32", "33", "34", "35", "36",
                               "37",
                               "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                               "51",
                               "55", "53", "54", "55", "56", "57", "58", "59")
ddl_s_opt_menu.config(width=2)
ddl_date = DateEntry(ddl_type_frame, width=12, year=current_year, month=current_month, day=current_date)
predict_time_lbl = tk.Label(ddl_type_frame, text="预计时间：", font=("黑体.ttf", 13))
predict_time_d_label = tk.Label(ddl_type_frame, width=5, text="天")
predict_time_h_label = tk.Label(ddl_type_frame, width=5, text="时")
predict_time_m_label = tk.Label(ddl_type_frame, width=5, text="分")
predict_time_s_label = tk.Label(ddl_type_frame, width=5, text="秒")
predict_time_d_entry = tk.Entry(ddl_type_frame, width=5)
predict_time_h_entry = tk.Entry(ddl_type_frame, width=5)
predict_time_m_entry = tk.Entry(ddl_type_frame, width=5)
predict_time_s_entry = tk.Entry(ddl_type_frame, width=5)
s_s_type_frame = tk.Frame(win2, width=600, height=60)
start_time_label = tk.Label(s_s_type_frame, text="开始时间：", font=("黑体.ttf", 13))
start_hour = tk.StringVar()
start_hour.set(str(current_hour))
start_h_opt_menu = tk.OptionMenu(s_s_type_frame, start_hour, "00", "01", "02", "03", "04", "05", "06", "07", "08",
                                 "09",
                                 "10",
                                 "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                                 "24")
start_h_opt_menu.config(width=2)
start_time_label1 = tk.Label(s_s_type_frame, text=":", font=("黑体.ttf", 13))
start_min = tk.StringVar()
start_min.set(str(current_min))
start_m_opt_menu = tk.OptionMenu(s_s_type_frame, start_min, "00", "01", "02", "03", "04", "05", "06", "07", "08",
                                 "09",
                                 "10",
                                 "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                                 "24",
                                 "25", "26", "27", "28", "29", "30", "30", "31", "32", "33", "34", "35", "36",
                                 "37",
                                 "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                                 "51",
                                 "55", "53", "54", "55", "56", "57", "58", "59")
start_m_opt_menu.config(width=2)
start_time_label2 = tk.Label(s_s_type_frame, text=":", font=("黑体.ttf", 13))
start_sec = tk.StringVar()
start_sec.set(str(current_sec))
start_s_opt_menu = tk.OptionMenu(s_s_type_frame, start_sec, "00", "01", "02", "03", "04", "05", "06", "07", "08",
                                 "09",
                                 "10",
                                 "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                                 "24",
                                 "25", "26", "27", "28", "29", "30", "30", "31", "32", "33", "34", "35", "36",
                                 "37",
                                 "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                                 "51",
                                 "55", "53", "54", "55", "56", "57", "58", "59")
start_s_opt_menu.config(width=2)
start_date = DateEntry(s_s_type_frame, width=12, year=current_year, month=current_month, day=current_date)
stop_time_label = tk.Label(s_s_type_frame, text="截止时间：", font=("黑体.ttf", 13))
stop_hour = tk.StringVar()
stop_hour.set(str(current_hour))
stop_h_opt_menu = tk.OptionMenu(s_s_type_frame, stop_hour, "00", "01", "02", "03", "04", "05", "06", "07", "08",
                                "09", "10",
                                "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                                "24")
stop_h_opt_menu.config(width=2)
stop_time_label1 = tk.Label(s_s_type_frame, text=":", font=("黑体.ttf", 13))
stop_min = tk.StringVar()
stop_min.set(str(current_min))
stop_m_opt_menu = tk.OptionMenu(s_s_type_frame, stop_min, "00", "01", "02", "03", "04", "05", "06", "07", "08",
                                "09", "10",
                                "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                                "24",
                                "25", "26", "27", "28", "29", "30", "30", "31", "32", "33", "34", "35", "36",
                                "37",
                                "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                                "51",
                                "55", "53", "54", "55", "56", "57", "58", "59")
stop_m_opt_menu.config(width=2)
stop_time_label2 = tk.Label(s_s_type_frame, text=":", font=("黑体.ttf", 13))
stop_sec = tk.StringVar()
stop_sec.set(str(current_sec))
stop_s_opt_menu = tk.OptionMenu(s_s_type_frame, stop_sec, "00", "01", "02", "03", "04", "05", "06", "07", "08",
                                "09", "10",
                                "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                                "24",
                                "25", "26", "27", "28", "29", "30", "30", "31", "32", "33", "34", "35", "36",
                                "37",
                                "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                                "51",
                                "55", "53", "54", "55", "56", "57", "58", "59")
stop_s_opt_menu.config(width=2)
stop_date = DateEntry(s_s_type_frame, width=12, year=current_year, month=current_month, day=current_date)
long_type_frame = tk.Frame(win2, width=600, height=60)
long_frame = tk.Frame(long_type_frame, width=580, height=50, background="#888888")
long_frame.place(x=10, y=5)
long_lbl = tk.Label(long_frame, text="长期目标", background="#888888")
long_lbl.place(x=263, y=13)
unsetted_type_frame = tk.Frame(win2, width=600, height=60)
unsetted_frame = tk.Frame(unsetted_type_frame, background="#888888", width=580, height=50)
unsetted_frame.place(x=10, y=5)
unsetted_lbl = tk.Label(unsetted_frame, text="请设置", background="#888888")
unsetted_lbl.place(x=270, y=13)
ddl_time_label.place(x=0, y=0)
ddl_h_opt_menu.place(x=75, y=0)
ddl_time_label1.place(x=140, y=0)
ddl_m_opt_menu.place(x=150, y=0)
ddl_time_label2.place(x=215, y=0)
ddl_s_opt_menu.place(x=225, y=0)
ddl_date.place(x=300, y=0)
predict_time_lbl.place(x=0, y=30)
predict_time_d_label.place(x=117, y=30)
predict_time_h_label.place(x=192, y=30)
predict_time_m_label.place(x=267, y=30)
predict_time_s_label.place(x=342, y=30)
predict_time_d_entry.place(x=75, y=30)
predict_time_h_entry.place(x=150, y=30)
predict_time_m_entry.place(x=225, y=30)
predict_time_s_entry.place(x=300, y=30)
start_time_label.place(x=0, y=0)
start_h_opt_menu.place(x=75, y=0)
start_time_label1.place(x=140, y=0)
start_m_opt_menu.place(x=150, y=0)
start_time_label2.place(x=215, y=0)
start_s_opt_menu.place(x=225, y=0)
start_date.place(x=300, y=0)
stop_time_label.place(x=0, y=30)
stop_h_opt_menu.place(x=75, y=30)
stop_time_label1.place(x=140, y=30)
stop_m_opt_menu.place(x=150, y=30)
stop_time_label2.place(x=215, y=30)
stop_s_opt_menu.place(x=225, y=30)
stop_date.place(x=300, y=30)


def type_update():
    print(event_y)
    print("type", event_y.get)
    if event_y.get() == 'ddl':
        print('type = ddl')
        ddl_type_frame.place(x=0, y=120)
        s_s_type_frame.place_forget()
        long_type_frame.place_forget()
        unsetted_type_frame.place_forget()
        root_edit.iconphoto(False, Icon_ddl)
    elif event_y.get() == 'route':
        print('type = route')
        ddl_type_frame.place_forget()
        s_s_type_frame.place(x=0, y=120)
        long_type_frame.place_forget()
        unsetted_type_frame.place_forget()
        root_edit.iconphoto(False, Icon_route)
    elif event_y.get() == 'long':
        print('type = long')
        ddl_type_frame.place_forget()
        s_s_type_frame.place_forget()
        long_type_frame.place(x=0, y=120)
        unsetted_type_frame.place_forget()
        root_edit.iconphoto(False, Icon_Long)
    elif event_y.get() == 'unsetted':
        print('type = unsetted')
        ddl_type_frame.place_forget()
        s_s_type_frame.place_forget()
        long_type_frame.place_forget()
        unsetted_type_frame.place(x=0, y=120)
        root_edit.iconphoto(False, Icon_New)


indispensable_scale = tk.Scale(win2, from_=0, to=10, length=500, orient=tk.HORIZONTAL)
indispensable_scale.place(x=75, y=0)
indispensable_label = tk.Label(win2, text="重要程度：", font=("黑体.ttf", 13))
indispensable_label.place(x=0, y=18)
emergency_scale = tk.Scale(win2, from_=0, to=10, length=500, orient=tk.HORIZONTAL)
emergency_scale.place(x=75, y=40)
emergency_label = tk.Label(win2, text="紧迫参数：", font=("黑体.ttf", 13))
emergency_label.place(x=0, y=58)
event_type_label = tk.Label(win2, text="事件类型：", font=("黑体.ttf", 13))
event_type_label.place(x=0, y=90)
event_type_var = tk.StringVar()
event_type_var.set("设置类型")
ddl_type_radio_btn = tk.Radiobutton(win2, text="DDL型", command=type_update, variable=event_y, value='ddl')
ddl_type_radio_btn.place(x=75, y=90)
s_s_type_radio_btn = tk.Radiobutton(win2, text="时间区间型", command=type_update, variable=event_y, value='route')
s_s_type_radio_btn.place(x=175, y=90)
long_type_radio_btn = tk.Radiobutton(win2, text="长期目标", command=type_update, variable=event_y, value='long')
long_type_radio_btn.place(x=300, y=90)
unsetted_type_radio_btn = tk.Radiobutton(win2, text="未设置", command=type_update, variable=event_y,
                                         value='unsetted')
unsetted_type_radio_btn.place(x=420, y=90)

event_y.set("unsetted")
type_update()

load()
geometry = "600x455"
root_edit.geometry(geometry)
root_edit.update()
win2.wait_window()
root_edit.iconphoto(False, Icon_New)
load()
# win2.mainloop()
