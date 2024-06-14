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
import customtkinter as ctk
from PIL import ImageTk, Image


class SelectionScreen:

  def __init__(self, win):
    self.win = win

  def __call__(self):

    icon_image = PhotoImage(file="DatafyLogo.png")

    ctk.set_appearance_mode("dark")

    self.win.withdraw()

    main_screen = ctk.CTkToplevel(self.win)

    main_screen.title("Data Analyzer")

    main_screen.geometry("400x400")

    main_screen.resizable(True, True)

    main_screen.iconphoto(False, icon_image)

    csv_file = filedialog.askopenfilename()

    dataframe = pd.read_csv(csv_file)

    fileLabel = ctk.CTkLabel(master=self.win,
                             text=" ",
                             bg_color='white',
                             font=("Comic Sans", 10),
                             text_color='black')
    fileLabel.pack()

    fileLabel.configure(text="File used: " + csv_file)

    bar = Bar(self.win, dataframe)

    scatter = Scatter(self.win, dataframe)

    linreg = LinReg(self.win, dataframe)

    def back_to_main():
      self.win.deiconify()

      main_screen.withdraw()

    selection_title = ctk.CTkLabel(master=main_screen,
                                   text="Data Analyzer",
                                   font=('Comic Sans Bold', 35),
                                   text_color="#399adb")

    selection_title.pack()

    bar_image = ctk.CTkImage(Image.open("bargraph.png"), size=(60, 60))

    scatter_image = ctk.CTkImage(Image.open("scatterplot.png"), size=(60, 60))

    linreg_image = ctk.CTkImage(Image.open("linreg.png"), size=(60, 60))

    bar_button = ctk.CTkButton(master=main_screen,
                               image=bar_image,
                               text="Go to Bar Plot page",
                               font=("Arial", 15),
                               fg_color="#399adb",
                               command=bar.__call__)

    bar_button.pack(padx=10, pady=15)

    scatter_button = ctk.CTkButton(main_screen,
                                   image=scatter_image,
                                   text="Go to Scatter Plot page",
                                   font=('Arial', 15),
                                   fg_color="#399adb",
                                   command=scatter.__call__)

    scatter_button.pack(padx=10, pady=20)

    linreg_button = ctk.CTkButton(main_screen,
                                  image=linreg_image,
                                  text="Go to Linear Regression Graph page",
                                  font=('Arial', 15),
                                  fg_color="#399adb",
                                  command=linreg.__call__)

    linreg_button.pack(padx=10, pady=30)

    back_button = ctk.CTkButton(master=main_screen,
                                text="Back to Main Menu",
                                fg_color="#399adb",
                                height=25,
                                font=("Arial", 15),
                                command=back_to_main)

    back_button.pack(padx=10, pady=34)
