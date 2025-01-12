# OrderedSetsAlgorithms
### МЛиТА Альтернативный экзамен по теме "Алгоритмы нахождения числовых характеристик конечных упорядоченных множеств"
Отчет с теорией по теме и самим алгоритмам можно посмотреть [тут](https://docs.google.com/document/d/1-QENwO-fG32NBz_HnemdY_RkaK82Tclz/edit?usp=share_link&ouid=113213168064534822284&rtpof=true&sd=true)

### Установка проекта:

1. Склонируйте репозиторий с помощью `git clone` или, находясь в main ветке, скачайте проект архивом через `Code → Download ZIP`.
2. Создайте виртуальное окружение в проекте: 
   ```bash
   # Для Windows
   python -m venv venv
   
   # Для Linux и macOS
   python3 -m venv venv
3. Активируйте созданное виртуальное окружение:
   ```bash
   # Для Windows
   venv\Scripts\activate
   
   # Для Linux и macOS
   source venv/bin/activate 
   
4. Скачайте зависимости:
   ```bash
   pip install -r requirements.txt
   
5. Запустите проект:
   ```bash
    # Для Windows
    python main.py
    
    # Для Linux и macOS
    python3 main.py
   
Далее следуйте инструкции и вводите номера алгоритма и графа. С диаграммами графов можно ознакомиться в папке `data → graphs`.
В результате работы программы будет создан файл `result.png`. Если вы запускали 1 алгоритм, там будет сохранен исходный граф с подписанными высотами элементов.
Если вы запускали 2 алгоритм - дерево матриц, где в качестве узлов выступают названия матриц.

Получившийся результат и изначальная диаграмма у.м. сохраняются в папку `result`, которая будет создана автоматически.

### Пример запуска программы:
<img width="945" alt="image" src="https://github.com/user-attachments/assets/304b808d-04e9-425c-8fb4-31ee1acddfc4" />


