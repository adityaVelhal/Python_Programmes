import cv2
import numpy as np


def nothing(x):
    pass


def draw(event, x, y, flag, params):
    if m == 1:
        if event == cv2.EVENT_MOUSEMOVE:
            if flag == cv2.EVENT_LBUTTONDOWN:
                if len(coordinates) == 0:
                    coordinates.append((x, y))
        elif event == cv2.EVENT_LBUTTONUP:
            coordinates.append((x, y))
        if len(coordinates) == 2:
            cv2.setTrackbarPos("Circle", "Paint", 0)
            cv2.line(drawWindow, coordinates[0], coordinates[1], drawingColor, s, cv2.LINE_AA)
            coordinates.clear()
    elif c == 1:
        cv2.setTrackbarPos("Line", "Paint", 0)
        cv2.putText(drawWindow, "Double click to draw circle", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1,
                    cv2.LINE_AA)
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(drawWindow, (x, y), s, drawingColor, 5, cv2.LINE_AA)


drawWindow = np.zeros((500, 1080, 3), np.uint8)
drawWindow[:] = [255, 255, 255]
cv2.namedWindow("Paint", cv2.WINDOW_NORMAL)
drawingColor = (0, 0, 0)

coordinates = []

cv2.createTrackbar("Red", "Paint", 0, 255, nothing)
cv2.createTrackbar("Green", "Paint", 0, 255, nothing)
cv2.createTrackbar("Blue", "Paint", 0, 255, nothing)
cv2.createTrackbar("Line", "Paint", 0, 1, nothing)
cv2.createTrackbar("Circle", "Paint", 0, 1, nothing)
cv2.createTrackbar("Size/Radius", "Paint", 1, 200, nothing)
cv2.createTrackbar("Clear", "Paint", 0, 1, nothing)

cv2.setMouseCallback("Paint", draw)

while 1:
    cv2.imshow("Paint", drawWindow)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

    r = cv2.getTrackbarPos("Red", "Paint")
    g = cv2.getTrackbarPos("Green", "Paint")
    b = cv2.getTrackbarPos("Blue", "Paint")

    drawingColor = (b, g, r)

    m = cv2.getTrackbarPos("Line", "Paint")
    c = cv2.getTrackbarPos("Circle", "Paint")
    s = cv2.getTrackbarPos("Size/Radius", "Paint")
    clear = cv2.getTrackbarPos("Clear", "Paint")

    if clear == 1:
        drawWindow[:] = [255, 255, 255]
        cv2.setTrackbarPos("Clear", "Paint", 0)
    if m == 1:
        cv2.setTrackbarPos("Circle", "Paint", 0)
    if c == 1:
        cv2.setTrackbarPos("Line", "Paint", 0)

cv2.destroyAllWindows()
