class DataPreprocessor:
    def __init__(self):



    def standardize_data(self ,df,columns, method='minmax'):
        return Scaler.standardize_data(df,columns, method)

    def handle_missing_values(self, df,columns, strategy='mean',value:any= None):
        return MissingValueHandler.handle_missing_values(df,columns, strategy,value)
