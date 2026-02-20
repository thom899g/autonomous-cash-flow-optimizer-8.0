import pandas as pd
from sklearn.linear_model import LinearRegression

class PredictiveAnalytics:
    def __init__(self):
        self.model = LinearRegression()
        
    def predict(self, data):
        # Convert data to DataFrame and train model
        df = pd.DataFrame(data)
        # Assuming 'amount' and 'time' are columns
        self.model.fit(df[['time']], df['amount'])
        # Make predictions
        future_time = [max(df['time']) + 1]  # Next time point
        prediction = self.model.predict([future_time])
        return prediction[0]