import cv2


# Загрузка классификатора для детектирования лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("Ошибка: не удалось загрузить классификатор Haar Cascade.")
    exit()

# Загрузка изображения
image = cv2.imread('samplee.jpg')
if image is None:
    print("Ошибка: изображение не найдено по указанному пути.")
    exit()

# Преобразование изображения в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Детектирование лиц
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Печать количества найденных лиц
print(f"Обнаружено лиц: {len(faces)}")

# Опционально: рисование рамок вокруг лиц и отображение результата
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Сохранение изображения с рамками вокруг лиц
output_path = 'output_detected_faces.jpg'
cv2.imwrite(output_path, image)
print(f'Результат сохранен в {output_path}')


