from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import average_precision_score
import joblib

class model:
    def __init__(self, id):
        self.id = id
        self.model = None

    def modeldef(self):
        self.model=None

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def tune(self, X_train, y_train, param):
        self.tunedmodel = param
        self.tunedmodel.fit(X_train, y_train)
        self.model = self.tunedmodel.best_estimator_

    def predict(self, X):
        return self.model.predict(X), self.model.decision_function(X)

    def print_evaluation_scores(self, y_val, predicted):
        # print(len(y_val), len(y_val))
        print("Accracy={}".format(accuracy_score(y_val, predicted)),
              "F1_macro={}".format(f1_score(y_val, predicted, average='macro')),
              "F1_micro={}".format(f1_score(y_val, predicted, average='micro')),
              "F1_wted={}".format(f1_score(y_val, predicted, average='weighted')),
              "Precsion_macro={}".format(average_precision_score(y_val, predicted, average='macro')),
              "Precsion_micro={}".format(average_precision_score(y_val, predicted, average='micro')),
              "Precsion_wted={}".format(average_precision_score(y_val, predicted, average='weighted')))

    def save(self, filename, path='./'):
        joblib.dump(self.model, path + filename, protocol=2)

    def load(self, filename, path='./'):
        self.model = joblib.load(path + filename)
        print('model loaded')