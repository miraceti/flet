import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")

def main(page: ft.Page):
    # Generate sample data
    data = np.random.rand(10, 10)
    
    fig, ax = plt.subplots()
    # Create a heatmap
    im = ax.imshow(data, cmap='hot', interpolation='nearest')
    fig.colorbar(im)  # Add a colorbar
    
    # Set axis labels
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    
    # Set the title
    ax.set_title('Example of a heatmap')
    
    # Display the plot
    page.add(MatplotlibChart(fig, expand=True))

ft.app(target=main)