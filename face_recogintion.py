import face_recognition
import cv2
image = face_recognition.load_image_file("test1.jpg")
face_locations = face_recognition.face_locations(image)
print(face_locations)

img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

for face_location in face_locations:
    top, right, bottom, left = face_location
    cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 5)

cv2.imshow('Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
