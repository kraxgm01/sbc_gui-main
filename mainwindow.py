from PySide6.QtWidgets import QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Light Runner")

        # Menubar and menus
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")
        exit = file_menu.addAction("Exit")
        # exit.triggered.connect(self)

        # Help Menu
        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction("Experiment Basics")
        help_menu.addAction("Numerical Aperture")
        help_menu.addAction("Modes in Optical Fiber")
        help_menu.addAction("Attenuation in Optical Fiber")
        help_menu.addAction("Bending Loss in Optical Fiber")
        help_menu.addAction("Dispersion in Optical Fiber")
        help_menu.addAction("Characteristics Of Laser Diode")
        help_menu.addAction("Characteristics Of Photo Diode")
        help_menu.addAction("Characterization of WDM Mux & Demux")
        help_menu.addAction("Characterization of FBG and Optical Circulator")
        help_menu.addAction("Characterization of Erbium Doped Fiber Amplifier")
        help_menu.addAction("Analog and Digital Fiber Optic Links")
        help_menu.addAction("Time Division Multiplexing of Digital Signals")
        help_menu.addAction("WDM Fiber Optic Link")
        help_menu.addAction("Optical Amplification in a WDM Link")
        help_menu.addAction("Adding and Dropping of channels in a WDM Link")
        help_menu.addAction("Optical Time Domain Reflectometer")
        help_menu.addAction("Bit Error Rate and Eye Pattern Analysis")
        help_menu.addAction("Power Budgeting of an Optical Fiber Link")
        help_menu.addAction("Rise Time Budgeting of an Optical Fiber Link")

        # Experiment Menu

        experiment_menu = menu_bar.addMenu("Experiment")
        experiment_menu.addAction("Numerical Aperture")
        experiment_menu.addAction("Modes in Optical Fiber")
        experiment_menu.addAction("Attenuation in Optical Fiber")
        experiment_menu.addAction("Bending Loss in Optical Fiber")
        experiment_menu.addAction("Dispersion in Optical Fiber")
        experiment_menu.addAction("Characteristics Of Laser Diode")
        experiment_menu.addAction("Characteristics Of Photo Diode")
        experiment_menu.addAction("Characterization of WDM Mux & Demux")
        experiment_menu.addAction("Characterization of FBG and Optical Circulator")
        experiment_menu.addAction("Characterization of Erbium Doped Fiber Amplifier")
        experiment_menu.addAction("Analog and Digital Fiber Optic Links")
        experiment_menu.addAction("Time Division Multiplexing of Digital Signals")
        experiment_menu.addAction("WDM Fiber Optic Link")
        experiment_menu.addAction("Optical Amplification in a WDM Link")
        experiment_menu.addAction("Adding and Dropping of channels in a WDM Link")
        experiment_menu.addAction("Optical Time Domain Reflectometer")
        experiment_menu.addAction("Bit Error Rate and Eye Pattern Analysis")
        experiment_menu.addAction("Power Budgeting of an Optical Fiber Link")
        experiment_menu.addAction("Rise Time Budgeting of an Optical Fiber Link")
        experiment_menu.addAction("Custom Experiment")

        # Configuration Menu

        configuration_menu = menu_bar.addMenu("Configuration")
        configuration_menu.addAction("Exam Mode")
        configuration_menu.addAction("Change Password")

        # System Menu

        system_menu = menu_bar.addMenu("System")
        system_menu.addAction("Shutdown")
        system_menu.addAction("Restart")

        # About Menu

        about_menu = menu_bar.addMenu("About")
        about_menu.triggered.connect(self.app.message_pop_new)
        # TODO: Add Message Box

        # Update Menu

        update_menu = menu_bar.addMenu("Update")
        # TODO: Add Update Functionality

    def message_pop_new(self):
        ret = QMessageBox.information(
            self,
            "About Light Runner",
            "Light Runner is a software developed by the students of Department of Electronics and Communication Engineering, NIT Durgapur",
            QMessageBox.Ok,
        )
        if ret == QMessageBox.Ok:
            pass
        else:
            pass
