import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("514x114")
bg = "#000000"
fg = "#ffffff"
root.configure(background=bg)
root.wm_attributes("-alpha", 0.8)
root.title("验证码登陆")


def get():
    pass


def done():
    pass


label_num = tk.Label(bg=bg, fg=fg, text="在下方输入手机号\_____________________________________________________")
label_num.pack(anchor="nw")
entry_num = tk.Entry(bg=bg, fg=fg, relief="flat", highlightthickness=0)
entry_num.pack(anchor="nw", fill="x")
label_psw = tk.Label(bg=bg, fg=fg, text="在下方输入验证码\_____________________________________________________")
label_psw.pack(anchor="nw")
entry_psw = tk.Entry(bg=bg, fg=fg, relief="flat", highlightthickness=0)
entry_psw.pack(anchor="nw", fill="x")
style = ttk.Style(root)
style.theme_use("alt")
style.configure("TButton", foreground=fg, background=fg, relief="flat", activebackground=fg)
style.configure("TButton", background=bg)
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

btn_get = ttk.Button(text="获取验证码", command=get)
btn_get.place(x=0, y=85)
btn_done = ttk.Button(text="完成", command=done)
btn_done.place(x=110, y=85)
root.mainloop()
