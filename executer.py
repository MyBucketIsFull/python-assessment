import pandas as pd
from analyzer import Analyzer
from visualizer import Visualizer


class Executer:
    def __init__(self):
        file = 'winemag-data-130k-v2.csv'
        df = pd.read_csv(file, nrows=20000)
        df = df[pd.notnull(df['country'])]
        df = df[pd.notnull(df['points'])]
        df = df[pd.notnull(df['price'])]
        df = df[pd.notnull(df['taster_name'])]
        df = df[pd.notnull(df['title'])]
        df = df[pd.notnull(df['variety'])]

        print('Rows: {}\n'.format(df.shape[0]))
        self.df = df

    def visualize(self):
        visualizer = Visualizer()

        data = self.df.groupby(['country'])['points'].mean()
        visualizer.create_bar_plot(data.index, data.values, 'Average points per country', 'Country', 'Points')

        data = self.df.groupby('variety').agg({'points': 'mean', 'price': 'mean', 'variety': 'size'}).rename(columns={'variety': 'count'})
        visualizer.create_scatter_plot(data.index, data['price'], data['points'], data['count'], 'Average points and price per variety', 'Price', 'Points', 'Total')

        data = self.df['taster_name'].value_counts()
        visualizer.create_pie_chart(data.index, data.values, 'Amount of reviews')

        visualizer.show_plots()

    def analyze(self):
        analyzer = Analyzer()

        points = self.df['points'].values

        print('Calculations made on points column:')
        print('Maximum: {}'.format(analyzer.calculate_maxmimum(points)))
        print('Sum: {}'.format(analyzer.calculate_sum(points)))
        print('Mean: {}'.format(analyzer.calculate_mean(points)))
        print('Variance: {}'.format(analyzer.calculate_variance(points)))
        print('Standard Deviation: {}'.format(analyzer.calculate_standard_deviation(points)))


executer = Executer()
executer.analyze()
executer.visualize()
