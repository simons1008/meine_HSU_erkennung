# Klassifikator auf Testdaten anwenden und Voraussage machen
# Quelle: https://eloquentarduino.com/micropython-machine-learning/

# Bibliotheken importieren
from random_forest import RandomForestClassifier

# Testdaten laden
from HSU_test_data import X_test

# Testlabels laden
from HSU_test_labels import y_test

# Modell definieren
clf = RandomForestClassifier()

# Modell mit den Testdaten testen
# In MicroPython hat der RandomForestClassifier kein Attribut "score"
# In MicroPython funktioniert clf.predict() nur mit einzelnen Samples 
predicted = []
for i in range(len(X_test)):
    predicted.append(clf.predict(X_test[i]))

# Vorhersage ausgeben
print(predicted)

# Labels ausgeben
print(y_test)

# Fehler ausgeben
unterschiede = []
for i in range(len(X_test)):
    unterschiede.append(predicted[i] - y_test[i])
print(unterschiede)               

# Ende
input("Fertig? ")
