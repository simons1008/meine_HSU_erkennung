# Testdaten anzeigen
# Quellen: https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html
#          https://eloquentarduino.com/micropython-machine-learning/ 

# Bibliotheken importieren
import matplotlib.pyplot as plt
import numpy as np

# Testdaten importieren
from HSU_test_data import X_test
# Testlabels importieren
from HSU_test_labels import y_test

# Testdaten in numpy-array konvertieren
X_test_array = np.array(X_test)
# Testdaten von 23 x 256 Grauwerte in 23 x 16 x 16 Grauwerte konvertieren
X_test_array = np.reshape(X_test_array, (23, 16, 16))

# Testdaten als Bilder anzeigen
_, axes = plt.subplots(nrows=2, ncols= 12, figsize=(20, 4))
# x enthält die 16 x 16 Grauwerte
# Zeile und Spalte mit i, j adressieren
for i in range(2):
    for j in range(12):
        ax = axes[i, j]
        ax.set_axis_off()
        # X_test_array und y_label mit index adressieren
        index = i*12 + j
        # kein Bild bei i = 1 und j = 11
        if index < 23:
            x = X_test_array[index]
            ax.imshow(x, cmap=plt.cm.gray, interpolation="nearest")
            ax.set_title("{:}".format(y_test[index]))
plt.show()
