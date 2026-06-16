import pandas as pd
import numpy as np

def generate_csv():
    # Define the raw data exactly as shown in the target table
    data = {
        'first_name': ['Corey', 'Jane', 'John', np.nan, np.nan, 'NA'],
        'last_name': ['Schafer', 'Doe', 'Doe', 'Anonymous', np.nan, 'Missing'],
        'email': ['corey@email.com', 'jane@email.com', np.nan, 'anon@email.com', np.nan, 'NA'],
        'age': [33, 55, 63, 36, np.nan, 'Missing']
    }

    # Load data into a Pandas DataFrame
    df = pd.DataFrame(data)

    # Export to CSV, naming the default index column 'Index' to match your image
    output_filename = 'messy_people_data.csv'
    df.to_csv(output_filename, index_label='Index')
    
    print(f"Success! {output_filename} has been generated.")
    print("\nDataFrame Preview:")
    print(df)

if __name__ == "__main__":
    generate_csv()