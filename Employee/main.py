from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import sys
from pathlib import Path
import sqlite3
from PIL import Image
from typing import Union, Optional

con = sqlite3.connect("employee.db")
cur = con.cursor()
default_img = "person.png"
person_id = None


class Main(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super(Main, self).__init__(parent=parent)
        self.setWindowTitle("My Employee")
        self.setGeometry(450, 150, 750, 600)
        self.ui()
        self.show()

    def ui(self) -> None:
        """Set UI"""
        self.main_design()
        self.layouts()
        self.connect_slot()
        self.get_employees()
        self.display_first_record()

    def main_design(self) -> None:
        """Create widgets"""
        self.setStyleSheet("font-size:14pt;font-family:Arial;")
        self.employee_list = QListWidget()
        self.btn_new = QPushButton("New")
        self.btn_new.clicked.connect(self.add_employee)
        self.btn_update = QPushButton("Update")
        self.btn_delete = QPushButton("Delete")

    def layouts(self) -> None:
        """Create layouts"""
        ##################Layouts####################
        self.main_layout = QHBoxLayout()
        self.left_layout = QFormLayout()
        self.left_layout.setVerticalSpacing(20)
        self.left_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_btn_layout = QHBoxLayout()
        ##################Adding child layouts to main layouts####################
        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_btn_layout)
        self.main_layout.addLayout(self.left_layout, 40)
        self.main_layout.addLayout(self.right_main_layout, 60)
        ##################adding widgets to layout####################
        self.right_top_layout.addWidget(self.employee_list)
        self.right_btn_layout.addWidget(self.btn_new)
        self.right_btn_layout.addWidget(self.btn_update)
        self.right_btn_layout.addWidget(self.btn_delete)
        ##################setting main window layout ####################
        self.setLayout(self.main_layout)

    def connect_slot(self) -> None:
        self.employee_list.itemClicked.connect(self.change_display_record)
        self.btn_delete.clicked.connect(self.delete_employee)
        self.btn_update.clicked.connect(self.update_employee)

    def add_employee(self) -> None:
        self.new_employee = AddEmployee()
        self.close()

    def get_employees(self) -> None:
        query = "SELECT id, name, surname FROM employees"
        employees = cur.execute(query).fetchall()
        for id_, name, surname in employees:
            self.employee_list.addItem(f"{id_}-{name} {surname}")

    def display_record(self, person: tuple) -> None:
        img = QLabel()
        img.setPixmap(QPixmap(fr"images/{person[5]}"))
        name = QLabel(person[1])
        surname = QLabel(person[2])
        phone = QLabel(person[3])
        email = QLabel(person[4])
        address = QLabel(person[6])
        self.left_layout.addRow("", img)
        self.left_layout.addRow("Name: ", name)
        self.left_layout.addRow("Surname: ", surname)
        self.left_layout.addRow("Phone: ", phone)
        self.left_layout.addRow("Email: ", email)
        self.left_layout.addRow("Address: ", address)

    def display_first_record(self) -> None:
        query = "SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
        employee: Optional[tuple] = cur.execute(query).fetchone()
        if employee is None:
            employee = ("", "", "", "", "", "person.png", "")
        self.display_record(person=employee)

    def change_display_record(self) -> None:
        employee = self.employee_list.currentItem().text()
        id_, _ = employee.split("-")
        query = ("SELECT * FROM employees WHERE id=?")
        person = cur.execute(query, (id_,)).fetchone()  # single item tuple=(i,)
        for i in reversed(range(self.left_layout.count())):
            widget = self.left_layout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        self.display_record(person=person)

    def delete_employee(self):
        if self.employee_list.selectedItems():
            person = self.employee_list.currentItem().text()
            id_, _ = person.split("-")
            mbox = QMessageBox.question(self, "Warning", "Are you sure to delete this person?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if mbox == QMessageBox.Yes:
                try:
                    query = "DELETE FROM employees WHERE id=?"
                    cur.execute(query, (id_,))
                    con.commit()
                    QMessageBox.information(self, "Error", "Person has been deleted")
                    self.close()
                    self.main = Main()
                except:
                    QMessageBox.critical(self, "Error", "Person has not been deleted")
        else:
            QMessageBox.information(self, "Error", "Please select a person to delete")

    def update_employee(self):
        global person_id
        if self.employee_list.selectedItems():
            person = self.employee_list.currentItem().text()
            person_id, _ = person.split("-")
            self.update_window = UpdateEmployee()
            self.close()
        else:
            QMessageBox.information(self, "Error", "Please select a person to update")


class UpdateEmployee(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super(UpdateEmployee, self).__init__(parent=parent)
        self.setWindowTitle("Update Employees")
        self.setGeometry(450, 150, 350, 600)
        self.ui()
        self.show()

    def ui(self) -> None:
        """Set ui"""
        self.main_design()
        self.get_person_id()
        self.layouts()
        self.connect_slot()

    def closeEvent(self, event) -> None:
        self.main = Main()

    def get_person_id(self) -> None:
        global person_id

        query = "SELECT * FROM employees WHERE id=?"
        _, name, surname, phone, email, img, address = cur.execute(query, (person_id,)).fetchone()

        self.name_entry.setText(name)
        self.surname_entry.setText(surname)
        self.phone_entry.setText(phone)
        self.email_entry.setText(email)
        self.img_update.setPixmap(QPixmap(fr"images/{img}"))
        self.address_entry.setText(address)

    def main_design(self) -> None:
        """Create widgets"""
        ####################Top layout widgets###############
        self.setStyleSheet("background-color:white;font-size:14pt;font-family:Times;")
        self.title = QLabel("Update Person")
        self.title.setStyleSheet("font-size: 24pt;")  # font-family: Arial Bold;")
        self.img_update = QLabel()
        self.img_update.setPixmap(QPixmap(r"icons/person.png"))

        ####################Bottom layout widgets###############
        self.name_lable = QLabel("Name :")
        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText("Enter Employee Name")
        self.surname_lable = QLabel("Surname :")
        self.surname_entry = QLineEdit()
        self.surname_entry.setPlaceholderText("Enter Employee Surname")
        self.phone_lable = QLabel("Phone :")
        self.phone_entry = QLineEdit()
        self.phone_entry.setPlaceholderText("Enter Employee Phone Number")
        self.email_lable = QLabel("Email :")
        self.email_entry = QLineEdit()
        self.email_entry.setPlaceholderText("Enter Employee Email")
        self.img_label = QLabel("Picture :")
        self.img_button = QPushButton("Browse")
        self.img_button.setStyleSheet("background-color:orange;font-size:10pt;")
        self.address_lable = QLabel("Address :")
        self.address_entry = QTextEdit()
        self.update_button = QPushButton("Update")
        self.update_button.setStyleSheet("background-color:orange;font-size:10pt;")

    def layouts(self) -> None:
        """Create layouts"""
        ####################Createing main layouts###############
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.top_layout.setAlignment(Qt.AlignHCenter)
        self.bottom_layout = QFormLayout()
        self.bottom_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)

        ####################Adding child layouts to main layouts###############
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)

        ####################Adding widgets to layputs###############
        ##########Top layput#######
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.title)
        self.top_layout.addWidget(self.img_update)
        self.top_layout.addStretch()
        # self.top_layout.setContentsMargins(110, 20, 10, 10)  # left, top, right, bottom
        ##########Bottom layput#######
        self.bottom_layout.addRow(self.name_lable, self.name_entry)
        self.bottom_layout.addRow(self.surname_lable, self.surname_entry)
        self.bottom_layout.addRow(self.phone_lable, self.phone_entry)
        self.bottom_layout.addRow(self.email_lable, self.email_entry)
        self.bottom_layout.addRow(self.img_label, self.img_button)
        self.bottom_layout.addRow(self.address_lable, self.address_entry)
        self.bottom_layout.addRow("", self.update_button)
        ####################Setting main layout for window###############
        self.setLayout(self.main_layout)

    def connect_slot(self) -> None:
        """Connect slot"""
        self.img_button.clicked.connect(self.upload_image)
        self.update_button.clicked.connect(self.update_employee)

    def upload_image(self) -> None:
        """Upload employee image"""
        global default_img
        size = (120, 120)
        file_name, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files(*.jpg *.png)")
        if ok:
            default_img = Path(file_name).name
            img = Image.open(file_name)
            img = img.resize(size)
            img.save(fr"images/{default_img}")
            self.img_update.setPixmap(QPixmap(fr"images/{default_img}"))

    def update_employee(self) -> None:
        """Update employee to database"""
        global default_img, person_id
        name: str = self.name_entry.text()
        surname: str = self.surname_entry.text()
        phone: str = self.phone_entry.text()
        email: str = self.email_entry.text()
        img: str = default_img
        address: str = self.address_entry.toPlainText()

        if name and surname and phone != "":
            try:
                query = "UPDATE employees set name =?, surname =?, phone =?, email =?, image =?, address =? WHERE id =?"
                cur.execute(query, (name, surname, phone, email, img, address, person_id))
                con.commit()
                QMessageBox.information(self, "Success", "Person has been updated")
                self.close()
            except:
                QMessageBox.critical(self, "Error", "Person has not been updated")
        else:
            QMessageBox.warning(self, "Warning", "Fields can not be empty")


