import pandas as pd


class DateTimeHandler:
    @staticmethod
    def to_datetime(df, columns):
        for col in columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        return df

    @staticmethod
    def extract_date_parts(df, column):
        df[column + '_year'] = df[column].dt.year
        df[column + '_month'] = df[column].dt.month
        df[column + '_day'] = df[column].dt.day
        return df
