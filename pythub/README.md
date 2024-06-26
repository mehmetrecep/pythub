# PyTHub

## Project Description

PyTHub is a comprehensive Python library designed for data preprocessing tasks. It provides a variety of functions for data cleaning, transformation, and manipulation, making it an essential tool for data engineering projects. The library is built to be publishable on the Python Package Index (PyPI).

## Installation

To install PyTHub, use the following command:

pip install pythub

## Usage Examples

Here's a brief example of how to use some of the key features of PyTHub:

```python
from pythub import (
    MissingValueHandler,
    OutlierHandler,
    Scaler,
    TextCleaner,
    FeatureEngineer,
    DataTypeConverter,
    CategoricalEncoder,
    DateTimeHandler,
    DataFrameLoader,
    DataSorter,
    DataFrameModifier
)
import pandas as pd

# Load a CSV file into a DataFrame
data = DataFrameLoader.read_csv('synthetic_sample_data.csv')

# Delete rows with missing data in the 'Rating' column
data_1 = MissingValueHandler.delete_missing(data, columns=['Rating'])

# Display the processed DataFrame
print(data_1)
```

## Features

PyTHub includes the following modules and functionalities:

**MissingValueHandler**: Handle missing values by replacement or deletion.
-replace_value(df, value)
-impute_mean(df, columns)
-impute_median(df, columns)
-impute_constant(df, columns, value)
-delete_missing(df, columns)
-get_rows_with_missing_data(df, column)

**OutlierHandler**: Detect and handle outliers using the IQR method.
-iqr_outliers(df, column, threshold=1.5)

**Scaler**: Standardize and normalize data.
-standard_scale(df, columns)
-minmax_scale(df, columns)

**TextCleaner**: Perform string manipulation and text cleaning.
-remove_stopwords(text)
-to_lowercase(text)
-remove_punctuation(text)
-lemmatize(text)
-clean_text(text)
-clean_columns(df, columns)

**FeatureEngineer**: Create new features.
-create_feature(df, column, func)

**DataTypeConverter**: Convert data types.
-to_numeric(df, columns)
-to_categorical(df, columns)

**CategoricalEncoder**: Encode categorical data.
-one_hot_encode(df, columns)
-label_encode(df, columns)

**DateTimeHandler**: Handle date and time data.
-to_datetime(df, columns)
-extract_date_parts(df, column)

**DataFrameLoader**: Read data from CSV files.
-read_csv(file_path, **kwargs)

**DataSorter**: Sort DataFrame rows.
-sort_by_row(df, column, ascending=True)

**DataFrameModifier**: Modify DataFrames.
-delete_column(df, column)


## Dependencies

PyTHub requires the following libraries:

- re
- string
- nltk
- numpy
- pandas
- typing

## Authors

- MHD Alhabeb Alshalah
- Mohamed Ragab Abdelfattah Abdelfadeel
- AHMED EMAD ELSAYED MOHAMED ABDELFATTAH

## Changelog

Version 1.0.0: Initial release with basic functionalities.