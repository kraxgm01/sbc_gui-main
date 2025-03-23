from PySide6.QtWidgets import QPushButton

class NewButton(QPushButton):
    def __init__(self, text="Click Me", isCheckable=False):
        super().__init__()
        self.setText(text)
        self.setCheckable(isCheckable)
