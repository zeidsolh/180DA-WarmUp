import numpy as np
import cv2


cap = cv2.VideoCapture(0)
n_clusters = 1
cap.set(3, 640)
cap.set(4, 420)

while True:
    status, image = cap.read()
    cropped_image = image[100:450, 250:450]
    cv2.rectangle(image, (250, 100), (450,450), (255, 0, 0), 2)
    if not status:
        break

    # to reduce complexity resize the image
    data = cv2.resize(cropped_image, (100, 100)).reshape(-1, 3)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, labels, centers = cv2.kmeans(data.astype(np.float32), n_clusters, None, criteria, 10, flags)

    cluster_sizes = np.bincount(labels.flatten())

    palette = []
    for cluster_idx in np.argsort(-cluster_sizes):
        palette.append(np.full((cropped_image.shape[0], cropped_image.shape[1], 3), fill_value=centers[cluster_idx].astype(int), dtype=np.uint8))
    palette = np.hstack(palette)

    sf = image.shape[1] / palette.shape[1]
    out = np.vstack([image, cv2.resize(palette, (0, 0), fx=sf, fy=sf)])

    cv2.imshow("dominant_colors", out)
    cv2.waitKey(1)

