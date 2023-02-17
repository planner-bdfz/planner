import os
import oss2;
import tkinter as tk
from tkinter import messagebox
from itertools import islice
import requests
import feedback
import getage
import system
import webbrowser;
import threading;
import platform;
import time;
import sys;
import base64;
import json;
import webbrowser;
path = (os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
def to_phone():
    global root;
    global cnt;
    root.destroy();
    import login_phone;
def done():
    global email, pswd,cnt;
    email = input_label.get().strip();
    pswd = input_label2.get().strip();
    try:
        rt = next(system.run(id=email, pswd=pswd,mode=mode))  # 调用用next调用，要不然没法调用
        if rt == -3:
            messagebox.showerror(message="authorization有误，请检查是否粘贴错误，或者authorization已过期,\n若长时间有此问题，请在问题反馈中反馈此问题")
        if rt == -1:
            messagebox.showerror(message="输入账号密码有误，请重试")
            cnt+=1;
        if(rt==-8):
            messagebox.showerror(message="未通过白名单验证，请将申请白名单");
        if(rt==-2):
            messagebox.showerror(message="未连接到互联网或连接云端失败，请重试");
    except StopIteration as s:
        root.destroy();
        auth = oss2.Auth("LTAI5tMkyCMpgP7TbnekHBe4","jgFNE0w35VwFr5AiFcbFvVXAMORmtt");
        bucket = oss2.Bucket(auth, 'http://oss-cn-qingdao.aliyuncs.com', 'dckong-114514')
        bucket.put_object("Keys/login_%s.json"%email,base64.b64encode(str(int(time.time())).encode()));
        while(1):
            try:
                fl=bucket.get_object("Keys/login_%s_accept.json"%email);
            except oss2.exceptions.NoSuchKey:
                pass;
            else:
                ff=fl.read().decode();
                try:
                    token=json.loads(ff);
                except:
                    token={"status":400}
                break;
        if(token["status"]==400):
            messagebox.showerror(message="400 Bad request");
            sys.exit();
        elif(token["status"]==403):
            messagebox.showerror(message="403 Forbidden\n您可能不是白名单用户");
            sys.exit();
        elif(token["status"]==204):
            messagebox.showerror(message="请勿频繁访问");
            sys.exit();
        else:
            token=token["token"];
        auth = oss2.StsAuth(token["AccessKeyId"], token['AccessKeySecret'], token['SecurityToken']);
        bucket = oss2.Bucket(auth, 'http://oss-cn-qingdao.aliyuncs.com', 'dckong-114514')
        bucket.put_object('token/%s.txt'%email,base64.b64encode(str(s).encode()).decode());
        tim=int(time.time());
        status=4;
        infos_=["408 Request Time-out","500 Internal Server Error","200 OK","禁止频繁访问"];
        while(1):
            if(int(time.time())-tim>=10):
                status=0;
                break;
            try:
                bucket.get_object_to_file("status/"+email+".txt", os.path.dirname(__file__)+"/../temp/status.txt");
            except oss2.exceptions.NoSuchKey as o:
                pass;
            else:
                with open(os.path.dirname(__file__)+"/../temp/status.txt","r",encoding="utf-8") as f:
                    fl=f.read();
                    if(fl.strip()=="200"):
                        status=2;
                        break;
                    if(fl.strip()=="500"):
                        status=1;
                        break;
                    if(fl.strip()=="401"):
                        status=3;
                        break;
                os.remove(os.path.dirname(__file__)+"/../temp/status.txt")
            if(status!=4):
                break;
        cnt=-1;
        messagebox.showerror(message=infos_[status]);
        ls=os.listdir(os.path.dirname(__file__)+"/../temp");
        for i in ls:
            os.remove(os.path.dirname(__file__)+"/../temp/"+i);
        sys.exit();
    except requests.exceptions.ConnectionError:
        messagebox.showerror(message="连接服务器错误，请稍后再试，或检查网络是否正常,\n若长时间有此问题，请在问题反馈中反馈此问题")

def che_show_pswd():
        global input_label2
        pswda = input_label2.get()
        if show_pswd.get() == 0:
            input_label2.destroy()
            input_label2 = tk.Entry(f2, fg="#000088", bg="#ffff77", show="*")
            input_label2.insert(tk.INSERT, pswda)
            input_label2.place(x=300, y=15)
        elif show_pswd.get() == 1:
            input_label2.destroy()
            input_label2 = tk.Entry(f2, fg="#000088", bg="#ffff77")
            input_label2.insert(tk.INSERT, pswda)
            input_label2.place(x=300, y=15)
def cg():
    global mode;
    mode=mode^1;
    label2["text"] = txt[mode];
    bdfzbt["text"]=bttxt[mode]
if(1):
    mode=0;
    txt=["请输入登录密码:","请输入门户密码:"]
    bttxt=["单击以使用北大附中门户登录","单击以使用希悦账户密码登录"]
    root = tk.Tk();
    root.title("同步希悦日程");
    w = root.winfo_screenwidth();
    h = root.winfo_screenheight();
    if (platform.system() == "Darwin" or platform.system() == "Linux"):
        height=300
    else:
        height=270
    geometry = "600x%d+"%height + str(int(int(w) / 2 - 300)) + "+" + str(int(int(h) / 2 - 135))
    root.geometry(geometry)
    root.resizable(width=False, height=False)
    f1 = tk.Frame(root, width=10000, height=50)
    label = tk.Label(f1, text="输入登录账号(学号):", font=('宋体', 24))
    label.place(x=50, y=10)
    input_label = tk.Entry(f1, fg="#000088", bg="#ffff77")
    input_label.place(x=300, y=15)
    f1.pack()
    f2 = tk.Frame(root, width=10000, height=50)
    label2 = tk.Label(f2, text="输入登录密码:", font=('宋体', 24))
    label2.place(x=50, y=10)
    input_label2 = tk.Entry(f2, fg="#000088", bg="#ffff77", show="*")
    input_label2.place(x=300, y=15);
    show_pswd = tk.IntVar();
    show_pswd.set(0);
    show = tk.Checkbutton(f2, text="显示密码", command=che_show_pswd, variable=show_pswd, offvalue=0, onvalue=1)
    show.place(x=500, y=20)
    f2.pack()
    authorization = ""
    done_btn = tk.Button(text="完成", command=done, bg="#ffffff", font=("宋体", 28), fg="#000000")
    done_btn.pack(fill="x", pady=10)
    pro = tk.Button(root, text="  问题反馈  ", font=("宋体", 40), width=10, command=feedback.fdback)
    pro.pack(fill="x", pady=10)
    cv = tk.IntVar()
    bdfzbt=tk.Button(root,text="单击以使用北大附中门户登录",width=22,font=("宋体",18),bg="#000000",fg="#000000",command=lambda:cg());
    bdfzbt.place(x=330,y=230);
    phonelgin=tk.Button(root,text="单击以使用手机验证码登录",width=22,font=("宋体",18),bg="#000000",fg="#000000",command=lambda:to_phone());
    phonelgin.place(x=30,y=230);
    link=tk.Button(root,text="    申请白名单点这里    ",font=("宋体",18),bg="#000000",fg="#000000",
                   command=lambda:webbrowser.open("https://www.wjx.top/vj/mMkw1Ng.aspx"))
    link.place(x=200,y=260);
    root.mainloop()
