# Mengimpor library yang dibutuhkan
import numpy as np
import imutils
import time
import cv2
import os
from datetime import datetime
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
from pushbullet import PushBullet

# Inisialisasi variabel counter, label dan tanggal
inc = 0
label = "Init"
intercept = [None, None]
frameIntercept = [None, None, None, None, None, None, None, None]
frameCount = 0

# Token untuk PushBullet
token = 'o.ddpV3vtIXKx3vRVPbeoDaI2rsyGzHAvx'

# Setting untuk PushBullet
p = PushBullet(token)
devices = p.getDevices()
contacts = p.getContacts()

# Fungsi untuk mendeteksi apakah memakai masker
def deteksi_masker(frame, faceNet, maskNet):
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224), (104.0, 177.0, 123.0))

    faceNet.setInput(blob)
    detections = faceNet.forward()

    faces = []
    locs = []
    preds = []

    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w-1, endX), min(h - 1, endY))

            face = frame[startY:endY, startX:endX]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224, 224))
            face = img_to_array(face)
            face = preprocess_input(face)

            faces.append(face)
            locs.append((startX, startY, endX, endY))

    if len(faces) > 0:
        faces = np.array(faces, dtype="float32")
        preds = maskNet.predict(faces, batch_size=32)
    
    return (locs, preds)

prototxtPath = r"face_detector\deploy.prototxt"
weightsPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

maskNet = load_model("mask_detector.model")

print("[PERHATIAN] Penggunaan masker akan segera dideteksi...")
vs = VideoStream(src=0).start()

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    (locs, preds) = deteksi_masker(frame, faceNet, maskNet)

    for (box, pred) in zip(locs, preds):
        (startX, startY, endX, endY) = box
        (mask, withoutMask) = pred

        label = "Mask" if mask > withoutMask else "No Mask"
        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

        frameCount += 1

        if (intercept[0] == "Mask") and (intercept[1] == "Mask"):
            inc = 0

        if label == "No Mask":
            if frameCount >2:
                if (startX >= frameIntercept[6]) or (endX <= frameIntercept[4]) or (startY >= frameIntercept[7]) or (endY <= frameIntercept[5]):
                    if (startX >= frameIntercept[2]) or (endX <= frameIntercept[0]) or (startY >= frameIntercept[3]) or (endY <= frameIntercept[1]):
                        inc = 0
            inc += 1
        # else:
        #     inc = 0

        intercept[0] = intercept[1]
        intercept[1] = label

        frameIntercept[0] = frameIntercept[4]
        frameIntercept[1] = frameIntercept[5]
        frameIntercept[2] = frameIntercept[6]
        frameIntercept[3] = frameIntercept[7]
        frameIntercept[4] = startX
        frameIntercept[5] = startY
        frameIntercept[6] = endX
        frameIntercept[7] = endY

        now = datetime.now()
        waktu = now.strftime("intruder\%d%m%Y_%H%M%S.png")
        waktuRapi = now.strftime("%H:%M:%S, %d %B %Y")

        print(inc)

        if (label == "No Mask") and (inc == 5):
            cv2.imwrite(waktu, frame)
            p.pushFile(devices[0]["iden"], waktu, "Ada pengunjung tanpa menggunakan masker!\nTerdeteksi pada jam " + waktuRapi, open(waktu, "rb"))

        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

        cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

    if label == "Kosong":
        inc = 0

    label = "Kosong"

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()