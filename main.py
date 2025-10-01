"""
    author : Mohamed Khaled
    version: 0.0.1
    Thanks For everyone

"""


from gui_design import App
from convert_txt_tocsv import Converter

import sys, os

def icon_path():
    icon_path = ''
    if hasattr(sys, "_MEIPASS"):
        icon_path = os.path.join(sys._MEIPASS, "logo.ico")
    else:
        icon_path = "logo.ico"
    return icon_path
app = App(icon_path=icon_path(), converter=Converter())
app.mainloop()

# build command 
# pyinstaller --onefile --noconsole --name "ConvertApp" --icon=logo.ico --add-data "logo.ico;." main.py
