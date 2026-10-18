"""Drawer Module"""
from PySide6.QtGui import QPaintEvent, QPainter, QColor #pylint: disable=no-name-in-module
from PySide6.QtWidgets import QWidget


class Drawer(QWidget):
    """Class that draws school maps from files"""
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.do_paint = False

    def trigger_paint(self):
        """Triggers to paint widget manually"""
        self.do_paint = True
        self.update()

    def paintEvent(self, _event: QPaintEvent) -> None: #pylint: disable=invalid-name
        """Draws school map"""
        if not self.do_paint:
            return

        with QPainter(self) as qp:
            self.draw(qp)

    def draw(self, qp: QPainter):
        """Draw method"""
        qp.fillRect(30, 30, 100, 100, QColor(255, 0, 0))
