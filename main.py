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
from Selection import SelectionScreen
import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("dark")

window = ctk.CTk()

window.title("Data Analyzer")

window.geometry("400x400")


#window.resizable(True, True)

# window.attributes('-fullscreen', False)

title = ctk.CTkLabel(master=window, text="DataFy", text_color="#399adb", font=("Comic Sans Bold", 60))

title.pack(pady=20)

selection = SelectionScreen(window)

start_button = ctk.CTkButton(master=window, text="Start", fg_color="#399adb", font= ("Arial", 15), height=25, command=selection.__call__)

start_button.pack()

title_img = ctk.CTkImage(Image.open("titlePhoto.png"), size=(300, 200))



title_img_label = ctk.CTkLabel(master=window, text='', image=title_img)

title_img_label.pack(padx=10, pady=50)

# fileLabel = tk.Label(text=" ", bg='white')
# fileLabel.pack()

# csv_file = filedialog.askopenfilename()

# dataframe = pd.read_csv(csv_file)

# fileLabel.config(text="File used: " + csv_file)

# bar = Bar(window, dataframe)

# scatter = Scatter(window, dataframe)

# linreg = LinReg(window, dataframe)

# bar_button = tk.Button(text="Go to Bar Plot page", command=bar.__call__)

# bar_button.pack()

# scatter_button = tk.Button(text="Go to Scatter Plot page", command=scatter.__call__)

# scatter_button.pack()

# linreg_button = tk.Button(text="Go to Linear Regression Graph page", command=linreg.__call__)

# linreg_button.pack()

window.mainloop()
