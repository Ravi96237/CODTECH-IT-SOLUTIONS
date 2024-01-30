import matplotlib.pyplot as plt
import numpy as np


def bar_chart():
    # Generating random marks for each subject
    subjects = ['Telugu', 'Hindi', 'English', 'Mathematics', 'Science', 'Social']
    marks = np.random.randint(50, 100, len(subjects))  # Random marks between 50 and 100

    # Plotting the bar graph
    plt.bar(subjects, marks, color='skyblue')
    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title('Student Marks in Different Subjects')
    plt.ylim(0, 100)  # Setting y-axis limit from 0 to 100
    plt.show()

def pie_chart():
    # src: https://en.wikipedia.org/wiki/Pie_chart
    groups = ['EUL', 'PES', 'EFA', 'EDD', 'ELDR', 'EPP', 'UEN', 'Others']
    seats = [39, 200, 42, 15, 67, 276, 27, 66]

    # Plotting the pie chart
    plt.pie(seats, labels=groups, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.axis('equal')
    plt.title('European Parliament Election - 2004')
    plt.show()

def scatter_plot():

    x_values = np.linspace(0, 10, 10)  # Equal distribution of x values
    y_values = np.abs(x_values - 5) # Trying to make it look like a "V"

    plt.scatter(x_values, y_values, color='red', marker='x', s=100)

    # Additional customization
    plt.axhline(0, color='black', linewidth=1) 
    plt.axvline(5, color='black', linewidth=1)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sample scatter plot')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    bar_chart()
    pie_chart()
    scatter_plot()