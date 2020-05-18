from os import path

from pyforms.basewidget import BaseWidget
from pyforms.controls   import ControlFile
from pyforms.controls   import ControlButton
from pyforms            import settings;
settings.PYFORMS_STYLESHEET = 'style.css'
settings.PYFORMS_MAIN_WINDOW_ICON_PATH = 'icon.ico'
import imagetext
import latex

class UserInterface(BaseWidget):

    def __init__(self, *args, **kwargs):
        super().__init__('LateX')

        self._imagefile = ControlFile('Select image file')
        self._runbutton = ControlButton('Run')


        self._runbutton.value = self.__runEvent
        self._formset = [
            ('_imagefile'),
            ('_runbutton')
        ]

    def __runEvent(self):
        try:
            print("IMAGE FILE SELECTED: " + self._imagefile.value)
            
            ocrtext = imagetext.ocr(self._imagefile.value)
            latex.generatepdf(ocrtext)
            
            print("DONE")
        except:
            print("ERROR")
            
        pass
