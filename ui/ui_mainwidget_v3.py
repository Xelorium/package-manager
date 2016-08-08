# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwidget_v3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(829, 559)
        MainWidget.setMinimumSize(QtCore.QSize(700, 500))
        self.gridLayout = QtWidgets.QGridLayout(MainWidget)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stateTab = QtWidgets.QTabWidget(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stateTab.sizePolicy().hasHeightForWidth())
        self.stateTab.setSizePolicy(sizePolicy)
        self.stateTab.setMaximumSize(QtCore.QSize(16777215, 26))
        self.stateTab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.stateTab.setDocumentMode(True)
        self.stateTab.setObjectName("stateTab")
        self.horizontalLayout.addWidget(self.stateTab)
        self.menuButton = QtWidgets.QToolButton(MainWidget)
        self.menuButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.menuButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.menuButton.setAutoRaise(True)
        self.menuButton.setObjectName("menuButton")
        self.horizontalLayout.addWidget(self.menuButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.searchActions = QtWidgets.QHBoxLayout()
        self.searchActions.setSpacing(0)
        self.searchActions.setObjectName("searchActions")
        self.searchLine = QtWidgets.QLineEdit(MainWidget)
        self.searchLine.setClearButtonEnabled(True)
        self.searchLine.setObjectName("searchLine")
        self.searchActions.addWidget(self.searchLine)
        self.searchButton = QtWidgets.QToolButton(MainWidget)
        self.searchButton.setText("")
        self.searchButton.setObjectName("searchButton")
        self.searchActions.addWidget(self.searchButton)
        self.typeCombo = QtWidgets.QComboBox(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeCombo.sizePolicy().hasHeightForWidth())
        self.typeCombo.setSizePolicy(sizePolicy)
        self.typeCombo.setMaximumSize(QtCore.QSize(260, 16777215))
        self.typeCombo.setObjectName("typeCombo")
        self.searchActions.addWidget(self.typeCombo)
        self.gridLayout.addLayout(self.searchActions, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.content = QtWidgets.QWidget(MainWidget)
        self.content.setObjectName("content")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupList = GroupList(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupList.sizePolicy().hasHeightForWidth())
        self.groupList.setSizePolicy(sizePolicy)
        self.groupList.setMaximumSize(QtCore.QSize(230, 16777215))
        self.groupList.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.groupList.setObjectName("groupList")
        self.horizontalLayout_3.addWidget(self.groupList)
        self.packageList = PackageView(self.content)
        self.packageList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.packageList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.packageList.setProperty("showDropIndicator", False)
        self.packageList.setDragDropOverwriteMode(False)
        self.packageList.setAlternatingRowColors(True)
        self.packageList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.packageList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.packageList.setShowGrid(False)
        self.packageList.setWordWrap(True)
        self.packageList.setCornerButtonEnabled(False)
        self.packageList.setObjectName("packageList")
        self.packageList.horizontalHeader().setVisible(False)
        self.packageList.horizontalHeader().setStretchLastSection(True)
        self.packageList.verticalHeader().setVisible(False)
        self.packageList.verticalHeader().setDefaultSectionSize(52)
        self.packageList.verticalHeader().setMinimumSectionSize(52)
        self.horizontalLayout_3.addWidget(self.packageList)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_5.addWidget(self.content)
        self.contentHistory = QtWidgets.QWidget(MainWidget)
        self.contentHistory.setObjectName("contentHistory")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.contentHistory)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.contentHistory)
        self.label.setText("History KCM will be here.")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.horizontalLayout_5.addWidget(self.contentHistory)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.actions = QtWidgets.QWidget(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actions.sizePolicy().hasHeightForWidth())
        self.actions.setSizePolicy(sizePolicy)
        self.actions.setMaximumSize(QtCore.QSize(16777215, 25))
        self.actions.setObjectName("actions")
        self.mainLayout = QtWidgets.QHBoxLayout(self.actions)
        self.mainLayout.setContentsMargins(0, 0, 2, 0)
        self.mainLayout.setObjectName("mainLayout")
        self.showBasketButton = QtWidgets.QPushButton(self.actions)
        self.showBasketButton.setMinimumSize(QtCore.QSize(22, 22))
        self.showBasketButton.setMaximumSize(QtCore.QSize(22, 22))
        self.showBasketButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/data/slide_up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showBasketButton.setIcon(icon)
        self.showBasketButton.setShortcut("F7")
        self.showBasketButton.setFlat(True)
        self.showBasketButton.setObjectName("showBasketButton")
        self.mainLayout.addWidget(self.showBasketButton)
        self.statusLabel = QtWidgets.QLabel(self.actions)
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.mainLayout.addWidget(self.statusLabel)
        self.checkUpdatesButton = QtWidgets.QPushButton(self.actions)
        self.checkUpdatesButton.setObjectName("checkUpdatesButton")
        self.mainLayout.addWidget(self.checkUpdatesButton)
        self.actionButton = QtWidgets.QPushButton(self.actions)
        self.actionButton.setObjectName("actionButton")
        self.mainLayout.addWidget(self.actionButton)
        self.mainLayout.setStretch(1, 3)
        self.gridLayout.addWidget(self.actions, 3, 0, 1, 1)

        self.retranslateUi(MainWidget)
        self.stateTab.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)
        MainWidget.setTabOrder(self.typeCombo, self.groupList)
        MainWidget.setTabOrder(self.groupList, self.packageList)
        MainWidget.setTabOrder(self.packageList, self.menuButton)
        MainWidget.setTabOrder(self.menuButton, self.stateTab)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Form"))
        self.menuButton.setText(_translate("MainWidget", "Settings"))
        self.searchLine.setPlaceholderText(_translate("MainWidget", "Type to search..."))
        self.typeCombo.setWhatsThis(_translate("MainWidget", "Update Types"))
        self.groupList.setWhatsThis(_translate("MainWidget", "Category Panel"))
        self.packageList.setWhatsThis(_translate("MainWidget", "Package List"))
        self.showBasketButton.setToolTip(_translate("MainWidget", "Show Basket"))
        self.checkUpdatesButton.setText(_translate("MainWidget", "Check for Updates"))
        self.actionButton.setText(_translate("MainWidget", "Install Package(s)"))

from grouplist import GroupList
from packageview import PackageView
import data_rc
