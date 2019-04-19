from arayuz_bim import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
import sys


class ProjectUi(QtWidgets.QMainWindow):
    def __init__(self):

        self.qt_app = QtWidgets.QApplication(sys.argv)
        QtWidgets.QWidget.__init__(self, None)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.textEdit
        # self.ui.lineEdit
        # self.ui.building
        # self.ui.building_2
        # self.ui.room

        self.ui.building.pressed.connect(self.denemeFonc)
        # # list1 =[]
        # self.ui.connect_button.pressed.connect(self.connect)
        # # self.ui.connect_button.pressed.connect(self.get_host_with_port)
        # self.ui.connect_button.pressed.connect(self.change_profile_name)
        # # self.ui.connect_button.pressed.connect(self.disable_button)
        # self.ui.LogOut_button.pressed.connect(self.logout_button)
        # self.ui.Subscribe_button.pressed.connect(self.subscribe_button)
        # self.ui.UnSubscribe_button.pressed.connect(self.unsubscribe_button)
        # self.ui.UnBlock_button.pressed.connect(self.unblock_button)
        # self.ui.Block_button.pressed.connect(self.block_button)
        # self.ui.SendMessage_button.pressed.connect(self.send_message_button)
        # self.ui.Share_button.pressed.connect(self.share_twit_button)
        # self.ui.Pubkey_button.pressed.connect(self.pubkey_button)
        # self.ui.users_button.pressed.connect(self.users_button)
        # self.initializeIpPort()
        # self.initialize_button_conf()
        # self.initializeMyBlogsList()

    def denemeFonc(self):
        print("ABASFAFAFAS")
        pass
    def initRooms(self,building):
        for r in building.rooms:
            self.ui.room.addItem(r.name)

    def initBuildings(self,buildings):
        self.ui.building.clear()
        self.ui.room.clear()
        print("ahahaha")
        for b in buildings:
            self.ui.building.addItem(b.name)
            self.initRooms(b)

        self.ui.myWindow.setPixmap(QtGui.QPixmap("./gsu.jpg"))
        # self.ui.myWindow.pixmap("gsu.jpg")
        self.ui.myLog.setText("LogDeneme")
        # pic.setGeometry(10, 10, 400, 100)
        # use full ABSOLUTE path to the image, not relative
        # pic.setPixmap(QtGui.QPixmap("./gsu.png"))
        pass

    def run(self):
        self.show()
        self.qt_app.exec_()
        # self.initBuildings()


def main():
    app = ProjectUi()
    app.run()

if __name__ == '__main__':
    main()