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
# Testdaten von 5 x 256 Grauwerte in 5 x 16 x 16 Grauwerte konvertieren
X_test_array = np.reshape(X_test_array, (5, 16, 16))

# Testdaten als Bilder anzeigen
_, axes = plt.subplots(nrows=1, ncols= 5, figsize=(10, 3))
# x enthält die 16 x 16 Grauwerte
# Spalte mit i adressieren
for i in range(5):
    ax = axes[i]
    ax.set_axis_off()
    # X_test_array und y_label mit index adressieren
    x = X_test_array[i]
    ax.imshow(x, cmap=plt.cm.gray, interpolation="nearest")
    ax.set_title("{:}".format(y_test[i]))
plt.show()
