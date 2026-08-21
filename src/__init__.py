import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("UMA")
app.geometry("1000x1000")

tabview = customtkinter.CTkTabview(master=app, width=800, height=600)
tabview.grid(padx=0, pady=0)

tabview.add("Distance") # add tab at the end
tabview.add("tab 2") # add tab at the end
tabview.set("Distance") # set currently visible tab



# button_feetConvert | Convert inches (default) to feet [get entry text, convert to float, divide by 12, set new text]

# Check list:
#
# Common Distance Math: 
#
# Milimeters Conversion ->  DONE
# Centimeters Conversion -> DONE
# Feet Conversion->         DONE
# Yards Conversion ->       DONE
# Meters Conversion ->      DONE
# Decameters Conversion ->  DONE
# Hectometers Conversion -> DONE
# Kilometers Conversion ->  DONE
# Miles Conversion ->       DONE
# Nautical Miles ->         DONE
#
#

def convert_on_key_release(event):
    print(f"Key released: {event.keysym}")
    distConvert()
    comboCalc()

def distConvert(): # Every conversion here (Distance)
    milimetersConvert()
    centimetersConvert()
    feetConvert()
    yardsConvert()
    metersConvert()
    decametersConvert()
    hectometersConvert()
    kilometersConvert()
    milesConvert()
    nauticalConvert()


def milimetersConvert():
    text_newMilimeters = entry.get()
    text_finalNewMilimeters = float(text_newMilimeters)
    text_finalNewMilimeters = text_finalNewMilimeters * 25.4
    str(text_finalNewMilimeters)
    label_milimeters.configure(text=text_finalNewMilimeters)

def centimetersConvert():
    text_newCentimeters = entry.get()
    text_finalNewCentimeters = float(text_newCentimeters)
    text_finalNewCentimeters = text_finalNewCentimeters * 2.54
    str(text_finalNewCentimeters)
    label_centimeters.configure(text=text_finalNewCentimeters)

def feetConvert():
    text_newFeet = entry.get()
    text_finalNewFeet = float(text_newFeet)
    text_finalNewFeet = text_finalNewFeet / 12
    str(text_finalNewFeet)
    label_feet.configure(text=text_finalNewFeet)

def yardsConvert():
    text_newYards = entry.get()
    text_finalNewYards = float(text_newYards)
    text_finalNewYards = text_finalNewYards / 36
    str(text_finalNewYards)
    label_yards.configure(text=text_finalNewYards)

def metersConvert():
    text_newMeters = entry.get()
    text_finalNewMeters = float(text_newMeters)
    text_finalNewMeters = text_finalNewMeters / 39.37
    str(text_finalNewMeters)
    label_meters.configure(text=text_finalNewMeters)

def decametersConvert():
    text_newDecameters = entry.get()
    text_finalNewDecameters = float(text_newDecameters)
    text_finalNewDecameters = text_finalNewDecameters / 393.7
    str(text_finalNewDecameters)
    label_decameters.configure(text=text_finalNewDecameters)

def hectometersConvert():
    text_newHectometers = entry.get()
    text_finalNewHectometers = float(text_newHectometers)
    text_finalNewHectometers = text_finalNewHectometers / 3937
    label_hectometers.configure(text=text_finalNewHectometers)

def kilometersConvert():
    text_newKilometers = entry.get()
    text_finalNewKilometers = float(text_newKilometers)
    text_finalNewKilometers = text_finalNewKilometers / 39370
    label_kilometers.configure(text=text_finalNewKilometers)

def milesConvert():
    text_newMiles = entry.get()
    text_finalNewMiles = float(text_newMiles)
    text_finalNewMiles = text_finalNewMiles / 63360
    label_miles.configure(text=text_finalNewMiles)

def nauticalConvert():
    text_newNautical = entry.get()
    text_finalNewNautical = float(text_newNautical)
    text_finalNewNautical = text_finalNewNautical / 72910
    label_nauticalmiles.configure(text=text_finalNewNautical)

