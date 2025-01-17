# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fota.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FOTA(object):
    def setupUi(self, FOTA):
        FOTA.setObjectName("FOTA")
        FOTA.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FOTA.sizePolicy().hasHeightForWidth())
        FOTA.setSizePolicy(sizePolicy)
        FOTA.setMinimumSize(QtCore.QSize(800, 600))
        FOTA.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FOTA.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FOTA)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(250, 0, 500, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_8 = QtWidgets.QLabel(self.page_4)
        self.label_8.setGeometry(QtCore.QRect(90, 0, 329, 133))
        self.label_8.setStyleSheet("color:rgb(75, 151, 226);\n"
"border:rounded;\n"
"font: bold 30pt \"Times New Roman\";\n"
"padding:10px;\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.layoutWidget = QtWidgets.QWidget(self.page_4)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 140, 371, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.date_label = QtWidgets.QLabel(self.layoutWidget)
        self.date_label.setStyleSheet("color:rgb(75, 151, 226);\n"
"background-color:white;\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";\n"
"padding:10px;\n"
"")
        self.date_label.setObjectName("date_label")
        self.verticalLayout_12.addWidget(self.date_label)
        self.time_label = QtWidgets.QLabel(self.layoutWidget)
        self.time_label.setStyleSheet("color:rgb(75, 151, 226);\n"
"background-color:white;\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";\n"
"padding:10px;\n"
"")
        self.time_label.setObjectName("time_label")
        self.verticalLayout_12.addWidget(self.time_label)
        self.speed_label = QtWidgets.QLabel(self.layoutWidget)
        self.speed_label.setStyleSheet("color:rgb(0, 170, 0);\n"
"background-color:white;\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";\n"
"padding:10px;\n"
"")
        self.speed_label.setObjectName("speed_label")
        self.verticalLayout_12.addWidget(self.speed_label)
        self.layoutWidget1 = QtWidgets.QWidget(self.page_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(-30, 140, 121, 411))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.date_label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.date_label_2.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 50%;\n"
"color:rgb(75, 151, 226);\n"
"background-color:white;\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";\n"
"padding:10px;\n"
"")
        self.date_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label_2.setObjectName("date_label_2")
        self.verticalLayout_14.addWidget(self.date_label_2)
        self.date_label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.date_label_3.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 50%;\n"
"color:rgb(75, 151, 226);\n"
"background-color:white;\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";\n"
"padding:10px;\n"
"")
        self.date_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label_3.setObjectName("date_label_3")
        self.verticalLayout_14.addWidget(self.date_label_3)
        self.date_label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.date_label_5.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 50%;\n"
