from gui import if __name__ == '__main__':


class PythonMongoDb(main.UI_MainWindow,QtWidgets.QMainWindow):
    def __init_subclass__(cls, **kwargs):
        super(PythonMongoDb,self)._init_()
        self.setupUi(self)

if _name_== '__man__':
    app = QtWidget.QApplication([])
    my_app = PythonMongoDb()
    my_app.show()
    app.exec()