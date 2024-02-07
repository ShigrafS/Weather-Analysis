import pandas as pd
from ydata_profiling import ProfileReport
from reportlab.lib.pagesizes import letter
import reportlab.pdfgen as pdfgen

df = pd.read_csv('weather.csv')

print(df)

profile = ProfileReport(df)
profile.to_file(output_file="weather.html")