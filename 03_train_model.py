## Train the model
!pip install ultralytics --quiet
from ultralytics import YOLO

# تحميل موديل YOLOv8 جاهز للتدريب
model = YOLO("yolov8n.pt")

# تدريب الموديل على البيانات المقسمة
results = model.train(
    data='/content/SeljukDetection/seljuk_data_split.yaml',
    epochs=20,
    imgsz=640,
    batch=16,
    device="cuda",
    name="seljuk_detection_gpu"
)

print("Training finished on GPU!")
