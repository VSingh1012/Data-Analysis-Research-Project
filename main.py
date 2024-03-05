import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk


def makeBarGraph():

  new_window = tk.Toplevel(win)

  new_window.title('Bar Graph')

  new_window.geometry('400x400')


  plt.bar(label_values, numerical_vals)

  fig = plt.figure(1)

  canvas = FigureCanvasTkAgg(fig, master=new_window)

  plot_widget = canvas.get_tk_widget()

  plot_widget.pack()


def makeLine():

  try:

    errorLabel2.config(text="")

    chosen_val = selection5.index(lin_clicked.get())
    chosen_val2 = selection6.index(lin_clicked2.get())

    numPoints = int(linInput.get())

    maxDataPoints = len(df.axes[0])

    data_selection = df.iloc[:numPoints, chosen_val]
    data_selection2 = df.iloc[:numPoints, chosen_val2]

    linInput.delete(0, tk.END)

    newData = []
    newData2 = []

    for o in data_selection:
      newData.append(o)
    for i in data_selection2:
      newData2.append(i)

    plt.plot(newData, newData2)

    plt.show()

  except TypeError:

    if (numPoints > maxDataPoints):
      errorLabel2.config(
        text=
        "You have exceeded the amount of data from this dataset, maximum data points are "
        + str(maxDataPoints))


def plot(dataframe, index1, index2, d1, d2):
  options = dataframe.columns.values

  fig, ax = plt.subplots()

  plt.xlabel(options[index1])
  plt.ylabel(options[index2])
  ax.scatter(d1, d2)

  plt.show()


def makeScatterPlot():

  try:

    errorLabel.config(text=" ")

    dataInd1 = selection3.index(scatter_clicked1.get())
    dataInd2 = selection4.index(scatter_clicked2.get())

    numberOfRows = int(scatterInput.get())

    maxRows = len(df.axes[0])

    scatterInput.delete(0, tk.END)

    col1 = df.iloc[:numberOfRows, dataInd1]

    col2 = df.iloc[:numberOfRows, dataInd2]

    data1 = []

    data2 = []

    for x in col1:
      data1.append(x)
    for y in col2:
      data2.append(y)

    plot(df, dataInd1, dataInd2, data1, data2)

  except:

    if (numberOfRows > maxRows):
      errorLabel.config(
        text=
        'You have exceeded the amount of data from this dataset, maximum data points are '
        + str(maxRows))


# Main Window setup with with main prompts and questions

win = tk.Tk()

win.title("Data Analyzer")

win.geometry("400x400")

win.resizable(True, True)

win.attributes('-fullscreen', False)

main_frame = tk.Frame(win)

main_frame.pack(fill=tk.BOTH, expand=1)

