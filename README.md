# Provider-Phenotyping

## 1. Data Wrangling and Categorical Analysis

If EPIC Signal file is saved as XML, open in Excel and save as Excel Workbook (.xlsx) file

0. GetColumns.py: Contains method to generate column names based on metrics of interest

1. ExcelParser.py:  Format data, output 4 sheets
    - metrics_raw.xlsx: numerical data of providers, 3 columns per metric
    - metrics_na_removed.xlsx: metrics data, providers with missing metrics data removed
    - categorical_raw.xlsx: categorical data of providers and characteristics
    - categorical_na_removed.xlsx: categorical data, providers with missing metrics data removed

2. CategoryAnalysis.py: Output categorical analysis of provider characteristics
    - 2.5: CategoryUpdate.py: Remove unnecessary/redundant columns from categorical_na_removed based on categorical analysis
    
3. CategoryExcluded.py: Output information on excluded providers

## 2. Transform Numerical Data

5. TransformLog.py: Perform log transformation on data
    - Output to new columns with _log tag
    
6. TransformLogZ.py: Generate z-scores from log transformed data
    - Output to new columns with _zscore tag
    
## 3. Cluster Analysis

1. ClusterNumberDeterminationElbow.py: Determine optimal k value for K-Means cluster algorithm

2. KMeansClusterLogZ.py: Perform cluster analysis
    - Run multiple times, choose clustering with lowest SSE

3. HeatmapLogZ.py: Generate Heatmap visualization of data
    
4. ClusterAnalysis.py: Calculate numerical analysis within clusters

## 4. Cluster Analysis of Shuffled Data

1. Shuffle.py: Shuffle data

2. Repeat #3: Cluster Analysis on Shuffled data, compare results for patterns
    - ClusterNumberDeterminationElbowShuffled.py
    - KMeansClusterShuffled.py
    - HeatmapShuffled.py



