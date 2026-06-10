# Automatsko prepoznavanje registarskih oznaka – usporedba detekcije i OCR pristupa

Seminarski rad izrađen u sklopu kolegija **Računalni vid** na Sveučilištu u Slavonskom Brodu.

Autor: **Leon Nikolas Kerdić**

## Opis projekta

Cilj projekta bio je implementirati sustav za automatsko prepoznavanje registarskih oznaka (Automatic License Plate Recognition – ALPR).

Sustav se sastoji od dvije glavne komponente:

* **YOLOv8n** model za detekciju registarskih oznaka
* **Tesseract OCR** sustav za prepoznavanje znakova na registarskim oznakama

Nakon detekcije registarske oznake izdvojeno je područje oznake, provedena je osnovna obrada slike te je OCR sustav pokušao prepoznati tekst registarske oznake.

## Korištene tehnologije

* Python 3
* Ultralytics YOLOv8
* OpenCV
* Tesseract OCR
* NVIDIA GeForce GTX 1650

## Dataset

Za treniranje modela korišten je **Kaggle ALPR Dataset**.

Dataset sadrži:

* 21 173 slike za treniranje
* 2 046 slika za validaciju
* 1 019 slika za testiranje

Ukupno: **24 238 slika**

## Struktura repozitorija

```text
.
├── README.md
├── data.yaml
├── alpr_ocr.py
├── Automatsko prepoznavanje registarskih oznaka – usporedba detekcije i OCR pristupa.pdf
│
├── model/
│   └── best.pt
│
└── results/
    ├── results.png
    ├── detection_example.jpg
    └── plate_processed.jpg
```

## Treniranje modela

Model je treniran korištenjem sljedeće naredbe:

```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=5 imgsz=640
```

## Pokretanje OCR sustava

Za pokretanje detekcije registarske oznake i OCR prepoznavanja:

```bash
python alpr_ocr.py putanja_do_slike.jpg
```

## Rezultati

### Rezultati nakon 1 epohe

| Metrika   | Vrijednost |
| --------- | ---------- |
| Precision | 95.6 %     |
| Recall    | 87.9 %     |
| mAP50     | 92.9 %     |
| mAP50-95  | 56.7 %     |

### Rezultati nakon 5 epoha

| Metrika   | Vrijednost |
| --------- | ---------- |
| Precision | 97.6 %     |
| Recall    | 94.6 %     |
| mAP50     | 97.0 %     |
| mAP50-95  | 65.3 %     |

Rezultati pokazuju da je model uspješno naučio detektirati registarske oznake te je nakon pet epoha ostvario vrlo visoku preciznost detekcije.

## Priloženi rezultati

* `results.png` – graf treniranja modela
* `detection_example.jpg` – primjer uspješne detekcije registarske oznake
* `plate_processed.jpg` – primjer izdvojene i obrađene registarske oznake za OCR
* `best.pt` – istrenirani YOLOv8n model

## Literatura

Literatura korištena u radu navedena je unutar priloženog PDF dokumenta seminarskog rada.
