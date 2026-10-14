import pandas as pd
import requests 

class DataSource:

    def __init__(self,name):
        self.name = name

    def load(self):
        raise NotImplementedError("You must implement this method")

class CsvDataSource(DataSource):

    def __init__(self,name,path):
        super().__init__(name)
        self.path = path 

    def load(self):
        data = pd.read_csv(self.path)
        print(data.head())


class ApiDataSource(DataSource):

    def __init__(self,name,backend_domain):
        super().__init__(name)
        self.backend_domain = backend_domain 

    def load(self):
        response = requests.get(self.backend_domain)
        packed_response = response.json()['data']
        df = pd.DataFrame(packed_response)
        print(df.shape)
        print(df.head())


back_end_api = 'https://ecommerce.routemisr.com/api/v1/products'


csv_source = CsvDataSource('csv file','Iris.csv')

api_source = ApiDataSource('route academy',back_end_api)

print(csv_source.name)
csv_source.load()

print("The backend API \n")
print(api_source.name)
api_source.load()


