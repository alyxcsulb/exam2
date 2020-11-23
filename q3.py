#revised answer for midterm 2 from lecture - Eric's revised code posted in MS Teams

import math
import matplotlib.pyplot as plt # why so slow? https://stackoverflow.com/questions/8955869/why-is-plotting-with-matplotlib-so-slow
import seaborn as sns
import numpy as np
import time

def get_rando_numbers(count=100, min=1, max=20):
    from random import randint
    COUNT = count
    START = min
    END = max
    return [randint(START, END) for x in range(COUNT)]

def is_prime(number):
    for i in range(2, math.floor(math.sqrt(number))):
        if number % i == 0:
            return False
    return True

def get_primes(min, max):
    primes = set()
    for number in range(min, max + 1):
        if is_prime(number):
            primes.add(number)
    print(primes)
    return primes

def show_freq_distribution(chart_title='Frequency Distribution', axis_lbl = '', data=[], data_labels=True, vertical=True):
    '''
    Displays a bar chart representing the frequency distribution of the unique values of a given List object.

            Parameters:
                    chart_title (str): a string representing the chart title
                    axis_lbl (str): a string representing the axis label for the dependent variable 
                    data (List): a list containing the datapoints to be charted 
                    data_labels (bool): a boolean value indicating whether to display the frequency value and percentage over each bar 

            Returns:
                    None
    '''
    this_data = data
    this_y_label = 'Frequency'

    vals, freq = np.unique(this_data, return_counts=True)
    sns.set_style('whitegrid')

    axes = sns.barplot(x=vals, y=freq, palette='bright')
    title = chart_title
    x_label = axis_lbl
    y_label = this_y_label

    axes.set_title(title)
    axes.set(xlabel=x_label, ylabel=y_label)
    axes.set_ylim(top=max(freq) * 1.10)

    for bar, freq in zip(axes.patches, freq):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = ''
        if data_labels:
            text = f'{freq:,}\n{freq / len(this_data):.3%}'
        axes.text(text_x, text_y, text, fontsize=9, ha='center', va='bottom')

    plt.show()

MIN = 1000
MAX = 1050
def main():
    start = time.time()
    COUNT = 10_000_000

    #for testing
    #COUNT = 100
    #primes = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049]

    rando_numbers = get_rando_numbers(COUNT, MIN, MAX) # generate random integers from MIN to MAX inclusively
    primes = get_primes(MIN, MAX)

    end1 = time.time()
    print(f'Execution time: {end1 - start} sec') 

    random_primes = []
    for number in rando_numbers:
        if number in primes:
        #if is_prime(number):
            random_primes.append(number)
    
    end2 = time.time()
    print(f'Execution time: {end2 - end1} sec') 
    
    show_freq_distribution(chart_title='Frequency Distribution', axis_lbl = 'Primes', data=random_primes, data_labels=True, vertical=True)


main()