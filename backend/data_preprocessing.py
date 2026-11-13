
import pandas as pd
from hbase_connection import get_hbase_data


def preprocess_data():
    # Retrieve data from HBase
    records = get_hbase_data()

    # Convert records into a Pandas DataFrame
    df = pd.DataFrame(records)

    df['wind_speed'] = pd.to_numeric(df['wind_speed'], errors='coerce').fillna(0)

    # Convert numerical columns from strings to numbers
    numerical_columns = [
        'solar_radiation',
        'wind_speed',
        'temperature',
        'energy_output'
    ]

    for column in numerical_columns:
        df[column] = pd.to_numeric(df[column])

    return df


# Test preprocessing
if __name__ == "__main__":
    df = preprocess_data()

    print("Preprocessed Renewable Energy Dataset:")
    print(df)

    print("\nDataset Information:")
    print(df.info())
