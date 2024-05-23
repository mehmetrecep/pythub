class Changing_value:
   @staticmethod
    def change_value(df: pd.DataFrame, columns: List[str], old_value: Any, new_value:Any) -> pd.DataFrame:
       
        for col in columns:
            df[col].replace(old_value,new_value،inplace=True)
        return df
