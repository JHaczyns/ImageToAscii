import cv2

img = cv2.imread("source.png", cv2.IMREAD_REDUCED_GRAYSCALE_2)
# img=cv2.resize(img,(0,0), fx=1.3, fy=1) #for resizing
imagelist = []
t = open('output.txt', 'w')
cv2.waitKey(0)
tab = [' ', '.', ':', '-', '+', '+', '*', '#', '%', '@']  # Character representation of grey scale
a = ''
for i in img:
    w = ""
    for x in i:
        if (x > -1 and x < 10):
            a = tab[9]
        elif (x > 10 and x < 30):
            a = tab[8]
        elif (x > 30 and x < 60):
            a = tab[7]
        elif (x > 60 and x < 90):
            a = tab[6]
        elif (x > 90 and x < 120):
            a = tab[5]
        elif (x > 120 and x < 150):
            a = tab[4]
        elif (x > 150 and x < 180):
            a = tab[3]
        elif (x > 180 and x < 210):
            a = tab[2]
        elif (x > 210 and x < 230):
            a = tab[1]
        elif (x > 230 and x < 260):
            a = tab[0]
        w = w + a
    t.write(w + "\n")
t.close()
