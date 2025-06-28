import os
import cv2 as cv

img_path = "C:/Users/ASUS/pythonProject/machin_learning_20"
labels = ["paint_VideoCapture"]
num_img = 3

for label in labels:
    label_dir = os.path.join(img_path, label)
    os.makedirs(label_dir, exist_ok=True)
    cap = cv.VideoCapture(0)
    print("press < S > ")

    img_count = 0
    while img_count < num_img:
        ret, frame = cap.read()
        cv.imshow("Live Webcam", frame)

        key = cv.waitKey(1) & 0xFF
        if key == ord('s'):
            for i in range(3, 0, -1):
                ret, frame = cap.read()
                cv.putText(frame, str(i), (250, 250), cv.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 5, cv.LINE_AA)
                cv.imshow("Live Webcam", frame)

                cv.waitKey(1000)
            ret, frame = cap.read()
            gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            inverted_gray_img = 255 - gray_img
            blur_inverted_gray_img = cv.GaussianBlur(inverted_gray_img, (21, 21), 0)
            inverted_blur = 255 - blur_inverted_gray_img
            sketch = cv.divide(gray_img, inverted_blur, scale=256)

            imgName = os.path.join(label_dir, f"{label}_{img_count}.jpg")
            cv.imwrite(imgName, sketch)

            img_count += 1

        if key == 27:
            break

    cap.release()
    cv.destroyAllWindows()

print("done")



