import numpy as np
import base64
import cv2

imgdata = base64.b64decode(json_file['imageData'])
img = np.frombuffer(imgdata, np.uint8)
img = cv2.imdecode(img, cv2.IMREAD_COLOR)
