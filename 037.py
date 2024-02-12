import cv2
import numpy as np 
cap = cv2.VideoCapture('')

if (cap.isOpened() == False):
    print('Erro ao reproduzir o vídeo.')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Reproduzindo', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
