```python
# Importing necessary modules
from time import time
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class PerformanceMetrics:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.prediction_time = None
        self.accuracy = None
        self.precision = None
        self.recall = None
        self.f1 = None

    def start(self):
        self.start_time = time()

    def end(self):
        self.end_time = time()

    def calculate_time(self):
        self.prediction_time = self.end_time - self.start_time
        print(f"Execution Time: {self.prediction_time} seconds")

    def calculate_metrics(self, y_true, y_pred):
        self.accuracy = accuracy_score(y_true, y_pred)
        self.precision = precision_score(y_true, y_pred, average='weighted')
        self.recall = recall_score(y_true, y_pred, average='weighted')
        self.f1 = f1_score(y_true, y_pred, average='weighted')

        print(f"Accuracy: {self.accuracy}")
        print(f"Precision: {self.precision}")
        print(f"Recall: {self.recall}")
        print(f"F1 Score: {self.f1}")

    def start_metrics(self, y_true, y_pred):
        self.start()
        self.calculate_metrics(y_true, y_pred)
        self.end()
        self.calculate_time()
```
