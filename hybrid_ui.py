# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\images\hybrid-gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(816, 900))
        MainWindow.setMaximumSize(QtCore.QSize(816, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(210, 10, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.vehicle_type = QtWidgets.QLineEdit(self.centralwidget)
        self.vehicle_type.setGeometry(QtCore.QRect(490, 10, 60, 22))
        self.vehicle_type.setObjectName("vehicle_type")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(620, 320, 111, 41))
        self.start.setObjectName("start")
        self.enviado = QtWidgets.QLabel(self.centralwidget)
        self.enviado.setGeometry(QtCore.QRect(590, 420, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.enviado.setFont(font)
        self.enviado.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enviado.setWordWrap(True)
        self.enviado.setObjectName("enviado")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(570, 20, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(570, 50, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 471, 331))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/1/car_follow.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 375, 471, 301))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/1/lane_change.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 680, 471, 201))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/1/lateral_behave.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.LookAheadDistMin = QtWidgets.QLineEdit(self.centralwidget)
        self.LookAheadDistMin.setGeometry(QtCore.QRect(490, 90, 60, 23))
        self.LookAheadDistMin.setObjectName("LookAheadDistMin")
        self.LookAheadDistMax = QtWidgets.QLineEdit(self.centralwidget)
        self.LookAheadDistMax.setGeometry(QtCore.QRect(490, 110, 60, 23))
        self.LookAheadDistMax.setObjectName("LookAheadDistMax")
        self.LookBackDistMin = QtWidgets.QLineEdit(self.centralwidget)
        self.LookBackDistMin.setGeometry(QtCore.QRect(490, 150, 60, 23))
        self.LookBackDistMin.setObjectName("LookBackDistMin")
        self.LookBackDistMax = QtWidgets.QLineEdit(self.centralwidget)
        self.LookBackDistMax.setGeometry(QtCore.QRect(490, 170, 60, 23))
        self.LookBackDistMax.setObjectName("LookBackDistMax")
        self.W74ax = QtWidgets.QLineEdit(self.centralwidget)
        self.W74ax.setGeometry(QtCore.QRect(490, 250, 60, 23))
        self.W74ax.setObjectName("W74ax")
        self.W74bxAdd = QtWidgets.QLineEdit(self.centralwidget)
        self.W74bxAdd.setGeometry(QtCore.QRect(490, 290, 60, 23))
        self.W74bxAdd.setObjectName("W74bxAdd")
        self.W74bxMult = QtWidgets.QLineEdit(self.centralwidget)
        self.W74bxMult.setGeometry(QtCore.QRect(490, 330, 60, 23))
        self.W74bxMult.setObjectName("W74bxMult")
        self.MaxDecelOwn = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxDecelOwn.setGeometry(QtCore.QRect(490, 400, 60, 23))
        self.MaxDecelOwn.setObjectName("MaxDecelOwn")
        self.MaxDecelTrail = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxDecelTrail.setGeometry(QtCore.QRect(490, 420, 60, 23))
        self.MaxDecelTrail.setObjectName("MaxDecelTrail")
        self.DecelRedDistOwn = QtWidgets.QLineEdit(self.centralwidget)
        self.DecelRedDistOwn.setGeometry(QtCore.QRect(490, 440, 60, 23))
        self.DecelRedDistOwn.setObjectName("DecelRedDistOwn")
        self.DecelRedDistTrail = QtWidgets.QLineEdit(self.centralwidget)
        self.DecelRedDistTrail.setGeometry(QtCore.QRect(490, 460, 60, 23))
        self.DecelRedDistTrail.setObjectName("DecelRedDistTrail")
        self.AccDecelOwn = QtWidgets.QLineEdit(self.centralwidget)
        self.AccDecelOwn.setGeometry(QtCore.QRect(490, 480, 60, 23))
        self.AccDecelOwn.setObjectName("AccDecelOwn")
        self.AccDecelTrail = QtWidgets.QLineEdit(self.centralwidget)
        self.AccDecelTrail.setGeometry(QtCore.QRect(490, 500, 60, 23))
        self.AccDecelTrail.setObjectName("AccDecelTrail")
        self.carpet = QtWidgets.QPushButton(self.centralwidget)
        self.carpet.setGeometry(QtCore.QRect(640, 490, 93, 41))
        self.carpet.setObjectName("carpet")
        self.report = QtWidgets.QPushButton(self.centralwidget)
        self.report.setGeometry(QtCore.QRect(690, 580, 93, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.report.setFont(font)
        self.report.setAutoRepeat(False)
        self.report.setAutoExclusive(False)
        self.report.setAutoDefault(False)
        self.report.setObjectName("report")
        self.activar = QtWidgets.QPushButton(self.centralwidget)
        self.activar.setGeometry(QtCore.QRect(590, 580, 93, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.activar.setFont(font)
        self.activar.setAutoRepeat(False)
        self.activar.setAutoExclusive(False)
        self.activar.setAutoDefault(False)
        self.activar.setObjectName("activar")
        self.DiffusTm = QtWidgets.QLineEdit(self.centralwidget)
        self.DiffusTm.setGeometry(QtCore.QRect(490, 520, 60, 23))
        self.DiffusTm.setObjectName("DiffusTm")
        self.SafDistFactLnChg = QtWidgets.QLineEdit(self.centralwidget)
        self.SafDistFactLnChg.setGeometry(QtCore.QRect(490, 570, 60, 23))
        self.SafDistFactLnChg.setObjectName("SafDistFactLnChg")
        self.CoopDecel = QtWidgets.QLineEdit(self.centralwidget)
        self.CoopDecel.setGeometry(QtCore.QRect(490, 590, 60, 23))
        self.CoopDecel.setObjectName("CoopDecel")
        self.MinCollTmGain = QtWidgets.QLineEdit(self.centralwidget)
        self.MinCollTmGain.setGeometry(QtCore.QRect(490, 770, 60, 23))
        self.MinCollTmGain.setObjectName("MinCollTmGain")
        self.MinSpeedForLat = QtWidgets.QLineEdit(self.centralwidget)
        self.MinSpeedForLat.setGeometry(QtCore.QRect(490, 790, 60, 23))
        self.MinSpeedForLat.setObjectName("MinSpeedForLat")
        self.LatDistStandDef = QtWidgets.QLineEdit(self.centralwidget)
        self.LatDistStandDef.setGeometry(QtCore.QRect(490, 830, 60, 23))
        self.LatDistStandDef.setObjectName("LatDistStandDef")
        self.LatDistDrivDef = QtWidgets.QLineEdit(self.centralwidget)
        self.LatDistDrivDef.setGeometry(QtCore.QRect(490, 850, 60, 23))
        self.LatDistDrivDef.setObjectName("LatDistDrivDef")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(630, 640, 171, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/1/logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(630, 680, 171, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(650, 700, 131, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.liviano = QtWidgets.QPushButton(self.centralwidget)
        self.liviano.setGeometry(QtCore.QRect(580, 130, 61, 28))
        self.liviano.setObjectName("liviano")
        self.menor = QtWidgets.QPushButton(self.centralwidget)
        self.menor.setGeometry(QtCore.QRect(580, 160, 61, 28))
        self.menor.setObjectName("menor")
        self.publico = QtWidgets.QPushButton(self.centralwidget)
        self.publico.setGeometry(QtCore.QRect(580, 190, 61, 28))
        self.publico.setObjectName("publico")
        self.carga = QtWidgets.QPushButton(self.centralwidget)
        self.carga.setGeometry(QtCore.QRect(580, 220, 61, 28))
        self.carga.setObjectName("carga")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(560, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.fijar = QtWidgets.QPushButton(self.centralwidget)
        self.fijar.setGeometry(QtCore.QRect(490, 40, 61, 41))
        self.fijar.setObjectName("fijar")
        self.exportar = QtWidgets.QPushButton(self.centralwidget)
        self.exportar.setGeometry(QtCore.QRect(620, 370, 111, 41))
        self.exportar.setObjectName("exportar")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(600, 450, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(640, 540, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(570, 280, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.early = QtWidgets.QCheckBox(self.centralwidget)
        self.early.setGeometry(QtCore.QRect(680, 50, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.early.setFont(font)
        self.early.setObjectName("early")
        self.morning = QtWidgets.QCheckBox(self.centralwidget)
        self.morning.setGeometry(QtCore.QRect(680, 80, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.morning.setFont(font)
        self.morning.setObjectName("morning")
        self.evening = QtWidgets.QCheckBox(self.centralwidget)
        self.evening.setGeometry(QtCore.QRect(680, 110, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.evening.setFont(font)
        self.evening.setObjectName("evening")
        self.night = QtWidgets.QCheckBox(self.centralwidget)
        self.night.setGeometry(QtCore.QRect(680, 140, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.night.setFont(font)
        self.night.setObjectName("night")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(690, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.DesLatPos = QtWidgets.QComboBox(self.centralwidget)
        self.DesLatPos.setGeometry(QtCore.QRect(490, 680, 91, 22))
        self.DesLatPos.setObjectName("DesLatPos")
        self.DesLatPos.addItem("")
        self.DesLatPos.addItem("")
        self.DesLatPos.addItem("")
        self.DesLatPos.addItem("")
        self.ObsrvAdjLn = QtWidgets.QCheckBox(self.centralwidget)
        self.ObsrvAdjLn.setGeometry(QtCore.QRect(490, 710, 171, 20))
        self.ObsrvAdjLn.setObjectName("ObsrvAdjLn")
        self.DiamQueu = QtWidgets.QCheckBox(self.centralwidget)
        self.DiamQueu.setGeometry(QtCore.QRect(490, 730, 151, 20))
        self.DiamQueu.setObjectName("DiamQueu")
        self.ConsNextTurn = QtWidgets.QCheckBox(self.centralwidget)
        self.ConsNextTurn.setGeometry(QtCore.QRect(490, 750, 151, 20))
        self.ConsNextTurn.setObjectName("ConsNextTurn")
        self.OvtLDef = QtWidgets.QCheckBox(self.centralwidget)
        self.OvtLDef.setGeometry(QtCore.QRect(560, 830, 151, 20))
        self.OvtLDef.setObjectName("OvtLDef")
        self.OvtRDef = QtWidgets.QCheckBox(self.centralwidget)
        self.OvtRDef.setGeometry(QtCore.QRect(560, 850, 151, 20))
        self.OvtRDef.setObjectName("OvtRDef")
        self.get_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.get_pushButton.setGeometry(QtCore.QRect(580, 250, 61, 28))
        self.get_pushButton.setObjectName("get_pushButton")
        self.ZipperMinSpeed = QtWidgets.QLineEdit(self.centralwidget)
        self.ZipperMinSpeed.setGeometry(QtCore.QRect(730, 780, 60, 23))
        self.ZipperMinSpeed.setObjectName("ZipperMinSpeed")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(600, 780, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_13.setText(_translate("MainWindow", "Nro. Comportamiento Vehicular:"))
        self.start.setText(_translate("MainWindow", "SEND PARAMS."))
        self.enviado.setText(_translate("MainWindow", "ESTADO:"))
        self.checkBox.setText(_translate("MainWindow", "Vissim 10"))
        self.checkBox_2.setText(_translate("MainWindow", "Vissim 24"))
        self.carpet.setText(_translate("MainWindow", "VISSIM"))
        self.report.setText(_translate("MainWindow", "MODELO"))
        self.activar.setText(_translate("MainWindow", "CAMPO"))
        self.label_6.setText(_translate("MainWindow", "Credits: Nakamura & Mikipe"))
        self.label_7.setText(_translate("MainWindow", "Versión: v2.3"))
        self.liviano.setText(_translate("MainWindow", "Liviano"))
        self.menor.setText(_translate("MainWindow", "Menor"))
        self.publico.setText(_translate("MainWindow", "Público"))
        self.carga.setText(_translate("MainWindow", "Carga"))
        self.label_8.setText(_translate("MainWindow", "Parámetros Default"))
        self.fijar.setText(_translate("MainWindow", "FIJAR"))
        self.exportar.setText(_translate("MainWindow", "EXP. PARAMS."))
        self.label_9.setText(_translate("MainWindow", "VALIDACION"))
        self.label_10.setText(_translate("MainWindow", "ESCRITURA"))
        self.label_11.setText(_translate("MainWindow", "CAMBIO DE PARÁMETROS"))
        self.early.setText(_translate("MainWindow", "MADRUGADA"))
        self.morning.setText(_translate("MainWindow", "MAÑANA"))
        self.evening.setText(_translate("MainWindow", "TARDE"))
        self.night.setText(_translate("MainWindow", "NOCHE"))
        self.label_12.setText(_translate("MainWindow", "TURNO"))
        self.DesLatPos.setItemText(0, _translate("MainWindow", "MIDDLE"))
        self.DesLatPos.setItemText(1, _translate("MainWindow", "ANY"))
        self.DesLatPos.setItemText(2, _translate("MainWindow", "RIGHT"))
        self.DesLatPos.setItemText(3, _translate("MainWindow", "LEFT"))
        self.ObsrvAdjLn.setText(_translate("MainWindow", "Observe adjacent lane(s)"))
        self.DiamQueu.setText(_translate("MainWindow", "Diamond queuing"))
        self.ConsNextTurn.setText(_translate("MainWindow", "Consider next turn"))
        self.OvtLDef.setText(_translate("MainWindow", "Overtake left (default)"))
        self.OvtRDef.setText(_translate("MainWindow", "Overtake right (default)"))
        self.get_pushButton.setText(_translate("MainWindow", "GET"))
        self.checkBox_3.setText(_translate("MainWindow", "Zipper Min Speed"))