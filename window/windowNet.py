# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowNet.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import csv
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from creeper.baiduNetdisk import BaiduNetdisk
from database.database import Database
from window import aboutDialog
from window.actionSpeakerThread import SpeakerThread
from window.tipDig import ActionWarnException


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1178, 798)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./source/icon/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_operate = QtWidgets.QWidget()
        self.tab_operate.setObjectName("tab_operate")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_operate)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_operate)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.verticalLayout_4.addWidget(self.tableWidget_2)
        self.verticalLayout_8.addWidget(self.groupBox_3)
        self.pushButton = QtWidgets.QPushButton(self.tab_operate)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab_operate)
        self.commandLinkButton.setMinimumSize(QtCore.QSize(0, 260))
        self.commandLinkButton.setMaximumSize(QtCore.QSize(700, 16777215))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout_8.addWidget(self.commandLinkButton)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./source/icon/animation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_operate, icon1, "")
        self.tab_position = QtWidgets.QWidget()
        self.tab_position.setObjectName("tab_position")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_position)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.tab_position)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.textEdit_review = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_review.setObjectName("textEdit_review")
        self.horizontalLayout.addWidget(self.textEdit_review)
        self.verticalLayout_2.addWidget(self.widget_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./source/icon/calender.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_position, icon2, "")
        self.tab_more = QtWidgets.QWidget()
        self.tab_more.setObjectName("tab_more")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_more)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mdiArea = QtWidgets.QMdiArea(self.tab_more)
        self.mdiArea.setStyleSheet("")
        brush = QtGui.QBrush(QtGui.QColor(194, 247, 255))
        brush.setStyle(QtCore.Qt.Dense4Pattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.TabbedView)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setObjectName("mdiArea")
        self.verticalLayout_3.addWidget(self.mdiArea)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./source/icon/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_more, icon3, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1178, 26))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_C = QtWidgets.QMenu(self.menubar)
        self.menu_C.setObjectName("menu_C")
        self.menu_S = QtWidgets.QMenu(self.menubar)
        self.menu_S.setObjectName("menu_S")
        self.menu_V = QtWidgets.QMenu(self.menubar)
        self.menu_V.setObjectName("menu_V")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.dockWidget_File = QtWidgets.QDockWidget(mainWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.dockWidget_File.setFont(font)
        self.dockWidget_File.setToolTip("")
        self.dockWidget_File.setFloating(False)
        self.dockWidget_File.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_File.setObjectName("dockWidget_File")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.treeView = QtWidgets.QTreeView(self.groupBox)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_5.addWidget(self.treeView)
        self.verticalLayout.addWidget(self.groupBox)
        self.dockWidget_File.setWidget(self.dockWidgetContents_2)
        mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_File)
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget_status = QtWidgets.QDockWidget(mainWindow)
        self.dockWidget_status.setMouseTracking(False)
        self.dockWidget_status.setTabletTracking(False)
        self.dockWidget_status.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dockWidget_status.setAutoFillBackground(False)
        self.dockWidget_status.setStyleSheet("")
        self.dockWidget_status.setFloating(False)
        self.dockWidget_status.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget_status.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_status.setObjectName("dockWidget_status")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.dockWidgetContents_4)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textEdit_status = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_status.setObjectName("textEdit_status")
        self.verticalLayout_7.addWidget(self.textEdit_status)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.dockWidget_status.setWidget(self.dockWidgetContents_4)
        mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_status)
        self.toolBar_2 = QtWidgets.QToolBar(mainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.menuItem_new = QtWidgets.QAction(mainWindow)
        self.menuItem_new.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./source/icon/baogao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_new.setIcon(icon4)
        self.menuItem_new.setObjectName("menuItem_new")
        self.menuItem_openFile = QtWidgets.QAction(mainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./source/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_openFile.setIcon(icon5)
        self.menuItem_openFile.setObjectName("menuItem_openFile")
        self.menuItem_saveFile = QtWidgets.QAction(mainWindow)
        self.menuItem_saveFile.setEnabled(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./source/icon/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_saveFile.setIcon(icon6)
        self.menuItem_saveFile.setObjectName("menuItem_saveFile")
        self.menuItem_quitSystem = QtWidgets.QAction(mainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./source/icon/decentralized-02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_quitSystem.setIcon(icon7)
        self.menuItem_quitSystem.setObjectName("menuItem_quitSystem")
        self.munuItem_markbook = QtWidgets.QAction(mainWindow)
        self.munuItem_markbook.setObjectName("munuItem_markbook")
        self.munuItem_controlNet = QtWidgets.QAction(mainWindow)
        self.munuItem_controlNet.setObjectName("munuItem_controlNet")
        self.munuItem_cacuPara = QtWidgets.QAction(mainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./source/icon/designer-tools.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_cacuPara.setIcon(icon8)
        self.munuItem_cacuPara.setObjectName("munuItem_cacuPara")
        self.munuItem_systemPara = QtWidgets.QAction(mainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./source/icon/set.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_systemPara.setIcon(icon9)
        self.munuItem_systemPara.setObjectName("munuItem_systemPara")
        self.munuItem_windowSet = QtWidgets.QAction(mainWindow)
        self.munuItem_windowSet.setIcon(icon2)
        self.munuItem_windowSet.setObjectName("munuItem_windowSet")
        self.munuItem_onlineHelp = QtWidgets.QAction(mainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./source/icon/lineOneline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_onlineHelp.setIcon(icon10)
        self.munuItem_onlineHelp.setObjectName("munuItem_onlineHelp")
        self.munuItem_localHelp = QtWidgets.QAction(mainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("./source/icon/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_localHelp.setIcon(icon11)
        self.munuItem_localHelp.setObjectName("munuItem_localHelp")
        self.munuItem_version = QtWidgets.QAction(mainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("./source/icon/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_version.setIcon(icon12)
        self.munuItem_version.setObjectName("munuItem_version")
        self.menuItem_backWelcome = QtWidgets.QAction(mainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("./source/icon/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_backWelcome.setIcon(icon13)
        self.menuItem_backWelcome.setObjectName("menuItem_backWelcome")
        self.munuItem_statusBar = QtWidgets.QAction(mainWindow)
        self.munuItem_statusBar.setCheckable(True)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("./source/icon/mes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_statusBar.setIcon(icon14)
        self.munuItem_statusBar.setObjectName("munuItem_statusBar")
        self.munuItem_fileStatusBar = QtWidgets.QAction(mainWindow)
        self.munuItem_fileStatusBar.setCheckable(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("./source/icon/tree.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_fileStatusBar.setIcon(icon15)
        self.munuItem_fileStatusBar.setObjectName("munuItem_fileStatusBar")
        self.munuItem_license = QtWidgets.QAction(mainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("./source/icon/zaogao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_license.setIcon(icon16)
        self.munuItem_license.setObjectName("munuItem_license")
        self.munuItem_coorSystemTran = QtWidgets.QAction(mainWindow)
        self.munuItem_coorSystemTran.setEnabled(False)
        self.munuItem_coorSystemTran.setObjectName("munuItem_coorSystemTran")
        self.menuItem_imagesDect = QtWidgets.QAction(mainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("./source/icon/document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_imagesDect.setIcon(icon17)
        self.menuItem_imagesDect.setObjectName("menuItem_imagesDect")
        self.munuItem_GussianTran = QtWidgets.QAction(mainWindow)
        self.munuItem_GussianTran.setEnabled(False)
        self.munuItem_GussianTran.setObjectName("munuItem_GussianTran")
        self.munuItem_contact = QtWidgets.QAction(mainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("./source/icon/conme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_contact.setIcon(icon18)
        self.munuItem_contact.setObjectName("munuItem_contact")
        self.menuItem_trainModel = QtWidgets.QAction(mainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("./source/icon/CPU_GPU.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_trainModel.setIcon(icon19)
        self.menuItem_trainModel.setObjectName("menuItem_trainModel")
        self.actiond = QtWidgets.QAction(mainWindow)
        self.actiond.setObjectName("actiond")
        self.menuItem_videoDect = QtWidgets.QAction(mainWindow)
        self.menuItem_videoDect.setIcon(icon1)
        self.menuItem_videoDect.setObjectName("menuItem_videoDect")
        self.actions_2 = QtWidgets.QAction(mainWindow)
        self.actions_2.setEnabled(False)
        self.actions_2.setObjectName("actions_2")
        self.menu_F.addAction(self.menuItem_new)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.menuItem_openFile)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.menuItem_saveFile)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.menuItem_quitSystem)
        self.menu_C.addAction(self.menuItem_imagesDect)
        self.menu_C.addSeparator()
        self.menu_C.addAction(self.menuItem_videoDect)
        self.menu_C.addSeparator()
        self.menu_C.addAction(self.menuItem_trainModel)
        self.menu_C.addSeparator()
        self.menu_C.addAction(self.munuItem_GussianTran)
        self.menu_C.addSeparator()
        self.menu_C.addAction(self.actions_2)
        self.menu_C.addSeparator()
        self.menu_C.addAction(self.munuItem_coorSystemTran)
        self.menu_C.addSeparator()
        self.menu_S.addAction(self.munuItem_windowSet)
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.menuItem_backWelcome)
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.munuItem_systemPara)
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.munuItem_statusBar)
        self.menu_S.addAction(self.munuItem_fileStatusBar)
        self.menu_V.addAction(self.munuItem_version)
        self.menu_V.addAction(self.munuItem_license)
        self.menu_V.addAction(self.munuItem_contact)
        self.menu_H.addAction(self.munuItem_onlineHelp)
        self.menu_H.addAction(self.munuItem_localHelp)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_C.menuAction())
        self.menubar.addAction(self.menu_S.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())
        self.menubar.addAction(self.menu_V.menuAction())
        self.toolBar.addAction(self.menuItem_new)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.menuItem_openFile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.menuItem_saveFile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.menuItem_backWelcome)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.munuItem_license)
        self.toolBar_2.addAction(self.munuItem_systemPara)
        self.toolBar_2.addAction(self.munuItem_statusBar)
        self.toolBar_2.addAction(self.munuItem_fileStatusBar)
        self.toolBar_2.addAction(self.munuItem_localHelp)
        self.toolBar_2.addAction(self.munuItem_onlineHelp)
        self.toolBar_2.addSeparator()

        self.tableWidget_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  # 允许右键产生子菜单
        self.tableWidget_2.customContextMenuRequested.connect(self.generateMenu)  # 右键菜单

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.openSourceCertificate()

        self.baiduNetdisk = BaiduNetdisk()
        self.baiduNetdisk.infoEmit.connect(self.showInfo)

        self.pushButton.clicked.connect(self.linkDetect)

        self.speakerThread = SpeakerThread()
        self.speakerThread.infoEmit.connect(self.showInfo)
        self.actionSpeaker(Database.welcomeSpeak)

        self.aboutDialog_ui = aboutDialog.Ui_Dialog()

        self.menuItem_new.triggered.connect(self.moreWindow)
        self.menuItem_saveFile.triggered.connect(self.actionSaveFile)
        self.menuItem_quitSystem.triggered.connect(self.quitSystemEvent)

        self.munuItem_onlineHelp.triggered.connect(self.onlineHelp)
        self.menuItem_openFile.triggered.connect(self.actionOpenFile)
        self.munuItem_version.triggered.connect(self.aboutDialog)
        self.munuItem_contact.triggered.connect(self.aboutDialog)

        self.munuItem_fileStatusBar.triggered.connect(self.actionMenuItem_fileStatusBar)
        self.munuItem_statusBar.triggered.connect(self.actionMenuItem_statusBar)
        self.dockWidget_File.visibilityChanged['bool'].connect(self.dockWight_fileStatusCloseEvent)
        self.dockWidget_status.visibilityChanged['bool'].connect(self.dockWight_statusCloseEvent)
        self.dockWidget_File.visibilityChanged['bool'].connect(self.dockWidget_File.update)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "网盘链接有效性检测软件 2.0.0"))
        self.groupBox_3.setTitle(_translate("mainWindow", "链接数据"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("mainWindow", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("mainWindow", "2"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "资源"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "链接"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "提取码"))
        self.pushButton.setText(_translate("mainWindow", "一键检测"))
        self.commandLinkButton.setText(_translate("mainWindow", "说明\n"
                                                                " 1. 开发者GanAHE,网站：www.ganahe.top\n"
                                                                " 2.合作者：星辰换日(微信公众号)\n"
                                                                " 3.后续软件开发与完善，请关注最新推送，预计更新如下功能：\n"
                                                                "  (1)有效链接自动填写提取码进入保存页面;  (2)自动保存到个人百度网盘;\n"
                                                                "  （3）自动搜索全网资源链接;  （4）其他功能，敬请期待！ \n"
                                                                "4.更多分享与软件开发等资源请关注合作微信公众号获取，\n"
                                                                "更多分享知识请关注开发者网站。"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_operate), _translate("mainWindow", "识别与监测"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("mainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("mainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "P1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "P2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_position), _translate("mainWindow", "监控"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_more), _translate("mainWindow", "更多操作"))
        self.menu_F.setTitle(_translate("mainWindow", "文件(&F)"))
        self.menu_C.setTitle(_translate("mainWindow", "功能(&C)"))
        self.menu_S.setTitle(_translate("mainWindow", "设置(&S)"))
        self.menu_V.setTitle(_translate("mainWindow", "版本(&V)"))
        self.menu_H.setTitle(_translate("mainWindow", "帮助(&H)"))
        self.dockWidget_File.setWindowTitle(_translate("mainWindow", "文件列表"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.dockWidget_status.setWindowTitle(_translate("mainWindow", "状态信息"))
        self.toolBar_2.setWindowTitle(_translate("mainWindow", "toolBar_2"))
        self.menuItem_new.setText(_translate("mainWindow", "新建(&N)"))
        self.menuItem_openFile.setText(_translate("mainWindow", "打开文件(&O)"))
        self.menuItem_saveFile.setText(_translate("mainWindow", "保存文件(&S)"))
        self.menuItem_quitSystem.setText(_translate("mainWindow", "退出系统(&Q)"))
        self.munuItem_markbook.setText(_translate("mainWindow", "训练模型(&M)"))
        self.munuItem_markbook.setIconText(_translate("mainWindow", "训练模型(&M)"))
        self.munuItem_controlNet.setText(_translate("mainWindow", "码率调整(&D)"))
        self.munuItem_cacuPara.setText(_translate("mainWindow", "计算参数(&P)"))
        self.munuItem_systemPara.setText(_translate("mainWindow", "系统参数(&S)"))
        self.munuItem_windowSet.setText(_translate("mainWindow", "界面设置(&W)"))
        self.munuItem_onlineHelp.setText(_translate("mainWindow", "在线帮助(&I)"))
        self.munuItem_localHelp.setText(_translate("mainWindow", "本地文档(&I)"))
        self.munuItem_version.setText(_translate("mainWindow", "版本信息(&V)"))
        self.menuItem_backWelcome.setText(_translate("mainWindow", "返回欢迎界面(&B)"))
        self.munuItem_statusBar.setText(_translate("mainWindow", "状态信息栏(&I) "))
        self.munuItem_fileStatusBar.setText(_translate("mainWindow", "文件列表栏(&F)"))
        self.munuItem_license.setText(_translate("mainWindow", "开源证书(&L)"))
        self.munuItem_coorSystemTran.setText(_translate("mainWindow", "更多功能(待开发)...(&H)"))
        self.menuItem_imagesDect.setText(_translate("mainWindow", "影像目标检测(&T)"))
        self.munuItem_GussianTran.setText(_translate("mainWindow", "违章侦测(&S)"))
        self.munuItem_contact.setText(_translate("mainWindow", "联系方式(&L)"))
        self.menuItem_trainModel.setText(_translate("mainWindow", "模型训练(&L)"))
        self.actiond.setText(_translate("mainWindow", "图像识别(&P)"))
        self.menuItem_videoDect.setText(_translate("mainWindow", "视频目标检测(&V)"))
        self.actions_2.setText(_translate("mainWindow", "在线/监控流视频实时监测(&T)"))

    def actionOpenFile(self):
        try:
            filePath, type = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "导入检测集文件", Database.fileDir,
                                                                   "csv(*.csv)")
            if filePath != "":
                # 显示打开的文件区域
                (dir, videoName) = os.path.split(filePath)
                self.showPan(dir)
                # 存入留待下次使用
                Database.fileDir = dir
                # 存入数据库
                data = self.readCSV(filePath)
                # 设置表格数据
                self.setTabOneTableWightData(data)
                Database.fileDataList = data
                self.showInfo("T", "已导入csv文件，路径为 " + filePath)
        except Exception as e:
            self.showInfo("E", "导入文件错误，信息：" + e.__str__())

    def moreWindow(self):
        # 跳转到指定标签页
        self.tabWidget.setCurrentIndex(2)
        # 子窗口增加一个
        # 实例化多文档界面对象
        self.sub = QtWidgets.QMdiArea()
        # 设置新建子窗口的标题
        self.sub.setWindowTitle("更多...")
        self.verticalLayout_more = QtWidgets.QVBoxLayout(self.sub)
        self.verticalLayout_more.setObjectName("verticalLayout_more")
        self.sub.setLayout(self.verticalLayout_more)
        # 将子窗口添加到Mdi区域
        self.mdiArea.addSubWindow(self.sub)
        # 子窗口显示
        self.sub.show()

    def actionSaveFile(self):
        try:
            # 从数据库获取数据
            resultDa = Database.resultLinkList
            if resultDa is None:
                self.showInfo("T", "无可导出数据")
            elif len(resultDa) <= 0:
                self.showInfo("T", "无可导出数据")
            else:
                filePath, k = QtWidgets.QFileDialog.getSaveFileName(self.centralwidget, "保存结果", Database.fileDir,
                                                                    "csv(*.csv)")
                if filePath != "":
                    self.writeCSVFile(resultDa, filePath)
                    self.showInfo("V", "导出文件完成")
            # self.showInfo("T", "当前所有功能暂不需要该功能支持！")
        except Exception as e:
            self.showInfo("E", "异常错误：" + e.__str__())

    def quitSystemEvent(self):
        self.showInfo("V", "即将关闭系统，未保存文件将会丢失,是否继续！")
        userReply = ActionWarnException(self.centralwidget).actionWarnException("R", "即将关闭系统，未保存文件将会丢失，是否继续？\n")
        if userReply:
            QtCore.QCoreApplication.quit()

    def aboutDialog(self):
        self.aboutAndContactDialog = QtWidgets.QDialog()
        self.aboutDialog_ui.setupUi(self.aboutAndContactDialog)
        # 设定无边框
        # self.aboutAndContactDialog.setWindowFlags(QtCore.Qt.Dialog|QtCore.Qt.FramelessWindowHint)
        self.aboutAndContactDialog.show()

    def onlineHelp(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(Database.onlineHelpLink))

    def showPan(self, dirPath):
        """
        文件列表树
        :param dirPath: 文件所在相对目录，不能包含文件名
        :return:None
        """
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(dirPath)
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(dirPath))

    def showInfo(self, type, strInfo):
        """
        集成信息显示中心
        :param type: 需要指向的显示类型
        :param strInfo: 需要显示的信息
        :return:
        """
        if type == "I":  # 状态信息栏
            self.textEdit_status.append(strInfo)
        elif type == "V":
            self.actionSpeaker(strInfo)
        elif type == "finish":
            # 启动显示
            self.setTabTwoTableWightData(Database.headList, True)
            self.setTabTwoTableWightData(Database.resultLinkList)
            self.showInfo("T", strInfo)
        else:  # 异常弹窗提醒
            ActionWarnException(self.centralwidget).actionWarnException(type, strInfo)

    def actionMenuItem_fileStatusBar(self):
        stat = self.munuItem_fileStatusBar.isChecked()
        if stat:  # 选中状态
            self.dockWidget_File.show()
        else:  # 取消选择状态
            self.dockWidget_File.setVisible(False)

    def actionMenuItem_statusBar(self):
        stat = self.munuItem_statusBar.isChecked()
        if stat:  # 选中状态
            self.dockWidget_status.show()
        else:  # 取消选择状态
            self.dockWidget_status.setVisible(False)

    def dockWight_fileStatusCloseEvent(self):
        self.munuItem_fileStatusBar.setChecked(False)

    def dockWight_statusCloseEvent(self):
        self.munuItem_statusBar.setChecked(False)

    def actionSpeaker(self, text):
        self.speakerThread.setText(text)
        self.speakerThread.wait(20)
        # 启动线程
        self.speakerThread.start()

    def readCSV(self, path):
        data = []
        with open(path, "r", encoding="utf8") as F:
            reader = csv.reader(F)
            count = 1
            for row in reader:
                if count == 1:
                    count = 2
                    Database.headList = row
                    self.showInfo("I", "文件信息" + str(row))
                    self.showInfo("V", "文件信息" + str(row))
                else:
                    data.append(row[:3])
        return data

    def writeCSVFile(self, listData, filePath, headList=None):
        """
        写入CSV数据
        :param listData: list文件
        :param filePath: 文件路径及文件名
        :param headList: csv的标题，作为可选参数
        :return: None
        """
        with open(filePath, 'w', newline="") as csvFile:
            csvFile.flush()
            csvWriter = csv.writer(csvFile)
            if headList is not None:
                csvWriter.writerow(headList)
            try:  # 无奈之举，只有一行list该怎么判断？即内部不嵌套
                for i in range(len(listData)):
                    csvWriter.writerow(listData[i])
            except:
                csvWriter.writerow(listData)

            os.fsync(csvFile)
            csvFile.close()

    def linkDetect(self):

        try:
            data = []
            self.showInfo("V", "开始检测，请等待")
            # 从表格获取数据信息
            for i in range(self.tableWidget_2.rowCount()):
                data.append([self.tableWidget_2.item(i, 0).text(), self.tableWidget_2.item(i, 1).text(),
                             self.tableWidget_2.item(i, 2).text()])
            self.baiduNetdisk.setLink(data)
            self.baiduNetdisk.start()
            self.showInfo("T", "开始检测，请等待...")

        except Exception as e:
            self.showInfo("E", "错误：" + e.__str__())

    def setTabOneTableWightData(self, dataList):
        tableLen = self.tableWidget_2.rowCount()
        if tableLen < len(dataList):
            # 表格加长
            self.tableWidget_2.setRowCount(len(dataList))
        tableLen = len(dataList)
        for i in range(tableLen):
            for col in range(3):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setItem(i, col, item)
                self.tableWidget_2.item(i, col).setText(str(dataList[i][col]))

    def setTabTwoTableWightData(self, dataList, head=False):
        if head:
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setRowCount(0)
            for i in range(3):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(i, item)
                item.setText(dataList[i])
        else:
            # 跳转
            self.tabWidget.setCurrentIndex(1)
            tableLen = self.tableWidget.rowCount()
            if tableLen < len(dataList):
                # 表格加长
                self.tableWidget.setRowCount(len(dataList))
            tableLen = len(dataList)
            for i in range(tableLen):
                for col in range(3):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(i, col, item)
                    self.tableWidget.item(i, col).setText(str(dataList[i][col]))

    def generateMenu(self, pos):
        menu = QtWidgets.QMenu()
        item1 = menu.addAction(u"添加一行")
        item2 = menu.addAction(u"删除尾行")
        item3 = menu.addAction(u"清空表格数据")
        action = menu.exec_(self.tableWidget_2.mapToGlobal(pos))
        try:
            if action == item1:
                self._addGround()
            elif action == item2:
                self._deleteGround()
            elif action == item3:
                self._clearTable()
        except Exception as e:
            print("Error", e.args.__str__())

    def _addGround(self):
        """
        添加单组记录区域
        :return: None
        """
        # 当前表格长度
        index = self.tableWidget_2.rowCount()
        self.tableWidget_2.setRowCount(index + 1)
        for col in range(3):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(index + 1, col, item)

    def _deleteGround(self):
        """
        删除最后一组记录值
        :return:
        """
        if self.tableWidget_2.rowCount() != 1:  # 仅第一行保留
            self.tableWidget_2.removeRow(self.tableWidget_2.rowCount() - 1)

    def _clearTable(self):
        """
        清空表格内容
        :return:
        """
        for i in range(self.tableWidget_2.rowCount()):
            for k in range(3):
                self.tableWidget_2.item(i, k).setText("")

    def openSourceCertificate(self):
        """
        开源证书
        :return: None
        """
        # 显示到文本区域
        self.textEdit_review.setText("                      ===========开源证书===========")
        with open(Database.LicensePath, "r",encoding='UTF-8') as F:
            for line in F:
                self.textEdit_review.append(line)
