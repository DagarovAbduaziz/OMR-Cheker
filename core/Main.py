import cv2
import numpy as np
from .utils import rectCounter, reorder, getCornerPoints, splitBoxes,showAnswer
def cheking(image, answer ):

    path = image
    width = 700
    heigh = 700
    questions = 20
    choices = 4

    img = cv2.imread(path)

    img = cv2.resize(img,(width, heigh))
    imgcountours = img.copy()
    imgbiggestcount= img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    imgCanny = cv2.Canny(imgBlur, 5, 50 )
    # cv2.imwrite('view_1.png', imgCanny )


    countours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgcountours, countours, -1, (0,255,0), 10)

######
    # cv2.imwrite('view_2.png', imgcountours )
#####

    rectCon = rectCounter(countours)
    grading = []

    for k in range(questions // 10):
        questions1 = questions // 2

        counter = getCornerPoints(rectCon[k])
        # print(biggestcounter.shape)




        if counter.size != 0:

            cv2.drawContours(imgbiggestcount, counter, -1, (0,255,0), 30)

            # cv2.imwrite('view_3.png', imgbiggestcount )


            counter=reorder(counter) # REORDER FOR WARPING


            pts1 = np.float32(counter) # PREPARE POINTS FOR WARP
            pts2 = np.float32([[0, 0],[width, 0], [0, heigh],[width, heigh]]) # PREPARE POINTS FOR WARP
            matrix = cv2.getPerspectiveTransform(pts1, pts2) # GET TRANSFORMATION MATRIX
            imgWarpColored = cv2.warpPerspective(img, matrix, (width, heigh)) # APPLY WARP PERSPECTIVE
            # cv2.imwrite(f'squere_{k+1}/view_4.png', imgWarpColored)
            #Apply threshold
            imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
            imgTrash  = cv2.threshold(imgWarpGray, 150, 255, cv2.THRESH_BINARY_INV)[1]
            # cv2.imwrite(f'squere_{k+1}/view_5.png', imgTrash)

            boxes = splitBoxes(imgTrash)
            #print(cv2.countNonZero(boxes[1]), cv2.countNonZero(boxes[2]))


            # Getting No Zero Pixel values of each
            myPixesVal = np.zeros((questions1, choices))
            #print(myPixesVal)
            countC = 0
            countR = 0
            for image in boxes:
                TotalPixel = cv2.countNonZero(image)
                myPixesVal[countR][countC] = TotalPixel
                countC += 1
                if countC == choices:
                    countR += 1
                    countC = 0
            # print(myPixesVal, ' \n')

            myIndex = []
            for x in range(0, questions1):
                arr = myPixesVal[x]
                myindexValu = np.where(arr == np.amax(arr))
                # print(sum(arr) / len(arr), np.amax(arr) )
                if 5000 > np.amax(arr):
                    myIndex.append(None)
                else:
                    myIndex.append(myindexValu[0][0])
            # print(myIndex)


            for i in range(0, questions1):
                if myIndex[i] == answer[i + 10 * k ]:
                    grading.append(1)
                elif myIndex[i] == None:
                    grading.append(None)
                else:
                    grading.append(0)

    return grading


    
    # Displaying answer
    # imgResult = imgWarpColored.copy()
    # imgResult = ut.showAnswer(imgResult, myIndex, grading, answer, questions, choices)
    # cv2.imwrite('result.png', imgResult)

# # plt.imshow(img)
# plt.show()



