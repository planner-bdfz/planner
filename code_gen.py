for i in range(24):
    print("self.h" + str(i + 1) + " = QLabel(self.timeAxisWidget)\n"
          "self.h" + str(i + 1) + ".setText(" + '"__' + str(i + 1) + ":" + "00" + '"' + ")\n"
          "self.h" + str(i + 1) + ".setStyleSheet(" + '"font:10px"' + ")\n"
          "self.h" + str(i + 1) + ".setAlignment(Qt.AlignBottom)")
print("\n")
for i in range(24):
    print("self.h" + str(i + 1) + ".setGeometry(5, int(self.timeAxisWidget.height() / 24) * " + str(i) +
          " + 1, 100, int(self.timeAxisWidget.height() / 24))")
