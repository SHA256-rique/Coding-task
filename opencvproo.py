import cv2


cap = cv2.VideoCapture(0)

cv2.namedWindow("Original Image")
cv2.namedWindow("Grayscale Image")
cv2.namedWindow("Edge Detection")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    blur = cv2.GaussianBlur(gray, (7, 7), 0)

    
    edges = cv2.Canny(blur, 50, 150)

    
    cv2.imshow("Original Image", frame)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Edge Detection", edges)

    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
