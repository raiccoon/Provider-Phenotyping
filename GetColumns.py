def get_columns(metrics, suffix = ""):
    """
    Return parsed list of column names.

    metrics (list of str): List of metrics as they would appear in EPIC Signal
    suffic (str): Optional suffix (ex. "_log" if data has been transformed)
    """
    # Create 3 variables (numerator, denominator, value) per metric , compile into column names
    columns =  []
    for m in metrics:
        columns.append(m.replace(" ", "_") + "_numerator" + suffix)
        columns.append(m.replace(" ", "_") + "_denominator" + suffix)
        columns.append(m.replace(" ", "_") + "_value" + suffix)

    return columns