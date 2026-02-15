import cv2

# Load image
img = cv2.imread("image1.png")

# Check if image loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(gray, (7,7), 0)

# Edge detection
edges = cv2.Canny(blur, 50, 150)

# Show results
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
