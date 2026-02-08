# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_interfaz(object):
    def setupUi(self, interfaz):
        if not interfaz.objectName():
            interfaz.setObjectName(u"interfaz")
        interfaz.resize(489, 356)
        self.lblBuscarTramite = QLabel(interfaz)
        self.lblBuscarTramite.setObjectName(u"lblBuscarTramite")
        self.lblBuscarTramite.setGeometry(QRect(80, 20, 91, 16))
        self.TxTBuscarTramite = QLineEdit(interfaz)
        self.TxTBuscarTramite.setObjectName(u"TxTBuscarTramite")
        self.TxTBuscarTramite.setGeometry(QRect(200, 20, 113, 20))
        self.TxTBuscarTramite.setMaxLength(3)
        self.lblDescripcion = QLabel(interfaz)
        self.lblDescripcion.setObjectName(u"lblDescripcion")
        self.lblDescripcion.setGeometry(QRect(60, 100, 111, 16))
        self.TxTDescripcion = QLineEdit(interfaz)
        self.TxTDescripcion.setObjectName(u"TxTDescripcion")
        self.TxTDescripcion.setGeometry(QRect(200, 100, 113, 20))
        self.TxTDescripcion.setMaxLength(60)
        self.lblCosto = QLabel(interfaz)
        self.lblCosto.setObjectName(u"lblCosto")
        self.lblCosto.setGeometry(QRect(70, 140, 101, 20))
        self.TxTCosto = QLineEdit(interfaz)
        self.TxTCosto.setObjectName(u"TxTCosto")
        self.TxTCosto.setGeometry(QRect(200, 140, 113, 20))
        self.TxTCosto.setMaxLength(6)
        self.groupBox = QGroupBox(interfaz)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 180, 301, 151))
        self.lblCedula = QLabel(self.groupBox)
        self.lblCedula.setObjectName(u"lblCedula")
        self.lblCedula.setGeometry(QRect(10, 30, 121, 16))
        self.TxTCedula = QLineEdit(self.groupBox)
        self.TxTCedula.setObjectName(u"TxTCedula")
        self.TxTCedula.setGeometry(QRect(160, 30, 113, 20))
        self.TxTCedula.setMaxLength(10)
        self.lblNombre = QLabel(self.groupBox)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(70, 70, 51, 20))
        self.TxTNombre = QLineEdit(self.groupBox)
        self.TxTNombre.setObjectName(u"TxTNombre")
        self.TxTNombre.setGeometry(QRect(160, 70, 113, 20))
        self.TxTNombre.setMaxLength(60)
        self.lblApellido = QLabel(self.groupBox)
        self.lblApellido.setObjectName(u"lblApellido")
        self.lblApellido.setGeometry(QRect(70, 110, 47, 13))
        self.TxTApellido = QLineEdit(self.groupBox)
        self.TxTApellido.setObjectName(u"TxTApellido")
        self.TxTApellido.setGeometry(QRect(160, 110, 113, 20))
        self.TxTApellido.setMaxLength(60)
        self.btnBuscar = QPushButton(interfaz)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(370, 20, 75, 23))
        self.btnCrear = QPushButton(interfaz)
        self.btnCrear.setObjectName(u"btnCrear")
        self.btnCrear.setGeometry(QRect(370, 60, 75, 23))
        self.btnActualizar = QPushButton(interfaz)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(370, 100, 75, 23))
        self.btnEliminar = QPushButton(interfaz)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setGeometry(QRect(370, 140, 75, 23))
        self.btnGuardar = QPushButton(interfaz)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(370, 220, 75, 23))
        self.btnLimpiar = QPushButton(interfaz)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(370, 260, 75, 23))
        self.lblCodigo = QLabel(interfaz)
        self.lblCodigo.setObjectName(u"lblCodigo")
        self.lblCodigo.setGeometry(QRect(80, 60, 101, 16))
        self.TxTCodigo = QLineEdit(interfaz)
        self.TxTCodigo.setObjectName(u"TxTCodigo")
        self.TxTCodigo.setGeometry(QRect(200, 60, 113, 20))
        self.TxTCodigo.setMaxLength(10)

        self.retranslateUi(interfaz)

        QMetaObject.connectSlotsByName(interfaz)
    # setupUi

    def retranslateUi(self, interfaz):
        interfaz.setWindowTitle(QCoreApplication.translate("interfaz", u"Sistema Registro de Tramites Ciudadanos", None))
        self.lblBuscarTramite.setText(QCoreApplication.translate("interfaz", u"Buscar Tr\u00e1mite", None))
        self.lblDescripcion.setText(QCoreApplication.translate("interfaz", u"Descripci\u00f3n Tr\u00e1mite", None))
        self.lblCosto.setText(QCoreApplication.translate("interfaz", u"Costo del Tr\u00e1mite", None))
        self.groupBox.setTitle(QCoreApplication.translate("interfaz", u"Datos del Ciudadano", None))
        self.lblCedula.setText(QCoreApplication.translate("interfaz", u"C\u00e9dula de Indentidad", None))
        self.lblNombre.setText(QCoreApplication.translate("interfaz", u"Nombre", None))
        self.lblApellido.setText(QCoreApplication.translate("interfaz", u"Apellido", None))
        self.btnBuscar.setText(QCoreApplication.translate("interfaz", u"Buscar", None))
        self.btnCrear.setText(QCoreApplication.translate("interfaz", u"Nuevo", None))
        self.btnActualizar.setText(QCoreApplication.translate("interfaz", u"Actualizar", None))
        self.btnEliminar.setText(QCoreApplication.translate("interfaz", u"Eliminar", None))
        self.btnGuardar.setText(QCoreApplication.translate("interfaz", u"Guardar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("interfaz", u"Limpiar", None))
        self.lblCodigo.setText(QCoreApplication.translate("interfaz", u"C\u00f3digo Tr\u00e1mite", None))
    # retranslateUi