canvas = tk.Canvas(master=main_frame)

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = ttk.Scrollbar(master=main_frame,
                          orient=tk.VERTICAL,
                          command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>',
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

frame2 = tk.Frame(canvas)

canvas.create_window((0, 0), window=frame2, anchor="nw")

# Bar Graph Prompts -------------------------------------------------

fileLabel = tk.Label(text=" ", bg='white')
fileLabel.pack()

csv_file = filedialog.askopenfilename()

df = pd.read_csv(csv_file)

fileLabel.config(text="File used: " + csv_file)

barTitle = tk.Label(master=frame2,
                    text="Bar Graph",
                    font=('Helvetica bold', 16))

barTitle.pack()

questionLabel = tk.Label(
  master=frame2,
  text="How many column labels of information would you like?",
  width=50)

questionLabel.pack()

options = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

bar_clicked = tk.IntVar()

bar_clicked.set(2)

dropdown = tk.OptionMenu(frame2, bar_clicked, *options)

dropdown.pack()

selection1 = list(df.columns.values)

selection2 = list(df.columns.values)

# Creation of x-axis dropdown and labels for bar graph

questionLabel = tk.Label(
  master=frame2,
  text="What selection of data would like to choose for the x-axis?")
questionLabel.pack()

bar_clicked1 = tk.StringVar()

bar_clicked1.set(selection1[0])

xAxisDropdown = tk.OptionMenu(frame2, bar_clicked1, *selection1)
xAxisDropdown.pack()

#------------------------------------------------

# Creation of y-axis dropdown menu and labels for bar graph

questionLabel2 = tk.Label(
  master=frame2,
  text="What selection of data would like to choose for the y-axis?")
questionLabel2.pack()

bar_clicked2 = tk.StringVar()

bar_clicked2.set(selection1[1])

yAxisDropdown = tk.OptionMenu(frame2, bar_clicked2, *selection1)
yAxisDropdown.pack()



#for x in range(len(selection1)-1):
  #taken_val = df.iloc[0, x]
  #lab_type = str(type(taken_val))
  #if (lab_type[8:11] != "str"): 
   # selection1.remove(selection1[x])


x_axis = selection1.index(bar_clicked1.get())
y_axis = selection1.index(bar_clicked2.get())

labels = df.iloc[:bar_clicked.get(), x_axis]
data = df.iloc[:bar_clicked.get(), y_axis]
label_values = []
numerical_vals = []

for val in labels:
  label_values.append(val)
for element in data:
  numerical_vals.append(element)


barLabel = tk.Label(master=frame2,
                    text="Click the button below to make a bar graph!")

barLabel.pack()

bg_button = tk.Button(master=frame2,
                      text="Plot Bar Graph",
                      height=3,
                      command=makeBarGraph)

bg_button.pack()

# Scatter Plot Prompts ---------------------------------------

scatter_title = tk.Label(master=frame2,
                         text="\nScatter Plot",
                         font=('Helvetica bold', 16))

scatter_title.pack()

scatter_prompt = 'How many data points would you like to have? The maximum points you can have are: ' + str(
  len(df))

scatter_question = tk.Label(master=frame2, text=scatter_prompt)
scatter_question.pack()

errorLabel = tk.Label(master=frame2, text="", fg='red', font=('Arial', 7))
errorLabel.pack()

scatterInput = tk.Entry(master=frame2)
scatterInput.pack()
#---------------------------------------------

selection3 = list(df.columns.values)

selection4 = list(df.columns.values)

scatter_question = tk.Label(
  master=frame2, text="What selection of data would you like for the x-axis?")
scatter_question.pack()

scatter_clicked1 = tk.StringVar()

scatter_clicked1.set(selection3[0])

xAxisDropdown1 = tk.OptionMenu(frame2, scatter_clicked1, *selection3)
xAxisDropdown1.pack()

#------------------------------------------------------------

scatter_question2 = tk.Label(
  master=frame2, text="What selection of data would you like for the y-axis?")
scatter_question2.pack()

scatter_clicked2 = tk.StringVar()

scatter_clicked2.set(selection4[1])

yAxisDropdown2 = tk.OptionMenu(frame2, scatter_clicked2, *selection4)
yAxisDropdown2.pack()

scatter_label = tk.Label(
  master=frame2,
  text=
  "Click the button to plot your scatter plot! (2 sets of numerical data are needed)"
)

scatter_label.pack()

sp_button = tk.Button(master=frame2,
                      text="Plot Scatter Plot",
                      height=3,
                      command=makeScatterPlot)

sp_button.pack()

# Linear Regression Plot Prompts ------------------------------------------------

lr_title = tk.Label(master=frame2,
                    text="\nLinear Regression",
                    font=('Helvetica Bold', 16))
lr_title.pack()

lin_question = tk.Label(master=frame2, text=scatter_prompt)
lin_question.pack()

errorLabel2 = tk.Label(master=frame2, text="", fg='red', font=('Arial', 7))
errorLabel2.pack()

linInput = tk.Entry(master=frame2)
linInput.pack()

selection5 = list(df.columns.values)
selection6 = list(df.columns.values)

#---------------------------------------------------------------------
lin_label1 = tk.Label(
  master=frame2, text="What selection of data would you like for the x-axis?")
lin_label1.pack()

lin_clicked = tk.StringVar()

lin_clicked.set(selection5[0])

xAxisDropdown3 = tk.OptionMenu(frame2, lin_clicked, *selection5)
xAxisDropdown3.pack()

#---------------------------------------------------------------------

lin_label2 = tk.Label(
  master=frame2, text="What selection of data would you like for the y-axis?")
lin_label2.pack()

lin_clicked2 = tk.StringVar()

lin_clicked2.set(selection6[1])

yAxisDropdown3 = tk.OptionMenu(frame2, lin_clicked2, *selection6)
yAxisDropdown3.pack()

#---------------------------------------------------------------------

bw_question = tk.Label(
  master=frame2,
  text="Click the button below to plot a Linear Regression plot!")
bw_question.pack()

bw_button = tk.Button(master=frame2,
                      text="Plot Linear Regression",
                      height=3,
                      command=makeLine)
bw_button.pack()

win.mainloop()
