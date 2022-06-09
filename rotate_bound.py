#import packages
import sys
import math
import cv2
import cv2 as cv
import numpy as np

def rotate_bound(image, angle, line1, line2):
    (h, w) = image.shape[:2]
    #cv.circle(image,(h/2,w/2), radius=0, color=(0, 0, 255), thickness=-1)



    delx1 = line1[2] - line1[0]
    delx2 = line2[2] - line2[0]
    dely1 = line1[3] - line1[1]
    dely2 = line2[3] - line1[1]

    y10 = line1[1]
    y20 = line2[1]

    if (delx1 != 0 and delx2 != 0):#brak prostych pionowych
        print("dziala0")



       # a1 = dely1 / delx1
       # a2 = dely2 / delx2
       # b1 = line1[1] - line1[0] * a1
       # b2 = line2[1] - line2[0] * a2

     #   y10 = line1[1]
     #   y20 = line2[1]
     #   cX=(dely2*delx1*y20-dely1*delx2*y10+y10*delx2*delx1-y20*delx2*delx1)/(delx1*dely2-dely1*delx2)#(dely2*line2[0]/delx2-dely1*line1[0]/delx1+line1[1]-line2[1])/(dely2/delx2-dely1/delx1)
     #   cY=(cX-line2[0])*dely2/delx2+y20
      #  cX = (b2 - b1) / (a1 - a2)
      #  cY = a1 * cX + b1





        #cX=(dely2*delx1*line2[0]-dely1*delx2*line1[0]+line1[1]*delx2*delx1-line2[1]*delx2*delx1)/(delx1*dely2-dely1*delx2)#(dely2*line2[0]/delx2-dely1*line1[0]/delx1+line1[1]-line2[1])/(dely2/delx2-dely1/delx1)
       # cY=(cX-line2[0])*dely2/delx2+line2[1]
        #print(cX,"  ",w/2,"  ",h/2,"  ",cY)
        cX=round((line1[0]+line1[2]+line2[0]+line2[2])/4)
        cY=round((line1[1]+line1[3]+line2[1]+line2[3])/4)
       # if(dely2>dely1):
         #   h=dely2
        #    w=delx1
       # else:
        #    h=dely1
        #    w=delx2
        #####(w/2,h/2)#(255/2,255/2)#// ((y20 - y10) / ((dely1 / delx1) - (dely2 / delx2)),  (delx2 * dely1)*(y20 - y10) / (( (delx2 * dely1) - (delx1 * dely2) ))+y10)
        M = cv2.getRotationMatrix2D((round(cX), round(cY)), -angle, 1.0)#rotation matrix around point, angle,

        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])

        # compute the new bounding dimensions of the image
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))

        # adjust the rotation matrix to take into account translation
        M[0, 2] += (nW / 2) - cX
        M[1, 2] += (nH / 2) - cY
        # perform the actual rotation and return the image

        return cv2.warpAffine(image, M, (nW, nH))

    else:
        if (delx2 != 0):#pierwsza prosta jest pionowa
            print("dziala1")

            (cX, cY) = ((line1[0] + line1[2]) / 2, dely2 / delx2 * (line1[0] + line1[2]) / 2 + line2[1])
            # grab the rotation matrix (applying the negative of the
            # angle to rotate clockwise), then grab the sine and cosine
            # (i.e., the rotation components of the matrix)

            M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])
            # compute the new bounding dimensions of the image
            nW = int((h * sin) + (w * cos))
            nH = int((h * cos) + (w * sin))
            # adjust the rotation matrix to take into account translation
            M[0, 2] += (nW / 2) - cX
            M[1, 2] += (nH / 2) - cY
            # perform the actual rotation and return the image
            return cv2.warpAffine(image, M, (nW, nH))
        else:#druga prosta jest pionowa
            print("dziala2222")
            (cX, cY) = ((line2[0] + line2[2]) / 2, dely1 / delx1 * (line2[0] + line2[2]) / 2 + line1[1])
            # grab the rotation matrix (applying the negative of the
            # angle to rotate clockwise), then grab the sine and cosine
            # (i.e., the rotation components of the matrix)
            M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])
            # compute the new bounding dimensions of the image
            nW = int((h * sin) + (w * cos))
            nH = int((h * cos) + (w * sin))
            # adjust the rotation matrix to take into account translation
            M[0, 2] += (nW / 2) - cX
            M[1, 2] += (nH / 2) - cY
            # perform the actual rotation and return the image
            return cv2.warpAffine(image, M, (nW, nH))

            # print("jednak zero")
