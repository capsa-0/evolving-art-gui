import sys

if __name__ == "__main__":

    from PySide6.QtWidgets import QApplication
    from src.app.main_window import MainWindow
    from src.app.theme import set_modern_theme

    app = QApplication(sys.argv)

    set_modern_theme(app)

    window = MainWindow()
    window.showFullScreen()

    sys.exit(app.exec())
