import tkinter
from tkinter import *
from tkinter import messagebox
from datetime import datetime

import csv


class BMI:

    def __init__(self, root):
        self.root = root
        self.root.title("Body Mass Index Calculator - Eamon Coleman")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background="Gray")
        mainframe = Frame(self.root, bd=20, width=1350, height=700, padx=10, pady=10, bg="Gray", relief=RIDGE)
        mainframe.grid()

        leftframe = Frame(mainframe, bd=10, width=600, height=600, padx=10, pady=13, bg="Gray", relief=RIDGE)
        leftframe.pack(side=LEFT)

        rightframe = Frame(mainframe, bd=10, width=560, height=600, padx=10, pady=13, bg="Gray", relief=RIDGE)
        rightframe.pack(side=RIGHT)

        # ===========================================================================

        leftframe0 = Frame(leftframe, bd=5, width=900, height=170, padx=5, bg="light coral", relief=RIDGE)
        leftframe0.grid(row=0, column=0)

        leftframe1 = Frame(leftframe, bd=5, width=900, height=170, padx=5, pady=6, relief=RIDGE)
        leftframe1.grid(row=1, column=0)

        leftframe2 = Frame(leftframe, bd=5, width=900, height=170, padx=5, pady=6, relief=RIDGE)
        leftframe2.grid(row=2, column=0)

        leftframe3 = Frame(leftframe, bd=5, width=900, height=170, padx=5, pady=5, relief=RIDGE)
        leftframe3.grid(row=3, column=0)

        leftframe4 = Frame(leftframe, bd=5, width=900, height=170, padx=5, pady=6, relief=RIDGE)
        leftframe4.grid(row=4, column=0)

        leftframe5 = Frame(leftframe, bd=5, width=900, height=170, padx=5, pady=6, relief=RIDGE)
        leftframe5.grid(row=5, column=0)

        leftframe6 = Frame(leftframe, bd=5, width=900, height=170, padx=5, pady=6, relief=RIDGE)
        leftframe6.grid(row=6, column=0)

        leftframe7 = Frame(leftframe, bd=5, width=900, height=170, padx=5, pady=6, relief=RIDGE)
        leftframe7.grid(row=7, column=0)

        leftframe8 = Frame(leftframe, bd=5, width=712, height=170, padx=5, pady=6, relief=RIDGE)
        leftframe8.grid(row=8, column=0)

        rightframe0 = Frame(rightframe, bd=5, width=522, height=143, padx=5, bg="light coral", relief=RIDGE)
        rightframe0.grid(row=0, column=0)
        rightframe1 = Frame(rightframe, bd=5, width=522, height=143, padx=5, pady=5, relief=RIDGE)
        rightframe1.grid(row=1, column=0)

        rightframe2 = Frame(rightframe, bd=5, width=522, height=143, padx=5, pady=5, relief=RIDGE)
        rightframe2.grid(row=2, column=0)

        rightframe3 = Frame(rightframe, bd=5, width=522, height=143, padx=5, pady=5, relief=RIDGE)
        rightframe3.grid(row=3, column=0)

        rightframe4 = Frame(rightframe, bd=5, width=522, height=143, padx=5, pady=5, relief=RIDGE)
        rightframe4.grid(row=4, column=0)

        # =============================  VARIABLES    ===================================

        name = StringVar()
        age = StringVar()
        stone = StringVar()
        pounds = StringVar()
        kg = StringVar()
        feet = StringVar()
        inches = StringVar()
        metres = StringVar()
        cm_scale = DoubleVar()
        kg_scale = DoubleVar()



        # =============================  FUNCTIONS    ===================================

        def reset():
            """
            Resets field entries
            """
            inches.set("")
            feet.set("")
            pounds.set("")
            stone.set("")
            kg.set("")
            metres.set("")
            name.set("")
            age.set("")
            cm_scale.set(0)
            kg_scale.set(0)
            self.txtBMIResult.delete("1.0", END)
            self.txtBMIClassResult.delete("1.0", END)
            self.btnExport.config(state=DISABLED, bg='gray', relief="sunken")

        def reset_toggle():
            """
            Resets field entries excluding Name/Age
            """
            inches.set("")
            feet.set("")
            pounds.set("")
            stone.set("")
            kg.set("")
            metres.set("")
            cm_scale.set(0)
            kg_scale.set(0)
            self.txtBMIResult.delete("1.0", END)
            self.txtBMIClassResult.delete("1.0", END)
            self.btnExport.config(state=DISABLED, bg='gray', relief="sunken")

        def metric_or_imperial__class():
            """
            Determines if the user has selected imperial or metric
            """
            if self.btnImperial["state"] == DISABLED:
                Calulate_BMI_IMPERIAL()
            else:
                Calulate_BMI()

        def minimum_checker_imperial():
            """
            Catches if the user has input a too small/large value in the imperial fields
            """
            CHECK_FEET = (feet.get())
            CHECK_STONES = (stone.get())
            CHECK_FEET = float(CHECK_FEET)
            CHECK_STONES = float(CHECK_STONES)
            if CHECK_FEET <= 2 or CHECK_STONES <= 0.5:
                tkinter.messagebox.showwarning("Body Mass Index", "Weight/Height too small to calculate BMI.")
                reset_toggle()
            elif CHECK_FEET > 9 or CHECK_STONES > 99:
                tkinter.messagebox.showwarning("Body Mass Index", "Weight/Height too large to calculate BMI.")
                reset_toggle()

        def Calulate_BMI_IMPERIAL():
            """
            Gets the users inputs from the imperial fields, converts them to a float then converts them to their metric
            value. (Feet/Inches to Metres and Stones/Pounds to Kg).
            Performs BMI calculation and populates result to "txtBMIResult".
            Updates scale value in metres/kg scale.
            Calls Calulate_BMI_Class(bmi_val) to determine and update the users BMI Class.
            Activates the export button allowing the user to store their results in a CSV. file.

            Exception Handling,
            1. If you user enters a zero for their height this will be caught with the except ZeroDivisionError line.
            2. If a none digit is entered by the user this be caught in the .isdigit() line.
            3. A minimum/maximum amount has been defined in the "checker" functions and will be caught if entered.
            """
            try:
                BMI_Stone = (stone.get())
                BMI_Pounds = (pounds.get())
                BMI_Feet = (feet.get())
                BMI_Inches = (inches.get())
                self.txtBMIClassResult.delete("1.0", END)
                self.txtBMIResult.delete("1.0", END)

                if BMI_Stone.isdigit() and BMI_Feet.isdigit() and BMI_Pounds.isdigit() and BMI_Inches.isdigit():
                    BMI_Stone = float(BMI_Stone)
                    BMI_Pounds = float(BMI_Pounds)
                    BMI_Feet = float(BMI_Feet)
                    BMI_Inches = float(BMI_Inches)
                    BMI_Pounds = BMI_Pounds // 2.2
                    BMI_Stone = BMI_Stone * 6.35029
                    BMI_Feet = BMI_Feet * 0.3048
                    BMI_Inches = BMI_Inches * 0.0254
                    BMI_KG = BMI_Stone + BMI_Pounds
                    BMI_metres = BMI_Feet + BMI_Inches
                    bmi_val = float('%.2f' % (BMI_KG / (BMI_metres * BMI_metres)))
                    self.txtBMIResult.insert(END, bmi_val)
                    cm_scale.set(BMI_metres * 100)
                    kg_scale.set(BMI_KG)
                    Calulate_BMI_Class(bmi_val)
                    minimum_checker_imperial()
                    self.btnExport.config(state=NORMAL, bg='goldenrod', relief="raised")
                    return True

                else:
                    tkinter.messagebox.showwarning("Body Mass Index", "Please Enter a Valid Number in all fields.")
                    self.txtBMIResult.delete("1.0", END)
                    self.txtBMIClassResult.delete("1.0", END)

            except ZeroDivisionError:
                tkinter.messagebox.showwarning("Body Mass Index", "Number cannot be divided by Zero.")

        def minimum_checker_metric():
            """
            Catches if the user has input a too small/large value in the imperial fields
            """
            CHECK_KG = (kg.get())
            CHECK_metres = (metres.get())
            CHECK_KG = float(CHECK_KG)
            CHECK_metres = float(CHECK_metres)
            if CHECK_metres <= 0.5 or CHECK_KG <= 1:
                tkinter.messagebox.showwarning("Body Mass Index", "Weight/Height too small to calculate BMI.")
                reset_toggle()
            elif CHECK_KG > 200 or CHECK_metres > 99:
                tkinter.messagebox.showwarning("Body Mass Index", "Weight/Height too large to calculate BMI.")
                reset_toggle()

        def Calulate_BMI():
            """
            Gets the users inputs from the metric fields, converts them to a float.
            Performs BMI calculation and populates result to "txtBMIResult".
            Updates scale value in metres/kg scale.
            Calls Calulate_BMI_Class(bmi_val) to determine and update the users BMI Class.
            Activates the export button allowing the user to store their results in a CSV. file.

            Exception Handling,
            1. If you user enters a zero for their height this will be caught with the except ZeroDivisionError line.
            2. If a none digit is entered by the user this be caught in the .isdigit() line.
            3. A minimum/maximum amount has been defined in the "checker" functions and will be caught if entered.
            """
            try:
                BMI_KG = (kg.get())
                BMI_metres = (metres.get())
                self.txtBMIClassResult.delete("1.0", END)
                self.txtBMIResult.delete("1.0", END)

                if BMI_KG.isdigit() or BMI_KG.isdigit():
                    BMI_KG = float(BMI_KG)
                    BMI_metres = float(BMI_metres)
                    bmi_val = float('%.2f' % (BMI_KG / (BMI_metres * BMI_metres)))
                    self.txtBMIResult.insert(END, bmi_val)
                    cm_scale.set(BMI_metres * 100)
                    kg_scale.set(BMI_KG)
                    Calulate_BMI_Class(bmi_val)
                    minimum_checker_metric()
                    self.btnExport.config(state=NORMAL, bg='goldenrod', relief="raised")
                    return True

                else:
                    tkinter.messagebox.showwarning("Body Mass Index", "Please Enter a Valid Number in both fields.")
                    self.txtBMIResult.delete("1.0", END)
                    self.txtBMIClassResult.delete("1.0", END)

            except ZeroDivisionError:
                tkinter.messagebox.showwarning("Body Mass Index", "Number cannot be divided by Zero.")

        def Metric_Imperial():
            """
            Toggles the imperial fields to become active and disables the metric
            """
            self.btnMetric.config(state=NORMAL, bg='light coral', relief="raised")
            self.btnImperial.config(state=DISABLED, bg='springgreen', relief="sunken")
            reset_toggle()
            self.txt_metres.config(bg='gray', state=DISABLED)
            self.txt_KG.config(bg='gray', state=DISABLED)
            self.txt_stones.config(bg='white', state=NORMAL)
            self.txt_pounds.config(bg='white', state=NORMAL)
            self.txt_inches.config(bg='white', state=NORMAL)
            self.txt_feet.config(bg='white', state=NORMAL)

        def Metric_Toggle():
            """
             This toggles the metric fields to become active and disables the imperial
            """
            self.btnMetric.config(state=DISABLED, bg='springgreen', relief="sunken")
            self.btnImperial.config(state=NORMAL, bg='light coral', relief="raised")
            reset_toggle()
            self.txt_stones.config(bg='gray', state=DISABLED)
            self.txt_pounds.config(bg='gray', state=DISABLED)
            self.txt_inches.config(bg='gray', state=DISABLED)
            self.txt_feet.config(bg='gray', state=DISABLED)
            self.txt_metres.config(bg='white', state=NORMAL)
            self.txt_KG.config(bg='white', state=NORMAL)

        def Calulate_BMI_Class(bmi_val):
            """
            With the bmi_val that is passed through the users BMI is determined with an If statement
            """
            if bmi_val <= 18.5:
                self.txtBMIClassResult.insert(END, "Under Weight")
            elif 18.6 < bmi_val < 24.9:
                self.txtBMIClassResult.insert(END, "Normal Weight")
            elif 25 < bmi_val < 29.9:
                self.txtBMIClassResult.insert(END, "Overweight")
            else:
                self.txtBMIClassResult.insert(END, "Obese")

        def export_exe():
            """
            Exports the users input/results to a local CSV file
            """
            try:
                CSV_NAME = (name.get())
                CSV_AGE = (age.get())
                CSV_Feet = (feet.get())
                CSV_Inches = (inches.get())
                CSV_metres = (metres.get())
                CSV_KG = (kg.get())
                CSV_Stone = (stone.get())
                CSV_Pounds = (pounds.get())
                bmi_val = self.txtBMIResult.get("1.0", 'end-1c')
                bmi_class = self.txtBMIClassResult.get("1.0", 'end-1c')
                current_time = datetime.now().time()

                with open('your_bmi_result', 'w', newline='') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(['Name', 'Age', 'BMI', 'BMI Class'])
                    thewriter.writerow([CSV_NAME, CSV_AGE, bmi_val, bmi_class])
                    thewriter.writerow([])

                    if self.btnImperial["state"] == DISABLED:
                        thewriter.writerow(['Your height is {} feet and {} inches.'.format(CSV_Feet, CSV_Inches)])
                        thewriter.writerow(['Your weight is {} stone and {} pounds.'.format(CSV_Stone, CSV_Pounds)])
                    else:
                        thewriter.writerow(['Your height is {} metres.'.format(CSV_metres)])
                        thewriter.writerow(['Your weight is {} KGs.'.format(CSV_KG)])

                    thewriter.writerow([])
                    thewriter.writerow(['Time: {}'.format(current_time)])

                tkinter.messagebox.showinfo("Body Mass Index", "Your results have been saved to a CSV file!")

            except NameError:
                tkinter.messagebox.showwarning("Body Mass Index", "Missing information, Please fill all fields.")

        def exit():
            """
            Exits the program
            """
            global root
            root.quit()

        # ===========================    LEFT FRAMES    ==================================

        self.lblTitle = Label(leftframe0, text="BMI Calculator", padx=17, pady=4, bd=1, fg="#000000",
                              font=('arial', 40, 'bold'), bg='light coral', width=20)
        self.lblTitle.pack()

        # ===== LEFT FRAME 1 =====

        self.lbName = Label(leftframe1, text="Enter your Name:", font=('arial', 17, 'bold'), width=19, bd=2, )
        self.lbName.grid(row=0, column=0, padx=7)
        self.txtName = Entry(leftframe1, textvariable=name, font=('arial', 17, 'bold'), bd=5, width=20, justify=LEFT)
        self.txtName.grid(row=0, column=1, pady=7)
        self.lbAge = Label(leftframe1, text="Enter your Age:", font=('arial', 17, 'bold'), bd=2)
        self.lbAge.grid(row=1, column=0, pady=7)
        self.txtAge = Entry(leftframe1, textvariable=age, font=('arial', 17, 'bold'), bd=5, width=15, justify=LEFT)
        self.txtAge.grid(row=1, column=1, pady=7)

        # ===== LEFT FRAME 2 =====

        self.lb_weight = Label(leftframe2, text="Type", padx=17, pady=4, bd=1, fg="#000000",
                               font=('arial', 17, 'bold'), width=32)
        self.lb_weight.pack()

        # ===== LEFT FRAME 3 =====

        self.btnImperial = Button(leftframe3, text="Imperial", padx=4, pady=2, bd=4, width=15, relief="sunken",
                                  state=DISABLED,
                                  font=('arial', 17, 'bold'), height=1, bg='springgreen', command=Metric_Imperial)
        self.btnImperial.bind('<Return>', Calulate_BMI)
        self.btnImperial.grid(row=0, column=0)
        self.btnMetric = Button(leftframe3, text="Metric", padx=4, pady=2, bd=4, width=15, relief="raised",
                                state=NORMAL,
                                font=('arial', 17, 'bold'), height=1, bg='light coral', command=Metric_Toggle)
        self.btnMetric.bind('<Return>', Metric_Toggle)
        self.btnMetric.grid(row=0, column=1)

        # ===== LEFT FRAME 4 =====

        self.lb_stones = Label(leftframe4, text="Stones", font=('arial', 15, 'bold'), width=6, bd=2)
        self.lb_stones.grid(row=1, column=0, padx=5)
        self.txt_stones = Entry(leftframe4, textvariable=stone, font=('arial', 15, 'bold'), bd=5, width=5, justify=LEFT)
        self.txt_stones.grid(row=1, column=1, pady=5)
        self.lb_pounds = Label(leftframe4, text="Pounds", font=('arial', 15, 'bold'), width=6, bd=2, justify=LEFT)
        self.lb_pounds.grid(row=1, column=2, padx=5)
        self.txt_pounds = Entry(leftframe4, textvariable=pounds, font=('arial', 15, 'bold'), bd=5, width=7,
                                justify=LEFT)
        self.txt_pounds.grid(row=1, column=3, pady=5)
        self.lb_KG = Label(leftframe4, text=" or KGs", font=('arial', 15, 'bold'), width=8, bd=2, justify=LEFT)
        self.lb_KG.grid(row=1, column=4, padx=5)
        self.txt_KG = Entry(leftframe4, textvariable=kg, font=('arial', 15, 'bold'), bd=5, width=7, bg='gray',
                            state=DISABLED, justify=LEFT)
        self.txt_KG.grid(row=1, column=5, pady=5)

        # ===== LEFT FRAME 5 =====

        self.lb_feet = Label(leftframe5, text="Feet", font=('arial', 15, 'bold'), width=6, bd=2)
        self.lb_feet.grid(row=1, column=0, padx=5)
        self.txt_feet = Entry(leftframe5, textvariable=feet, font=('arial', 15, 'bold'), bd=5, width=5, justify=LEFT)
        self.txt_feet.grid(row=1, column=1, pady=5)
        self.lb_inches = Label(leftframe5, text="Inches", font=('arial', 15, 'bold'), width=6, bd=2, justify=LEFT)
        self.lb_inches.grid(row=1, column=2, padx=5)
        self.txt_inches = Entry(leftframe5, textvariable=inches, font=('arial', 15, 'bold'), bd=5, width=7,
                                justify=LEFT)
        self.txt_inches.grid(row=1, column=3, pady=5)
        self.lb_metres = Label(leftframe5, text=" or Metres", font=('arial', 15, 'bold'), width=8, bd=2, justify=LEFT)
        self.lb_metres.grid(row=1, column=4, padx=5)
        self.txt_metres = Entry(leftframe5, textvariable=metres, font=('arial', 15, 'bold'), bd=5, width=7, bg='gray',
                            state=DISABLED, justify=LEFT)
        self.txt_metres.grid(row=1, column=5, pady=5)

        # ===== LEFT FRAME 6 =====

        self.btnBMI = Button(leftframe6, text="Calulate BMI", padx=4, pady=2, bd=4, width=38,
                             font=('arial', 17, 'bold'), height=1, bg='dodgerblue', command=metric_or_imperial__class)
        self.btnBMI.bind('<Return>', metric_or_imperial__class)
        self.btnBMI.grid(row=0, column=0)

        # ===== LEFT FRAME 7 =====

        self.lbBMIResult = Label(leftframe7, text="Your BMI Result is:", font=('arial', 17, 'bold'), bd=2)
        self.lbBMIResult.grid(row=1, column=0, padx=4)
        self.txtBMIResult = Text(leftframe7, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=7, height=1,
                                 relief='sunk')
        self.txtBMIResult.grid(row=1, column=1)

        self.btnExport = Button(leftframe7, text="Export Results", padx=4, pady=2, bd=4, width=11, state=DISABLED,
                                bg='gray', relief="sunken",
                                font=('arial', 17, 'bold'), height=1, command=export_exe)
        self.btnExport.grid(row=1, column=2)

        # ===== LEFT FRAME 8 =====

        self.btnReset = Button(leftframe8, text="Reset", padx=4, pady=2, bd=4, width=19, font=('arial', 17, 'bold'),
                               height=1, command=reset)
        self.btnReset.grid(row=0, column=1, )
        self.btnExit = Button(leftframe8, text="Exit", padx=4, pady=2, bd=4, width=19, font=('arial', 17, 'bold'),
                              height=1, command=exit)
        self.btnExit.grid(row=0, column=2)

        # ===========================    RIGHT FRAME    ==================================

        self.lblBMITable = Label(rightframe0, font=('arial', 20, 'bold'), text="BMI Values", padx=17, pady=4, bd=1,
                                 fg="#000000", width=20, bg='light coral').grid(row=0, column=0)

        self.txtBMITable = Text(rightframe0, height=10, width=53, bd=16, font=('arial', 12, 'bold'))
        self.txtBMITable.grid(row=1, column=0)

        self.txtBMITable.insert(END, 'Result \t\t\t\t' + "BMI \n\n")
        self.txtBMITable.insert(END, 'Under Weight \t\t\t\t' + "< 18.5\n\n")
        self.txtBMITable.insert(END, 'Normal Weight (Healthy Weight) \t\t\t\t' + "18.5 - 24.9\n\n")
        self.txtBMITable.insert(END, 'Overweight \t\t\t\t' + "25 - 29.9 \n\n")
        self.txtBMITable.insert(END, 'Obese \t\t\t\t' + "> 30 \n\n")

        # ===== RIGHT FRAME 1 =====

        self.lb_your_results = Label(rightframe1, text="Your Results", padx=17, pady=4, bd=1, fg="#000000",
                                     font=('arial', 17, 'bold'), width=34)
        self.lb_your_results.pack()

        # ===== RIGHT FRAME 2 =====

        self.BodyHeight = Scale(rightframe2, variable=cm_scale, from_=0, to=250, length=507, tickinterval=50,
                                state=DISABLED, orient=HORIZONTAL, label="Height in Centimetres",
                                font=('arial', 10, 'bold'))
        self.BodyHeight.grid(row=1, column=1)

        # ===== RIGHT FRAME 3 =====

        self.BodyWeight = Scale(rightframe3, variable=kg_scale, from_=0, to=150, length=507, tickinterval=30,
                                state=DISABLED,
                                orient=HORIZONTAL, label="Weight in Kilograms", font=('arial', 10, 'bold'))
        self.BodyWeight.grid(row=2, column=1)

        # ===== RIGHT FRAME 4 =====

        self.lbBMIClassResult = Label(rightframe4, text="Your BMI Class is:", font=('arial', 17, 'bold'), bd=2)
        self.lbBMIClassResult.grid(row=1, column=0, padx=4)
        self.txtBMIClassResult = Text(rightframe4, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=20,
                                      height=1, bg='lime green', relief='sunk')
        self.txtBMIClassResult.grid(row=1, column=1)

        # ===========================================================================


if __name__ == '__main__':
    root = Tk()
    application = BMI(root)
    root.mainloop()
