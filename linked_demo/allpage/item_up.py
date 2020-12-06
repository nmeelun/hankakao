from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *
from PyQt5.Qt import Qt
import json


class ItemUp(QMainWindow):
    person_dict = {}

    def fill_table(self, data=None):
        data = self.data if not data else data

        for desc, price, person in data.items():
            descItem = QTableWidgetItem(desc)
            priceItem = QTableWidgetItem("{0:.2f}".format(price))
            personItem = QTableWidgetItem(person)
            priceItem.setTextAlignment(Qt.AlignRight | Qt.AlignCenter)

            self.item_table.insertRow(self.items)
            self.item_table.setItem(self.items, 0, descItem)
            self.item_table.setItem(self.items, 1, priceItem)
            self.item_table.setItem(self.items, 2, personItem)
            self.items += 1

    def add_item(self):
        desc = self.item_box.text()
        price = self.price_box.text()
        person = self.name_box.text()
        price = float(price)

        try:
            descItem = QTableWidgetItem(desc)
            priceItem = QTableWidgetItem("{0:.2f}".format(float(price)))
            personItem = QTableWidgetItem(person)

            self.item_table.insertRow(self.items)
            self.item_table.setItem(self.items, 0, descItem)
            self.item_table.setItem(self.items, 1, priceItem)
            self.item_table.setItem(self.items, 2, personItem)
            self.items += 1

            self.item_box.setText("")
            self.price_box.setText("")
            self.name_box.setText("")
            print(person)
            len_person = person.split(" ")
            print(len_person)

            for i in len_person:
                if i in self.person_dict:
                    old_value = self.person_dict[i]
                    new_value = old_value + price // len(len_person)
                    self.person_dict[i] = new_value
                else:
                    self.person_dict[i] = price // len(len_person)
            print(self.person_dict)
            with open("data_file.json", "w") as write_file:
                json.dump(self.person_dict, write_file)

        except ValueError:
            pass

    def check_disable(self):
        if self.item_box.text() and self.price_box.text():
            self.btn_add.setEnabled(True)
        else:
            self.btn_add.setEnabled(False)

    def reset_table(self):
        self.item_table.setRowCount(0)
        self.items = 0

        chart = QChart()
        self.chartView.setChart(chart)
        self.person_dict.clear()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 667)
        MainWindow.setMinimumSize(QSize(200, 667))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(66, 73, 90))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        brush = QBrush(QColor(55, 61, 75))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush)
        brush = QBrush(QColor(29, 32, 40))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush)
        brush = QBrush(QColor(255, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(44, 49, 60))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(66, 73, 90))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        brush = QBrush(QColor(55, 61, 75))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        brush = QBrush(QColor(29, 32, 40))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush)
        brush = QBrush(QColor(255, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(44, 49, 60))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(66, 73, 90))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        brush = QBrush(QColor(55, 61, 75))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        brush = QBrush(QColor(29, 32, 40))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush = QBrush(QColor(51, 153, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush)
        brush = QBrush(QColor(255, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush)
        brush = QBrush(QColor(44, 49, 60))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(44, 49, 60))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        self.items = 0
        self.data = {}
        self.sizeHint()
        self.chartView = QChartView()
        self.chartView.setRenderHint(QPainter.Antialiasing)

        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(
            "QMainWindow {background: transparent; }\n"
            "QToolTip {\n"
            "    color: #ffffff;\n"
            "    background-color: rgba(27, 29, 35, 160);\n"
            "    border: 1px solid rgb(100, 100, 100);\n"
            "}"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "background: transparent;\n" "color: rgb(210, 210, 210);"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setMaximumSize(QSize(16777215, 60))
        self.frame_top.setStyleSheet("background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setStyleSheet("background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.frame_top_right.setObjectName("frame_top_right")
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setMaximumSize(QSize(16777215, 30))
        self.frame_top_btns.setStyleSheet("background-color: rgba(33, 37, 43, 150);")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.frame_top_btns.setObjectName("frame_top_btns")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setMaximumSize(QSize(16777215, 25))
        self.frame_label_top_btns.setStyleSheet("background-color: rgb(226, 13, 99);")
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setContentsMargins(8, 0, 10, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.MainWindowBase = QLabel(self.frame_label_top_btns)
        self.MainWindowBase.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.MainWindowBase.setFont(font)
        self.MainWindowBase.setStyleSheet(
            "background: transparent;\n"
            "background-color: rgb(226, 13, 99);\n"
            "margin-left: 5px;"
        )
        self.MainWindowBase.setText("")
        self.MainWindowBase.setObjectName("MainWindowBase")
        self.horizontalLayout_10.addWidget(self.MainWindowBase)
        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setStyleSheet("background-color: rgb(226, 13, 99);")
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4.addWidget(self.frame_btns_right)
        self.verticalLayout_2.addWidget(self.frame_top_btns)
        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setStyleSheet(
            "background-color: rgb(39, 44, 54);\n" "background-color: rgb(226, 13, 99);"
        )
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.frame_top_info.setObjectName("frame_top_info")
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.hankakao_top_info_1 = QLabel(self.frame_top_info)
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(11)
        self.hankakao_top_info_1.setFont(font)
        self.hankakao_top_info_1.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(226, 13, 99);"
        )
        self.hankakao_top_info_1.setObjectName("hankakao_top_info_1")
        self.horizontalLayout_8.addWidget(self.hankakao_top_info_1)
        self.item_top_info_2 = QLabel(self.frame_top_info)
        self.item_top_info_2.setMinimumSize(QSize(0, 0))
        self.item_top_info_2.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.item_top_info_2.setFont(font)
        self.item_top_info_2.setStyleSheet(
            "\n" "color: rgb(255, 255, 255);\n" "background-color: rgb(226, 13, 99);"
        )
        self.item_top_info_2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.item_top_info_2.setObjectName("item_top_info_2")
        self.horizontalLayout_8.addWidget(self.item_top_info_2)
        self.verticalLayout_2.addWidget(self.frame_top_info)
        self.horizontalLayout_3.addWidget(self.frame_top_right)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setStyleSheet("background-color: rgb(16, 30, 65);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setStyleSheet("background-color: rgb(16, 30, 65);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.frame_content_right.setObjectName("frame_content_right")
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QLabel(self.frame_content)
        self.label_8.setMaximumSize(QSize(16777215, 5))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.item = QLabel(self.frame_content)
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(9)
        self.item.setFont(font)
        self.item.setObjectName("item")
        self.verticalLayout_5.addWidget(self.item)
        self.label_10 = QLabel(self.frame_content)
        self.label_10.setMaximumSize(QSize(16777215, 10))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.price = QLabel(self.frame_content)
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(9)
        self.price.setFont(font)
        self.price.setObjectName("price")
        self.verticalLayout_5.addWidget(self.price)
        self.label_3 = QLabel(self.frame_content)
        self.label_3.setMaximumSize(QSize(16777215, 10))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.name = QLabel(self.frame_content)
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(9)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.verticalLayout_5.addWidget(self.name)
        self.label_9 = QLabel(self.frame_content)
        self.label_9.setMaximumSize(QSize(16777215, 5))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.item_box = QLineEdit(self.frame_content)
        self.item_box.setMaximumSize(QSize(150, 16777215))
        self.item_box.setObjectName("item_box")
        self.verticalLayout_6.addWidget(self.item_box)
        self.price_box = QLineEdit(self.frame_content)
        self.price_box.setMaximumSize(QSize(150, 16777215))
        self.price_box.setObjectName("price_box")
        self.verticalLayout_6.addWidget(self.price_box)
        self.name_box = QLineEdit(self.frame_content)
        self.name_box.setMaximumSize(QSize(150, 16777215))
        self.name_box.setObjectName("name_box")
        self.verticalLayout_6.addWidget(self.name_box)
        self.horizontalLayout_11.addLayout(self.verticalLayout_6)
        self.btn_add = QPushButton(self.frame_content)
        self.btn_add.setMaximumSize(QSize(50, 16777215))
        self.btn_add.setObjectName("btn_add")
        self.btn_add.clicked.connect(self.add_item)
        self.btn_add.setEnabled(False)
        self.horizontalLayout_11.addWidget(self.btn_add, 0, Qt.AlignRight)
        self.btn_clear = QPushButton(self.frame_content)
        self.btn_clear.setMaximumSize(QSize(50, 16777215))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_clear.clicked.connect(self.reset_table)
        self.horizontalLayout_11.addWidget(self.btn_clear, 0, Qt.AlignRight)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.item_table = QTableWidget(self.frame_content)
        self.item_table.setMaximumSize(QSize(16777215, 450))
        self.item_table.setObjectName("item_table")
        self.item_table.setColumnCount(3)
        self.item_table.setRowCount(0)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(10)
        item.setFont(font)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        item.setForeground(brush)
        self.item_table.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(10)
        item.setFont(font)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        item.setForeground(brush)
        self.item_table.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(10)
        item.setFont(font)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        item.setForeground(brush)
        self.item_table.setHorizontalHeaderItem(2, item)
        self.verticalLayout_9.addWidget(self.item_table)
        self.label_4 = QLabel(self.frame_content)
        self.label_4.setMaximumSize(QSize(16777215, 10))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.btn_hankakao = QPushButton(self.frame_content)
        self.btn_hankakao.setMaximumSize(QSize(300, 35))
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(11)
        self.btn_hankakao.setFont(font)
        self.btn_hankakao.setLayoutDirection(Qt.LeftToRight)
        self.btn_hankakao.setStyleSheet(
            "color: rgb(226, 13, 99);\n" "background-color: rgb(255, 255, 255);"
        )
        self.btn_hankakao.setObjectName("btn_hankakao")
        self.verticalLayout_9.addWidget(self.btn_hankakao, 0, Qt.AlignHCenter)
        self.label_2 = QLabel(self.frame_content)
        self.label_2.setMaximumSize(QSize(16777215, 0))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.verticalLayout_4.addWidget(self.frame_content)
        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.frame_label_bottom.setObjectName("frame_label_bottom")
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.name_project = QLabel(self.frame_label_bottom)
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(9)
        self.name_project.setFont(font)
        self.name_project.setStyleSheet("color: rgb(98, 103, 111);")
        self.name_project.setObjectName("name_project")
        self.horizontalLayout_7.addWidget(self.name_project)
        self.dev_name = QLabel(self.frame_label_bottom)
        self.dev_name.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(9)
        self.dev_name.setFont(font)
        self.dev_name.setStyleSheet("color: rgb(98, 103, 111);")
        self.dev_name.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.dev_name.setObjectName("dev_name")
        self.horizontalLayout_7.addWidget(self.dev_name)
        self.horizontalLayout_6.addWidget(self.frame_label_bottom)
        self.verticalLayout_4.addWidget(self.frame_grip)
        self.horizontalLayout_2.addWidget(self.frame_content_right)
        self.verticalLayout.addWidget(self.frame_center)
        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        self.item_box.textChanged[str].connect(self.check_disable)
        self.price_box.textChanged[str].connect(self.check_disable)
        self.fill_table()

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HANKAKAO"))
        self.hankakao_top_info_1.setText(_translate("MainWindow", "HAN KA KAO"))
        self.item_top_info_2.setText(_translate("MainWindow", "| item"))
        self.item.setText(_translate("MainWindow", "  ITEM"))
        self.price.setText(_translate("MainWindow", "  price"))
        self.name.setText(_translate("MainWindow", "  name"))
        self.btn_add.setText(_translate("MainWindow", "add"))
        self.btn_clear.setText(_translate("MainWindow", "clear"))
        item = self.item_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Items"))
        item = self.item_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price  (฿)"))
        item = self.item_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "name"))
        self.btn_hankakao.setText(_translate("MainWindow", "HAN KA KAO !"))
        self.name_project.setText(_translate("MainWindow", "OOP FINAL PROJECT"))
        self.dev_name.setText(_translate("MainWindow", "developed by ae, mind, pao"))
