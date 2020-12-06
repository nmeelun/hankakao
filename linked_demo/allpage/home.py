from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import Qt


class Home(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Home")
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
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(8)
        MainWindow.setFont(font)
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
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
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
        self.home_top_info_2 = QLabel(self.frame_top_info)
        self.home_top_info_2.setMinimumSize(QSize(0, 0))
        self.home_top_info_2.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.home_top_info_2.setFont(font)
        self.home_top_info_2.setStyleSheet(
            "\n" "color: rgb(255, 255, 255);\n" "background-color: rgb(226, 13, 99);"
        )
        self.home_top_info_2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.home_top_info_2.setObjectName("home_top_info_2")
        self.horizontalLayout_8.addWidget(self.home_top_info_2)
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
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setStyleSheet("background: transparent;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout_5 = QVBoxLayout(self.page_home)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QLabel(self.page_home)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.hankakao_home = QLabel(self.page_home)
        self.hankakao_home.setMinimumSize(QSize(0, 30))
        self.hankakao_home.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(22)
        self.hankakao_home.setFont(font)
        self.hankakao_home.setStyleSheet("color: rgb(255, 255, 255);")
        self.hankakao_home.setAlignment(Qt.AlignCenter)
        self.hankakao_home.setObjectName("hankakao_home")
        self.verticalLayout_5.addWidget(self.hankakao_home)
        self.btn_start = QPushButton(self.page_home)
        self.btn_start.setEnabled(True)
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(16)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout_5.addWidget(self.btn_start)
        self.label = QLabel(self.page_home)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.stackedWidget.addWidget(self.page_home)
        self.page_settings = QWidget()
        self.page_settings.setObjectName("page_settings")
        self.horizontalLayout_9 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.stackedWidget.addWidget(self.page_settings)
        self.verticalLayout_9.addWidget(self.stackedWidget)
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
        self.label_credits = QLabel(self.frame_label_bottom)
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(9)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_credits.setObjectName("label_credits")
        self.horizontalLayout_7.addWidget(self.label_credits)
        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(9)
        self.label_version.setFont(font)
        self.label_version.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_version.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label_version.setObjectName("label_version")
        self.horizontalLayout_7.addWidget(self.label_version)
        self.horizontalLayout_6.addWidget(self.frame_label_bottom)
        self.verticalLayout_4.addWidget(self.frame_grip)
        self.horizontalLayout_2.addWidget(self.frame_content_right)
        self.verticalLayout.addWidget(self.frame_center)
        self.verticalLayout_3.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HANKAKAO"))
        self.hankakao_top_info_1.setText(_translate("MainWindow", "HAN KA KAO"))
        self.home_top_info_2.setText(_translate("MainWindow", "| HOME"))
        self.hankakao_home.setText(_translate("MainWindow", "HAN / KA KAO"))
        self.btn_start.setText(_translate("MainWindow", "start"))
        self.label_credits.setText(_translate("MainWindow", "OOP FINAL PROJECT"))
        self.label_version.setText(
            _translate("MainWindow", "developed by ae, mind, pao")
        )
