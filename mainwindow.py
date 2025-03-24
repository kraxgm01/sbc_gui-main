from PySide6.QtWidgets import QMainWindow, QMessageBox, QStackedWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtPdf import QPdfDocument


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        # Create a stacked widget to hold multiple pages
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # Initialize loader and widget placeholders
        self.loader = QUiLoader()
        self.pdf_view = None
        self.mission_control_widget = None

        # Default flag: True means show PDF viewer page
        self.load_pdf = True
        self.widgetSwitcher()

        # Menubar and menus
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.app.quit)

        # Help Menu
        help_menu = menu_bar.addMenu("Help")
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
        num_ap_action = experiment_menu.addAction("Numerical Aperture")
        num_ap_action.triggered.connect(lambda: self.setLoadPdf(False))
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

        # Configuration Menu
        configuration_menu = menu_bar.addMenu("Configuration")
        exam_mode = configuration_menu.addAction("Exam Mode")
        exam_mode.triggered.connect(lambda: self.setLoadPdf(True))
        configuration_menu.addAction("Change Password")

        # System Menu
        system_menu = menu_bar.addMenu("System")
        about = system_menu.addAction("About")
        about.triggered.connect(self.message_pop_new)
        system_menu.addAction("Shutdown")
        system_menu.addAction("Restart")

        # Update Menu
        update_menu = menu_bar.addMenu("Update")
        # (Additional update functionality if needed)

    def setLoadPdf(self, value: bool):
        print("Inside setLoadPdf", value)
        self.load_pdf = value
        self.widgetSwitcher()

    def widgetSwitcher(self):
        print("Inside widgetSwitcher")
        print("load_pdf", self.load_pdf)
        if self.load_pdf:
            # Show PDF viewer page
            if self.pdf_view is None:
                self.pdf_view = self.create_pdf_view("manual.pdf")
                # Add the new page to the stack
                self.stack.addWidget(self.pdf_view)
            self.stack.setCurrentWidget(self.pdf_view)
        else:
            # Show mission control widget page
            if self.mission_control_widget is None:
                self.mission_control_widget = self.loader.load("ui/mission_control.ui", None)
                self.stack.addWidget(self.mission_control_widget)
            self.stack.setCurrentWidget(self.mission_control_widget)

    def create_pdf_view(self, pdf_path: str):
        print("Inside create_pdf_view")
        pdf_document = QPdfDocument(self)
        status = pdf_document.load(pdf_path)
        if status == QPdfDocument.Status.Error:
            QMessageBox.critical(self, "Error", "Failed to load PDF file!")
            return None
        pdf_view = QPdfView(self)
        pdf_view.setDocument(pdf_document)
        pdf_view.setPageMode(QPdfView.PageMode.MultiPage)
        pdf_view.setZoomMode(QPdfView.ZoomMode.FitToWidth)
        return pdf_view

    def message_pop_new(self):
        ret = QMessageBox.information(
            self,
            "About Light Runner",
            "Light Runner is a software developed by FiberOptika and Reslink Technologies Pvt. Ltd.",
            QMessageBox.Ok,
        )
