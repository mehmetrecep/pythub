from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd


class CategoricalEncoder:
    @staticmethod
    def one_hot_encode(df, columns):
        encoder = OneHotEncoder(sparse=False)
        encoded_columns = encoder.fit_transform(df[columns])
        df = df.drop(columns, axis=1)
        df = df.join(pd.DataFrame(encoded_columns, columns=encoder.get_feature_names_out(columns)))
        return df

    @staticmethod
    def label_encode(df, columns):
        encoder = LabelEncoder()
        for col in columns:
            df[col] = encoder.fit_transform(df[col])
        return df
