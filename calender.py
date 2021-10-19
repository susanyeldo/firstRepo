#import calendar module
import calendar
#import tkinter module
from tkinter import *
def showCalender():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calender for the year")
    gui.geometry("600x600")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    
    calYear = Label(gui, text= "Calender for the Year" +gui_content, font= "Consolas 10 bold")
    calYear.grid(row=1, column=1)
 
    
    gui.mainloop()


if __name__=='__main__':
    new = Tk()
    new.config(background='gray')
    new.title("Calender")
    new.geometry("260x200")
    cal = Label(new, text="Calender",bg='grey',font=("times", 28, "bold"), fg='yellow')
    
    #Label for enter year
    year = Label(new, text="Enter year: ", bg='grey', fg='white')
    
    #text box for year input
    year_field=Entry(new)
    button = Button(new, text='Show Calender',fg='Black',bg='Blue',command=showCalender)
     #adjusting widgets in position
    
    cal.grid(row=1, column=2, pady=6)
    year.grid(row=5, column=1)
    year_field.grid(row=5, column=2, pady=10)
    button.grid(row=8, column=2)
    
    """new.mainloop()"""


