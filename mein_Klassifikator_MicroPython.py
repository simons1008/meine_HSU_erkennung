# Klassifikator für H S U Grauwert-Bilder
# Quellen: https://eloquentarduino.com/micropython-machine-learning/
#          https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html      

# Bibliotheken importieren
import numpy as np
from everywhereml.sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Daten laden
data = np.load("HSU_data.npy")

# Labels laden
labels = np.load("HSU_labels.npy")

# Daten in Trainingsdaten und Testdaten aufspalten
X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.3, random_state = 1, shuffle=True)

# Klassifikator erstellen
clf = RandomForestClassifier(n_estimators=7, max_leaf_nodes=20)

# Mit den Trainingsdaten trainieren (fit - dazupassen)
clf.fit(X_train, y_train)

# Ergebnis ausgeben
print('Training completed')
print('Score: {:5.2f}'.format(clf.score(X_test, y_test)))
input('Continue? ')

# Modell mit den Testdaten testen
print("Vorhersage des trainierten Modells")
predicted = clf.predict(X_test)

# Vorhersage ausgeben
print(predicted)

# Sollwerte ausgeben
print(y_test)

# Fehler ausgeben
print(predicted - y_test)

# Metrics Classification Report ausgeben
print(
    f"Classification report for classifier {clf}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)

# Klassifikator zu MicroPython portieren
# Ergebnis speichern und drucken
print(clf.to_micropython_file('random_forest.py'))
print('Port to MicroPython completed')

# Testdaten als Python-Datei speichern
test_daten = "X_test = {:}".format(X_test.tolist())
with open("HSU_test_data.py", mode="w") as datei:
    datei.write(test_daten)

# Testlabels als Python-Datei speichern
test_labels = "y_test = {:}".format(y_test.tolist())
with open("HSU_test_labels.py", mode="w") as datei:
    datei.write(test_labels)

# Ende
input('Done? ')
