import pandas as pd

def clean_logs(input_file, output_file):
    print(f"Starting log aggregation for {input_file}...")
    
    # 1. Ingestion
    df = pd.read_csv(input_file)
    
    # 2. Cleaning & Patching
    df = df.dropna(subset=['timestamp'])
    df['ip_address'] = df['ip_address'].fillna('UNKNOWN_IP')
    df['status_code'] = df['status_code'].fillna(0)
    
    # 3. Export
    df.to_csv(output_file, index=False)
    print(f"Success! Cleaned logs safely exported to {output_file}")

# This block ensures the script runs automatically when executed from the terminal
if __name__ == "__main__":
    clean_logs('massive_raw_logs.csv', 'structured_logs.csv')