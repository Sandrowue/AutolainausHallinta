# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(563, 569)
        self.tietokantaLineEdit = QLineEdit(Dialog)
        self.tietokantaLineEdit.setObjectName(u"tietokantaLineEdit")
        self.tietokantaLineEdit.setGeometry(QRect(290, 160, 150, 25))
        font = QFont()
        font.setPointSize(12)
        self.tietokantaLineEdit.setFont(font)
        self.vanhaSalasanaLineEdit = QLineEdit(Dialog)
        self.vanhaSalasanaLineEdit.setObjectName(u"vanhaSalasanaLineEdit")
        self.vanhaSalasanaLineEdit.setGeometry(QRect(290, 330, 150, 25))
        self.vanhaSalasanaLineEdit.setFont(font)
        self.vanhaSalasanaLineEdit.setEchoMode(QLineEdit.Normal)
        self.porttiLabel = QLabel(Dialog)
        self.porttiLabel.setObjectName(u"porttiLabel")
        self.porttiLabel.setGeometry(QRect(130, 110, 100, 20))
        font1 = QFont()
        font1.setPointSize(14)
        self.porttiLabel.setFont(font1)
        self.tietokantaLabel = QLabel(Dialog)
        self.tietokantaLabel.setObjectName(u"tietokantaLabel")
        self.tietokantaLabel.setGeometry(QRect(130, 160, 100, 20))
        self.tietokantaLabel.setFont(font1)
        self.porttiLineEdit = QLineEdit(Dialog)
        self.porttiLineEdit.setObjectName(u"porttiLineEdit")
        self.porttiLineEdit.setGeometry(QRect(290, 110, 150, 25))
        self.porttiLineEdit.setFont(font)
        self.kayttajatunnusLabel = QLabel(Dialog)
        self.kayttajatunnusLabel.setObjectName(u"kayttajatunnusLabel")
        self.kayttajatunnusLabel.setGeometry(QRect(130, 210, 140, 20))
        self.kayttajatunnusLabel.setFont(font1)
        self.palvelinLineEdit = QLineEdit(Dialog)
        self.palvelinLineEdit.setObjectName(u"palvelinLineEdit")
        self.palvelinLineEdit.setGeometry(QRect(290, 60, 150, 25))
        self.palvelinLineEdit.setFont(font)
        self.tallennaPushButton = QPushButton(Dialog)
        self.tallennaPushButton.setObjectName(u"tallennaPushButton")
        self.tallennaPushButton.setGeometry(QRect(290, 260, 90, 25))
        self.tallennaPushButton.setFont(font1)
        self.KayttajatunnusLineEdit = QLineEdit(Dialog)
        self.KayttajatunnusLineEdit.setObjectName(u"KayttajatunnusLineEdit")
        self.KayttajatunnusLineEdit.setGeometry(QRect(290, 210, 150, 25))
        self.KayttajatunnusLineEdit.setFont(font)
        self.palvelinLabel = QLabel(Dialog)
        self.palvelinLabel.setObjectName(u"palvelinLabel")
        self.palvelinLabel.setGeometry(QRect(130, 60, 100, 20))
        self.palvelinLabel.setFont(font1)
        self.vanhaSalasanaLabel = QLabel(Dialog)
        self.vanhaSalasanaLabel.setObjectName(u"vanhaSalasanaLabel")
        self.vanhaSalasanaLabel.setGeometry(QRect(130, 330, 140, 20))
        self.vanhaSalasanaLabel.setFont(font1)
        self.uusiSalasanaLabel = QLabel(Dialog)
        self.uusiSalasanaLabel.setObjectName(u"uusiSalasanaLabel")
        self.uusiSalasanaLabel.setGeometry(QRect(130, 380, 140, 20))
        self.uusiSalasanaLabel.setFont(font1)
        self.uusiSalasanaLineEdit = QLineEdit(Dialog)
        self.uusiSalasanaLineEdit.setObjectName(u"uusiSalasanaLineEdit")
        self.uusiSalasanaLineEdit.setGeometry(QRect(290, 380, 150, 25))
        self.uusiSalasanaLineEdit.setFont(font)
        self.uusiSalasanaLineEdit.setEchoMode(QLineEdit.Normal)
        self.vaihdaSalasanapushButton = QPushButton(Dialog)
        self.vaihdaSalasanapushButton.setObjectName(u"vaihdaSalasanapushButton")
        self.vaihdaSalasanapushButton.setGeometry(QRect(290, 430, 150, 25))
        self.vaihdaSalasanapushButton.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.porttiLabel.setText(QCoreApplication.translate("Dialog", u"Portti", None))
        self.tietokantaLabel.setText(QCoreApplication.translate("Dialog", u"Tietokanta", None))
        self.kayttajatunnusLabel.setText(QCoreApplication.translate("Dialog", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.tallennaPushButton.setText(QCoreApplication.translate("Dialog", u"Tallenna", None))
        self.palvelinLabel.setText(QCoreApplication.translate("Dialog", u"Palvelin", None))
        self.vanhaSalasanaLabel.setText(QCoreApplication.translate("Dialog", u"Vanha Salasana", None))
        self.uusiSalasanaLabel.setText(QCoreApplication.translate("Dialog", u"Uusi Salasana", None))
        self.vaihdaSalasanapushButton.setText(QCoreApplication.translate("Dialog", u"Vaihda Salasana", None))
    # retranslateUi

