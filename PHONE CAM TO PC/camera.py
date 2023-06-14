import requests
import numpy as np
import cv2

while True:
    response = requests.get("URL_TO_YOUR_IMAGE")  # Replace "URL_TO_YOUR_IMAGE" with the actual URL or path to the image
    image = np.array(bytearray(response.content), dtype=np.uint8)
    render = cv2.imdecode(image, -1)
    cv2.imshow("frame", render)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
