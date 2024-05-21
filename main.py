import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from BarFile import Bar
from LinRegFile import LinReg
from ScatterFile import Scatter


window = tk.Tk()

window.title("Data Analyzer")

window.geometry("400x400")

window.resizable(True, True)

window.attributes('-fullscreen', False)

title = tk.Label(text="Data Analyzer", font=("Arial", 40))

title.pack(pady=20)

fileLabel = tk.Label(text=" ", bg='white')
fileLabel.pack()

csv_file = filedialog.askopenfilename()

dataframe = pd.read_csv(csv_file)

fileLabel.config(text="File used: " + csv_file)

bar = Bar(window, dataframe)

scatter = Scatter(window, dataframe)

linreg = LinReg(window, dataframe)

bar_button = tk.Button(text="Go to Bar Plot page", command=bar.__call__)

bar_button.pack()

scatter_button = tk.Button(text="Go to Scatter Plot page", command=scatter.__call__)

scatter_button.pack()

linreg_button = tk.Button(text="Go to Linear Regression Graph page", command=linreg.__call__)

linreg_button.pack()

window.mainloop()
