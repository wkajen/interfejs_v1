from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from window_new import Ui_MainWindow


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()

    sys.exit(app.exec_())

