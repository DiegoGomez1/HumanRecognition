import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression

human_detection = cv2.HOGDescriptor()
human_detection.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def image_detection(path, output_path):
    image = cv2.imread(path)
    if image is None:
        print(f"Error: Unable to load image at {path}")
        return

    image = imutils.resize(image, width=min(400, image.shape[1]))

    deep_copy = image.copy()

    # analysis of image
    (boxes, weights) = human_detection.detectMultiScale(image, winStride=(4, 4),
                                                        padding=(8, 8), scale=1.05)

    # bounds for detecting humans
    for (x, y, w, h) in boxes:
        cv2.rectangle(deep_copy, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # verifying the results made by the human recognition
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    select = non_max_suppression(boxes, probs=None, overlapThresh=0.65)

    # final recognition
    for (a, b, c, d) in select:
        cv2.rectangle(image, (a, b), (c, d), (0, 255, 0), 2)

    print(f"Final detections after NMS: {len(select)}")  # Debug print

    # Save the final image
    cv2.imwrite(output_path, image)
    print(f"Processed image saved as {output_path}")

    return len(select)



if __name__ == "__main__":
    image_detection('4bd9d6764ad7c49654f02ed2078e84c3_XL.jpg', 'Processed_Photo1.jpg')
