import pandas as pd
from typing import List, Union, Any


class MissingValueHandler:
    @staticmethod
    def replace_value(df: pd.DataFrame, value: Any) -> pd.DataFrame:
        """
        Replace all possible missing values in the DataFrame with a specified value.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        value (Any): The value to replace missing values with.

        Returns:
        pd.DataFrame: The DataFrame with missing values replaced.
        """
        missing_values = [None, pd.NA, pd.NaT, 'NA', 'N/A', 'n/a', 'na', 'NaN', 'nan', 'null', 'Null', '', '/N', '\\N']
        return df.replace(missing_values, value)

    @staticmethod
    def impute_mean(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        Impute missing values in specified columns with the mean of the column.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        columns (List[str]): List of column names to impute.

        Returns:
        pd.DataFrame: The DataFrame with imputed values.
        """
        for col in columns:
            df[col].fillna(df[col].mean(), inplace=True)
        return df

    @staticmethod
    def impute_median(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        Impute missing values in specified columns with the median of the column.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        columns (List[str]): List of column names to impute.

        Returns:
        pd.DataFrame: The DataFrame with imputed values.
        """
        for col in columns:
            df[col].fillna(df[col].median(), inplace=True)
        return df

    @staticmethod
    def impute_constant(df: pd.DataFrame, columns: List[str], value: Any) -> pd.DataFrame:
        """
        Impute missing values in specified columns with a constant value.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        columns (List[str]): List of column names to impute.
        value (Any): The constant value to impute.

        Returns:
        pd.DataFrame: The DataFrame with imputed values.
        """
        for col in columns:
            df[col].fillna(value, inplace=True)
        return df

    @staticmethod
    def delete_missing(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        Delete rows with missing values in specified columns.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        columns (List[str]): List of column names to check for missing values.

        Returns:
        pd.DataFrame: The DataFrame with rows containing missing values removed.
        """
        return df.dropna(subset=columns)
    
    ##edited***********************************************************************************************************
    @staticmethod
    def handle_missing_values(df: pd.DataFrame, columns: List[str], strategy='mean',value:any= None) -> pd.DataFrame:
        missing_values = [None, pd.NA, pd.NaT, 'NA', 'N/A', 'n/a', 'na', 'NaN', 'nan', 'null', 'Null', '', '/N', '\\N']

        if strategy not in ['mean', 'median', 'constant', 'delete']:
            raise ValueError("Invalid strategy. Choose from 'mean', 'median', 'constant', 'delete', or 'replace'.")
            
        if strategy == 'mean':
            for col in columns:
                df[col].fillna(df[col].mean(), inplace=True)
        
        elif strategy == 'median':
            for col in columns:
                df[col].fillna(df[col].median(), inplace=True)
            
        elif strategy == 'constant':
            if value is None:
                raise ValueError("When using 'constant' strategy, you must provide a value.")
            for col in columns:
                df[col].fillna(value, inplace=True)
                
        elif strategy == 'delete':
            df.dropna(subset=columns, inplace=True)
            
        elif strategy == 'replace':
            if value is None:
                raise ValueError("When using 'replace' strategy, you must provide a value.")
            df.replace(missing_values, value, inplace=True)
        return df
                    
        
