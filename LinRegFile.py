import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk



class LinReg:
  def __init__(self, win, df):
    self.win = win
    self.df = df

  def __call__(self):
    
    def makeLine():
      
      errorLabel2.config(text="")
    
      chosen_val = selection5.index(lin_clicked.get())
      chosen_val2 = selection6.index(lin_clicked2.get())
    
      numPoints = int(linInput.get())
    
    
      data_selection = self.df.iloc[:numPoints, chosen_val]
      data_selection2 = self.df.iloc[:numPoints, chosen_val2]
    
      linInput.delete(0, tk.END)
    
      newData = []
      newData2 = []
    
      for o in data_selection:
        newData.append(o)
      for i in data_selection2:
        newData2.append(i)
    
      plt.plot(newData, newData2)
    
      plt.show()


# Start of Linear Regression Setup 


    lr_page = tk.Toplevel(self.win)

    lr_page.title("Linear Regression Page")

    lr_page.geometry("400x400")

    lr_title = tk.Label(master=lr_page,
                        text="\nLinear Regression",
                        font=('Helvetica Bold', 16))
    lr_title.pack()

    scatter_prompt = 'How many data points would you like to have? The maximum points you can have are: ' + str(
      len(self.df))

    lin_question = tk.Label(master=lr_page, text=scatter_prompt)
    lin_question.pack()

    errorLabel2 = tk.Label(master=lr_page, text="", fg='red', font=('Arial', 7))
    errorLabel2.pack()

    linInput = tk.Entry(master=lr_page)
    linInput.pack()

    selection5 = list(self.df.columns.values)
    selection6 = list(self.df.columns.values)

    #---------------------------------------------------------------------
    lin_label1 = tk.Label( 
      master=lr_page, text="What selection of data would you like for the x-axis?")
    lin_label1.pack()

    lin_clicked = tk.StringVar()

    lin_clicked.set(selection5[0])

    xAxisDropdown3 = tk.OptionMenu(lr_page, lin_clicked, *selection5)
    xAxisDropdown3.pack()

    #---------------------------------------------------------------------

    lin_label2 = tk.Label(
      master=lr_page, text="What selection of data would you like for the y-axis?")
    lin_label2.pack()

    lin_clicked2 = tk.StringVar()

    lin_clicked2.set(selection6[1])

    yAxisDropdown3 = tk.OptionMenu(lr_page, lin_clicked2, *selection6)
    yAxisDropdown3.pack()

    #---------------------------------------------------------------------

    lr_question = tk.Label(
      master=lr_page,
      text="Click the button below to plot a Linear Regression plot!")
    lr_question.pack()

    lr_button = tk.Button(master=lr_page,
                          text="Plot Linear Regression",
                          height=3,
                          command=makeLine)
    lr_button.pack()
      
