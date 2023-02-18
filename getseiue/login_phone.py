import time
import tkinter as tk
from tkinter import ttk
import login_by_phone as pho;
from tkinter import messagebox
import json;
import threading;
import base64;
import requests;
import oss2;
import os;
import sys;
root = tk.Tk()
root.geometry("514x200+300+200")
bg = "#ffffff"
fg = "#000000"
root.configure(background=bg)
root.resizable(width=0,height=0);
exists=1;
idid="";
def quit():
    global exists;
    exists=0;
    root.quit();
root.protocol('WM_DELETE_WINDOW', quit)
root.title("验证码登陆")
def bk(tm=3):
    for i in range(tm*10):
        time.sleep(0.1);
        if(not exists):
            return;
    btn_get["text"] = "获取验证码"
    btn_get.config(state=tk.NORMAL);
def get():
    global idid;
    global btn_get,root;
    num=phone.get().strip();
    try:
        res=next(pho.phone_login(phone=num));
    except requests.exceptions.ConnectionError:
        messagebox.showerror(message="连接服务器错误，请稍后再试，或检查网络是否正常,\n若长时间有此问题，请在问题反馈中反馈此问题")
    except StopIteration as s:
        s_=str(s)[1:-1];
        rt={};
        rt[s_.split(",")[0].split(":")[0]]=s_.split(",")[0].split(":")[1]
        rt[s_.split(",")[1].split(":")[0]] = s_.split(",")[1].split(":")[1]
        if(rt[" 'info'"]==" 'identifier 不能为空。'"):
            btn_get["text"]="手机号不能为空"
            btn_get.config(state=tk.DISABLED);
            root.update();
            thread = threading.Thread(target=bk);
            thread.start()
        else:
            btn_get["text"] = "请勿频繁发送"
            btn_get.config(state=tk.DISABLED);
            root.update();
            thread = threading.Thread(target=bk);
            thread.start()
    else:
        if(1):
            btn_get["text"]="验证码已发送";
            btn_get.config(state=tk.DISABLED);
            root.update();
            thread = threading.Thread(target=bk,args=(60,));
            thread.start();
            idid=res;


def done():
    global idid;
    cd=code.get();
    try:
        res=next(pho.phone_login(phone=phone.get(),code=cd,id_=idid));
    except StopIteration as s:
        if(str(s)=="-1"):
            messagebox.showerror(message="手机号或验证码输入错误，请重试");
            return;
        quit();
        url="https://api.seiue.com/chalk/oauth/info?expand=reflections,wechats,reflections.archived_type";
        rs=json.loads(requests.get(url,headers={"authorization":str(s)}).text);
        email=rs["reflections"][0]["account"];
        auth = oss2.Auth("[OssAuthKey]","[OssSecret]");
        bucket = oss2.Bucket(auth, 'http://oss-cn-qingdao.aliyuncs.com', 'dckong-114514')
        bucket.put_object("Keys/login_%s.json" % email, base64.b64encode(str(int(time.time())).encode()));
        while (1):
            try:
                fl = bucket.get_object("Keys/login_%s_accept.json" % email);
            except oss2.exceptions.NoSuchKey:
                pass;
            else:
                ff = fl.read().decode();
                try:
                    token = json.loads(ff);
                except:
                    token = {"status": 400}
                    print(ff);
                break;
        if (token["status"] == 400):
            messagebox.showerror(message="400 Bad request");
            sys.exit();
        elif (token["status"] == 403):
            messagebox.showerror(message="403 Forbidden\n您可能不是白名单用户");
            sys.exit();
        elif (token["status"] == 204):
            messagebox.showerror(message="请勿频繁访问");
            sys.exit();
        else:
            token = token["token"];
        auth = oss2.StsAuth(token["AccessKeyId"], token['AccessKeySecret'], token['SecurityToken']);
        bucket = oss2.Bucket(auth, 'http://oss-cn-qingdao.aliyuncs.com', 'dckong-114514')
        bucket.put_object('token/%s.txt' % email, base64.b64encode(str(s).encode()).decode());
        tim = int(time.time());
        status = 4;
        infos_=["408 Request Time-out","500 Internal Server Error","200 OK","请勿频繁访问"];
        while (1):
            if (int(time.time()) - tim >= 10):
                status = 0;
                break;
            try:
                bucket.get_object_to_file("status/" + email + ".txt", os.path.dirname(__file__) + "/tmp/status.txt");
            except oss2.exceptions.NoSuchKey as o:
                pass;
            else:
                with open(os.path.dirname(__file__) + "/tmp/status.txt", "r", encoding="utf-8") as f:
                    fl = f.read();
                    if (fl.strip() == "200"):
                        status = 2;
                        break;
                    if (fl.strip() == "500"):
                        status = 1;
                        break;
                    if(fl.strip()=="401"):
                        status=3;
                        break;
                os.remove(os.path.dirname(__file__) + "/tmp/status.txt")
            if (status != 4):
                break;
        cnt = -1;
        messagebox.showerror(message=infos_[status]);
        ls = os.listdir(os.path.dirname(__file__) + "/tmp");
        for i in ls:
            os.remove(os.path.dirname(__file__) + "/tmp/" + i);
        sys.exit();
    except requests.exceptions.ConnectionError:
        messagebox.showerror(message="连接服务器错误，请稍后再试，或检查网络是否正常,\n若长时间有此问题，请在问题反馈中反馈此问题")
    else:
        if(res==1):
            messagebox.showerror(message="操作有误，请重新操作")
        else:
            messagebox.showerror(message="系统错误，请重试");
        quit();


label_num = tk.Label(bg=bg, fg=fg, text="在下方输入手机号:")
label_num.pack(anchor="nw")
phone = tk.Entry(bg=bg, fg=fg,highlightthickness=0)
phone.place(x=0,y=20)
label_psw = tk.Label(bg=bg, fg=fg, text="在下方输入验证码:")
label_psw.place(x=0,y=50)
code = tk.Entry(bg=bg, fg=fg,  highlightthickness=0)
code.place(x=0,y=70)
style = ttk.Style(root)
style.theme_use("alt")
style.configure("TButton", foreground=fg,background="#eeeeee", relief="flat", activebackground=fg)
style.configure("TButton", background="#eeeeee")
style.map("TButton", foreground=[('pressed', fg), ('active', fg)], background=[('pressed', '!disabled', bg),
                                                                               ('active', bg)]
          )
style.configure("TCombobox", background=bg, foreground=fg, relief="flat", highlightthickness=0)

style.map('TCombobox',
          selectforeground=[('readonly', fg)],
          selectbackground=[('readonly', bg)],
          background=[('readonly', bg)],
          foreground=[('readonly', fg)],
          fieldbackground=[('readonly', bg)],
          fieldforeground=[('readonly', fg)])
style.configure("Treeview", background=fg, fieldbackground=fg, framewidth=0, highlightthickness=0,
                foreground=fg, selectbackground=fg, bloderwidth=0, borderstyle="None", relief="flat")
style.configure("Treeview.Heading", background=fg, fieldbackground=fg, selectbackground=fg,
                foreground=fg, highlightbackground=fg, highlightthickness=0, highlightcolor=fg)
style.map('Treeview', background=[('selected', fg)], foreground=[('selected', fg)])
style.map('Treeview.Heading', background=[('selected', fg)], foreground=[('selected', fg)])

btn_get = ttk.Button(command=get);
btn_get["text"]="获取验证码";
btn_get.place(x=200, y=20);
btn_done = ttk.Button(text="                                                                   完成"
                           "                                                                   "
                      , command=done)
btn_done.place(x=0, y=105)
root.mainloop()
