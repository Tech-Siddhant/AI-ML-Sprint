import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_massive_messy_logs(filename, num_rows=100000):
    print(f"Generating {num_rows} rows of messy logs...")
    
    # Base data
    dates = [datetime(2026, 6, 1) + timedelta(seconds=i*10) for i in range(num_rows)]
    ips = [f"192.168.1.{random.randint(1, 255)}" for _ in range(num_rows)]
    endpoints = random.choices(['/api/login', '/api/data', '/api/users', '/api/billing'], k=num_rows)
    statuses = random.choices([200, 404, 500, 502], weights=[0.7, 0.1, 0.1, 0.1], k=num_rows)
    
    df = pd.DataFrame({'timestamp': dates, 'ip_address': ips, 'endpoint': endpoints, 'status_code': statuses})
    
    # Introduce Chaos (The "Mess")
    # 1. Delete some timestamps
    df.loc[df.sample(frac=0.05).index, 'timestamp'] = np.nan 
    # 2. Delete some IP addresses
    df.loc[df.sample(frac=0.1).index, 'ip_address'] = np.nan
    # 3. Corrupt some status codes
    df.loc[df.sample(frac=0.02).index, 'status_code'] = np.nan
    
    df.to_csv(filename, index=False)
    print(f"Chaos created. Saved to {filename}.")

if __name__ == "__main__":
    generate_massive_messy_logs('massive_raw_logs.csv')