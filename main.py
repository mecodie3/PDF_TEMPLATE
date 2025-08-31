#create pdf instances
from fpdf import FPDF
#data analysis
import pandas as pd

pdf = FPDF(orientation="P",unit="mm",format="A4")
#to manage the footer,by default it is True
pdf.set_auto_page_break(auto=False,margin=0)
#create dataframe
df=pd.read_csv("topics.csv")

for index,row in df.iterrows():

    #add main page with the header
    pdf.add_page()
    pdf.set_font(family="Times" , style="B", size=24)
    #grey color
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="L",
         ln=1)

    #add multiple lines,every 10mm
    for y in range(20,298,10):
        pdf.line(10,y,200,y)
    pdf.line(10,21,200,21)

    #add the footer:in mm
    pdf.ln(265)
    #add the text in the footer side
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R")


    #add the other pages,depending what column Pages requires
    for i in range(row["Pages"]-1):
        pdf.add_page()
        #set the footer in the nested loop
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # add multiple lines,every 10mm
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)
pdf.output("output.pdf")


