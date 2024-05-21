import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

class Scatter:

  
  
  def __init__(self, win, df):
    self.win = win
    self.df = df

  def __call__(self):

    def plot(dataframe, index1, index2, d1, d2):
      options = dataframe.columns.values

      fig, ax = plt.subplots()

      plt.xlabel(options[index1])
      plt.ylabel(options[index2])
      ax.scatter(d1, d2)

      plt.show()

    def makeScatterPlot():
      errorLabel.config(text=" ")
    
      dataInd1 = selection3.index(scatter_clicked1.get())
      dataInd2 = selection4.index(scatter_clicked2.get())
    
      numberOfRows = int(scatterInput.get())
    
    
    
      scatterInput.delete(0, tk.END)
    
      col1 = self.df.iloc[:numberOfRows, dataInd1]
    
      col2 = self.df.iloc[:numberOfRows, dataInd2]
    
      data1 = []
    
      data2 = []
    
      for x in col1:
        data1.append(x)
      for y in col2:
        data2.append(y)
    
      plot(self.df, dataInd1, dataInd2, data1, data2)

    scatter_page = tk.Toplevel(self.win)

    scatter_page.title("Scatter Plot")

    scatter_page.geometry('400x400')

    scatter_title = tk.Label(master=scatter_page,
                             text="\nScatter Plot",
                             font=('Helvetica bold', 16))

    scatter_title.pack()


# Beginning of Scatter plot stuff

    scatter_prompt = 'How many data points would you like to have? The maximum points you can have are: ' + str(
      len(self.df))
    scatter_question = tk.Label(master=scatter_page, text=scatter_prompt)
    scatter_question.pack()

    errorLabel = tk.Label(master=scatter_page, text="", fg='red', font=('Arial', 7))
    errorLabel.pack()

    scatterInput = tk.Entry(master=scatter_page)
    scatterInput.pack()
    #---------------------------------------------

    selection3 = list(self.df.columns.values)

    selection4 = list(self.df.columns.values)

    scatter_question = tk.Label(
      master=scatter_page, text="What selection of data would you like for the x-axis?")
    scatter_question.pack()

    scatter_clicked1 = tk.StringVar()

    scatter_clicked1.set(selection3[0])

    xAxisDropdown1 = tk.OptionMenu(scatter_page, scatter_clicked1, *selection3)
    xAxisDropdown1.pack()

    #------------------------------------------------------------

    scatter_question2 = tk.Label(
      master=scatter_page, text="What selection of data would you like for the y-axis?")
    scatter_question2.pack()

    scatter_clicked2 = tk.StringVar()

    scatter_clicked2.set(selection4[1])

    yAxisDropdown2 = tk.OptionMenu(scatter_page, scatter_clicked2, *selection4)
    yAxisDropdown2.pack()

    scatter_label = tk.Label(
      master=scatter_page,
      text=
      "Click the button to plot your scatter plot! (2 sets of numerical data are needed)"
    )

    scatter_label.pack()

    sp_button = tk.Button(master=scatter_page,
                          text="Plot Scatter Plot",
                          height=3,
                          command=makeScatterPlot)

    sp_button.pack()


