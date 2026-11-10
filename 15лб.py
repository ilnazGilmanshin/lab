from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import train_test_split
from imutils import paths
import numpy as np
import cv2
import os

def extract_histogram(image, bins=(8, 8, 8)):
    hist = cv2.calcHist([image], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()

train_dir = 'train15' 
imagePaths = sorted(list(paths.list_images(train_dir))) 
data = []
labels = []

for (i, imagePath) in enumerate(imagePaths):
    image = cv2.imread(imagePath, 1)
    if image is None:
        continue 

    filename = imagePath.split(os.path.sep)[-1]
    label = filename.split(".")[0] 
    
    hist = extract_histogram(image)
    data.append(hist)
    labels.append(label)

le = LabelEncoder()
labels = le.fit_transform(labels)

(trainData, testData, trainLabels, testLabels) = train_test_split(
    np.array(data), labels, test_size=0.25, random_state=2)

model = LinearSVC(random_state=2, C=0.94, max_iter=10000)
model.fit(trainData, trainLabels)

predictions = model.predict(testData)

print("МАТРИЦА ОШИБОК")
print(classification_report(testLabels, predictions, target_names=le.classes_))

macro_f1 = f1_score(testLabels, predictions, average='macro')
print(f"Среднее значение метрик (Macro-F1): {macro_f1:.3f}")

coefs = model.coef_[0]

print("\nКОЭФФИЦИЕНТЫ ГИПЕРПЛОСКОСТИ")
print(f"θ_130: {coefs[129]:.2f}")
print(f"θ_131: {coefs[130]:.2f}") 
print(f"θ_132: {coefs[131]:.2f}") 

print("\nПРЕДСКАЗАНИЕ ДЛЯ ИЗОБРАЖЕНИЙ")


target_files = ['dog.133.jpg', 'cat.130.jpg', 'dog.106.jpg', 'cat.124.jpg']

for filename in target_files:
    img_path = os.path.join(train_dir, filename)
    if os.path.exists(img_path):
        singleImage = cv2.imread(img_path)
        histt = extract_histogram(singleImage)
        histt2 = histt.reshape(1, -1)
        prediction = model.predict(histt2)
        pred_class = prediction[0]
        class_name = le.inverse_transform([pred_class])[0]
        
        print(f"Изображение: {filename:12} - класс: {pred_class} ({class_name})")