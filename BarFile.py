import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image


class Bar: 
  
  def __init__(self, win, df):
    self.win = win
    self.df = df


  def __call__(self):

    ctk.set_appearance_mode("dark")
    
    def makeBarGraph():

      new_window = ctk.CTkToplevel(self.win)
  
      new_window.title('Bar Graph')
  
      new_window.geometry('400x400')

      
    
      x_axis = selection1.index(bar_clicked1.get())
      y_axis = selection1.index(bar_clicked2.get())
  
      labels = self.df.iloc[:int(bar_clicked.get()), x_axis]
      data = self.df.iloc[:int(bar_clicked.get()), y_axis]
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

    options = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]


# Creation of main bar window controls and configurations

    icon_image = PhotoImage(file="DatafyLogo.png")
    
    bar_clicked = tk.IntVar()
  
    bar_clicked.set(2)

    selection1 = list(self.df.columns.values)
  
    selection2 = list(self.df.columns.values)

    bar_page = ctk.CTkToplevel(self.win)

    bar_page.title('Bar Graph')

    bar_page.geometry('400x400')

    bar_page.iconphoto(False, icon_image)

    barTitle = ctk.CTkLabel(master=bar_page,
                        text="Bar Graph", text_color="#399adb",
                        font=('Comic Sans Bold', 25))

    barTitle.pack()

    questionLabel = ctk.CTkLabel(
      master=bar_page,
      text="How many column labels of information would you like?", text_color="#399adb",
      font=('Comic Sans', 15),
      width=50)

    questionLabel.pack(padx=10, pady=2)
    dropdown = ctk.CTkOptionMenu(master=bar_page, variable=bar_clicked, values=options, fg_color="#399adb", dropdown_fg_color="#399adb")
    
    dropdown.pack(padx=10, pady=3)

    # Creation of x-axis dropdown and labels for bar graph

    questionLabel = ctk.CTkLabel(
      master=bar_page,
      text="What selection of data would like to choose for the x-axis?", text_color="#399adb", font=('Comic Sans', 15))
    questionLabel.pack(padx=10, pady=6)


    bar_clicked1 = tk.StringVar()

    bar_clicked1.set(selection1[0])

    xAxisDropdown = ctk.CTkOptionMenu(master=bar_page, variable=bar_clicked1, values=selection1, fg_color="#399adb", dropdown_fg_color="#399adb")
    xAxisDropdown.pack(padx=10, pady=7)

    #------------------------------------------------

    # Creation of y-axis dropdown menu and labels for bar graph

    questionLabel2 = ctk.CTkLabel(
      master=bar_page,
      text="What selection of data would like to choose for the y-axis?",  font=("Comic Sans", 15), text_color="#399adb")
    questionLabel2.pack(padx=10, pady=9)

    bar_clicked2 = tk.StringVar()

    bar_clicked2.set(selection1[1])

    yAxisDropdown = ctk.CTkOptionMenu(master=bar_page, variable=bar_clicked2, values=selection2, fg_color="#399adb", dropdown_fg_color="#399adb")
    yAxisDropdown.pack(padx=10, pady=10)
    
    barLabel = ctk.CTkLabel(master=bar_page,
                        text="Click the button below to make a bar graph!", font=("Comic Sans", 15), text_color="#399adb")

    barLabel.pack()

    bg_button = ctk.CTkButton(master=bar_page,
                          text="Plot Bar Graph",
                          height=25, font=("Arial", 15), corner_radius=10,
                          command=makeBarGraph)

    bg_button.pack()



