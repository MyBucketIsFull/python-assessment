import matplotlib.pyplot as plt
import mplcursors as mplc


class Visualizer:
    figureNumber = 1

    def create_bar_plot(self, labels, sizes, title, xlabel, ylabel, xlabelRot=40):
        self.add_figure()

        plt.bar(labels, height=sizes)

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=xlabelRot)

    def create_scatter_plot(self, labels, x, y, c, title, xlabel, ylabel, clabel):
        self.add_figure()

        ax = plt.scatter(x, y, c=c)
        cbar = plt.colorbar()

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        cbar.set_label(clabel, rotation=270, labelpad=15)

        cursor = mplc.cursor(ax, hover=True)

        @cursor.connect("add")
        def on_add(sel):
            sel.annotation.set(text="{}\n{}: {}\n{}: {}\n{}: {}".format(labels[sel.target.index], xlabel, x[sel.target.index], ylabel, y[sel.target.index], clabel, c[sel.target.index]))

    def create_pie_chart(self, labels, sizes, title, autopct='%1.1f%%'):
        self.add_figure()

        plt.pie(sizes, labels=labels, autopct=autopct)
        plt.axis('equal')

        plt.title(title)

    def add_figure(self):
        plt.figure(self.figureNumber)
        self.figureNumber += 1

    def show_plots(self):
        plt.show()
