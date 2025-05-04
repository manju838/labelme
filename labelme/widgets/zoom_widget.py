from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets

"""_summary_:
    This code defines the automatic zoom amount set for each image based on the image size and the screen size and also allows to control the zoom level using a text box widget in tool menu beside Detect btn.

"""

class ZoomWidget(QtWidgets.QSpinBox):
    # Zoom Level widget in labelme(present beside Detect button in Tools menu present below Menubar, mouse rightclick to activate it if not visible)
    # QSpinBox is a Qt based GUI element widget that allows user to type a number and have increment/decrement arrows(disabled in labelme)
    def __init__(self, value=100):
        super(ZoomWidget, self).__init__()
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons) # No increment/decrement arrow buttons, disabled here 
        self.setRange(1, 1000) # Allows values from 1% to 1000%
        self.setSuffix(" %")
        self.setValue(value)
        self.setToolTip("Zoom Level")
        self.setStatusTip(self.toolTip())
        self.setAlignment(QtCore.Qt.AlignCenter)

    def minimumSizeHint(self):
        # This method tells the layout manager what minimum size the widget should have.
        height = super(ZoomWidget, self).minimumSizeHint().height()
        fm = QtGui.QFontMetrics(self.font())
        width = fm.width(str(self.maximum()))
        return QtCore.QSize(width, height)
