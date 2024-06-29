import cv2
import numpy as np
import matplotlib.pyplot as plt

def rectCounter(coutours):

    rectCon = []
    for i in coutours:
        area = cv2.contourArea(i)

        if area > 50:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True )

            if len(approx) == 4:
                rectCon.append(i)
    rectCon = sorted(rectCon, key=cv2.contourArea, reverse=True)

    return rectCon
    

def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True)
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True )

    return approx


def reorder(myPoints):

    myPoints = myPoints.reshape((4, 2)) # REMOVE EXTRA BRACKET
    # print(myPoints)
    myPointsNew = np.zeros((4, 1, 2), np.int32) # NEW MATRIX WITH ARRANGED POINTS
    add = myPoints.sum(1)
    # print(add)
    # print(np.argmax(add))
    myPointsNew[0] = myPoints[np.argmin(add)]  #[0,0]
    myPointsNew[3] =myPoints[np.argmax(add)]   #[w,h]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] =myPoints[np.argmin(diff)]  #[w,0]
    myPointsNew[2] = myPoints[np.argmax(diff)] #[h,0]

    return myPointsNew

def splitBoxes(img):
    rows = np.vsplit(img, 10)

    boxes = []
    for r in rows:
        cols = np.hsplit(r, 4)
        for box in cols:
            boxes.append(box)
            # plt.imshow(box)
            # plt.show()
    return boxes

def showAnswer(img, myIndex, grading, answer, questions, choices):
    # print(img.shape[1])
    secW = int(img.shape[1] / questions)
    secH = int(img.shape[0] / choices)
    # print(secH,secW)
    for x in range(0, questions):
        myAns = myIndex[x]
        cX = (myAns * secW) + secW // 2
        cY = (x * secH) + secH // 2
        cv2.circle(img, (cX, cY), 30, (0, 255, 0), cv2.FILLED)
    return img
# import base64
# from PIL import Image
# from io import BytesIO

# with open("n.png", "rb") as image_file:
#     data = base64.b64encode(image_file.read())
# print(data)
# im = Image.open(BytesIO(base64.b64decode(data)))
# im.save('image1.png', 'PNG')