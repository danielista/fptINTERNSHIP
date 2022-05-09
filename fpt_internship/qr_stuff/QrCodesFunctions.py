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

    def save_qr_into_directory(self):
        self.qr_code.save("QRcodes/" + str(self.id) + ".png")

    def get_qr_code(self):
        return self.qr_code

## testing here ##
code = QrCode(44)
code.save_qr_into_directory()
print(code.id)

class RealObject:
    def __init__(self):
        None

    def __init__(self,name):
        self.name = name


class LicensePlateObject():
     def __init__(self):
         None
