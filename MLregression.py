import numpy as np
class RegressionModel:
    def __init__(self):
        self.b0 = 0
        self.b1 = 0
        self.mse = 0
        self.fitforprediction = False

    def fit(self,X,Y):
        self.X = X
        self.Y = Y
        self.b1 = np.sum((self.X - np.mean(self.X)) * (self.Y - np.mean(self.Y))) / np.sum(np.square(self.X - np.mean(self.X)))
        self.b0 = np.mean(self.Y) - (self.b1 * np.mean(self.X))
        self.mse = np.sum(np.square(self.predictYdash(self.X) - np.mean(self.Y))) / np.sum(np.square(self.Y - np.mean(self.Y)))

        print(">> b1 is :",self.b1)
        print(">> b0 is :",self.b0)
        print("Equation of Line is : Y = {} + {}X".format(self.b0,self.b1))
        print("MSE is :",self.mse)

        if self.mse >=0 and self.mse <=1:
            self.fitforprediction = True
            print(">> Equation of Line : Y = {} + {}X is fit for predictions".format(self.b0,self.b1))
        else:
            print(">> Equation of Line : Y = {} + {}X is not fit for predictions:".format(self.b0,self.b1))


    def predictYdash(self, X):
        Y = self.b0 + np.multiply(self.b1 ,X)
        return Y

    def predict(self, X):
        if self.fitforprediction == True:
            Y = self.b0 + np.multiply(self.b1, X)
            return Y
        else:
            return -1
def main():
    X = [1,2,3,4,5]
    Y = [2,4,5,4,5]

    # Model creation
    model = RegressionModel()

    # Model Training
    model.fit(X,Y)
    PredictedOutput = model.predict(6)
    print("Predicted output for 6 is:",PredictedOutput)
if __name__ == '__main__':
    main()




