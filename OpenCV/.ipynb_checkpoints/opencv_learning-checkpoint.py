import cv2
# img = cv2.imread("elephant.jpg", -1)
# img = cv2.arrowedLine(img, (0,0), (400,400), (255,0,0),10)
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# cv2.imwrite('result.png', img)
faceCascade = cv2.CascadeClassifier("cascade.xml")
# eyeCascade = cv2.CascadeClassifier("glasses.xml")
# noseCasecade = cv2.CascadeClassifier("nose.xml")
# mouthCascade = cv2.CascadeClassifier("mouth.xml")

def generateDataset(img, id, img_id):
    cv2.imwrite("data/pic."+str(id)+"."+str(img_id)+".jpg", img)

def drawSquare(img, classifier, scaleFactor, minNeighbors, color, text):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
    coords = []
    for (x,y,w,h) in features:
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1)
        coords = [x,y,w,h]
    return img, coords

def detect(img,imgID):
    img, coords = drawSquare(img=img, classifier=faceCascade, scaleFactor=1.1, minNeighbors=10, color=(255,0,0), text="face")
    # img, coords = drawSquare(img, eyeCascade, 1.1, 12, (0,255,0), "eye")
    # img, coords = drawSquare(img, noseCasecade, 1.1, 15, (0,0,255), "nose")
    # img, coords = drawSquare(img, mouthCascade, 1.3, 30, (100,100,100), "mouth")
    
    if len(coords) == 4: #Found face
        id = 1
        result = img[coords[1]:coords[1]+coords[3], coords[0]:coords[0]+coords[2]]
        generateDataset(result, id, imgID)
    return img
imgID = 0
cap = cv2.VideoCapture(-1)
while True:
    ret, frame = cap.read()
    frame = detect(frame, imgID)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gu Lhor Jud', frame)
    imgID += 1
    if (cv2.waitKey(1) & 0xFF==ord("q")):
        break

cap.release()
cv2.destroyAllWindows()

