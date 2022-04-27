import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox, QComboBox, QMessageBox
from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5 import QtCore, uic, QtGui
import sys
import os
from datetime import datetime
import yaml
import time

# copying over from PARASOL
# Set module directory, load yaml preferences
MODULE_DIR = os.path.dirname(__file__)
with open(os.path.join(MODULE_DIR, "..", "hardwareconstants.yaml"), "r") as f:
    defaults = yaml.safe_load(f)["RUN_UI"]  # , Loader=yaml.FullLoader)["relay"]

# Ensure resolution/dpi is correct for UI
if hasattr(QtCore.Qt, "AA_EnableHighDpiScaling"):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, "AA_UseHighDpiPixmaps"):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    
def RUNNER():
    """Create RUN UI window"""

    # Main function
    class RUN_UI(QMainWindow):
        """Run UI package for PARASOL"""

        def __init__(self) -> None:
            """Initliazes the RUN_UI class"""

            super(RUN_UI, self).__init__()

            # Initialize packages
            self.controller = Controller()
            self.characterization = Characterization()
            self.analysis = Analysis()
            self.grapher = Grapher()
            self.filestructure = FileStructure()

            # Make blank variables for the start date
            self.startdate1 = None
            self.startdate2 = None
            self.startdate3 = None
            self.startdate4 = None
            self.startdate5 = None
            self.startdate6 = None

            # Make blank variables for saveloc
            self.savedir1 = None
            self.savedir2 = None
            self.savedir3 = None
            self.savedir4 = None
            self.savedir5 = None
            self.savedir6 = None

            # Load the ui file
            ui_path = os.path.join(MODULE_DIR, "RUN_UI.ui")
            uic.loadUi(ui_path, self)
            self.show()