# Retrieve combobox value for calculation with combobox.get()
# Combobox output is label_comboCalcOut
# -----------------------------------------
# Order of operations:
# 1. Grab entry.get() | Take user input
# 2. Grab first combobox | The FROM unit
# 3. Grab second combobox | the TO unit
# 4. What is math for converting every unit to the other?
# 
#
#
#
UNIT_TO_METERS = {
    "Milimeters": 0.001,
    "Centimeters": 0.01,
    "Inches": 0.0254,
    "Feet": 0.3048,
    "Yards": 0.9144,
    "Meters": 1.0,
    "Decameters": 10.0,
    "Hectometers": 100.0,
    "Kilometers": 1000.0,
    "Miles": 1609.344,
    "Nautical Miles": 1852.0
}


def comboCalc():
    userInput = float(entry.get())
    fromInput = combobox.get()
    toInput = combobox2.get()
    inputToMeters = userInput * UNIT_TO_METERS[fromInput]
    finalConversion = inputToMeters / UNIT_TO_METERS[toInput]
    label_comboCalcOut.configure(text=f"{userInput} = {finalConversion:.6g} {toInput}")
#    new_comboVar1 = float(combobox.get())
#    print(new_comboVar1)
#    new_comboVar2 = float(combobox2.get())
#    final_comboOut = new_comboVar1+new_comboVar2
#    label_comboCalcOut.configure(text=final_comboOut)

# How to grab text from entry -> entry.get() / varName.get()
#-------------------------------

# Left Hand Frame

left_frame = customtkinter.CTkFrame(master=tabview.tab("Distance"), fg_color="transparent")
left_frame.grid(row=0, column=0, rowspan=11, sticky="nw", padx=10, pady=10)




# Create widgets
# Left_frame
button_feetConvert = customtkinter.CTkButton(master=left_frame,command=distConvert, text="Convert")
entry = customtkinter.CTkEntry(master=left_frame)
text_custom = customtkinter.CTkLabel(master=left_frame, text="Custom Conversion")
text_custom2 = customtkinter.CTkLabel(master=left_frame, text="To")
# Inches
text_inches = customtkinter.CTkLabel(master=tabview.tab("Distance"), text="(In Inches)")

# Milimeters
label_milimeters = customtkinter.CTkLabel(master=tabview.tab("Distance"))
text_milimeters = customtkinter.CTkLabel(master=tabview.tab("Distance"), text="Milimeters")

# Centimeters
label_centimeters = customtkinter.CTkLabel(master=tabview.tab("Distance"))
text_centimeters = customtkinter.CTkLabel(master=tabview.tab("Distance"), text="Centimeters")

# Feet
label_feet = customtkinter.CTkLabel(master=tabview.tab("Distance"))
text_feet = customtkinter.CTkLabel(master=tabview.tab("Distance"), text="Feet")

# Yards
label_yards = customtkinter.CTkLabel(master=tabview.tab("Distance"))
text_yards = customtkinter.CTkLabel(master=tabview.tab("Distance"), text="Yards")

# Meters
label_meters = customtkinter.CTkLabel(master=tabview.tab("Distance"))
text_meters = customtkinter.CTkLabel(master=tabview.tab("Distance"), text="Meters")

# Decameters
label_decameters = customtkinter.CTkLabel(master=tabview.tab("Distance"))
text_decameters = customtkinter.CTkLabel(master=tabview.tab("Distance"), text="Decameters")

# Hectometers
label_hectometers = customtkinter.CTkLabel(master=tabview.tab("Distance"))
text_hectometers = customtkinter.CTkLabel(master=tabview.tab("Distance"), text="Hectometers")

# Kilometers
label_kilometers = customtkinter.CTkLabel(master=tabview.tab("Distance"))
text_kilometers = customtkinter.CTkLabel(master=tabview.tab("Distance"), text="Kilometers")

# Miles
label_miles = customtkinter.CTkLabel(master=tabview.tab("Distance"))
text_miles = customtkinter.CTkLabel(master=tabview.tab("Distance"), text="Miles")

# Nautical Miles
label_nauticalmiles = customtkinter.CTkLabel(master=tabview.tab("Distance"))
text_nauticalmiles = customtkinter.CTkLabel(master=tabview.tab("Distance"), text="Nautical Miles")

