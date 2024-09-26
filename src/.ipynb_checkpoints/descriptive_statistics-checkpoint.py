from config import RAW_DATA_DIR, PROCESSED_DATA_DIR
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import pandas as pd


import pandas as pd

def advanced_describe(file_path, convert_columns=None):
    """
    Function to generate descriptive statistics for numerical variables in the employee dataset.

    Parameters:
    file_path (str): The path to the CSV file containing the employee dataset.
    convert_columns (list, optional): A list of column names to convert to numerical types. Default is None.

    Returns:
    pd.DataFrame: A DataFrame containing descriptive statistics for numerical variables.
    """
    # Import df
    df = pd.read_csv(RAW_DATA_DIR/file_path)
    
    # Convert specified columns to numerical if provided
    if convert_columns:
        for column in convert_columns:
            df[column] = pd.to_numeric(df[column], errors='coerce')

    # Selecting only numerical columns from the dataframe
    numerical_df = df.select_dtypes(include=['number'])

    # Generate descriptive statistics
    descriptive_stats = numerical_df.describe().transpose()

    # Add additional statistics: Median and Range
    descriptive_stats['median'] = numerical_df.median()
    descriptive_stats['range'] = numerical_df.max() - numerical_df.min()

    # Rename index to include column names
    descriptive_stats.index.name = 'Variable'

    return descriptive_stats


def plot_descriptive_stats(file_path):
    # Import dataframe
    df = pd.read_csv(RAW_DATA_DIR/file_path)

    # Remove columns if it exists
    # if "Name" in df.columns:
    #     df = df.drop(columns=["Name", "DOJ", "Position"])

    # Separate numerical and categorical columns
    num_cols = df.select_dtypes(include=['number']).columns
    cat_cols = df.select_dtypes(include=['object', 'category']).columns

    # Set the general aesthetic style of the plots
    sns.set(style="whitegrid")

    # Plot histograms for numerical columns
    for col in num_cols:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[col], kde=True, bins=30, color='skyblue')
        plt.title(f'Histogram for {col}', fontsize=14)
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    # Plot count plots for categorical columns
    for col in cat_cols:
        plt.figure(figsize=(8, 5))
        sns.countplot(data=df, x=col, palette='Set2')
        plt.title(f'Count Plot for {col}', fontsize=14)
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
