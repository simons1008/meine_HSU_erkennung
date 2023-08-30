# Meine HSU-Erkennung
Auf dem PC wird durch "Supervised Machine Learning" ein Klassifikator für die Erkennung der Buchstaben H, S und U erstellt. Der Klassifikator wird auf MicroPython portiert und auf einem ESP32 ausgeführt. 

## Voraussetzungen
Auf dem PC müssen folgende Bibliotheken installiert sein:
- scikit-learn
- everywhereml

Diese sind auf https://pypi.org/ verfügbar. 

## Ausführung auf dem PC
1. Auf dem PC wird das Programm mein_Klassifikator_MicroPython.py gestartet. Das Programm importiert die Bibliotheken und die Daten. Die Daten sind 75 Bilder der Buchstaben H, S und U. Jedes Bild besteht aus 256 Grauwerten. Dazu habe ich die Buchstaben in 5 Ansichten mit einer WebCam fotografiert und angepasst. 
2. Das Programm erstellt einen RandomForestClassifier und trainiert ihn mit 70 % der Daten. Die Auswahl erfolgt zufällig. Anschließend wird der Klassifikator auf die restlichen 30 % der Daten angewandt und die Erkennungsleistung angegeben (score). Der Klassifikator darf nicht zu komplex werden. Deshalb sind wir mit einer Erkennungsleistung von unter 100 % zufrieden. 
3. Danach wird der Klassifikator nach MicroPython portiert. Das Ergebnis ist die Datei random_forest.py.  

## Ausführung auf dem ESP32
1. Auf den ESP32 werden kopiert:
- main.py
- HSU_test_data.py (30 % der Daten)
- HSU_test_labels.py (zugehörige Labels) 
- random_forest.py
2. Auf dem ESP32 wird main.py (durch reboot) gestartet. Als Ergebnis werden 3 Listen ausgegeben:
- Vorhersage
- Label
- Differenz Vorhersage minus Label

Sind alle Differenzen Null, so wurden alle Buchstaben richtig erkannt. 

## Testdaten als Bild anzeigen
Die Testdaten in HSU_test_data.py sind ein Array mit der Dimension (23, 256). Es sind 23 angepasste Fotos der Buchstaben H, S und U, die durch eine Reihe mit 256 Grauwerten dargestellt werden. HSU_test_labels.py enthält die zugehörigen Labels.   

Das PC-Programm show_HSU_test_data.py stellt die ursprünglichen 16 x 16 Grauwerte wieder her. Anschließend wird für jeden Buchstaben eine Funktion aus der matplotlib aufgerufen, die den Buchstaben als Bild anzeigt. HSU_test_data.png zeigt das Ergebnis. 

## Quellen
Der Workflow und das Programm zur Portierung nach MicroPython stammen von hier: https://eloquentarduino.com/micropython-machine-learning/ Ich habe eigene Daten erstellt und damit den RandomForestClassifier trainiert. Hinweis: Bei der Ausführung von mein_Klassifikator_MicroPython.py werden "Warnings" ausgegeben.

## Dank 
Ich danke dem Autor "eloquentarduino" für seinen hilfreichen Beitrag. 