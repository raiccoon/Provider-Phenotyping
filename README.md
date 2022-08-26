# Provider-Phenotyping

## 1. Data Wrangling and Univariate Analysis

??. open xml file in excel?

0. get_columns.py: Contains method to generate column names based on metrics of interest

1. < ??? >:  Format data, output 2 sheets (raw_data.xlsx)
    - Exclude providers with missing data
    - sheet 1: numerical data of providers, 3 columns per metric
    - sheet 2: categorical data of providers and characteristics
    
2. < ??? >: Univariate analysis of numerical data

3. cat_analysis.py: Output categorical analysis of provider characteristics
    - 3.5: cat_update: Remove unnecessary/redundant columns from sheet 2 based on categorical analysis
    
4. excluded_providers.py: Output information on excluded providers

## 2. Transform Numerical Data

5. transorm_log.py: Perform log transformation on data
    - Output to new columns with _log tag
    
6. transform_logz.py: Generate z-scores from log transformed data
    - Output to new columns with _zscore tag
    
## 3. Cluster Analysis

1. KMeansCluster.py: Perform cluster analysis
    - TODO: If possible, add an extra column with cluster numbers to make following cluster analysis easier?
    
2. < ??? >: Calculate numerical analysis within clusters



