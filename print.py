import pandas as pd
import plotly.express as px

# Replace 'path/to/your/data.xlsx' with the actual path to your Excel file
excel_path = 'sample_data/GDP_dataset.xlsx'

# Load data from Excel
df = pd.read_excel(excel_path)

# Display available parameters with numbers
parameter_dict = {
    1: 'Population(in thousands)',
    2: 'Agricultureproduction(in lakh tonnes)',
    3: 'gdp(in billions)',
    4: 'Built-up(Sq.Km)',
    5: 'AgricultureArea(Sq.Km)'
}

print("Available parameters:")
for number, parameter in parameter_dict.items():
    print(f"{number}. {parameter}")

# Ask the user for the numbers corresponding to the parameters they want to compare
chosen_numbers = input(
    "Enter the numbers of the parameters you want to compare (comma-separated): ")
chosen_numbers = [int(number) for number in chosen_numbers.split(',')]

# Check if the chosen numbers are valid

# Replace 'path/to/your/data.xlsx' with the actual path to your Excel file
excel_path = 'sample_data/GDP_dataset.xlsx'

# Load data from Excel
df = pd.read_excel(excel_path)

# Display available parameters with numbers
parameter_dict = {
    1: 'Population(in thousands)',
    2: 'Agricultureproduction(in lakh tonnes)',
    3: 'gdp(in billions)',
    4: 'Built-up(Sq.Km)',
    5: 'AgricultureArea(Sq.Km)'
}

print("Available parameters:")
for number, parameter in parameter_dict.items():
    print(f"{number}. {parameter}")

# Ask the user for the numbers corresponding to the parameters they want to compare
chosen_numbers = input(
    "Enter the numbers of the parameters you want to compare (comma-separated): ")
chosen_numbers = [int(number) for number in chosen_numbers.split(',')]

# Check if the chosen numbers are valid
if len(chosen_numbers) != 3 or any(number not in parameter_dict for number in chosen_numbers):
    print("Error: Please enter exactly three valid numbers.")
else:
    chosen_parameters = [parameter_dict[number] for number in chosen_numbers]

    # Convert 'State' column to strings
    df['State'] = df['State'].astype(str)

    # Create an interactive bar chart using plotly
    fig = px.bar()

    # Add traces for each chosen parameter
    for i, chosen_parameter in enumerate(chosen_parameters):
        # Use a different color for each parameter
        color = px.colors.qualitative.Set1[i]
        # Convert GDP values to billions
        if 'gdp' in chosen_parameter.lower():
            df[chosen_parameter] = df[chosen_parameter] / 1e9
        fig.add_trace(px.bar(df, x='State', y=chosen_parameter,
                      color_discrete_sequence=[color]).data[0])

    # Set barmode to 'group' for side-by-side bars
    fig.update_layout(barmode='group', bargap=0.2)

    # Update y-axis label to indicate values are in billions
    fig.update_layout(yaxis=dict(title_text="Values (in billions)"))

    fig.show()
