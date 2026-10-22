import pandas as pd
import numpy as np

# 1. Generate Mock Deployment Data
data = {
    'Ticket_ID': ['T101', 'T102', 'T103', 'T104', 'T105', 'T106'],
    'Zone': ['Juja', 'Ruaka', 'Juja', 'Kikuyu', 'Ruaka', 'Juja'],
    'Assigned_Tech': ['Tech_A', 'Tech_B', 'Tech_A', 'Tech_C', 'Tech_B', 'Tech_A'],
    'Request_Date': ['2026-10-15', '2026-10-15', '2026-10-16', '2026-10-17', '2026-10-18', '2026-10-19'],
    'Completion_Date': ['2026-10-16', '2026-10-18', '2026-10-17', '2026-10-18', pd.NaT, '2026-10-20'],
    'Status': ['Completed', 'Completed', 'Completed', 'Completed', 'Pending', 'Completed']
}
df = pd.DataFrame(data)

# 2. Data Cleaning & Type Conversion
df['Request_Date'] = pd.to_datetime(df['Request_Date'])
df['Completion_Date'] = pd.to_datetime(df['Completion_Date'])

# 3. Feature Engineering: Calculate Turnaround Time (SLA) in days
df['Turnaround_Days'] = (df['Completion_Date'] - df['Request_Date']).dt.days

# 4. Data Aggregation: Analyze Technician Efficiency
completed_jobs = df[df['Status'] == 'Completed']
tech_performance = completed_jobs.groupby('Assigned_Tech')['Turnaround_Days'].mean().reset_index()
tech_performance.rename(columns={'Turnaround_Days': 'Avg_Days_to_Complete'}, inplace=True)

# 5. Output Results
print("--- Raw Deployment Data ---")
print(df)
print("\n--- Technician Performance (Average Turnaround) ---")
print(tech_performance)
