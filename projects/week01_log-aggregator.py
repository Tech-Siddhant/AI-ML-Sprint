import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# PHASE 1: DATA CLEANING (DAY 1)
# ==========================================
def clean_logs(input_file, output_file):
    print(f"🧹 PHASE 1: Starting log cleaning for {input_file}...")
    
    # 1. Ingestion
    df = pd.read_csv(input_file)
    
    # 2. Cleaning & Patching
    df = df.dropna(subset=['timestamp'])
    df['ip_address'] = df['ip_address'].fillna('UNKNOWN_IP')
    df['status_code'] = df['status_code'].fillna(0)
    
    # 3. Export
    df.to_csv(output_file, index=False)
    print(f"✅ Success! Cleaned logs safely exported to {output_file}\n")

# ==========================================
# PHASE 2: ANALYTICS & VISUALIZATION (DAY 2)
# ==========================================
def run_log_analytics(clean_file):
    print(f"📊 PHASE 2: Initiating Log Analytics on {clean_file}...")
    
    # Ingest the newly cleaned data
    df = pd.read_csv(clean_file)
    
    # Temporal Parsing
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Aggregation
    print("--- SERVER HEALTH SUMMARY ---")
    health_summary = df['status_code'].value_counts()
    print(health_summary.to_string(), "\n")

    print("--- TRAFFIC BY ENDPOINT ---")
    traffic_summary = df.groupby('endpoint').size().sort_values(ascending=False)
    print(traffic_summary.head(5).to_string(), "\n")

    # Visualization
    print("📈 Generating Visualizations...")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    health_summary.plot(kind='bar', ax=axes[0], color=['#2ca02c', '#d62728', '#ff7f0e'])
    axes[0].set_title('Server Health (Status Codes)')
    axes[0].set_ylabel('Number of Requests')
    axes[0].tick_params(axis='x', rotation=0)

    traffic_summary.head(5).plot(kind='pie', ax=axes[1], autopct='%1.1f%%', colormap='Blues_r')
    axes[1].set_title('Top 5 Endpoints by Traffic')
    axes[1].set_ylabel('')

    plt.tight_layout()
    # Remove or comment out plt.show()
    # plt.show() 
    # Add this to save the chart as a high-resolution PNG image
    plt.savefig('server_analytics_dashboard.png', dpi=300, bbox_inches='tight')
    print("✅ Visualizations saved as 'server_analytics_dashboard.png'")

# ==========================================
# MASTER EXECUTION TRIGGER
# ==========================================
if __name__ == "__main__":
    # Define your file names
    raw_data = 'massive_raw_logs.csv'
    clean_data = 'structured_logs.csv'
    
    # Run the pipeline in order
    clean_logs(raw_data, clean_data)
    run_log_analytics(clean_data)