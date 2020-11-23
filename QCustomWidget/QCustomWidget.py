from PyQt5.QtWidgets import *


class QCustomTableWidget(QTableWidget):
    def __init__(self, parent=None, rows_idx=0, columns_idx=0, v_header=None, h_header=None, readonly=True):
        super(QCustomTableWidget, self).__init__(parent)

        self.setRowCount(rows_idx)
        self.setColumnCount(columns_idx)

        self.__set_v_header(v_header)
        self.__set_h_header(h_header)

        self.__check_readonly(readonly)

    def __check_readonly(self, readonly):
        if readonly:
            self.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def __set_v_header(self, header):
        if header is not None:
            if hasattr(header, "__iter__"):
                self.setRowCount(len(header))
                for i, h in enumerate(header):
                    self.setVerticalHeaderItem(i, QTableWidgetItem(str(h)))
            else:
                raise TypeError("v_header should be iterable")

    def __set_h_header(self, header):
        if header is not None:
            if hasattr(header, "__iter__"):
                self.setColumnCount(len(header))
                for i, h in enumerate(header):
                    self.setHorizontalHeaderItem(i, QTableWidgetItem(str(h)))
            else:
                raise TypeError("h_header should be iterable")

    def add_last_row(self, add_items):
        if hasattr(add_items, "__iter__"):
            items_len = len(add_items)
            if items_len == self.columnCount():
                current_row_count = self.rowCount()
                self.insertRow(current_row_count)
                for i, item in enumerate(add_items):
                    self.setItem(current_row_count, i, QTableWidgetItem(str(item)))
            else:
                raise ValueError("len(add_items) not equal columnsCount()")
        else:
            raise TypeError("add_items should be iterable")
