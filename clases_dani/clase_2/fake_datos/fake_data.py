import pandas as pd
from faker import Faker

class BuildDataframe:

    def __init__(self):
        self.fake = Faker('es_AR')
        Faker.seed(4321)
        self.dictionary_df = {}
        self.n_rows = 15
        self.df = pd.DataFrame(data=self.dictionary_df)

    def add_column(self, column_name, func):
        """ Metodo general que hace append de una nueva columna """
        list_data = [func() for _ in range(self.n_rows)]
        self.dictionary_df[column_name] = list_data
        self.df = pd.DataFrame(self.dictionary_df)

    def generate_dataframe(self):
        # Requiere el lambda porque tiene parámetros, pero al usar lambda llega una función anonima para ser ejecutada por add_column
        self.add_column('Id_clients', lambda: self.fake.random_number(digits=8, fix_len=True))
        self.add_column('Banco', self.fake.bank)
        self.add_column('User Name', self.fake.user_name)
        self.add_column('Peliculas Vistas en el Mes', self.fake.random_digit_not_null)
        self.add_column('Series en el Mes', self.fake.random_digit_not_null)
        self.add_column('Predicción de Desuscripción', lambda: int(self.fake.boolean(chance_of_getting_true=50)))


    def main(self):
        self.generate_dataframe()
        return self.df
    

if "__main__" == __name__:
    df = BuildDataframe().main()
    df.to_excel('fake_data_diplomado.xlsx', index=False)