import cv2
import cvzone
from object_detector import HomogeneousBgDetector
import numpy as np
import Funciones_auxiliares

# Loading Aruco marker detector
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

classifier = cvzone.Classifier('C:/Alejandro/Universidad/CVProject/Model/keras_model.h5', 'C:/Alejandro/Universidad/CVProject/Model/labels.txt')

while True:

    _, img = capture.read()

    # Aruco marker detection
    corners, ids, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)
    dist = 0.0

    for c in corners:
        corners_list = c.reshape((4, 2))
        topLeft, topRight, bottomRight, bottomLeft = corners_list

        pt1 = topLeft
        pt2 = topRight

        dist = np.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
        print('Lado del cuadrado(pxls): ', dist)

        print('Top left corner: ', topLeft)
        print('Top left corner: ', topRight)
        print('Top left corner: ', bottomRight)
        print('Top left corner: ', bottomLeft)

    # Draw corners
    int_corners = np.int0(corners)
    cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

    aruco_perimeter = dist*4
    print('Perimetro del cuadrado: ', aruco_perimeter)

    # Pixel to cm ratio
    pixel2cm_ratio = aruco_perimeter/20
    print('Ratio: ', pixel2cm_ratio)

    # Object prediction
    predictions = classifier.getPrediction(img, scale=1, color=(74, 162, 255))

    # Load Object Detector
    detector = HomogeneousBgDetector()

    contours = detector.detect_objects(img)
    
    # Draw object contours
    for cnt in contours:

        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect

        # Convertimos las medidas en cm
        width = Funciones_auxiliares.pixel2cm(pixel2cm_ratio, w)
        height = Funciones_auxiliares.pixel2cm(pixel2cm_ratio, h)

        box = cv2.boxPoints(rect) # Encuentra los cuatro vértices del rectángulo
        box = np.int0(box)

        cv2.polylines(img, [box], True, (255, 0, 0), 2)
        cv2.putText(img, "W: {} cm H: {} cm".format(round(width, 1), round(height, 1)), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (74, 162, 255), 2)

        # print(box)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()