class AddEmployee(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super(AddEmployee, self).__init__(parent=parent)
        self.setWindowTitle("Add Employees")
        self.setGeometry(450, 150, 350, 600)
        self.ui()
        self.show()

    def ui(self) -> None:
        """Set ui"""
        self.main_design()
        self.layouts()
        self.connect_slot()

    def closeEvent(self, event) -> None:
        self.main = Main()

    def main_design(self) -> None:
        """Create widgets"""
        ####################Top layout widgets###############
        self.setStyleSheet("background-color:white;font-size:14pt;font-family:Times;")
        self.title = QLabel("Add Person")
        self.title.setStyleSheet("font-size: 24pt;")  # font-family: Arial Bold;")
        self.img_add = QLabel()
        self.img_add.setPixmap(QPixmap(r"icons/person.png"))

        ####################Bottom layout widgets###############
        self.name_lable = QLabel("Name :")
        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText("Enter Employee Name")
        self.surname_lable = QLabel("Surname :")
        self.surname_entry = QLineEdit()
        self.surname_entry.setPlaceholderText("Enter Employee Surname")
        self.phone_lable = QLabel("Phone :")
        self.phone_entry = QLineEdit()
        self.phone_entry.setPlaceholderText("Enter Employee Phone Number")
        self.email_lable = QLabel("Email :")
        self.email_entry = QLineEdit()
        self.email_entry.setPlaceholderText("Enter Employee Email")
        self.img_label = QLabel("Picture :")
        self.img_button = QPushButton("Browse")
        self.img_button.setStyleSheet("background-color:orange;font-size:10pt;")
        self.address_lable = QLabel("Address :")
        self.address_entry = QTextEdit()
        self.add_button = QPushButton("Add")
        self.add_button.setStyleSheet("background-color:orange;font-size:10pt;")

    def layouts(self) -> None:
        """Create layouts"""
        ####################Createing main layouts###############
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.top_layout.setAlignment(Qt.AlignHCenter)
        self.bottom_layout = QFormLayout()
        self.bottom_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)

        ####################Adding child layouts to main layouts###############
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)

        ####################Adding widgets to layputs###############
        ##########Top layput#######
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.title)
        self.top_layout.addWidget(self.img_add)
        self.top_layout.addStretch()
        # self.top_layout.setContentsMargins(110, 20, 10, 10)  # left, top, right, bottom
        ##########Bottom layput#######
        self.bottom_layout.addRow(self.name_lable, self.name_entry)
        self.bottom_layout.addRow(self.surname_lable, self.surname_entry)
        self.bottom_layout.addRow(self.phone_lable, self.phone_entry)
        self.bottom_layout.addRow(self.email_lable, self.email_entry)
        self.bottom_layout.addRow(self.img_label, self.img_button)
        self.bottom_layout.addRow(self.address_lable, self.address_entry)
        self.bottom_layout.addRow("", self.add_button)
        ####################Setting main layout for window###############
        self.setLayout(self.main_layout)

    def connect_slot(self) -> None:
        """Connect slot"""
        self.img_button.clicked.connect(self.upload_image)
        self.add_button.clicked.connect(self.add_employee)

    def upload_image(self) -> None:
        """Upload employee image"""
        global default_img
        size = (120, 120)
        file_name, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files(*.jpg *.png)")
        if ok:
            default_img = Path(file_name).name
            img = Image.open(file_name)
            img = img.resize(size)
            img.save(fr"images/{default_img}")
            self.img_add.setPixmap(QPixmap(fr"images/{default_img}"))

    def add_employee(self) -> None:
        """Add employee to database"""
        global default_img
        name: str = self.name_entry.text()
        surname: str = self.surname_entry.text()
        phone: str = self.phone_entry.text()
        email: str = self.email_entry.text()
        img: str = default_img
        address: str = self.address_entry.toPlainText()

        if name and surname and phone != "":
            try:
                query = "INSERT INTO employees (name, surname, phone, email, image, address) VALUES(?,?,?,?,?,?)"
                cur.execute(query, (name, surname, phone, email, img, address))
                con.commit()
                QMessageBox.information(self, "Success", "Person has been added")
                self.close()
            except:
                QMessageBox.critical(self, "Error", "Person has not been added")
        else:
            QMessageBox.warning(self, "Warning", "Fields can not be empty")


def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
