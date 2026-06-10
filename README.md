# Automatsko prepoznavanje registarskih oznaka – usporedba detekcije i OCR pristupa

Seminarski rad iz kolegija Računalni vid.

## Opis projekta

Cilj projekta bio je implementirati sustav za automatsko prepoznavanje registarskih oznaka (ALPR).

Sustav se sastoji od:

* YOLOv8n modela za detekciju registarskih oznaka
* Tesseract OCR sustava za prepoznavanje znakova

Za treniranje modela korišten je Kaggle ALPR Dataset.

## Korištene tehnologije

* Python 3
* Ultralytics YOLOv8
* OpenCV
* Tesseract OCR
* NVIDIA GeForce GTX 1650

## Struktura projekta

* `alpr_ocr.py` – detekcija registarske oznake i OCR
* `data.yaml` – konfiguracija dataseta
* `best.pt` – istrenirani YOLO model
* `seminar.pdf` – završni seminarski rad

## Treniranje modela

```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=5 imgsz=640
```

## Pokretanje detekcije i OCR-a

```bash
python alpr_ocr.py putanja_do_slike.jpg
```

## Rezultati

Rezultati nakon 1 epohe:

* Precision: 95.6 %
* Recall: 87.9 %
* mAP50: 92.9 %
* mAP50-95: 56.7 %

Rezultati nakon 5 epoha:

* Precision: 97.6 %
* Recall: 94.6 %
* mAP50: 97.0 %
* mAP50-95: 65.3 %

Autor: Leon Nikolas Kerdić
Sveučilište u Slavonskom Brodu
2026.
