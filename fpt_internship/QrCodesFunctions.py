import qrcode

def qr_generator(id):
    #Returns qr code qrcode.image.pil.PilImage

    #Parameters:
    #   id (str): The string which is to be encoded into qr code.

    #Returns:
    #   image(qrcode.image.pil.PilImage): The qrCode image with encoded string.

    qr = qrcode.QRCode(version=1,
                       # The version parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1,
                       # is a 21x21 matrix). Set to None and use the fit parameter when making the code to determine this automatically.
                       box_size=50,
                       # The box_size parameter controls how many pixels each “box” of the QR code is.
                       border=1)
                       # The border parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).                             #

    qr.add_data(id)
    # Adding data to the instance 'qr'

    img_object = qr.make_image(fill_color='red', back_color='white')
    # fill_color and back_color can change the background and the painting color of the QR, when using the default image factory.
    # Both parameters accept RGB color tuples.

    # to display qr code
    # img_object.show()

    return img_object


def save_qr_as_png(img_object, path_to_save, id):
    # Save the input image object into png format

    # Parameters:
    #   img (qrcode.image.pil.PilImage): The image.
    #   path_to_save (string): The string will be used as path to new png file.
    #   id (string): The string will be used in naming the file.


    if path_to_save == "":
        return "You didn't provide the path"

    img_object.save(path=path_to_save + "qr_id_" + id + ".png")