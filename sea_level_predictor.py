import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level', figsize=(20,10))
    

    # Create first line of best fit
    first_line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_Ax = np.arange(df['Year'].min(),2050,1)
    y_Ax = x_Ax * first_line.slope + first_line.intercept

    plt.plot(x_Ax,y_Ax)
    plt.show()
    # Create second line of best fit
    df1= df.loc[df['Year'] >= 2000]
    
    sec_line = linregress(df1['Year'], df1['CSIRO Adjusted Sea Level'])
    x_Ax = np.arange(df1['Year'].min(),2050,1)
    y_Ax = x_Ax * sec_line.slope + sec_line.intercept

    plt.plot(x_Ax,y_Ax)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()