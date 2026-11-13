
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from data_preprocessing import preprocess_data


def perform_clustering():
    # Get preprocessed data
    df = preprocess_data()

    # Select numerical features for clustering
    features = [
        'solar_radiation',
        'wind_speed',
        'temperature',
        'energy_output'
    ]

    X = df[features]

    # Standardize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply K-Means clustering
    kmeans = KMeans(
        n_clusters=2,
        random_state=42,
        n_init=10
    )

    df['cluster'] = kmeans.fit_predict(X_scaled)

    return df


# Test clustering
if __name__ == "__main__":
    result = perform_clustering()

    print("Renewable Energy Clustering Results:")
    print(result[['row_key', 'source', 'location', 'energy_output', 'cluster']])

    print("\nCluster Counts:")
    print(result['cluster'].value_counts().sort_index())
