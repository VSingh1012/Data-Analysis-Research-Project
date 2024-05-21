import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk


class Bar: 
  
  def __init__(self, win, df):
    self.win = win
    self.df = df


  def __call__(self):
  
    def makeBarGraph():

      new_window = tk.Toplevel(self.win)
  
      new_window.title('Bar Graph')
  
      new_window.geometry('400x400')
  
    
      x_axis = selection1.index(bar_clicked1.get())
      y_axis = selection1.index(bar_clicked2.get())
  
      labels = self.df.iloc[:bar_clicked.get(), x_axis]
      data = self.df.iloc[:bar_clicked.get(), y_axis]
      label_values = []
      numerical_vals = []
  
      for val in labels:
        label_values.append(val)
      for element in data:
        numerical_vals.append(element)
  
      plt.bar(label_values, numerical_vals)
  
      fig = plt.figure(1)
  
      canvas = FigureCanvasTkAgg(fig, master=new_window)
  
      plot_widget = canvas.get_tk_widget()
  
      plot_widget.pack()

    options = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  
    bar_clicked = tk.IntVar()
  
    bar_clicked.set(2)

    selection1 = list(self.df.columns.values)
  
    selection2 = list(self.df.columns.values)

    bar_page = tk.Toplevel(self.win)

    bar_page.title('Bar Graph')

    bar_page.geometry('400x400')

    barTitle = tk.Label(master=bar_page,
                        text="Bar Graph",
                        font=('Helvetica bold', 16))

    barTitle.pack()

    questionLabel = tk.Label(
      master=bar_page,
      text="How many column labels of information would you like?",
      width=50)

    questionLabel.pack()


    # Creation of x-axis dropdown and labels for bar graph

    questionLabel = tk.Label(
      master=bar_page,
      text="What selection of data would like to choose for the x-axis?")
    questionLabel.pack()

    dropdown = tk.OptionMenu(bar_page, bar_clicked, *options)

    dropdown.pack()

    bar_clicked1 = tk.StringVar()

    bar_clicked1.set(selection1[0])

    xAxisDropdown = tk.OptionMenu(bar_page, bar_clicked1, *selection1)
    xAxisDropdown.pack()

    #------------------------------------------------

    # Creation of y-axis dropdown menu and labels for bar graph

    questionLabel2 = tk.Label(
      master=bar_page,
      text="What selection of data would like to choose for the y-axis?")
    questionLabel2.pack()

    bar_clicked2 = tk.StringVar()

    bar_clicked2.set(selection1[1])

    yAxisDropdown = tk.OptionMenu(bar_page, bar_clicked2, *selection2)
    yAxisDropdown.pack()
    
    barLabel = tk.Label(master=bar_page,
                        text="Click the button below to make a bar graph!")

    barLabel.pack()

    bg_button = tk.Button(master=bar_page,
                          text="Plot Bar Graph",
                          height=3,
                          command=makeBarGraph)

    bg_button.pack()



