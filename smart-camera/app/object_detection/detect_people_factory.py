import os
from object_detection.detect_people import DetectPeople
from object_detection.download_model import download_model


def detect_people_factory() -> DetectPeople:
    tflite_file, labels_file = download_model()
    threshold = float(os.getenv('MODEL_THRESHOLD', 0.6))

    return DetectPeople(tflite_file, labels_file, threshold)
