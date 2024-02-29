# Only works in Python 3 (Created in 3.4.2)
# tkinter comes as part of the standard install - messagebox has to be imported explicitly

from tkinter import *
from tkinter import messagebox

def saveHoliday() :
    # for each field get the value from the screen and pad with spaces or chop if necessary
    HolidayIDSave = HolidayIDVar.get()
    HolidayIDSave = HolidayIDSave.ljust(50)
    
    HolidayNameSave=HolidayNameVar.get()
    HolidayNameSave = HolidayNameSave.ljust(50)
    
    LocationSave = LocationVar.get()
    LocationSave = LocationSave.ljust(50)
    
    HolidayTypeSave = HolidayTypeVar.get()
    HolidayTypeSave = HolidayTypeSave.ljust(50)
    
    RatingSave = RatingVar.get()
    RatingSave = RatingSave.ljust(50)
    

    
    #open the file to append - if it's not there it'll be created
    fileObject = open("Holidays.txt","a")
    # write to the file with a newline character at the end
    fileObject.write(HolidayIDSave + HolidayNameSave + LocationSave + HolidayTypeSave + RatingSave + "\n")
    fileObject.close()
    
    return

def countHoliday() :
    HolidayCount=0
    CountNeeded=0

    #get the fields off the screen and validate them
    HolidayIDSave = HolidayIDVar.get()
    
    HolidayNameSave=HolidayNameVar.get()
    
    LocationSave = LocationVar.get()
    
    HolidayTypeSave = HolidayTypeVar.get()
    
    RatingSave = RatingVar.get()

    #    ". . . ." Indicates missing or broken code.  
    
    if not HolidayIDSave == "" :
        CountNeeded +=1
    if not HolidayNameSave == "" :
        CountNeeded +=1
    if not LocationSave == "" :
        CountNeeded +=1
    if not HolidayTypeSave == "" :
        CountNeeded +=1
    if not RatingSave == "" :
        CountNeeded +=1
    

    if CountNeeded == 0 :
        messagebox.showerror("Error","Please enter something to count!")
        return
    # try opening the file for reading
    try:
        fileObject=open("Holidays.txt","r")
        
    # if it's not there then say
    except IOError:
        messagebox.showerror("Error","No file to read")

    # if we did open it then let's carry on!
    else:
        while True:
            CountGot=0
            recordVar=fileObject.readline()
            # Python keeps reading till EOF then returns a blank
            if recordVar=="":
                fileObject.close()
                break
         
            if HolidayIDSave in recordVar[0:50] and not HolidayIDSave=="" :
                CountGot +=1
            if HolidayNameSave in recordVar[50:100] and not HolidayNameSave=="" :
                CountGot +=1
            if LocationSave in recordVar[100:150] and not LocationSave=="":
                CountGot +=1
            if HolidayTypeSave in recordVar[150:200] and not HolidayTypeSave =="":
                CountGot +=1
            if RatingSave in recordVar[200:250] and not RatingSave=="":
                CountGot +=1
          
            if CountGot == CountNeeded:
                HolidayCount = HolidayCount + 1
                
        messagebox.showinfo("Found: ",str("Item has been found"))    
    
    return


def makeWindow():
    #declared the globals here as this is the 1st routine called
    # the other routines have to be in front of this one as they get called by it
    # and the parser may throw an error if they weren't there
    
    global HolidayIDVar, HolidayNameVar, LocationVar, HolidayTypeVar, RatingVar

    #here's my window
    win = Tk()
    
    #split into two sections then further split into a grid
    frame1=Frame(win)
    frame1.pack()

    Label(frame1, text="Holidays", font=("Helvetica 12 bold")).grid(row=0, column=0)
    
    Label(frame1, text="HolidayID").grid(row=1, column=0, sticky=W)
    HolidayIDVar=StringVar()
    HolidayID= Entry(frame1, textvariable=HolidayIDVar)
    HolidayID.grid(row=1,column=1,sticky=W)

    Label(frame1, text="HolidayName").grid(row=2, column=0, sticky=W)
    HolidayNameVar=StringVar()
    HolidayName= Entry(frame1, textvariable=HolidayNameVar)
    HolidayName.grid(row=2,column=1,sticky=W)

    Label(frame1, text="Location").grid(row=3, column=0, sticky=W)
    LocationVar=StringVar()
    Location= Entry(frame1, textvariable=LocationVar)
    Location.grid(row=3,column=1,sticky=W)
    
    Label(frame1, text="HolidayType").grid(row=4, column=0, sticky=W)
    HolidayTypeVar=StringVar()
    HolidayType= Entry(frame1, textvariable=HolidayTypeVar)
    HolidayType.grid(row=4,column=1,sticky=W)
    
    Label(frame1, text="Rating").grid(row=5, column=0, sticky=W)
    RatingVar=StringVar()
    Rating= Entry(frame1, textvariable=RatingVar)
    Rating.grid(row=5,column=1,sticky=W)
    
   
  

    frame2 = Frame(win)
    frame2.pack()

    # build my buttons in the other frame then pack them side by side
    b1= Button(frame2, text=" Save ", command=saveHoliday)
    b2= Button(frame2, text=" Count ", command=countHoliday)
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    
    return win


#this is the main program!
win = makeWindow()
win.mainloop()
