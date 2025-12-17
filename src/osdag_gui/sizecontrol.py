# osdag_gui/sizecontrol.py

from PySide6.QtCore import QSize

# Default icon size for navbar buttons
# This can be overridden for specific icons if needed
DEFAULT_NAVBAR_ICON_SIZE = QSize(40, 40) 

# Dictionary to store custom sizes for specific navbar icons.
# Keys should match the icon names used in NAVBAR_ICONS in ui_data.py
# Example: "Tension Member": QSize(30, 30)
CUSTOM_NAVBAR_ICON_SIZES = {
    "Tension Member": QSize(70, 70),
    # "Icon Name": QSize(width, height),
    "Connection" : QSize(25,25),
}

# Default icon size for floating navbar buttons
DEFAULT_FLOATING_NAVBAR_ICON_SIZE = QSize(40, 40)

# Dictionary to store custom sizes for specific floating navbar icons.
CUSTOM_FLOATING_NAVBAR_ICON_SIZES = {
   # "Tension Member": QSize(40, 40),
    # "Icon Name": QSize(width, height),
}
