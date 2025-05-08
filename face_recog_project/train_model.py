import cv2
import os

dataset_dir = 'dataset'

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

for person_name in os.listdir(dataset_dir):
    person_folder = os.path.join(dataset_dir, person_name)

    for img_name in os.listdir(person_folder):
        img_path = os.path.join(person_folder, img_name)
        print(f'[INFO] Processing {img_path}...')

        image = cv2.imread(img_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Face', image)
        cv2.waitKey(500)  # show for 500ms
cv2.destroyAllWindows()
