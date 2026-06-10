from ultralytics import YOLO
import cv2
import pytesseract
import sys
import re

if len(sys.argv) < 2:
    print("Korištenje: python alpr_ocr.py putanja/do/slike.jpg")
    sys.exit(1)

image_path = sys.argv[1]
model_path = "runs/detect/train-2/weights/best.pt"

model = YOLO(model_path)
image = cv2.imread(image_path)

if image is None:
    print("Greška: slika nije pronađena.")
    sys.exit(1)

results = model(image)

for i, result in enumerate(results):
    for j, box in enumerate(result.boxes):
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])

        plate = image[y1:y2, x1:x2]

        gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        text = pytesseract.image_to_string(
            thresh,
            config="--psm 11"
        )

        text = text.strip()
        text = re.sub(r"[^A-Z0-9\-]", "", text)

        cv2.imwrite(f"plate_crop_{i}_{j}.jpg", plate)
        cv2.imwrite(f"plate_processed_{i}_{j}.jpg", thresh)

        print("Detekcija:", j + 1)
        print("Pouzdanost YOLO:", round(conf, 2))
        print("OCR rezultat:", text)
        print("Crop spremljen kao:", f"plate_crop_{i}_{j}.jpg")
        print("Obrađena slika spremljena kao:", f"plate_processed_{i}_{j}.jpg")
