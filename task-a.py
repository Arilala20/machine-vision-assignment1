import cv2

img = cv2.imread("image1.png")

if img is None:
    print("Error: Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (7,7), 0)

edges = cv2.Canny(blur, 50, 150)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
