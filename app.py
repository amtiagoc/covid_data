from CovidDataService import CovidDataService

countries = ['United States', 'Brazil', 'India', 'Russia', 'China', 'United Kingdom']
covid_service = CovidDataService(countries)

# Get data for more countries
data = covid_service.get_country_data(countries)
print(data)

# Get historical data for more countries and dates
start_date1 = '2021-10-01'
end_date1 = '2022-03-31'
historical_data1 = covid_service.get_country_historic_data(countries, start_date1, end_date1)
print(historical_data1)

start_date2 = '2022-04-01'
end_date2 = '2022-09-30'
historical_data2 = covid_service.get_country_historic_data(countries, start_date2, end_date2)
print(historical_data2)