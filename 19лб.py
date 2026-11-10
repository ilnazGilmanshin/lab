import os
import cv2
import numpy as np
from imutils import paths
from IPython.display import Image
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def extract_histogram(image, bins=(8, 8, 8)):
    hist = cv2.calcHist([image], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()

imagePaths = sorted(list(paths.list_images('train19')))
trainData = []
labels = []

for (i, imagePath) in enumerate(imagePaths):
    image = cv2.imread(imagePath, 1)
    label = imagePath.split(os.path.sep)[-1].split(".")[0]
    hist = extract_histogram(image)
    trainData.append(hist)
    labels.append(label)

trainData = np.array(trainData)
Y = np.array([1 if x == 'cat' else 0 for x in labels])

svm = SVC(C=1.19, random_state=288)
svm.fit(trainData, Y)

tree = DecisionTreeClassifier(
    criterion='entropy', 
    min_samples_leaf=10, 
    max_leaf_nodes=20, 
    random_state=288
)
bagging = BaggingClassifier(
    estimator=tree, 
    n_estimators=21, 
    random_state=288
)
bagging.fit(trainData, Y)

forest = RandomForestClassifier(
    n_estimators=21, 
    criterion='entropy', 
    min_samples_leaf=10, 
    max_leaf_nodes=20, 
    random_state=288
)
forest.fit(trainData, Y)

lr = LogisticRegression(solver='lbfgs', random_state=288)

base_estimators = [
    ('SVM', svm), 
    ('Bagging DT', bagging), 
    ('RandomForest', forest)
]

sclf = StackingClassifier(
    estimators=base_estimators, 
    final_estimator=lr, 
    cv=2
)
sclf.fit(trainData, Y)

accuracy = sclf.score(trainData, Y)
print(f"Доля правильной классификации (Accuracy): {accuracy:.2f}")

test_images = [
    'dog.1025.jpg', 
    'cat.1027.jpg', 
    'cat.1006.jpg', 
    'cat.1002.jpg'
]

print("Результаты предсказания (вероятность класса 1 - cat):")
for img_name in test_images:
    img_path = os.path.join('test', img_name)
    try:
        singleImage = cv2.imread(img_path)
        if singleImage is None:
            print(f"Файл {img_name} не найден по пути {img_path}")
            continue
            
        histt = extract_histogram(singleImage)
        histt2 = histt.reshape(1, -1)
        
        proba = sclf.predict_proba(histt2)
        
        print(f"{img_name}: {proba[0][1]:.3f}")
        
    except Exception as e:
        print(f"Ошибка при обработке {img_name}: {e}")