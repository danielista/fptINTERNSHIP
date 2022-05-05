import cv2
import numpy

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    # basic image edits
    blur = cv2.medianBlur(img, 35)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 30, 150, 3)
    dilated = cv2.dilate(gray, (1, 1), iterations=2)

    # Advance image editing methods
    # applyied two types of tresholdnig binary and otsu
    ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # noise removal
    kernel = numpy.ones((3, 3), numpy.uint8)

    # Finding sure foreground area
    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel, iterations=2)

    # sure background area = finds the point of our looking object, where we are sure
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Finding unknown region (neistoty)
    sure_fg = numpy.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1

    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0
    markers = cv2.watershed(img, markers)

    # final step
    contours, hierarchy = cv2.findContours(markers.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

    cv2.imshow("dilated", dilated)
    cv2.imshow("blur", blur)
    cv2.imshow("canny", canny)
    cv2.imshow("predzadie", sure_fg)
    cv2.imshow("pozadie", sure_bg)
    cv2.imshow("treshold", threshold)

    cv2.imshow("live transmission", img)
    key = cv2.waitKey(5)

    # to end the application press 'q'
    if key == ord('q'):
        break

    # to count the number of countours press 'a'
    elif key == ord('a'):
        cow = len(contours)
        print(cow)

cv2.destroyAllWindows()