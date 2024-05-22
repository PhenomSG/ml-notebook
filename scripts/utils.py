import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

def load_csv(filepath):
    """
    Load a CSV file into a pandas DataFrame.
    
    :param filepath: str, path to the CSV file
    :return: pandas DataFrame
    """
    return pd.read_csv(filepath)

def handle_missing_values(df, strategy='mean'):
    """
    Handle missing values in a DataFrame.
    
    :param df: pandas DataFrame
    :param strategy: str, strategy to handle missing values ('mean', 'median', 'mode', 'drop')
    :return: pandas DataFrame
    """
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    elif strategy == 'drop':
        return df.dropna()
    else:
        raise ValueError("Strategy not recognized. Use 'mean', 'median', 'mode', or 'drop'.")

def scale_features(df, columns):
    """
    Scale specified features in a DataFrame using StandardScaler.
    
    :param df: pandas DataFrame
    :param columns: list of str, column names to scale
    :return: pandas DataFrame with scaled features
    """
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def encode_labels(df, column):
    """
    Encode categorical labels in a column using LabelEncoder.
    
    :param df: pandas DataFrame
    :param column: str, column name to encode
    :return: pandas DataFrame with encoded labels
    """
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    return df

def split_data(df, target_column, test_size=0.2, random_state=42):
    """
    Split data into training and testing sets.
    
    :param df: pandas DataFrame
    :param target_column: str, column name of the target variable
    :param test_size: float, proportion of the dataset to include in the test split
    :param random_state: int, random seed
    :return: tuple, (X_train, X_test, y_train, y_test)
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def plot_correlation_matrix(df):
    """
    Plot a correlation matrix for a DataFrame.
    
    :param df: pandas DataFrame
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

def plot_feature_importance(model, feature_names):
    """
    Plot feature importance for a trained model.
    
    :param model: trained model with feature_importances_ attribute
    :param feature_names: list of str, names of the features
    """
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    plt.figure(figsize=(10, 8))
    plt.title("Feature Importances")
    plt.bar(range(len(feature_names)), importances[indices], align='center')
    plt.xticks(range(len(feature_names)), [feature_names[i] for i in indices], rotation=90)
    plt.tight_layout()
    plt.show()
