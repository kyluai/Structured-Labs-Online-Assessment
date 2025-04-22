from preswald import table, text, slider, plotly, separator, image, alert
import pandas as pd
import plotly.express as px

# Load the CSV manually using pandas
try:
    df = pd.read_csv("data/uber_stock_data.csv")
    alert("Data loaded successfully!")  # Alert for successful data load
except Exception as e:
    alert(f"Error loading data: {str(e)}")  # Alert for any error in loading data

# Add a slider for dynamic threshold selection
threshold = slider(
    label="Threshold for 'Close' Value",
    min_val=0.0,   # Minimum threshold value
    max_val=100.0, # Maximum threshold value
    step=1.0,      # Step size for the slider
    default=50.0   # Default value of the slider
)

# Function to update the table and plot based on the threshold
def update_data(threshold_value):
    # Filter the DataFrame dynamically based on the threshold selected
    filtered_df = df[df['Close'] > threshold_value]
    
    # Check if filtered_df has data
    if filtered_df.empty:
        alert("No data available after filtering.")  # Alert if no data matches the threshold
    else:
        # Display a title for the app
        text("# My Data Analysis App")

        # Display the Uber logo at the top of the page (above everything else)
        image(src="https://logos-world.net/wp-content/uploads/2020/05/Uber-Logo.png", alt="Uber Logo")

        # Display the filtered data in a table format with the current threshold in the title
        table(filtered_df, title=f"Filtered Data (Threshold: {threshold_value})")
        
        # Add separator to force new row
        separator()

        # Create a scatter plot using Plotly
        fig = px.scatter(filtered_df, x="Date", y="Close", color="Volume", title="Close Price vs Volume")
        
        # Display the plot
        plotly(fig)

# Initial data update
update_data(threshold)

# Attach the update function to the slider so it updates dynamically
threshold.on_change(lambda value: update_data(value))  # Listen for slider change and update accordingly
