import pandas as pd
from datetime import datetime


def write_to_excel(product_list, file_name="Product_Data.xlsx"):
    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(product_list)

    # Add Timestamp column with current date and time
    df['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        # Write to Excel
        df.to_excel(file_name, index=False)
        print(f"Data written successfully to {file_name}")
    except Exception as e:
        print(f"Failed to write to Excel: {e}")
