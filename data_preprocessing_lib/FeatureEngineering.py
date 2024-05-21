import pandas as pd


class FeatureEngineer:
    @staticmethod
    def create_feature(df, column, func):
        df[column + '_feature'] = df[column].apply(func)
        return df
