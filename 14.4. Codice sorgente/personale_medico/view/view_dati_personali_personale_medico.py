from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from personale_medico.controller import controller_personale_medico

from tools.animazioni import Animazioni
from tools.menu_a_tendina_personale_medico import MenuATendinaPersonaleMedico
from tools import ridimensiona_widget


class ViewPersonaleMedico(QWidget):

    def __init__(self, personale_medico):
        """
        Costruttore della classe ViewPersonaleMedico, nella quale vengono creati e mostrati tutti gli
        oggetti della Graphical User Interface (GUI) relativi alla suddetta view

        :param personale_medico: Variabile d'istanza che rappresenta un oggetto della classe PersonaleMedico
        :type personale_medico: PersonaleMedico
        """
        super().__init__()

        self.personale_medico = personale_medico

        self.dati_personali = QtWidgets.QLabel(self)
        self.logo = QtWidgets.QLabel(self)
        self.titolo = QtWidgets.QLabel(self)
        self.cognome = QtWidgets.QLabel(self)
        self.codice_fiscale = QtWidgets.QLabel(self)
        self.nome = QtWidgets.QLabel(self)
        self.eta = QtWidgets.QLabel(self)
        self.provincia = QtWidgets.QLabel(self)
        self.sesso = QtWidgets.QLabel(self)
        self.citta_di_nascita = QtWidgets.QLabel(self)
        self.data_di_nascita = QtWidgets.QLabel(self)
        self.nome_label = QtWidgets.QLabel(self)
        self.codice_id = QtWidgets.QLabel(self)
        self.cognome_label = QtWidgets.QLabel(self)
        self.data_di_nascita_label = QtWidgets.QLabel(self)
        self.provincia_label = QtWidgets.QLabel(self)
        self.citta_di_nascita_label = QtWidgets.QLabel(self)
        self.codice_fiscale_label = QtWidgets.QLabel(self)
        self.eta_label = QtWidgets.QLabel(self)
        self.sesso_label = QtWidgets.QLabel(self)
        self.codice_id_label = QtWidgets.QLabel(self)
        self.password = QtWidgets.QLabel(self)
        self.password_line_edit = QtWidgets.QLineEdit(self)
        self.occhiello_barrato_button = QtWidgets.QPushButton(self)
        self.occhiello_button = QtWidgets.QPushButton(self)
        self.modifica_password = QtWidgets.QPushButton(self)
        self.annulla_modifica_password = QtWidgets.QPushButton(self)
        self.modifica_password_label = QtWidgets.QLabel(self)
        self.vecchia_password = QtWidgets.QLabel(self)
        self.nuova_password = QtWidgets.QLabel(self)
        self.confema_password = QtWidgets.QLabel(self)
        self.vecchia_password_line_edit = QtWidgets.QLineEdit(self)
        self.nuova_password_line_edit = QtWidgets.QLineEdit(self)
        self.conferma_password_line_edit = QtWidgets.QLineEdit(self)
        self.scritta = QtWidgets.QLabel(self)
        self.conferma_button = QtWidgets.QPushButton(self)
        self.line = QtWidgets.QFrame(self)
        self.email = QtWidgets.QLabel(self)
        self.ambulatorio = QtWidgets.QLabel(self)
        self.email_label = QtWidgets.QLabel(self)
        self.ambulatorio_label = QtWidgets.QLabel(self)
        self.setup_ui(self)

        self.menu_a_tendina = MenuATendinaPersonaleMedico(self)
        self.animazioni = Animazioni()

        self.controller_personale_medico = controller_personale_medico.ControllerPersonaleMedico(self)

        ridimensiona_widget.ridimensiona_view(self)

    def occhiello_button_pressed(self):
        """
        Funzione che rende visibile il testo inserito nella line_edit delle password nel momento in cui si preme
        l'apposito button
        """
        # non fa vedere la password digitata
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.vecchia_password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.nuova_password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conferma_password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.occhiello_barrato_button.setVisible(True)
        self.occhiello_button.setVisible(False)

    def occhiello_barrato_button_pressed(self):
        """
        Funzione che nasconde l testo inserito nella line_edit delle password nel momento in cui si preme l'apposito
        button
        """
        # fa vedere la password digitata
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.vecchia_password_line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.nuova_password_line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.conferma_password_line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.occhiello_button.setVisible(True)
        self.occhiello_barrato_button.setVisible(False)

    def setup_ui(self, dati_personali_personale_medico):
        """
        Funzione che crea e determina le caratteristiche degli oggetti della ViewPersonaleMedico

        :param dati_personali_personale_medico: Oggetto della view che rappresenta la view stessa
        :type dati_personali_personale_medico: ViewPersonaleMedico
        """
        dati_personali_personale_medico.setObjectName("dati_personali_personale_medico")
        dati_personali_personale_medico.move(0, 0)
        dati_personali_personale_medico.resize(1920, 1080)
        dati_personali_personale_medico.setMinimumSize(QtCore.QSize(1920, 1080))
        dati_personali_personale_medico.setMaximumSize(QtCore.QSize(1920, 1080))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        dati_personali_personale_medico.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Immagini/logo_casa_alfredo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dati_personali_personale_medico.setWindowIcon(icon)
        dati_personali_personale_medico.setStyleSheet("")
        self.dati_personali.setGeometry(QtCore.QRect(530, 20, 721, 131))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.dati_personali.setFont(font)
        self.dati_personali.setStyleSheet("color: rgb(84, 149, 223);")
        self.dati_personali.setObjectName("dati_personali")
        self.logo.setGeometry(QtCore.QRect(10, 5, 110, 130))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Immagini/logo_casa_alfredo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.titolo.setGeometry(QtCore.QRect(110, 20, 401, 110))
        self.titolo.setText("")
        self.titolo.setPixmap(QtGui.QPixmap("Immagini/titolo_casa_alfredo.png"))
        self.titolo.setScaledContents(True)
        self.titolo.setObjectName("titolo")
        self.cognome.setGeometry(QtCore.QRect(20, 270, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.cognome.setFont(font)
        self.cognome.setObjectName("cognome")
        self.codice_fiscale.setGeometry(QtCore.QRect(20, 830, 241, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.codice_fiscale.setFont(font)
        self.codice_fiscale.setObjectName("codice_fiscale")
        self.nome.setGeometry(QtCore.QRect(20, 190, 111, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.nome.setFont(font)
        self.nome.setObjectName("nome")
        self.eta.setGeometry(QtCore.QRect(20, 430, 71, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.eta.setFont(font)
        self.eta.setObjectName("eta")
        self.provincia.setGeometry(QtCore.QRect(20, 590, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.provincia.setFont(font)
        self.provincia.setObjectName("provincia")
        self.sesso.setGeometry(QtCore.QRect(20, 510, 111, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.sesso.setFont(font)
        self.sesso.setObjectName("sesso")
        self.citta_di_nascita.setGeometry(QtCore.QRect(20, 670, 261, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.citta_di_nascita.setFont(font)
        self.citta_di_nascita.setObjectName("citta_di_nascita")
        self.data_di_nascita.setGeometry(QtCore.QRect(20, 350, 261, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.data_di_nascita.setFont(font)
        self.data_di_nascita.setObjectName("data_di_nascita")
        self.nome_label.setGeometry(QtCore.QRect(350, 190, 570, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.nome_label.setFont(font)
        self.nome_label.setText("")
        self.nome_label.setObjectName("nome_label")
        self.codice_id.setGeometry(QtCore.QRect(980, 190, 175, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.codice_id.setFont(font)
        self.codice_id.setObjectName("codice_id")
        self.cognome_label.setGeometry(QtCore.QRect(350, 270, 570, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.cognome_label.setFont(font)
        self.cognome_label.setText("")
        self.cognome_label.setObjectName("cognome_label")
        self.data_di_nascita_label.setGeometry(QtCore.QRect(350, 350, 570, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.data_di_nascita_label.setFont(font)
        self.data_di_nascita_label.setText("")
        self.data_di_nascita_label.setObjectName("data_di_nascita_label")
        self.provincia_label.setGeometry(QtCore.QRect(350, 590, 570, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.provincia_label.setFont(font)
        self.provincia_label.setText("")
        self.provincia_label.setObjectName("provincia_label")
        self.citta_di_nascita_label.setGeometry(QtCore.QRect(350, 670, 570, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.citta_di_nascita_label.setFont(font)
        self.citta_di_nascita_label.setText("")
        self.citta_di_nascita_label.setObjectName("citta_di_nascita_label")
        self.codice_fiscale_label.setGeometry(QtCore.QRect(350, 830, 570, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.codice_fiscale_label.setFont(font)
        self.codice_fiscale_label.setText("")
        self.codice_fiscale_label.setObjectName("codice_fiscale_label")
        self.eta_label.setGeometry(QtCore.QRect(150, 430, 270, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.eta_label.setFont(font)
        self.eta_label.setText("")
        self.eta_label.setObjectName("eta_label")
        self.sesso_label.setGeometry(QtCore.QRect(188, 510, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.sesso_label.setFont(font)
        self.sesso_label.setText("")
        self.sesso_label.setObjectName("sesso_label")
        self.codice_id_label.setGeometry(QtCore.QRect(1180, 190, 630, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.codice_id_label.setFont(font)
        self.codice_id_label.setText("")
        self.codice_id_label.setObjectName("codice_id_label")
        self.password.setGeometry(QtCore.QRect(960, 330, 201, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.password_line_edit.setEnabled(True)
        self.password_line_edit.setGeometry(QtCore.QRect(1190, 330, 581, 40))
        self.password_line_edit.setFont(font)
        self.password_line_edit.setStyleSheet("border: 0px solid")
        self.password_line_edit.setText("")
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line_edit.setReadOnly(True)
        self.password_line_edit.setObjectName("password_line_edit")

        self.occhiello_barrato_button.setGeometry(QtCore.QRect(1776, 330, 40, 40))
        self.occhiello_barrato_button.setStyleSheet("QPushButton#occhiello_barrato_button:pressed {\n"
                                                    "background-color: rgb(0, 0, 0, 0);\n"
                                                    "}")
        self.occhiello_barrato_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Immagini/occhiello_barrato_password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.occhiello_barrato_button.setIcon(icon2)
        self.occhiello_barrato_button.setIconSize(QtCore.QSize(30, 30))
        self.occhiello_barrato_button.setFlat(True)
        self.occhiello_barrato_button.setObjectName("occhiello_barrato_button")
        self.occhiello_barrato_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.occhiello_button.setGeometry(QtCore.QRect(1776, 330, 40, 40))
        self.occhiello_button.setStyleSheet("QPushButton#occhiello_button:pressed {\n"
                                            "background-color: rgb(0, 0, 0, 0);\n"
                                            "}")
        self.occhiello_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Immagini/occhiello_password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.occhiello_button.setIcon(icon2)
        self.occhiello_button.setIconSize(QtCore.QSize(30, 30))
        self.occhiello_button.setFlat(True)
        self.occhiello_button.setObjectName("occhiello_button")
        self.occhiello_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.occhiello_button.setVisible(False)

        self.modifica_password.setGeometry(QtCore.QRect(1190, 380, 165, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(16)
        font.setItalic(True)
        font.setUnderline(True)
        self.modifica_password.setFont(font)
        self.modifica_password.setStyleSheet("QPushButton#modifica_password {\n"
                                             "color: rgb(0, 0, 255);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#modifica_password:pressed {\n"
                                             "background-color: rgb(0, 0, 0, 0);\n"
                                             "color: rgb(0, 0, 180);\n"
                                             "}")
        self.modifica_password.setFlat(True)
        self.modifica_password.setObjectName("modifica_password")
        self.modifica_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.annulla_modifica_password.setGeometry(QtCore.QRect(1190, 380, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(16)
        font.setItalic(True)
        font.setUnderline(True)
        self.annulla_modifica_password.setFont(font)
        self.annulla_modifica_password.setStyleSheet("QPushButton#annulla_modifica_password {\n"
                                                     "color: rgb(0, 0, 255);\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton#annulla_modifica_password:pressed {\n"
                                                     "background-color: rgb(0, 0, 0, 0);\n"
                                                     "color: rgb(0, 0, 180);\n"
                                                     "}")
        self.annulla_modifica_password.setFlat(True)
        self.annulla_modifica_password.setObjectName("annulla_modifica_password")
        self.annulla_modifica_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.annulla_modifica_password.setVisible(False)

        self.modifica_password_label.setGeometry(QtCore.QRect(980, 460, 831, 561))
        self.modifica_password_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                                   "border: 2px solid;\n"
                                                   "border-color: rgb(33, 97, 171);")
        self.modifica_password_label.setText("")
        self.modifica_password_label.setObjectName("annulla_modifica_password_label")
        self.modifica_password_label.setVisible(False)
        self.vecchia_password.setGeometry(QtCore.QRect(990, 480, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.vecchia_password.setFont(font)
        self.vecchia_password.setObjectName("vecchia_password")
        self.vecchia_password.setVisible(False)
        self.nuova_password.setGeometry(QtCore.QRect(990, 590, 310, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.nuova_password.setFont(font)
        self.nuova_password.setObjectName("nuova_password")
        self.nuova_password.setVisible(False)
        self.confema_password.setGeometry(QtCore.QRect(990, 700, 370, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.confema_password.setFont(font)
        self.confema_password.setObjectName("confema_password")
        self.confema_password.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.vecchia_password_line_edit.setEnabled(True)
        self.vecchia_password_line_edit.setGeometry(QtCore.QRect(1310, 480, 490, 40))
        self.vecchia_password_line_edit.setFont(font)
        self.vecchia_password_line_edit.setStyleSheet("QLineEdit#vecchia_password_line_edit {\n"
                                                      "border: 1px solid;\n"
                                                      "padding-left: 8px;\n"
                                                      "padding-right: 8px;\n"
                                                      "}")
        self.vecchia_password_line_edit.setText("")
        self.vecchia_password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.vecchia_password_line_edit.setReadOnly(False)
        self.vecchia_password_line_edit.setObjectName("vecchia_password_line_edit")
        self.vecchia_password_line_edit.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.nuova_password_line_edit.setEnabled(True)
        self.nuova_password_line_edit.setGeometry(QtCore.QRect(1310, 590, 490, 40))
        self.nuova_password_line_edit.setFont(font)
        self.nuova_password_line_edit.setStyleSheet("QLineEdit#nuova_password_line_edit {\n"
                                                    "border: 1px solid;\n"
                                                    "padding-left: 8px;\n"
                                                    "padding-right: 8px;\n"
                                                    "}")
        self.nuova_password_line_edit.setText("")
        self.nuova_password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.nuova_password_line_edit.setReadOnly(False)
        self.nuova_password_line_edit.setObjectName("nuova_password_line_edit")
        self.nuova_password_line_edit.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.conferma_password_line_edit.setEnabled(True)
        self.conferma_password_line_edit.setGeometry(QtCore.QRect(1365, 700, 435, 40))
        self.conferma_password_line_edit.setFont(font)
        self.conferma_password_line_edit.setStyleSheet("QLineEdit#conferma_password_line_edit {\n"
                                                       "border: 1px solid;\n"
                                                       "padding-left: 8px;\n"
                                                       "padding-right: 8px;\n"
                                                       "}")
        self.conferma_password_line_edit.setText("")
        self.conferma_password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conferma_password_line_edit.setReadOnly(False)
        self.conferma_password_line_edit.setObjectName("conferma_password_line_edit")
        self.conferma_password_line_edit.setVisible(False)
        self.scritta.setGeometry(QtCore.QRect(990, 780, 811, 151))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.scritta.setFont(font)
        self.scritta.setObjectName("scritta")
        self.scritta.setVisible(False)
        self.conferma_button.setGeometry(QtCore.QRect(1645, 950, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.conferma_button.setFont(font)
        self.conferma_button.setStyleSheet("QPushButton#conferma_button {\n"
                                           "background-color: rgb(33, 97, 171);\n"
                                           "border: 1px solid;\n"
                                           "border-color: rgb(13, 41, 73);\n"
                                           "border-radius: 10px;\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "}\n"
                                           "QPushButton#conferma_button:pressed {\n"
                                           "background-color: rgb(13, 41, 73);\n"
                                           "border-color: rgb(33, 97, 171);\n"
                                           "color: rgb(200, 200, 200);\n"
                                           "}")
        self.conferma_button.setObjectName("conferma_button")
        self.conferma_button.setVisible(False)
        self.line.setGeometry(QtCore.QRect(935, 180, 20, 860))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.email.setGeometry(QtCore.QRect(20, 750, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.ambulatorio.setGeometry(QtCore.QRect(20, 910, 221, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.ambulatorio.setFont(font)
        self.ambulatorio.setObjectName("ambulatorio")
        self.email_label.setGeometry(QtCore.QRect(350, 750, 570, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.email_label.setFont(font)
        self.email_label.setText("")
        self.email_label.setObjectName("email_label")
        self.ambulatorio_label.setGeometry(QtCore.QRect(350, 910, 570, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        self.ambulatorio_label.setFont(font)
        self.ambulatorio_label.setText("")
        self.ambulatorio_label.setObjectName("ambulatorio_label")

        self.retranslate_ui(dati_personali_personale_medico)
        QtCore.QMetaObject.connectSlotsByName(dati_personali_personale_medico)

    def retranslate_ui(self, dati_personali_personale_medico):
        """
        Funzione che formatta il testo degli oggetti creati all'interno della view

        :param dati_personali_personale_medico: Oggetto della view che rappresenta la view stessa
        :type dati_personali_personale_medico: ViewPersonaleMedico
        """
        _translate = QtCore.QCoreApplication.translate
        dati_personali_personale_medico.setWindowTitle(
            _translate("dati_personali_personale_medico", "Clinica Casa Alfredo"))
        self.dati_personali.setText(_translate("dati_personali_personale_medico", "- Dati Personali"))
        self.cognome.setText(_translate("dati_personali_personale_medico", "Cognome:"))
        self.codice_fiscale.setText(_translate("dati_personali_personale_medico", "Codice fiscale:"))
        self.nome.setText(_translate("dati_personali_personale_medico", "Nome:"))
        self.eta.setText(_translate("dati_personali_personale_medico", "Età:"))
        self.provincia.setText(_translate("dati_personali_personale_medico", "Provincia:"))
        self.sesso.setText(_translate("dati_personali_personale_medico", "Sesso:"))
        self.citta_di_nascita.setText(_translate("dati_personali_personale_medico", "Città di nascita:"))
        self.data_di_nascita.setText(_translate("dati_personali_personale_medico", "Data di nascita:"))
        self.codice_id.setText(_translate("dati_personali_personale_medico", "Codice ID:"))
        self.password.setText(_translate("dati_personali_personale_medico", "*Password:"))
        self.modifica_password.setText(_translate("dati_personali_personale_medico", "Modifica password"))
        self.annulla_modifica_password.setText(
            _translate("dati_personali_personale_medico", "Annulla modifica password"))
        self.vecchia_password.setText(_translate("dati_personali_personale_medico", "Vecchia password:"))
        self.nuova_password.setText(_translate("dati_personali_personale_medico", "*Nuova password:"))
        self.confema_password.setText(_translate("dati_personali_personale_medico", "*Conferma password:"))
        self.scritta.setText(_translate("dati_personali_personale_medico",
                                        "*Attenzione! La password deve contenere \n"
                                        " almeno 8 caratteri, di cui almeno 1 numero,\n"
                                        " 1 lettera Maiuscola, 1 carattere speciale"))
        self.conferma_button.setText(_translate("dati_personali_personale_medico", "Conferma"))
        self.email.setText(_translate("dati_personali_personale_medico", "E-mail:"))
        self.ambulatorio.setText(_translate("dati_personali_personale_medico", "Ambulatorio:"))
