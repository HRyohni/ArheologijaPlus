def spremi_clicked(self):
    # Get the selected group
    selected_group = self.comboBox_group.currentText()

    # Sample data for debugging
    data = {
        "lokalitet": self.lineEdit_lokalitet.text(),
        "vrsta_SJ": self.lineEdit_vrsta_SJ.text(),
        "datum": self.lineEdit_datum.text(),
        "sonda": self.lineEdit_sonda.text(),
        "sektor": self.lineEdit_sektor.text(),
        "kvadrant": self.lineEdit_kvadrant.text(),
        "visina": self.lineEdit_visina.text(),
        "ap_sol_visina_najvise_tocke": self.lineEdit_ap_sol_visina_najvise_tocke.text(),
        "ap_sol_visina_najnize_tocke": self.lineEdit_ap_sol_visina_najnize_tocke.text(),
        "sastav": self.lineEdit_sastav.text(),
        "boja_munsell": self.lineEdit_boja_munsell.text(),
        "konzistencija": self.lineEdit_konzistencija.text(),
        "oblik": self.lineEdit_oblik.text(),
        "duzina": self.lineEdit_duzina.text(),
        "sirina": self.lineEdit_sirina.text(),
        "promjer": self.lineEdit_promjer.text(),
        "opis": self.textEdit_opis.toPlainText(),
        "ostali_nalazi": self.textEdit_ostali_nalazi.toPlainText(),
        "posebni_nalazi": self.textEdit_posebni_nalazi.toPlainText(),
        "pn": self.checkBox_pn.isChecked(),
        "uzorci": self.textEdit_uzorci.toPlainText(),
        "napomene": self.textEdit_napomene.toPlainText(),
    }

    # Here you can add the logic to save the data to the selected group
    # For example, you could save the data to a file, database, or any other storage
    with open(f'{selected_group}.txt', 'a') as file:
        file.write(str(data) + '\n')

    QtWidgets.QMessageBox.information(self, "Saved", f"Data saved to {selected_group}")
