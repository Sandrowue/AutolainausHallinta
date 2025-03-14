import os # Polkumääritykset
import sys # Käynnistysargumentit
import json 
import dbOperations


from PySide6 import QtWidgets
from Autolainaus import Ui_MainWindow
from Settings_dialog import Ui_Dialog as Settings_Dialog
from About_dialog import Ui_Dialog as About_Dialog


import cipher

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # Rutiini, joka lukee asetukset, jos ne ovat olemassa
        try:
            with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)

                encryptedPassword = self.currentSettings['password']
                
                plainPassword = cipher.decryptString(encryptedPassword)
                
            # Päivitetään yhdistelmäruutjen arvot ohjelman käynnistyksen yhteydessä
            
        except Exception as e:
            self.openSettingsDialog()
            
        self.refreshUi()

        # OHJELMOIDUT SIGNAALIT
        # Valikkotoiminnot
        self.ui.actionMuokkaa.triggered.connect(self.openSettingsDialog)
        self.ui.actionTietoja_ohjelmasta.triggered.connect(self.openAboutDialog)

        # Välilehtien vaihdot päivittävät comboxit
        self.ui.tabWidget.currentChanged.connect(lambda: self.updateCombox(self.ui.ajoneuvotyyppiComboBox, 'ajoneuvotyyppi', 'ajoneuvotyyppi'))
        self.ui.tabWidget.currentChanged.connect(lambda: self.updateCombox(self.ui.vaihteistotyyppiComboBox, 'vaihteistotyyppi', 'vaihteistotyyppi'))

        # Painikkeet
        self.ui.tallennaLainaajatPushButton.clicked.connect(self.savePerson)
        self.ui.tallennaAutotPushButton.clicked.connect(self.saveCar)
        

    # OHJELMOIDUT SLOTIT

    # Valikkotoimintojen slotit

    # Dialogien avausmetodit
    def openSettingsDialog(self):
        self.saveSettingsDialog = SaveSettingsDialog()
        self.saveSettingsDialog.setWindowTitle('Palvelinasetukset')
        self.saveSettingsDialog.exec()

    def openAboutDialog(self):
        self. aboutDialog = AboutWindow()
        self.aboutDialog.setWindowTitle('Tietoja ohjelmasta')
        self.aboutDialog.exec()

    # Yleinen käyttöliittymän verestys (refresh)
    def refreshUi(self):
        self.updateLainaajaTableWidget()
        self.updateAutoTableWidget()
        self.updateCombox(self.ui.ajoneuvotyyppiComboBox, 'ajoneuvotyyppi', 'ajoneuvotyyppi')
        self.updateCombox(self.ui.vaihteistotyyppiComboBox, 'vaihteistotyyppi', 'vaihteistotyyppi')

    # PAINIKKEIDEN SLOTIT

    def updateCombox(self, comboBox, tableName, columnName):
        dbSettings = self.currentSettings
        dbConnection = dbOperations.DbConnection(dbSettings)
        # Tehdään lista lainaaja
        groupList = dbConnection.readChosenColumnFormTable(tableName, columnName)
        simpleList = []
        for tuple in groupList:
            simpleList.append(tuple[0])
        print('Ajoneuvtyyppilista:', simpleList)
        comboBox.clear()
        comboBox.addItems(simpleList)
        
    
    # Lainaajat-taulukon päivitys
    def updateLainaajaTableWidget(self):
        dbSettings = self.currentSettings
        dbConnection = dbOperations.DbConnection(dbSettings)
        tableData = dbConnection.readAllColumnsFromTable('lainaaja')
        headerRow = ['Henkilötunnus', 'Etunimi', 'Sukunimi', 'Ajokortti', 'Sähköposti']
        self.ui.lainaajatTableWidget.setHorizontalHeaderLabels(headerRow)
        for row in range(len(tableData)): # Luetaan listaa riveittäin
            for column in range(len(tableData[row])): # Luetaan monikkoa sarakkeittain
            # Muutetaan merkkijonoksi ja QTableWidgetItem-olioksi
                data = QtWidgets.QTableWidgetItem(str(tableData[row][column]))
                self.ui.lainaajatTableWidget.setItem(row, column, data)
    
    # Autot-taulukon päivitys
    def updateAutoTableWidget(self):
        dbSettings = self.currentSettings
        dbConnection = dbOperations.DbConnection(dbSettings)
        tableData = dbConnection.readAllColumnsFromTable('auto')
        headerRow = ['Rekisterinumero', 'Malli', 'Merkki', 'Vuosimalli', 'Henkilömäärä', 'Ajoneuvotyyppi', 'Vaihteistotyyppi']
        self.ui.autoluetteloTableWidget.setHorizontalHeaderLabels(headerRow)
        for row in range(len(tableData)):
            for column in range(len(tableData[row])):
                data = QtWidgets.QTableWidgetItem(str(tableData[row][column]))
                self.ui.autoluetteloTableWidget.setItem(row, column, data)
        
    def saveCar(self):
        dbSettings = self.currentSettings
        tableName = 'auto'

        rekisterinumero = self.ui.rekisterinumeroLineEdit.text()
        malli = self.ui.malliLineEdit.text()
        merkki = self.ui.merkkiLineEdit.text()
        vuosimalli = self.ui.vuosimalliLineEdit.text()
        henkilomaara = self.ui.henkilomaaraLineEdit.text()
        ajoneuvotyyppi = self.ui.ajoneuvotyyppiComboBox.currentText()
        vaihteistotyyppi = self.ui.vaihteistotyyppiComboBox.currentText()

        groupDictionary = {
            'rekisterinumero': rekisterinumero,
            'malli': malli,
            'merkki': merkki,
            'vuosimalli': vuosimalli,
            'henkilomaara': henkilomaara,
            'ajoneuvotyyppi': ajoneuvotyyppi,
            'vaihteistotyyppi': vaihteistotyyppi,
        }

        dbConnection = dbOperations.DbConnection(dbSettings)

        try:
            dbConnection.addToTable(tableName, groupDictionary)
            self.updateAutoTableWidget()
        except Exception as e:
            self.openWarning('Virhe!', f'Toiminto keskeytyi! {e}')

    def savePerson(self):
        dbSettings = self.currentSettings
        tableName = 'lainaaja'
        
        hetu = self.ui.henkilotunnusLineEdit.text()
        etunimi = self.ui.etunimiLineEdit.text()
        sukunimi = self.ui.sukunimiLineEdit.text()
        ajokortti = self.ui.ajoneuvoluokkaLineEdit.text()
        sahkoposti = self.ui.sahkopostiLineEdit.text()

        groupDictionary = {
            'hetu': hetu,
            'etunimi': etunimi,
            'sukunimi': sukunimi,
            'ajokorttiluokka': ajokortti,
            'sahkoposti': sahkoposti
        }

        dbConnection = dbOperations.DbConnection(dbSettings)
        

        try:
            dbConnection.addToTable(tableName, groupDictionary)
            self.updateLainaajaTableWidget()
        except Exception as e:
            self.openWarning('Virhe!', f'Toiminto keskeytyi! {e}')

    def openWarning(self, title: str, text: str) -> None:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

    # Asetusten tallennusikkunan luokka
