import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import time
import qrcode

class QrCode:
    def __init__(self,id):
        self.id = id
        self.version = 1
        self.box_size = 50
        self.border = 1
        self.fill_color = 'blue'
        self.back_color = 'white'
        self.qr_code = self.create_qr_with_id()

    def create_qr_with_id(self):
        qr = qrcode.QRCode(version=self.version,
                           box_size=self.box_size,
                           border=self.border)
        qr.add_data(self.id)
        img_object = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
        return img_object

    def save_qr_as_png(self):
        self.qr_code.save("qr_id_" + str(self.id) + ".png")
        return ("qr_id_" + str(self.id) + ".png")

    def save_qr_into_directory(self):
        self.qr_code.save("QRcodes/" + str(self.id) + ".png")
        return ("QRcodes/" + str(self.id) + ".png")

    def get_qr_code(self):
        return self.qr_code

#define my differnet screens
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class qr_gui_creating(GridLayout):
    def create_qr_code_with_id_textinput(self):
        code = QrCode(self.id_input.text)
        self.image.source = code.save_qr_into_directory()

class qr_scanner(GridLayout):
    pass

class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('main_gui.kv')

class App(App):
    def build(self):
        return kv

if __name__ == '__main__':
    App().run()