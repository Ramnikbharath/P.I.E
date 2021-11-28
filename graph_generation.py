# Program created by Aidan Beeching
# A rudimentary program designed to generate graphs based on a machine learning algorithm
# and its classification results. Uses matplotlib and pandas to generate five different graphs.
# As of now, ONLY works with the columns from the dataset in kaggle.

from matplotlib import pyplot as plt
from itertools import combinations
import pandas as pd

class graph_generator:
    # This function initializes a graph generator based on an input CSV file.
    # The file is read in as a DataFrame to be used with the later functions.
    # It also corrects some inconsistencies in the .csv file, should they exist.
    def __init__(self, FileWithPredictionsInput):
        self.FileWithPredictionsInput = pd.read_csv(FileWithPredictionsInput)
        stars_type = ['Red Dwarf','Brown Dwarf','White Dwarf','Main Sequence','Super Giants','Hyper Giants']
        self.FileWithPredictionsInput['Class'] = self.FileWithPredictionsInput['Type'].replace(self.FileWithPredictionsInput['Type'].unique(),stars_type)
        self.FileWithPredictionsInput['Color'].loc[self.FileWithPredictionsInput['Color'] =='Blue-white'] = 'Blue-White'
        self.FileWithPredictionsInput['Color'].loc[self.FileWithPredictionsInput['Color'] =='Blue White'] = 'Blue-White'
        self.FileWithPredictionsInput['Color'].loc[self.FileWithPredictionsInput['Color'] =='Blue white'] = 'Blue-White'
        self.FileWithPredictionsInput['Color'].loc[self.FileWithPredictionsInput['Color'] =='yellow-white'] = 'White-Yellow'
        self.FileWithPredictionsInput['Color'].loc[self.FileWithPredictionsInput['Color'] =='Yellowish White'] = 'White-Yellow'
        self.FileWithPredictionsInput['Color'].loc[self.FileWithPredictionsInput['Color'] =='white'] = 'White'
        self.FileWithPredictionsInput['Color'].loc[self.FileWithPredictionsInput['Color'] =='yellowish'] = 'Yellowish'
        # print(self.FileWithPredictionsInput) # Mainly for testing, feel free to comment out

    # This function generates a graph of each feature, displays it on the screen,
    # and saves the figure to the computer. Histograms are chosen for this purpose
    # since it permits the user to see the distribution of numerical data on the graph.
    def generate_histograms(self):
        plt.close()

        # Frequency of Star Colors
        plt.figure(1, figsize=(12, 8))
        self.FileWithPredictionsInput["Color"].value_counts().plot(kind='bar')
        plt.title("Frequency of Star Colors")
        plt.savefig('color_freqs.png')

        # Spectral Classes
        plt.figure(2, figsize=(12, 8))
        self.FileWithPredictionsInput["Spectral_Class"].value_counts().plot(kind='bar')
        plt.title("Spectral Classes")
        plt.savefig('spec_freqs.png')

        # Plot for the type of stars
        plt.figure(3, figsize=(12, 8))
        self.FileWithPredictionsInput["Type"].value_counts().plot(kind='bar')
        plt.title("Types of Stars")
        self.FileWithPredictionsInput["Type"].value_counts().plot().set_xticklabels(["Red", "Brown", "White", "Main", "Giant", "Hyper"])
        plt.savefig('star_types.png')
        plt.close(3)

        # Subplots for some other values from the .csv
        plt.figure(4, figsize=(13, 10))
        hist = self.FileWithPredictionsInput.hist(["Temperature", "L", "R", "A_M"])
        hist[0, 1].set_title("Luminosity")
        hist[1, 0].set_title("Relative Radius")
        hist[1, 1].set_title("Absolute Magnitude")
        plt.tight_layout()
        plt.savefig('star_hist.png')
        plt.close(4)

        
    # This function provides a majority of the graphs of various column elements against each other.
    # This does not necessarily include every potential combination at the moment. The overall subplot
    # will look wonky depending on the screen size with plt.show().
    def graph_values(self):
        plt.close()
        col_headers = list(self.FileWithPredictionsInput.columns)
        col_header_combinations = combinations(col_headers, 2)
        # print(col_headers) # for testing
        # print(list(col_header_combinations)) # for testing
        plotnum = 0
        value_figure = plt.figure(5, figsize=(25, 25), clear=True)

        # Iterate through the possible combinations and generate a graph of their features
        for list_element in list(col_header_combinations):
            # print(list_element) # for testing

            if (list_element[0] == "Color" or list_element[1] == "Color"):
                continue

            plotnum += 1

            if plotnum > 18:
                break

            ax = value_figure.add_subplot(6, 3, plotnum)
            # print(list_element[0], list_element[1])
            plt.bar(self.FileWithPredictionsInput[list_element[1]], self.FileWithPredictionsInput[list_element[0]])
            plt.title(list_element[1] + " vs. " + list_element[0])
            plt.xticks(
                rotation=45, 
                horizontalalignment='right',
                fontweight='light'
            )

        plt.tight_layout()
        plt.subplots_adjust(hspace=1)
        plt.savefig('features_subplot.png')
        # plt.show() # again, for testing