# Grid Method - Label = Number calculated and shown | Text = string units  
#button_feetConvert.grid(row=1, column=0, sticky="w", padx=10, pady=10)
entry.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# Inches Text Draw 
text_inches.grid(row=0, column=1, sticky="w", padx=10, pady=10)

# Milimeters Draw
label_milimeters.grid(row=1, column=1, sticky="w", padx=10, pady=10)
text_milimeters.grid(row=1, column=2, sticky="w", padx=10,pady=10)

# Centimeters Draw
label_centimeters.grid(row=2, column=1, sticky="w", padx=10, pady=10)
text_centimeters.grid(row=2, column=2, sticky="w", padx=10, pady=10)

# Feet Draw
label_feet.grid(row=3, column=1, sticky="w", padx=10, pady=10)
text_feet.grid(row=3, column=2, sticky="w", padx=10, pady=10)

# Yards Draw 
label_yards.grid(row=4, column=1, sticky="W", padx=10, pady=10)
text_yards.grid(row=4, column=2, sticky="W", padx=10, pady=10)

# Meters Draw
label_meters.grid(row=5, column=1, sticky="w", padx=10, pady=10)
text_meters.grid(row=5, column=2, sticky="w", padx=10, pady=10) 

# Decameters Draw
label_decameters.grid(row=6, column=1, sticky="w", padx=10, pady=10)
text_decameters.grid(row=6, column=2, sticky="w", padx=10, pady=10)

# Hectometers Draw
label_hectometers.grid(row=7, column=1, sticky="w", padx=10, pady=10)
text_hectometers.grid(row=7, column=2, sticky="w", padx=10, pady=10)

# Kilometers
label_kilometers.grid(row=8, column=1, sticky="w", padx=10, pady=10)
text_kilometers.grid(row=8, column=2, sticky="w", padx=10, pady=10)

# Miles
label_miles.grid(row=9, column=1, sticky="w", padx=10, pady=10)
text_miles.grid(row=9, column=2, sticky="w", padx=10, pady=10)

# Nautical Miles
label_nauticalmiles.grid(row=10, column=1, sticky="w", padx=10, pady=10)
text_nauticalmiles.grid(row=10, column=2, sticky="w", padx=10, pady=10)

# Pack and draw on screen [OBSOLETE]
#button.pack(padx=20, pady=20)
#entry.pack(padx=20, pady=20)
#label.pack(padx=20, pady=20)
#inches_label.pack(padx=20,pady=20)
# Run main window

# Combobox 
# ----------------------------------

def combobox_callback(choice):
    print("combobox drop down clicked:", choice)

combobox_var = customtkinter.StringVar(value=1)
combobox = customtkinter.CTkComboBox(master=left_frame, values=["Milimeters", "Centimeters","Inch", "Feet", "Yards", "Meters","Decameters","Hectometers", "Kilometers", "Miles", "Nautical Miles"],
                                     command=combobox_callback, variable=combobox_var)
combobox_var.set("Inches")

def combobox2_callback(choice):
    print("combobox2 drop down clicked:", choice)

combobox2_var = customtkinter.StringVar(value="option 2")
combobox2 = customtkinter.CTkComboBox(master=left_frame, values=["Milimeters", "Centimeters","Inch","Feet", "Yards", "Meters","Decameters","Hectometers", "Kilometers", "Miles", "Nautical Miles"],
                                      command=combobox2_callback, variable=combobox2_var)

combobox2_var.set("Inches")

# Combobox Math Output Label
label_comboCalc = customtkinter.CTkLabel(master=left_frame, text="Output")
label_comboCalc.grid(row=6, column=0, padx=10, pady=10)

label_comboCalcOut = customtkinter.CTkLabel(master=left_frame, text="....")
label_comboCalcOut.grid(row=7, column=0, padx=10, pady=10)
text_custom.grid(row=2, column=0, padx=10, pady=10)
text_custom2.grid(row=4, column=0, padx=10, pady=10)
combobox.grid(row=3, column=0, sticky="e", padx=10, pady=10)
combobox2.grid(row=5, column=0, padx=10, pady=10)

app.bind("<KeyRelease>", convert_on_key_release)
app.mainloop()

