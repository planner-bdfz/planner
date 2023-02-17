# -*- coding: utf-8 -*-
import csv
import json
import threading
import time
import traceback
from datetime import datetime
from shlex import split
from subprocess import Popen, PIPE

from PySide6 import QtWidgets
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from qt_material import *
import to_csv

import os
import sys
import platform

p = os.path.dirname(__file__)
s = platform.system()
plan_it = 0

init = ""
current = ""
current__ = ""


class CykaBlyat(Exception):
    def __init__(self):
        pass


def gen():
    to_csv.change(path=p + "/../temp")


def run_it(cmd, wait=True):
    cmd_run = split(cmd)
    if not cmd_run:
        return
    cmd_run_ = Popen(cmd_run, shell=False, stdout=PIPE, stderr=PIPE, universal_newlines=True, encoding="UTF-8")
    if wait:
        return_ = cmd_run_.wait()
        out, err = cmd_run_.communicate()
        return [return_, out, err]


with open(file=p + "/../options/importance_basis.json") as importance_basis_json:
    load_json = dict(json.load(importance_basis_json))
    work_basis = load_json["work"]
    relax_basis = load_json["relax"]
    sport_basis = load_json["sport"]
    read_basis = load_json["read"]
    study_basis = load_json["study"]
    communicate_basis = load_json["communicate"]
    play_basis = load_json["play"]
    others_basis = load_json["others"]


def get_current():
    global current__
    try:
        while True:
            current_year = datetime.now().year
            current_month = datetime.now().month
            current_date = datetime.now().day
            current_hour = datetime.now().hour
            current_min = datetime.now().minute
            current_sec = datetime.now().second
            current_day = str(current_year) + "-" + str(current_month) + "-" + str(current_date)
            current_time = str(current_hour) + ":" + str(current_min) + ":" + str(current_sec)
            current__ = current_day + " " + current_time
    except:
        pass


thread_current = threading.Thread(target=get_current)
thread_current.start()

with open(file=p + "/../options/planner_option.json") as planner_option_json:
    load_json = dict(json.load(planner_option_json))
    strategy = load_json["strategy"]


def plan(test_a=0, strategy_test="option"):
    global plan_it
    plan_it = 1
    if __name__ != '__main__':
        gen()
        test_a = 0
    if strategy_test == "option":
        with open(file=p + "/../options/planner_option.json") as planner_option_json_test:
            load_json_test = dict(json.load(planner_option_json_test))
            strategy_test = load_json_test["strategy"]
    if test_a == 1:
        run_it("python " + p + "/strategy/" + strategy_test)
    elif test_a == 2:
        run_it("python " + p + "/strategy/" + strategy_test)
    else:
        run_it("python " + p + "/strategy/" + strategy_test)


