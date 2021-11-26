### Module Testing: Graph Generation Algorithm
#### Last committed/pushed 11/25/2021
#### PLEASE NOTE: This is ONLY a report of testing this program on its own. Integration testing with the ML algorithm/menu still needs to happen and be reported!

This portion of the stars ML algorithm program generates graphs largely correctly based on the values present in the Kaggle dataset (located here: https://www.kaggle.com/brsdincer/star-type-classification). Note that this is the only dataset I had to work with, so testing of this code is, by necessity, limited.

You may see these results in the Graph Generation Results folder. These graphs are what will be output to the user:
- Various histograms showing the distribution of data in many of the columns
- Various bar graphs plotting the values of one column against another. Most of the 21 unique combinations of columns are graphed.

Some of the subplots look a bit wonky--it even looks like there is no data in some of them!--but I think that might have something to do with screen size and the fact that I tried to create an 6x3 subplot grid in Matplotlib.

Worth mentioning is that, due to how I coded this, the program will ONLY work if the columns of the csv to be read in are the exact same as those listed in the Kaggle csv. In other words:
- Temperature
- L (for relative luminosity)
- R (for relative radius)
- A_M (for absolute magnitude)
- Color
- Spectral_Class
- Type

I may likely tinker around with this some more:
- [ ] Add the remaining graphs (I personally think that getting ~18 combinations and four other graphs is good, but I can do better for sure)
- [ ] Make it more general (e.g. don't require it to have the same columns as the Kaggle dataset, maybe don't even make it limited to a .csv)
- [ ] Add more to the graphs themselves, like data labels, legends, and different colors
