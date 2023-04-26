from CovidDataService import CovidDataService
from plotter import CSVPlotter, JSONPlotter, PlotterManager
import pandas as pd


countries = ['United States', 'Brazil', 'India', 'Russia', 'China', 'United Kingdom']
covid_service = CovidDataService(countries)

# Get data for more countries
data = covid_service.get_countries_data(countries)
print(data)

# Get historical data for more countries and dates
start_date1 = '2021-10-01'
end_date1 = '2022-03-31'
historical_data1 = covid_service.get_countries_historic_data(countries, start_date1, end_date1)
print(historical_data1)

start_date2 = '2022-04-01'
end_date2 = '2022-09-30'
historical_data2 = covid_service.get_countries_historic_data(countries, start_date2, end_date2)
print(historical_data2)

# Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv('countries_data.csv', index=False)

# Convert to Pandas DataFrame
df = pd.DataFrame(historical_data1)

# Save to CSV file
df.to_csv('historical_data1.csv', index=False)

# create a PlotterManager instance
plotter_manager = PlotterManager('data_covid.json')

# create a CSVPlotter and a JSONPlotter instance
csv_plotter = CSVPlotter(covid_service)
json_plotter = JSONPlotter(covid_service)

# plot the data using the PlotterManager and the CSVPlotter
plotter_manager.plot(csv_plotter)

# plot the data using the PlotterManager and the JSONPlotter
plotter_manager.plot(json_plotter)
