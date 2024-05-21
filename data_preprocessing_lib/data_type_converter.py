class DataTypeConverter:
    @staticmethod
    def to_numeric(df, columns):
        for col in columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        return df

    @staticmethod
    def to_categorical(df, columns):
        for col in columns:
            df[col] = df[col].astype('category')
        return df
