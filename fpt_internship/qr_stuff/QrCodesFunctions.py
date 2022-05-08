import qrcode

class RealObject:
    def __init__(self):
        None

    def __init__(self,name):
        self.name = name

class QrCode:
    def __init__(self,id):
        self.id = id
        self.qr_code = self.create_qr_with_id()

    def create_qr_with_id(self):
        qr = qrcode.QRCode(version=1,
                           box_size=50,
                           border=1)
        qr.add_data(self.id)
        img_object = qr.make_image(fill_color='red', back_color='white')
        return img_object

    def save_qr_as_png(self):
        self.qr_code.save("qr_id_" + str(self.id) + ".png")

    def get_qr_code(self):
        return self.qr_code

    def save_qr_code(self, path):
        #self.get_qr_code().save(path)
        None

    def save_qr_code(self):
        # uloži defaultne
        None

code = QrCode(33)
#code.save_qr_as_png()
print(code.id)


class LicensePlateObject(PhysicalObject):
    def __init__(self):
        None

# def rounded_qr_code(data_to_be_encoded):
#     # The error_correction parameter controls the error correction used for the QR Code.
#     qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
#     qr.add_data(data_to_be_encoded)