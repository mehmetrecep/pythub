import pandas as pd
from typing import List, Any
class Changing_value:
   @staticmethod
    def change_value(df: pd.DataFrame, columns: List[str], old_value: Any, new_value:Any) -> pd.DataFrame:
       """
        Replace all possible missing values in the DataFrame with a specified value.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        columns (List[str]): List of column names to change.
        old_value (Any): The value will be change.
        new_value (Any):The value to which we will change.

       Returns:
        pd.DataFrame: The DataFrame with the new values.
        """
        for col in columns:
            df[col].replace(old_value,new_value،inplace=True)
        return df
