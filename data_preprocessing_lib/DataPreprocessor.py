from MissingValueHandler import MissingValueHandler
from Scaler import Scaler


class DataPreprocessor:

    @staticmethod
    def standardize_data(self, df, columns, method='minmax'):
        return Scaler.standardize_data(df, columns, method)

    @staticmethod
    def handle_missing_values(self, df, columns, strategy='mean', value: any = None):
        return MissingValueHandler.handle_missing_values(df, columns, strategy, value)