class SaveSettingsDialog(QtWidgets.QDialog, Settings_Dialog):
    def __init__(self):
        super().__init__()

        self.ui = Settings_Dialog()
        self.ui.setupUi(self)

        self.currentSettings = {}
        
        
        try:
            with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)

            self.ui.palvelinLineEdit.setText(self.currentSettings['server'])
            self.ui.porttiLineEdit.setText(self.currentSettings['port'])
            self.ui.tietokantaLineEdit.setText(self.currentSettings['database'])
            self.ui.KayttajatunnusLineEdit.setText(self.currentSettings['userName'])
            
            self.ui.vaihdaSalasanapushButton.setEnabled(False)
            self.ui.tallennaPushButton.clicked.connect(self.saveUserToJsonFile)

            # if self.ui.vanhaSalasanaLineEdit.text() == self.currentSettings['password']:
            self.ui.uusiSalasanaLineEdit.textEdited.connect(self.enableVaihdaSalasana)
            self.ui.vaihdaSalasanapushButton.clicked.connect(self.savePasswordToJsonFile)
        
        except Exception as e:
            self.openInfo()
            
            self.ui.tallennaPushButton.clicked.connect(self.saveAllToJsonFile)

            self.ui.vanhaSalasanaLineEdit.hide()
            self.ui.vaihdaSalasanapushButton.hide()
            self.ui.vanhaSalasanaLabel.hide()

    def enableVaihdaSalasana(self):
        if self.ui.vanhaSalasanaLineEdit.text() == cipher.decryptString(self.currentSettings['password']):
            self.ui.vaihdaSalasanapushButton.setEnabled(True)

    def saveAllToJsonFile(self):

        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        server = self.ui.palvelinLineEdit.text()
        port = self.ui.porttiLineEdit.text()
        database = self.ui.tietokantaLineEdit.text() 
        userName = self.ui.KayttajatunnusLineEdit.text()
        newPassword = self.ui.uusiSalasanaLineEdit.text()

        # Salataan ja muunnetaan tavalliseksi merkkijonoksi, jotta JSON-tallennus onnistuu
        encryptedPassword = cipher.encryptString(newPassword)

        # Muodostetaan muuttujista Python-sanakirja
        settingsDictionary = {
            'server': server,
            'port': port,
            'database': database,
            'userName': userName,
            'password': encryptedPassword
        }

        # Muunnetaan sanakirja JSON-muotoon
        jsonData = json.dumps(settingsDictionary)

        # Avataan asetustiedosto ja korjataan asetukset
        with open('settings.json', 'wt') as settingsFile:
            settingsFile.write(jsonData)


    def saveUserToJsonFile(self):

        with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                actualSettings = json.loads(jsonData)

        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        server = self.ui.palvelinLineEdit.text()
        port = self.ui.porttiLineEdit.text()
        database = self.ui.tietokantaLineEdit.text() 
        userName = self.ui.KayttajatunnusLineEdit.text()
        password = actualSettings['password']
        
        
        
        # Muodostetaan muuttujista Python-sanakirja
        settingsDictionary = {
            'server': server,
            'port': port,
            'database': database,
            'userName': userName, 
            'password': password
        }

        # Muunnetaan sanakirja JSON-muotoon
        jsonData = json.dumps(settingsDictionary)

        # Avataan asetustiedosto ja korjataan asetukse

        with open('settings.json', 'wt') as settingsFile:
            settingsFile.write(jsonData)
        
            
    def savePasswordToJsonFile(self):

        with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                actualSettings = json.loads(jsonData)

        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        newPassword = self.ui.uusiSalasanaLineEdit.text()

        # Salataan ja muunnetaan tavalliseksi merkkijonoksi, jotta JSON-tallennus onnistuu
        encryptedPassword = cipher.encryptString(newPassword)

        # Muodostetaan muuttujista Python-sanakirja
        settingsDictionary = {
            'server': actualSettings['server'],
            'port': actualSettings['port'],
            'database': actualSettings['database'],
            'userName': actualSettings['userName'],
            'password': encryptedPassword
        }

        # Muunnetaan sanakirja JSON-muotoon
        jsonData = json.dumps(settingsDictionary)

        # Avataan asetustiedosto ja korjataan asetukset
        if self.ui.vanhaSalasanaLineEdit.text() == cipher.decryptString(actualSettings['password']):
            with open('settings.json', 'wt') as settingsFile:
                settingsFile.write(jsonData)               

    # Avataan Message Box
    def openInfo(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle('Huomautus!')
        msgBox.setText('settings.json tiedosto puuttuu!')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

class AboutWindow(QtWidgets.QDialog, About_Dialog):
    def __init__(self):
        super().__init__()
        
        self.ui = About_Dialog()

        self.ui.setupUi(self)

if __name__ == "__main__":
    # Luodaan sovellus ja setetaan tyyliksi Fusion
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.setWindowTitle('Autolainauksen hallinta')
    window.show()

    app.exec()