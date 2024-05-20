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
    
    #edited
    @staticmethod
    def standardize_data(df,columns, method='minmax'):
        if method == 'minmax':
            scaler = MinMaxScaler()
        elif method == 'standard':
            scaler = StandardScaler()
        else:
            raise ValueError("Invalid method. Choose from 'minmax' or 'standard'.")
        df[columns] = scaler.fit_transform(df[columns])
        return df
