from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.lang import Builder

import numpy as np
from pyzbar.pyzbar import decode

import cv2

kv = Builder.load_file('skuska.kv')
#
# class BoxLayout(BoxLayout):
#     pass


class CamApp(App):
    def build(self):

        self.img1=Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)

        # opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0 / 33.0)

        return layout

    def update(self, dt):

        # display image from cam in opencv window
        ret, frame = self.capture.read()

        cv2.imshow("CV2 Image", frame)
        self.decoder(frame)
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer.
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1

    def decoder(ret, image):
        gray_img = cv2.cvtColor(image, 0)
        barcode = decode(gray_img)

        for obj in barcode:
            points = obj.polygon
            (x, y, w, h) = obj.rect
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)

            barcodeData = obj.data.decode("utf-8")
            barcodeType = obj.type
            string = "Coordinates: " + str(x) + ", " + str(y) + "  | ""Data: " + str(barcodeData)

            cv2.putText(image, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            #print("QRcode data: " + str(barcodeData) + " | Coordinates: " + str(x) + " " + str(y))


if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()