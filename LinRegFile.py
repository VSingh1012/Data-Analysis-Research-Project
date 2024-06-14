import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("dark")

class LinReg:
  def __init__(self, win, df):
    self.win = win
    self.df = df

  def __call__(self):
    
    def makeLine():
      
    #  errorLabel2.configure(text="")
    
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


# Start of Linear Regression Setup (Universal Color: "#399adb")

    icon_image = PhotoImage(file="DatafyLogo.png")

    lr_page = ctk.CTkToplevel(self.win)

    lr_page.title("Linear Regression Page")

    lr_page.geometry("400x400")

    lr_page.iconphoto(False, icon_image)

    lr_title = ctk.CTkLabel(master=lr_page,
                        text="\nLinear Regression",
                        font=('Comic Sans Bold', 25), text_color="#399adb")
    lr_title.pack(padx=10, pady=2)

    scatter_prompt = 'How many data points would you like to have? The maximum points you can have are: ' + str(
      len(self.df))

    lin_question = ctk.CTkLabel(master=lr_page, text=scatter_prompt, text_color="#399adb", font=("Comic Sans", 15))
    lin_question.pack(padx=10, pady=4)

    linInput = ctk.CTkEntry(master=lr_page,fg_color="#399adb", placeholder_text_color='white', placeholder_text="Number of Data Points")
    linInput.pack(padx=10, pady=5)

    selection5 = list(self.df.columns.values)
    selection6 = list(self.df.columns.values)

    #---------------------------------------------------------------------
    lin_label1 = ctk.CTkLabel( 
      master=lr_page, text="What selection of data would you like for the x-axis?", text_color="#399adb", font=("Comic Sans", 15))
    lin_label1.pack(padx=10, pady=7)

    lin_clicked = tk.StringVar()

    lin_clicked.set(selection5[0])

    xAxisDropdown3 = ctk.CTkOptionMenu(master=lr_page, variable=lin_clicked, values=selection5, fg_color="#399adb", dropdown_fg_color="#399adb")
    xAxisDropdown3.pack(padx=10, pady=8)

    #---------------------------------------------------------------------

    lin_label2 = ctk.CTkLabel(
      master=lr_page, text="What selection of data would you like for the y-axis?", font=("Comic Sans", 15), text_color="#399adb")
    lin_label2.pack(padx=10, pady=10)

    lin_clicked2 = tk.StringVar()

    lin_clicked2.set(selection6[1])

    yAxisDropdown3 = ctk.CTkOptionMenu(master=lr_page, variable=lin_clicked2, values=selection6, fg_color="#399adb", dropdown_fg_color="#399adb")
    yAxisDropdown3.pack(padx=10, pady=11)

    #---------------------------------------------------------------------

    lr_question = ctk.CTkLabel(
      master=lr_page,
      text="Click the button below to plot a Linear Regression plot!", font=('Comic Sans', 15), text_color="#399adb")
    lr_question.pack(padx=10, pady=13)

    lr_button = ctk.CTkButton(master=lr_page,
                          text="Plot Linear Regression", fg_color="#399adb", height=25, font=("Arial", 15), command=makeLine)
                        
    lr_button.pack(padx=10, pady=13)
      
