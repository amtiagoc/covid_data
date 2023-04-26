
class CovidDataService:
    def __init__(self, data):
        self.data = data

    def get_countries_data(self, country):
        return [d for d in self.data if d['country'] == country]

    def get_countries_historic_data(self, country, start_date, end_date):
        country_data = self.get_countries_data(country)
        filtered_data = []
        for d in country_data:
            if d['start_date'] <= end_date and d['end_date'] >= start_date:
                filtered_data.append({
                    'start_date': max(d['start_date'], start_date),
                    'end_date': min(d['end_date'], end_date),
                    'cases': d['cases'],
                    'deaths': d['deaths'],
                    'tests': d['tests']
                })
        return filtered_data