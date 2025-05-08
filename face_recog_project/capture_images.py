import cv2
import os

person_name = 'Nandha'  # <- change this each time
save_dir = f'dataset/{person_name}'
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('Press S to Save | Q to Quit', frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        img_path = os.path.join(save_dir, f'{count}.jpg')
        cv2.imwrite(img_path, frame)
        print(f'Saved {img_path}')
        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
