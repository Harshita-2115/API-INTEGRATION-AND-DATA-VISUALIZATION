import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fetch data from COVID-19 India API (state-wise data)
url = "https://api.covid19india.org/data.json"
response = requests.get(url)
data = response.json()

# Process data into a DataFrame (state names and confirmed cases)
states = data.get('statewise', [])
state_data = []
for state in states:
    name = state.get('state', 'Unknown')
    confirmed = int(state.get('confirmed', 0))
    if name != 'Total':  # Skip the total row
        state_data.append({'state': name, 'confirmed': confirmed})

df = pd.DataFrame(state_data)

# Sort by confirmed cases and take top 10
df = df.sort_values(by='confirmed', ascending=False).head(10)

# Create a bar chart for confirmed cases
plt.figure(figsize=(10, 6))
plt.bar(df['state'], df['confirmed'], color='orange')
plt.xlabel('State')
plt.ylabel('Confirmed Cases')
plt.title('Top 10 Indian States by COVID-19 Confirmed Cases')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as an image
plt.savefig('indian_states_covid.png')
print("Plot saved as 'indian_states_covid.png'. Open it manually to view.")

# Try to display the plot
try:
    plt.show()
except:
    print("Plot display failed. Check the saved image file.")

# Print the DataFrame for reference
print("\nTop 10 States DataFrame:")
print(df)

# Pause to keep terminal open
input("\nPress Enter to exit...")