def main_qt():
    global init
    running = True
    init = "qt"
    gen()

    class Ui_MainWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super(Ui_MainWindow, self).__init__()
            apply_stylesheet(self, "dark_red.xml")
            self.eye_force = 1919810
            self.table_model = None
            self.work_ = None
            self.line = None
            self.sports_ = None
            self.read_ = None
            self.study_ = None
            self.communicate_ = None
            self.play_ = None
            self.others_ = None
            self.strategy = None
            self.autorun_time = None
            self.line_2 = None
            self.start = None
            self.add = None
            self.chalk = None
            self.auto_run = None
            self.line_3 = None
            self.pushButton_3 = None
            self.pushButton_4 = None
            self.line_4 = None
            self.cmd_switch = None
            self.cmd_save = None
            self.cmd_edit = None
            self.cmd_text = None
            self.menubar = None
            self.pushButton = None
            self.pushButton_2 = None
            self.label = None
            self.label_3 = None
            self.label_4 = None
            self.label_5 = None
            self.label_6 = None
            self.label_7 = None
            self.label_8 = None
            self.label_9 = None
            self.label_10 = None
            self.label_11 = None
            self.label_12 = None
            self.label_13 = None
            self.label_14 = None
            self.label_16 = None
            self.label_17 = None
            self.label_18 = None
            self.label_19 = None
            self.tableView = None
            self.relax_ = None
            self.current = None
            self.centralwidget = None
            self.statusbar = None
            self.cmd = 0
            self.setupUi(self)
            self.retranslateUi(self)

        def close_(self):
            if self.cmd_save.isChecked():
                with open(p + "/../logs/planner_option_" + current__ + ".log", "w") as file_:
                    file_.write(self.cmd_text.toPlainText())
            os.remove(p + "/../temp/user_dairy.csv")
            os.kill(os.getpid(), 9)

        def exit_(self):
            if self.cmd_save.isChecked():
                with open(p + "/../logs/planner_option_" + current__ + ".log", "w") as file:
                    file.write(self.cmd_text.toPlainText())
            work_var = self.work_.value()
            relax_var = self.relax_.value()
            sport_var = self.sports_.value()
            read_var = self.read_.value()
            study_var = self.study_.value()
            communicate_var = self.communicate_.value()
            play_var = self.play_.value()
            others_var = self.others_.value()
            strategy_var = self.strategy.currentText()
            try:
                with open(p + "/../options/importance_basis.json", "r", encoding="utf-8") as file_basis:
                    work_code = dict(json.load(file_basis))
                    work_code["work"] = int(work_var)
                with open(p + "/../options/importance_basis.json", "w", encoding="utf-8") as file_basis:
                    json.dump(work_code, file_basis)
                    work_code.clear()
                with open(p + "/../options/importance_basis.json", "r", encoding="utf-8") as file_basis:
                    relax_code = dict(json.load(file_basis))
                    relax_code["relax"] = int(relax_var)
                with open(p + "/../options/importance_basis.json", "w", encoding="utf-8") as file_basis:
                    json.dump(relax_code, file_basis)
                    relax_code.clear()
                with open(p + "/../options/importance_basis.json", "r", encoding="utf-8") as file_basis:
                    sport_code = dict(json.load(file_basis))
                    sport_code["sport"] = int(sport_var)
                with open(p + "/../options/importance_basis.json", "w", encoding="utf-8") as file_basis:
                    json.dump(sport_code, file_basis)
                    sport_code.clear()
                with open(p + "/../options/importance_basis.json", "r", encoding="utf-8") as file_basis:
                    read_code = dict(json.load(file_basis))
                    read_code["read"] = int(read_var)
                with open(p + "/../options/importance_basis.json", "w", encoding="utf-8") as file_basis:
                    json.dump(read_code, file_basis)
                    read_code.clear()
                with open(p + "/../options/importance_basis.json", "r", encoding="utf-8") as file_basis:
                    study_code = dict(json.load(file_basis))
                    study_code["study"] = int(study_var)
                with open(p + "/../options/importance_basis.json", "w", encoding="utf-8") as file_basis:
                    json.dump(study_code, file_basis)
                    study_code.clear()
                with open(p + "/../options/importance_basis.json", "r", encoding="utf-8") as file_basis:
                    communicate_code = dict(json.load(file_basis))
                    communicate_code["communicate"] = int(communicate_var)
                with open(p + "/../options/importance_basis.json", "w", encoding="utf-8") as file_basis:
                    json.dump(communicate_code, file_basis)
                    communicate_code.clear()
                with open(p + "/../options/importance_basis.json", "r", encoding="utf-8") as file_basis:
                    play_code = dict(json.load(file_basis))
                    play_code["play"] = int(play_var)
                with open(p + "/../options/importance_basis.json", "w", encoding="utf-8") as file_basis:
                    json.dump(play_code, file_basis)
                    play_code.clear()
                with open(p + "/../options/importance_basis.json", "r", encoding="utf-8") as file_basis:
                    others_code = dict(json.load(file_basis))
                    others_code["others"] = int(others_var)
                with open(p + "/../options/importance_basis.json", "w", encoding="utf-8") as file_basis:
                    json.dump(others_code, file_basis)
                    others_code.clear()
                with open(p + "/../options/importance_basis.json", "r", encoding="utf-8") as file_basis:
                    unsetted_code = dict(json.load(file_basis))
                    unsetted_code["unsetted"] = int(1145141919810)
                with open(p + "/../options/importance_basis.json", "w", encoding="utf-8") as file_basis:
                    json.dump(unsetted_code, file_basis)
                    unsetted_code.clear()
                with open(p + "/../options/planner_option.json", "r", encoding="utf-8") as file_option:
                    strategy_code = dict(json.load(file_option))
                    strategy_code["strategy"] = strategy_var
                with open(p + "/../options/planner_option.json", "w", encoding="utf-8") as file_option:
                    json.dump(strategy_code, file_option)
                    strategy_code.clear()
            except ValueError:
                return
            os.kill(os.getpid(), 9)

        def setupUi(self, MainWindow):
            if not MainWindow.objectName():
                MainWindow.setObjectName(u"MainWindow")
            MainWindow.resize(900, 600)
            MainWindow.setMinimumSize(QSize(900, 600))
            MainWindow.setMaximumSize(QSize(900, 600))
            MainWindow.setDocumentMode(False)
            MainWindow.setWindowOpacity(0.9)
            self.centralwidget = QWidget(MainWindow)
            self.centralwidget.setObjectName(u"centralwidget")
            self.current = QLabel(self.centralwidget)
            self.current.setObjectName(u"current")
            self.current.setGeometry(QRect(0, 0, 331, 16))
            self.work_ = QSlider(self.centralwidget)
            self.work_.setObjectName(u"work_")
            self.work_.setGeometry(QRect(20, 250, 160, 16))
            self.work_.setOrientation(Qt.Horizontal)
            self.work_.setMinimum(0)
            self.work_.setMaximum(10)
            self.work_.setValue(work_basis)
            self.work_.setSingleStep(1)
            self.tableView = QTableView(self.centralwidget)
            self.tableView.setObjectName(u"tableView")
            self.tableView.setGeometry(QRect(0, 20, 901, 191))
            self.table_model = QStandardItemModel(0, 10)
            self.tableView.setModel(self.table_model)
            self.tableView.setColumnWidth(0, 180)
            self.tableView.setColumnWidth(1, 280)
            self.tableView.setColumnWidth(2, 180)
            self.tableView.setColumnWidth(3, 60)
            self.tableView.setColumnWidth(4, 80)
            self.tableView.setColumnWidth(5, 80)
            self.tableView.setColumnWidth(6, 80)
            self.tableView.setColumnWidth(7, 80)
            self.tableView.setColumnWidth(8, 80)
            self.tableView.setColumnWidth(9, 80)
            self.tableView.setColumnWidth(10, 80)
            self.tableView.setColumnWidth(11, 80)
            self.tableView.setColumnWidth(12, 180)
            self.tableView.setColumnWidth(13, 180)
            self.tableView.setColumnWidth(14, 180)
            self.tableView.setEditTriggers(QTableView.NoEditTriggers)
            self.label_3 = QLabel(self.centralwidget)
            self.label_3.setObjectName(u"label_3")
            self.label_3.setGeometry(QRect(20, 230, 60, 16))
            self.label_4 = QLabel(self.centralwidget)
            self.label_4.setObjectName(u"label_4")
            self.label_4.setGeometry(QRect(20, 270, 60, 16))
            self.relax_ = QSlider(self.centralwidget)
            self.relax_.setObjectName(u"relax_")
            self.relax_.setGeometry(QRect(20, 290, 160, 16))
            self.relax_.setOrientation(Qt.Horizontal)
            self.relax_.setMinimum(0)
            self.relax_.setMaximum(10)
            self.relax_.setValue(relax_basis)
            self.relax_.setSingleStep(1)
            self.label_5 = QLabel(self.centralwidget)
            self.label_5.setObjectName(u"label_5")
            self.label_5.setGeometry(QRect(0, 210, 81, 16))
            self.line = QFrame(self.centralwidget)
            self.line.setObjectName(u"line")
            self.line.setGeometry(QRect(0, 230, 20, 331))
            self.line.setFrameShape(QFrame.VLine)
            self.line.setFrameShadow(QFrame.Sunken)
            self.label_6 = QLabel(self.centralwidget)
            self.label_6.setObjectName(u"label_6")
            self.label_6.setGeometry(QRect(20, 310, 60, 16))
            self.sports_ = QSlider(self.centralwidget)
            self.sports_.setObjectName(u"sports_")
            self.sports_.setGeometry(QRect(20, 330, 160, 16))
            self.sports_.setOrientation(Qt.Horizontal)
            self.sports_.setMinimum(0)
            self.sports_.setMaximum(10)
            self.sports_.setValue(sport_basis)
            self.sports_.setSingleStep(1)
            self.label_7 = QLabel(self.centralwidget)
            self.label_7.setObjectName(u"label_7")
            self.label_7.setGeometry(QRect(20, 350, 60, 16))
            self.read_ = QSlider(self.centralwidget)
            self.read_.setObjectName(u"read_")
            self.read_.setGeometry(QRect(20, 370, 160, 16))
            self.read_.setOrientation(Qt.Horizontal)
            self.read_.setMinimum(0)
            self.read_.setMaximum(10)
            self.read_.setValue(read_basis)
            self.read_.setSingleStep(1)
            self.label_8 = QLabel(self.centralwidget)
            self.label_8.setObjectName(u"label_8")
            self.label_8.setGeometry(QRect(20, 390, 60, 16))
            self.study_ = QSlider(self.centralwidget)
            self.study_.setObjectName(u"study_")
            self.study_.setGeometry(QRect(20, 410, 160, 16))
            self.study_.setOrientation(Qt.Horizontal)
            self.study_.setMinimum(0)
            self.study_.setMaximum(10)
            self.study_.setValue(study_basis)
            self.study_.setSingleStep(1)
            self.label_9 = QLabel(self.centralwidget)
            self.label_9.setObjectName(u"label_9")
            self.label_9.setGeometry(QRect(20, 430, 60, 16))
            self.communicate_ = QSlider(self.centralwidget)
            self.communicate_.setObjectName(u"communicate_")
            self.communicate_.setGeometry(QRect(20, 450, 160, 16))
            self.communicate_.setOrientation(Qt.Horizontal)
            self.communicate_.setMinimum(0)
            self.communicate_.setMaximum(10)
            self.communicate_.setValue(communicate_basis)
            self.communicate_.setSingleStep(1)
            self.label_10 = QLabel(self.centralwidget)
            self.label_10.setObjectName(u"label_10")
            self.label_10.setGeometry(QRect(20, 470, 60, 16))
            self.play_ = QSlider(self.centralwidget)
            self.play_.setObjectName(u"play_")
            self.play_.setGeometry(QRect(20, 490, 160, 16))
            self.play_.setOrientation(Qt.Horizontal)
            self.play_.setMinimum(0)
            self.play_.setMaximum(10)
            self.play_.setValue(play_basis)
            self.play_.setSingleStep(1)
            self.label_11 = QLabel(self.centralwidget)
            self.label_11.setObjectName(u"label_11")
            self.label_11.setGeometry(QRect(20, 510, 60, 16))
            self.others_ = QSlider(self.centralwidget)
            self.others_.setObjectName(u"others_")
            self.others_.setGeometry(QRect(20, 530, 160, 16))
            self.others_.setOrientation(Qt.Horizontal)
            self.others_.setMinimum(0)
            self.others_.setMaximum(10)
            self.others_.setValue(others_basis)
            self.others_.setSingleStep(1)
            self.label_12 = QLabel(self.centralwidget)
            self.label_12.setObjectName(u"label_12")
            self.label_12.setGeometry(QRect(190, 210, 60, 16))
            strategy_list = os.listdir(p + "/strategy")
            tmp = []
            for i in strategy_list:
                if os.path.splitext(i)[-1] == ".py":
                    with open(p + "/strategy/" + i, "r", encoding="utf-8") as f:
                        fl = f.readlines()
                    if fl[1] == "# -=- planner_strategy -=-\n":
                        tmp.append(i)
            strategy_list = tmp
            self.strategy = QComboBox(self.centralwidget)
            self.strategy.setObjectName(u"strategy")
            self.strategy.setGeometry(QRect(190, 230, 185, 22))
            self.strategy.addItems(strategy_list)
            self.label_13 = QLabel(self.centralwidget)
            self.label_13.setObjectName(u"label_13")
            self.label_13.setGeometry(QRect(190, 260, 141, 16))
            self.autorun_time = QSpinBox(self.centralwidget)
            self.autorun_time.setObjectName(u"autorun_time")
            self.autorun_time.setGeometry(QRect(190, 280, 185, 22))
            self.autorun_time.setMaximum(720)
            self.autorun_time.setMinimum(10)
            self.autorun_time.setWrapping(False)
            self.autorun_time.setSingleStep(10)
            self.autorun_time.setSuffix(QCoreApplication.translate("MainWindow", u"min", None))
            self.label_14 = QLabel(self.centralwidget)
            self.label_14.setObjectName(u"label_14")
            self.label_14.setGeometry(QRect(190, 310, 131, 16))
            self.line_2 = QFrame(self.centralwidget)
            self.line_2.setObjectName(u"line_2")
            self.line_2.setGeometry(QRect(190, 330, 16, 81))
            self.line_2.setFrameShape(QFrame.VLine)
            self.line_2.setFrameShadow(QFrame.Sunken)
            self.start = QCheckBox(self.centralwidget)
            self.start.setObjectName(u"start")
            self.start.setGeometry(QRect(210, 350, 130, 21))
            self.add = QCheckBox(self.centralwidget)
            self.add.setObjectName(u"add")
            self.add.setGeometry(QRect(210, 370, 130, 21))
            self.chalk = QCheckBox(self.centralwidget)
            self.chalk.setObjectName(u"chalk")
            self.chalk.setGeometry(QRect(210, 390, 130, 21))
            self.auto_run = QCheckBox(self.centralwidget)
            self.auto_run.setObjectName(u"auto_run")
            self.auto_run.setGeometry(QRect(210, 330, 130, 21))
            self.pushButton = QPushButton(self.centralwidget)
            self.pushButton.setObjectName(u"pushButton")
            self.pushButton.setGeometry(QRect(210, 430, 165, 26))
            self.label_16 = QLabel(self.centralwidget)
            self.label_16.setObjectName(u"label_16")
            self.label_16.setGeometry(QRect(190, 410, 61, 16))
            self.line_3 = QFrame(self.centralwidget)
            self.line_3.setObjectName(u"line_3")
            self.line_3.setGeometry(QRect(190, 430, 16, 131))
            self.line_3.setFrameShape(QFrame.VLine)
            self.line_3.setFrameShadow(QFrame.Sunken)
            self.pushButton_2 = QPushButton(self.centralwidget)
            self.pushButton_2.setObjectName(u"pushButton_2")
            self.pushButton_2.setGeometry(QRect(210, 460, 165, 26))
            self.pushButton_3 = QPushButton(self.centralwidget)
            self.pushButton_3.setObjectName(u"pushButton_3")
            self.pushButton_3.setGeometry(QRect(210, 490, 165, 26))
            self.pushButton_4 = QPushButton(self.centralwidget)
            self.pushButton_4.setObjectName(u"pushButton_4")
            self.pushButton_4.setGeometry(QRect(210, 520, 165, 26))
            self.label_17 = QLabel(self.centralwidget)
            self.label_17.setObjectName(u"label_17")
            self.label_17.setGeometry(QRect(360, 210, 60, 16))
            self.line_4 = QFrame(self.centralwidget)
            self.line_4.setObjectName(u"line_4")
            self.line_4.setGeometry(QRect(360, 230, 20, 331))
            self.line_4.setFrameShape(QFrame.VLine)
            self.line_4.setFrameShadow(QFrame.Sunken)
            self.cmd_switch = QCheckBox(self.centralwidget)
            self.cmd_switch.setObjectName(u"cmd_switch")
            self.cmd_switch.setGeometry(QRect(410, 210, 101, 21))
            self.cmd_save = QCheckBox(self.centralwidget)
            self.cmd_save.setObjectName(u"cmd_save")
            self.cmd_save.setGeometry(QRect(510, 210, 191, 21))
            self.label_18 = QLabel(self.centralwidget)
            self.label_18.setObjectName(u"label_18")
            self.label_18.setGeometry(QRect(710, 210, 191, 16))
            self.cmd_edit = QLineEdit(self.centralwidget)
            self.cmd_edit.setObjectName(u"cmd_edit")
            self.cmd_edit.setGeometry(QRect(380, 530, 521, 22))
            self.label_19 = QLabel(self.centralwidget)
            self.label_19.setObjectName(u"label_19")
            self.label_19.setGeometry(QRect(380, 510, 111, 16))
            self.cmd_text = QTextBrowser(self.centralwidget)
            self.cmd_text.setObjectName(u"cmd_text")
            self.cmd_text.setGeometry(QRect(380, 230, 521, 281))

            def raise_c(error_information="unknown", fatal=False, error_type="UnknownError"):
                if fatal:
                    cmd_insert(error_type + ":" + error_information, "fatal_error")
                else:
                    cmd_insert(error_type + ":" + error_information, "error")

            def cmd_insert(cmd, tag="normal"):
                try:
                    cmd = str(cmd)
                except:
                    pass
                if tag == "normal":
                    self.cmd_text.append("<font color = '#eeeeee'>[INFO] " + cmd + "<font>")
                elif tag == "success":
                    self.cmd_text.append("<font color = '#00ff00'>[INFO] " + cmd + "<font>")
                elif tag == "note":
                    self.cmd_text.append("<font color = '#0000ff'>[INFO] " + cmd + "<font>")
                elif tag == "warning":
                    self.cmd_text.append("<font color = '#ffff00'>[WARN] " + cmd + "<font>")
                elif tag == "error":
                    self.cmd_text.append("<font color = '#ff0000'>[ERROR] " + cmd + "<font>")
                elif tag == "fatal_error":
                    self.cmd_text.append("<font color = '#880000'>[FATAL] " + cmd + "<font>")
                elif tag == "debug":
                    self.cmd_text.append("<font color = '#00ffff'>[DEBUG] " + cmd + "<font>")

            def cmd_command(command):
                with open(p + "/../src/word_black_list", "r") as black_list:
                    list_ = black_list.read().splitlines()
                    for text_replace in range(len(list_)):
                        position = command.find(list_[text_replace])
                        if position == -1:
                            continue
                        else:
                            c = len(list_[text_replace])
                            command = command[0:position] + '*' * c + command[position + c:len(command)]
                cmd_insert("adv_option>_" + command, "debug")

                def print_c(text):
                    cmd_insert(text)

                def say(text):
                    say_text = text
                    if str(platform.system()) == "Darwin":
                        os.system("say " + say_text)
                    elif str(platform.system()) == "Windows":
                        os.system('CreateObject("SAPI.SpVoice").Speak"' + say_text + '"')

                def help_c(help_command="all"):
                    if help_command == "all":
                        cmd_insert("print: print [string]")
                        cmd_insert("say: say [string]")
                        cmd_insert("help: help *command*")
                        cmd_insert("soviet: soviet «type»")

                if self.cmd_switch.isChecked():
                    if command[:6] == "print ":
                        print_c(command[6:])
                    elif command[:4] == "say ":
                        say(command[4:])
                    elif command[:5] == "help ":
                        help_c(command[5:])
                    elif command == "help":
                        help_c()
                    elif command[:7] == "soviet ":
                        try:
                            exec("soviet." + command[7:] + "()")
                        except:
                            raise_c("command 'soviet' has no attribute '" + command[7:] + "'", False,
                                    "AttributeError")
                        else:
                            print_c("ypa!")
                    elif command[:3] == "yee":
                        cmd_insert("░░░░░░░░░░░▄███▄▄▄░░░░░░░░")
                        cmd_insert("░░░░░░░▄▄▄██▀▀▀▀███▄░░░░░░")
                        cmd_insert("░░░░░▄▀▀░░░░░░░░░░░▀█░░░░░")
                        cmd_insert("░░▄▄▀░░░░░░░░░░░░░░░▀█░░░░")
                        cmd_insert("░░█░░░░░▀▄░░▄▀░░░░░░░░█░░░")
                        cmd_insert("░░▐██▄░░▀▄▀▀▄▀░░▄██▀░▐▌░░░")
                        cmd_insert("░░█▀█░▀░░░▀▀░░░▀░█▀░░▐▌░░░")
                        cmd_insert("░░█░░▀▐░░░░░░░░▌▀░░░░░█░░░")
                        cmd_insert("░█░░░░░░░░░░░░░░░░░░░█░░░░")
                        cmd_insert("░░█░░▀▄░░░░▄▀░░░░░░░░█░░░░")
                        cmd_insert("░░█░░░░░░░░░░░▄▄░░░░█░░░░░")
                        cmd_insert("░░░█▀██▀▀▀▀██▀░░░░░░█░░░░░")
                        cmd_insert("░░░█░░▀████▀░░░░░░░█░░░░░░")
                        cmd_insert("░░░░█░░░░░░░░░░░░▄█░░░░░░░")
                        cmd_insert("░░░░░██░░░░░█▄▄▀▀░█░░░░░░░")
                        cmd_insert("░░░░░░▀▀█▀▀▀▀░░░░░░█░░░░░░")
                        cmd_insert("░░░░░░░█░░░░░░░░░░░░█░░░░░")
                        cmd_insert("yee~")
                    elif command.split(" ")[0] == "raise":
                        try:
                            if command.split(" ")[1] == "true":
                                raise_c("RAISED FATAL " + '"' + command.split(" ")[2] + '"', True, "DebugError")
                            else:
                                raise_c("RAISED ERROR " + '"' + command.split(" ")[2] + '"', False, "DebugError")
                        except:
                            cmd_insert("Usage: raise <is fatal> [string]", "Warning")
                    else:
                        raise_c("command " + '"' + command + '"' + " not found", False, "InputError")
                else:
                    raise_c("request rejected", False, "InterruptError")

            def run_cmd():
                cmd_command(self.cmd_edit.text())
                self.cmd_edit.clear()

            def cmd_():
                if self.cmd == 0:
                    self.cmd = 1
                    cmd_insert("Planner command loaded", "success")
                    cmd_insert("This function may be dangerous to this app's system", "warning")
                    cmd_insert("It may causes serious error, even fatal error that can causes crash",
                               "warning")
                    cmd_insert("If you know how dangerous it is and you need to use it:", "note")
                    cmd_insert("Please entry at the bottom of this frame", "note")
                    cmd_insert("If you finished, press 'Enter' to run", "note")
                    self.cmd_edit.setEnabled(True)

            self.cmd_switch.stateChanged.connect(cmd_)

            self.cmd_edit.returnPressed.connect(run_cmd)

            def test_planner_strategy():
                cmd_insert("Testing: "+self.strategy.currentText(), "debug")
                location = p + "/strategy/" + self.strategy.currentText()
                try:
                    if s == "Windows":
                        a = run_it("python "+location)
                    else:
                        a = run_it("python3.9 " + location)
                except:
                    cmd_insert("FAILED", "error")
                    print(traceback.print_exc())
                else:
                    if a[2] != "":
                        cmd_insert("FAILED", "error")
                        print(traceback.format_exc())
                    else:
                        cmd_insert("SUCCESS", "success")

            self.pushButton.pressed.connect(test_planner_strategy)

            self.pushButton_4.pressed.connect(self.close_)
            self.pushButton_3.pressed.connect(self.exit_)
            self.cmd_edit.setEnabled(False)

            def read():
                self.table_model.clear()
                self.table_model.setHorizontalHeaderLabels(["ID",
                                                            "标题",
                                                            "DDL",
                                                            "类型",
                                                            "类型重要",
                                                            "重要基值",
                                                            "重要值",
                                                            "紧急参数",
                                                            "剩余时间",
                                                            "预计时间",
                                                            "紧急度",
                                                            "权重",
                                                            "起始时间",
                                                            "结束时间"
                                                            ])
                self.tableView.setEditTriggers(QTableView.NoEditTriggers)
                try:
                    with open(p + '/../temp/user_dairy.csv', 'r', newline="", encoding='utf-8',
                              errors='ignore') as file:
                        for row in csv.reader(file):
                            if str(row) == "['ID', " \
                                           "'标题', " \
                                           "'DDL', " \
                                           "'类型', " \
                                           "'类型重要', " \
                                           "'重要基值', " \
                                           "'重要值', " \
                                           "'紧急参数', " \
                                           "'剩余时间', " \
                                           "'预计时间', " \
                                           "'紧急度', " \
                                           "'权重', " \
                                           "'起始时间', " \
                                           "'结束时间']":
                                pass
                            elif str(row) == "[]":
                                pass
                            else:
                                items = [
                                    QStandardItem(field)
                                    for field in row
                                ]
                                self.table_model.appendRow(items)
                    file.close()
                except FileNotFoundError:
                    pass

            def reload():
                gen()
                read()

            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            read()

            QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u89c4\u5212\u5668\u8bbe\u7f6e",
                                                                 None))
            self.current.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u65f6\u95f4\uff1a", None))
            self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u4f5c\uff1a", None))
            self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4f11\u95f2\uff1a", None))
            self.label_5.setText(
                QCoreApplication.translate("MainWindow", u"\u91cd\u8981\u5ea6\u57fa\u503c\uff1a", None))
            self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\uff1a", None))
            self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u9605\u8bfb\uff1a", None))
            self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u4e60\uff1a", None))
            self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u793e\u4ea4\uff1a", None))
            self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5a31\u4e50\uff1a", None))
            self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5176\u5b83\uff1a", None))
            self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u89c4\u5212\u7b56\u7565\uff1a", None))
            self.label_13.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u81ea\u52a8\u8fd0\u884c\u95f4"
                                                             u"\u9694\uff08\u5206\u949f\uff09\uff1a",
                                                             None))
            self.label_14.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u5728\u8fd9\u4e9b\u65f6\u5019"
                                                             u"\u81ea\u52a8\u8fd0\u884c"
                                                             u"\uff1a",
                                                             None))
            self.start.setText(
                QCoreApplication.translate("MainWindow", u"\u6bcf\u6b21\u542f\u52a8\u7a0b\u5e8f\u65f6", None))
            self.add.setText(
                QCoreApplication.translate("MainWindow", u"\u6bcf\u6b21\u6dfb\u52a0\u65e5\u7a0b\u65f6", None))
            self.chalk.setText(
                QCoreApplication.translate("MainWindow", u"\u6bcf\u6b21\u540c\u6b65\u5e0c\u60a6\u65f6", None))
            self.auto_run.setText(
                QCoreApplication.translate("MainWindow", u"\u5b9a\u65f6\u7684\u81ea\u52a8\u8fd0\u884c", None))
            self.pushButton.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u8c03\u8bd5策略程序\u4f46\u4e0d"
                                                               u"\u4fdd\u5b58",
                                                               None))
            self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u8fd0\u884c\uff1a", None))
            self.pushButton_2.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u8fd0\u884c\u4e4b\u540e\u9009\u62e9\u662f\u5426"
                                                                 u"\u4fdd\u5b58",
                                                                 None))
            self.pushButton_3.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u5173\u95ed\u9875\u9762\u5e76\u8fd0\u884c\u548c"
                                                                 u"\u4fdd\u5b58",
                                                                 None))
            self.pushButton_4.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u4e0d\u4fdd\u5b58\u548c\u4e0d\u8fd0\u884c\u5e76"
                                                                 u"\u5173\u95ed",
                                                                 None))
            self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u63a7\u5236\u53f0\uff1a", None))
            self.cmd_switch.setText(
                QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u6307\u4ee4", None))
            self.cmd_save.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u5173\u95ed\u540e\u4fdd\u5b58\u5185"
                                                             u"\u5bb9\u81f3\u65e5"
                                                             u"\u5fd7\u6587\u4ef6\u5939",
                                                             None))
            self.label_18.setText(QCoreApplication.translate("MainWindow",
                                                             u"// \u6ee5\u7528\u63a7\u5236\u53f0\u53ef\u80fd\u9020"
                                                             u"\u6210\u6570\u636e\u635f\u5931",
                                                             None))
            self.label_19.setText(
                QCoreApplication.translate("MainWindow", u"\u5728\u8fd9\u91cc\u8f93\u5165\u6307\u4ee4\uff1a", None))

            def show_current():
                while running:
                    try:
                        work_var = int(self.work_.value())
                        relax_var = int(self.relax_.value())
                        sport_var = int(self.sports_.value())
                        read_var = int(self.read_.value())
                        study_var = int(self.study_.value())
                        communicate_var = int(self.communicate_.value())
                        play_var = int(self.play_.value())
                        others_var = int(self.others_.value())
                        self.current.setText(
                            QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u65f6\u95f4\uff1a" + current__,
                                                       None))
                        self.label_3.setText(
                            QCoreApplication.translate("MainWindow", u"\u5de5\u4f5c\uff1a" + str(work_var), None))
                        self.label_4.setText(
                            QCoreApplication.translate("MainWindow", u"\u4f11\u95f2\uff1a" + str(relax_var), None))
                        self.label_6.setText(
                            QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\uff1a" + str(sport_var), None))
                        self.label_7.setText(
                            QCoreApplication.translate("MainWindow", u"\u9605\u8bfb\uff1a" + str(read_var), None))
                        self.label_8.setText(
                            QCoreApplication.translate("MainWindow", u"\u5b66\u4e60\uff1a" + str(study_var), None))
                        self.label_9.setText(
                            QCoreApplication.translate("MainWindow", u"\u793e\u4ea4\uff1a" + str(communicate_var),
                                                       None))
                        self.label_10.setText(
                            QCoreApplication.translate("MainWindow", u"\u5a31\u4e50\uff1a" + str(play_var), None))
                        self.label_11.setText(
                            QCoreApplication.translate("MainWindow", u"\u5176\u5b83\uff1a" + str(others_var), None))
                    except:
                        pass

            thread_c = threading.Thread(target=show_current)
            thread_c.start()

        def closeEvent(self, event):
            msg = QMessageBox.question(self, "规划器设置", "规划器设置即将退出，是否保存并运行规划",
                                       QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            if msg == QMessageBox.Save:
                self.exit_()
            elif msg == QMessageBox.Discard:
                self.close_()
            elif msg == QMessageBox.Cancel:
                event.ignore()

    app = QApplication(sys.argv)
    root = Ui_MainWindow()
    root.show()
    app.exit(app.exec())
    running = False
    os.kill(os.getpid(), 9)


if __name__ == '__main__':
    try:
        main_qt()
    except:
        QMessageBox.about("规划器控制面板", "规划器出现错误崩溃，请将logs文件夹中的崩溃日志上传")
        os.kill(os.getpid(), 9)
