import pandas as pd
import plotly.express as px


# Function to preprocess data and calculate impedance
def preprocess_data(data):
    # Calculate Voltage and Current differences
    data['Voltage_diff'] = data['Voltage_measured'] - data['Voltage_load']
    data['Current_diff'] = data['Current_measured'] - data['Current_load']

    # Calculate Impedance, avoiding division by zero
    data['Impedance'] = data['Voltage_diff'] / data['Current_diff'].replace(0, pd.NA)

    # Drop rows with NaN or infinite values in the calculated columns
    data = data.dropna(subset=['Impedance'])
    return data


# Function to visualize the data
def plot_data(data):
    # Plot Battery Impedance vs. Time
    fig_impedance = px.line(
        data,
        x='Time',  # Use 'Time' instead of 'time'
        y='Impedance',
        title='Battery Impedance vs Time',
        labels={'Time': 'Time (s)', 'Impedance': 'Impedance (Ohms)'},
    )
    fig_impedance.show()

    # Plot Voltage Measured vs. Time
    fig_voltage = px.line(
        data,
        x='Time',  # Use 'Time' instead of 'time'
        y='Voltage_measured',
        title='Voltage Measured vs Time',
        labels={'Time': 'Time (s)', 'Voltage_measured': 'Voltage (V)'},
    )
    fig_voltage.show()

    # Plot Current Measured vs. Time
    fig_current = px.line(
        data,
        x='Time',  # Use 'Time' instead of 'time'
        y='Current_measured',
        title='Current Measured vs Time',
        labels={'Time': 'Time (s)', 'Current_measured': 'Current (A)'},
    )
    fig_current.show()


# Main function to execute the script
def main():
    # Specify the path to the CSV file
    csv_file_path = r'D:\hp laptop data\Documents\NIKITA V\pythonProject\archive\cleaned_dataset\data\00001.csv'

    # Step 1: Load data from the CSV file
    print("Loading data from CSV file...")
    data = pd.read_csv(csv_file_path)
    print(f"Loaded {len(data)} rows of data from {csv_file_path}")

    # Step 2: Preprocess the data
    print("Preprocessing data...")
    data = preprocess_data(data)
    print(f"Data after preprocessing: {len(data)} rows")

    # Save the processed data to a new CSV file (optional)
    processed_data_path = 'processed_battery_data.csv'
    data.to_csv(processed_data_path, index=False)
    print(f"Processed data saved to {processed_data_path}")

    # Step 3: Visualize the data
    print("Generating plots...")
    plot_data(data)


if __name__ == "__main__":
    main()
