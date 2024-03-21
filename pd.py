import pandas as pd

# Load the data
df = pd.read_csv('dummy_user_data.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Basic insights
print("Basic Statistical Summary:\n", df.describe())

# Average login duration
average_duration = df['Login_Duration'].mean()
print(f"\nAverage Login Duration: {average_duration:.2f} minutes")

# Most active day
most_active_day = df.groupby(df['Date'].dt.date).size().idxmax()
print(f"\nMost Active Day: {most_active_day}")

# User with the most page visits
most_active_user = df.groupby('User_ID')['Pages_Visited'].sum().idxmax()
print(f"\nUser with Most Page Visits: User_ID {most_active_user}")

# Average error count
average_errors = df['Error_Count'].mean()
print(f"\nAverage Error Count per Session: {average_errors:.2f}")
