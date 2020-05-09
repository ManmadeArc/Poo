from PyQt5 import QtWidgets


class ProfileFrame(QtWidgets.QFrame):

    def __init__(self, *args, **kwargs):
        QtWidgets.QFrame.__init__(self, *args, **kwargs)
        self.resize(640,360)
        self.Title=QtWidgets.QLabel("Carpetas")
        self.Title.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = ProfileFrame()
    window.show()
    window.Title.show()

    sys.exit(app.exec_())