"color:rgb(75, 151, 226);\n"
"background-color:white;\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";\n"
"padding:10px;\n"
"")
        self.date_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label_5.setObjectName("date_label_5")
        self.verticalLayout_14.addWidget(self.date_label_5)
        self.stackedWidget.addWidget(self.page_4)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.check_update_btn = QtWidgets.QPushButton(self.page)
        self.check_update_btn.setGeometry(QtCore.QRect(60, 450, 381, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_update_btn.sizePolicy().hasHeightForWidth())
        self.check_update_btn.setSizePolicy(sizePolicy)
        self.check_update_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.check_update_btn.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"color:rgb(75, 151, 226);\n"
"background-color:white;\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";\n"
"")
        self.check_update_btn.setObjectName("check_update_btn")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 479, 130))
        self.label_9.setStyleSheet("color:rgb(75, 151, 226);\n"
"border:rounded;\n"
"font: bold 30pt \"Times New Roman\";\n"
"padding:10px;\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.layoutWidget2 = QtWidgets.QWidget(self.page)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 290, 491, 92))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.progress_label = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_label.sizePolicy().hasHeightForWidth())
        self.progress_label.setSizePolicy(sizePolicy)
        self.progress_label.setMinimumSize(QtCore.QSize(0, 34))
        self.progress_label.setStyleSheet("color:rgb(75, 151, 226);\n"
"border:rounded;\n"
"font: bold 10pt \"Times New Roman\";\n"
"padding:5px;\\n")
        self.progress_label.setObjectName("progress_label")
        self.verticalLayout_10.addWidget(self.progress_label)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.layoutWidget3 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 20, 431, 481))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_10.setStyleSheet("color:rgb(75, 151, 226);\n"
"border:rounded;\n"
"font: bold 30pt \"Times New Roman\";\n"
"padding:10px;\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_13.addWidget(self.label_10)
        self.notification_list = QtWidgets.QListWidget(self.layoutWidget3)
        self.notification_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.notification_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.notification_list.setProperty("isWrapping", True)
        self.notification_list.setWordWrap(True)
        self.notification_list.setItemAlignment(QtCore.Qt.AlignCenter)
        self.notification_list.setObjectName("notification_list")
        self.verticalLayout_13.addWidget(self.notification_list)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(0, 20, 479, 130))
        self.label_11.setStyleSheet("color:rgb(75, 151, 226);\n"
"border:rounded;\n"
"font: bold 30pt \"Times New Roman\";\n"
"padding:10px;\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.layoutWidget4 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 180, 481, 201))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.version_label = QtWidgets.QLabel(self.layoutWidget4)
        self.version_label.setStyleSheet("color:rgb(75, 151, 226);\n"
"background-color:white;\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";\n"
"padding:10px;\n"
"")
        self.version_label.setObjectName("version_label")
        self.verticalLayout_11.addWidget(self.version_label)
        self.description_label = QtWidgets.QLabel(self.layoutWidget4)
        self.description_label.setStyleSheet("color:rgb(75, 151, 226);\n"
"background-color:white;\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";\n"
"padding:10px;\n"
"")
        self.description_label.setObjectName("description_label")
        self.verticalLayout_11.addWidget(self.description_label)
        self.stackedWidget.addWidget(self.page_3)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(0, 0, 221, 571))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(1, 1, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.dashboard_btn = QtWidgets.QPushButton(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboard_btn.sizePolicy().hasHeightForWidth())
        self.dashboard_btn.setSizePolicy(sizePolicy)
        self.dashboard_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dashboard_btn.setStyleSheet("color:white;\n"
"background-color:rgb(75, 151, 226);\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";")
        self.dashboard_btn.setObjectName("dashboard_btn")
        self.verticalLayout_8.addWidget(self.dashboard_btn)
        self.update_btn = QtWidgets.QPushButton(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_btn.sizePolicy().hasHeightForWidth())
        self.update_btn.setSizePolicy(sizePolicy)
        self.update_btn.setStyleSheet("color:white;\n"
"background-color:rgb(75, 151, 226);\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";")
        self.update_btn.setObjectName("update_btn")
        self.verticalLayout_8.addWidget(self.update_btn)
        self.notification_btn = QtWidgets.QPushButton(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notification_btn.sizePolicy().hasHeightForWidth())
        self.notification_btn.setSizePolicy(sizePolicy)
        self.notification_btn.setStyleSheet("color:white;\n"
"background-color:rgb(75, 151, 226);\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";")
        self.notification_btn.setObjectName("notification_btn")
        self.verticalLayout_8.addWidget(self.notification_btn)
        self.about_btn = QtWidgets.QPushButton(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_btn.sizePolicy().hasHeightForWidth())
        self.about_btn.setSizePolicy(sizePolicy)
        self.about_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.about_btn.setStyleSheet("color:white;\n"
"background-color:rgb(75, 151, 226);\n"
"border:rounded;\n"
"font: bold 15pt \"Times New Roman\";")
        self.about_btn.setObjectName("about_btn")
        self.verticalLayout_8.addWidget(self.about_btn)
        FOTA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FOTA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        FOTA.setMenuBar(self.menubar)

        self.retranslateUi(FOTA)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(FOTA)

    def retranslateUi(self, FOTA):
        _translate = QtCore.QCoreApplication.translate
        FOTA.setWindowTitle(_translate("FOTA", "MainWindow"))
        self.label_8.setText(_translate("FOTA", "DashBoard"))
        self.date_label.setText(_translate("FOTA", "Date"))
        self.time_label.setText(_translate("FOTA", "Time"))
        self.speed_label.setText(_translate("FOTA", "speed"))
        self.date_label_2.setText(_translate("FOTA", "Date"))
        self.date_label_3.setText(_translate("FOTA", "Time"))
        self.date_label_5.setText(_translate("FOTA", "Speed"))
        self.check_update_btn.setText(_translate("FOTA", "Check for update"))
        self.label_9.setText(_translate("FOTA", "Update"))
        self.progress_label.setText(_translate("FOTA", "Donwnloading Rate"))
        self.label_10.setText(_translate("FOTA", "Notification"))
        self.label_11.setText(_translate("FOTA", "About"))
        self.version_label.setText(_translate("FOTA", "Current Version"))
        self.description_label.setText(_translate("FOTA", "Description"))
        self.dashboard_btn.setText(_translate("FOTA", "Dashboard"))
        self.update_btn.setText(_translate("FOTA", "Update"))
        self.notification_btn.setText(_translate("FOTA", "Notification"))
        self.about_btn.setText(_translate("FOTA", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FOTA = QtWidgets.QMainWindow()
    ui = Ui_FOTA()
    ui.setupUi(FOTA)
    FOTA.show()
    sys.exit(app.exec_())
