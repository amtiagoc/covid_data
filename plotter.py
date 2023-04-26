from abc import ABC, abstractmethod
from CovidDataService import CovidDataService

class Plotter(CovidDataService,ABC):
    def __init__(self, data_service):
        self.data_service = data_service

    @abstractmethod
    def plot(self):
        pass

    def get_countries_data(self):
        return self.data_service.get_countries_data()

    def get_countries_historic_data(self, countries, start_date, end_date):
        return self.data_service.get_countries_historic_data(countries, start_date, end_date)


class CSVPlotter(Plotter):
    def __init__(self, data_service):
        super().__init__(data_service)

    def plot(self,csv_data):
        print("Plotting CSV data")


class JSONPlotter(Plotter):
    def __init__(self, data_service):
        super().__init__(data_service)

    def plot(self,json_data):
        print("Plotting JSON data")

class PlotterManager:
    def __init__(self, file_path):
        self.file = open(file_path, 'r')

    def plot(self, plotter):
        # plot depend on the extension of the file
        if self.file.name.endswith(".csv"):
            plotter.plot(self.file)
        elif self.file.name.endswith(".json"):
            plotter.plot(self.file)
        else:
            print("File format has not been recognized")
