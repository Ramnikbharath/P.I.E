from matplotlib import pyplot as plt
import pandas as pd

class graph_generator:
    # This function initializes a graph generator based on an input CSV file.
    # The file is read in as a DataFrame to be used with the later functions.
    def __init__(self, FileWithPredictionsInput):
        self.FileWithPredictionsInput = pd.read_csv(FileWithPredictionsInput)
        print(self.FileWithPredictionsInput) # Mainly for testing, feel free to comment out

    # This function generates a graph of each feature, displays it on the screen,
    # and saves the figure to the computer. Histograms are chosen for this purpose
    # since it permits the user to see the distribution of numerical data on the graph.
    def generate_histograms(self):
        plt.close()

        plt.figure(1, figsize=(13, 10))
        self.FileWithPredictionsInput["Color"].value_counts().plot(kind='bar')
        plt.title("Frequency of Star Colors")
        plt.savefig('color_freqs.png')

        plt.figure(2, figsize=(12, 8))
        self.FileWithPredictionsInput["Spectral_Class"].value_counts().plot(kind='bar')
        plt.title("Spectral Classes")
        plt.savefig('spec_freqs.png')

        plt.figure(3, figsize=(13, 10))
        hist = self.FileWithPredictionsInput.hist(["Temperature", "L", "R", "A_M"])
        hist[0, 1].set_title("Luminosity")
        hist[1, 0].set_title("Relative Radius")
        hist[1, 1].set_title("Absolute Magnitude")
        plt.tight_layout()
        plt.savefig('star_hist.png')
        plt.close(3)
        plt.figure(4, figsize=(12, 8))
        self.FileWithPredictionsInput["Type"].value_counts().plot(kind='bar')
        plt.title("Types of Stars")
        self.FileWithPredictionsInput["Type"].value_counts().plot().set_xticklabels(["Red", "Brown", "White", "Main", "Giant", "Hyper"])
        plt.savefig('star_types.png')

    def graph_values(self):
        # To graph columns against columns though I'm not 100% sure why we need this. I'll probably
        # refine the first part of this then push what I have into the repo tomorrow with initial testing results.
        pass