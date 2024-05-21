from sklearn.preprocessing import StandardScaler, MinMaxScaler


class Scaler:
    @staticmethod
    def standard_scale(df, columns):
        scaler = StandardScaler()
        df[columns] = scaler.fit_transform(df[columns])
        return df

    @staticmethod
    def minmax_scale(df, columns):
        scaler = MinMaxScaler()
        df[columns] = scaler.fit_transform(df[columns])
        return df
