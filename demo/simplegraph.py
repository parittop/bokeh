#Ploting
#Importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare somedata
df = pandas.read_csv("data.csv")
x=df["x"]
y=df["y"]

#prepare output file
output_file("line.html")

#create figure object
f=figure()
f.line(x,y)
show(f)
