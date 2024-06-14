import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from BarFile import Bar
import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("dark")

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
      # errorLabel.configure(text=" ")
    
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

# Beginning of Scatter plot stuff

    icon_image = PhotoImage(file="DatafyLogo.png")


    scatter_page = ctk.CTkToplevel(self.win)

    scatter_page.title("Scatter Plot")

    scatter_page.geometry('400x400')

    scatter_page.iconphoto(False, icon_image)

    scatter_title = ctk.CTkLabel(master=scatter_page,
                             text="Scatter Plot",
                             font=('Comic Sans Bold', 25), text_color="#399adb")

    scatter_title.pack(padx=10, pady=2)

    scatter_prompt = 'How many data points would you like to have? The maximum points you can have are: ' + str(len(self.df))
    scatter_question = ctk.CTkLabel(master=scatter_page, text=scatter_prompt, text_color="#399adb", font=("Comic Sans", 15))
    scatter_question.pack(padx=10, pady=4)

    scatterInput = ctk.CTkEntry(master=scatter_page, fg_color="#399adb", placeholder_text_color='white', placeholder_text="Number of Data Points")
    scatterInput.pack(padx=10, pady=5)
    
     # -------------------------------------------------------------------
    
    selection3 = list(self.df.columns.values)

    selection4 = list(self.df.columns.values)

    scatter_question = ctk.CTkLabel(
      master=scatter_page, text="What selection of data would you like for the x-axis?", text_color="#399adb", font=("Comic Sans" , 15))
    scatter_question.pack(padx=10, pady=7)

    scatter_clicked1 = tk.StringVar()

    scatter_clicked1.set(selection3[0])

    xAxisDropdown1 = ctk.CTkOptionMenu(master=scatter_page, variable=scatter_clicked1, values=selection3, fg_color="#399adb", dropdown_fg_color="#399adb")
    xAxisDropdown1.pack(padx=10, pady=8)

    #------------------------------------------------------------

    scatter_question2 = ctk.CTkLabel(
      master=scatter_page, text="What selection of data would you like for the y-axis?", text_color= "#399adb", font=("Comic Sans", 15))
    scatter_question2.pack(padx=10, pady=10)

    scatter_clicked2 = tk.StringVar()

    scatter_clicked2.set(selection4[1])

    yAxisDropdown2 = ctk.CTkOptionMenu(master=scatter_page, variable=scatter_clicked2, values=selection4, fg_color="#399adb", dropdown_fg_color="#399adb")
    yAxisDropdown2.pack()

    scatter_label = ctk.CTkLabel(
      master=scatter_page,
      text=
      "Click the button to plot your scatter plot! (2 sets of numerical data are needed)", text_color="#399adb", font=("Comic Sans", 15))

    scatter_label.pack(padx=10, pady=12)

    sp_button = ctk.CTkButton(master=scatter_page,
                          text="Plot Scatter Plot",
                          height=25, fg_color= "#399adb",
                          command=makeScatterPlot)

    sp_button.pack(padx=10, pady=13)


