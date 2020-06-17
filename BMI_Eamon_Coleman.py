import pandas as pd

import tkinter
from tkinter import *
from tkinter import messagebox


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
        weight = StringVar()
        feet = StringVar()
        inches = StringVar()
        height = StringVar()
        cm_scale = DoubleVar()
        kg_scale = DoubleVar()


        # =============================  VARIABLES    ===================================

        def reset():
            name.set("")
            age.set("")
            stone.set("")
            pounds.set("")
            weight.set("")
            feet.set("")
            inches.set("")
            height.set("")
            cm_scale.set(0)
            kg_scale.set(0)
            self.txtBMIResult.delete("1.0", END)
            self.txtBMIClassResult.delete("1.0", END)

        def Calulate_BMI():
            try:
                BMI_KG = (weight.get())
                BMI_CM = (height.get())
                self.txtBMIClassResult.delete("1.0", END)
                self.txtBMIResult.delete("1.0", END)

                if BMI_KG.isdigit() or BMI_KG.isdigit():
                    BMI_KG = float(BMI_KG)
                    BMI_CM = float(BMI_CM)



                    bmi_val = float('%.2f' % (BMI_KG / (BMI_CM * BMI_CM)))


                    self.txtBMIResult.insert(END, bmi_val)


                    cm_scale.set(BMI_CM * 100)
                    kg_scale.set(BMI_KG)
                    Calulate_BMI_Class(bmi_val)

                    return True

                else:
                    tkinter.messagebox.showwarning("Body Mass Index", "Please Enter a Valid Number in both fields.")
                    height.set("")
                    weight.set("")
                    self.txtBMIResult.delete("1.0", END)
                    self.txtBMIClassResult.delete("1.0", END)

            except ZeroDivisionError:
                tkinter.messagebox.showwarning("Body Mass Index", "Number cannot be divided by Zero.")

        def Metric_Imperial():
            self.btnMetric.config(state=NORMAL, bg='light coral')
            self.btnImperial.config(state=DISABLED, bg='springgreen')
            self.lb_height.config(text="Enter your Height in Inches")
            self.lb_weight.config(text="Enter your Height in Pounds")


        def Metric_Toggle():
            self.btnMetric.config(state=DISABLED, bg='springgreen')
            self.btnImperial.config(state=NORMAL, bg='light coral')
            self.lb_height.config(text="Enter your Height in Meters")
            self.lb_weight.config(text="Enter your Height in Kilograms")


        def Calulate_BMI_Class(bmi_val):
            if bmi_val <= 18.5:
                self.txtBMIClassResult.insert(END, "Under Weight")
            elif 18.6 < bmi_val < 24.9:
                self.txtBMIClassResult.insert(END, "Normal Weight")
            elif 25 < bmi_val < 29.9:
                self.txtBMIClassResult.insert(END, "Overweight")
            else:
                self.txtBMIClassResult.insert(END, "Obese")

        def export():

            datatoexcel = pd.ExcelWriter("FromPython.xlsx", engine='xlswriter')
            data.to_excel(datatoexcel, sheet_name='Sheet1')
            datatoexcel.save()
            tkinter.messagebox.showwarning("Body Mass Index", "Worked.")

        def exit():
            messagebox.askokcancel("Body Mass Index", "Are you sure you want to exit?")
            if exit > 0:
                root.destroy()
                return

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
        self.btnMetric = Button(leftframe3, text="Metirc", padx=4, pady=2, bd=4, width=15, relief="raised",
                                state=NORMAL,
                                font=('arial', 17, 'bold'), height=1, bg='light coral', command=Metric_Toggle)
        self.btnMetric.bind('<Return>', Metric_Toggle)
        self.btnMetric.grid(row=0, column=1)

        # ===== LEFT FRAME 4 =====

        self.lb_height = Label(leftframe4, text="Enter your Height in Inches", font=('arial', 15, 'bold'),
                             width=27, bd=2)
        self.lb_height.grid(row=1, column=0, padx=5)
        self.txt_feet = Entry(leftframe4, textvariable=height, font=('arial', 15, 'bold'), bd=5, width=10, justify=LEFT)
        self.txt_feet.grid(row=1, column=1, pady=5)
        self.lb_weight = Label(leftframe4, text="Enter your Weight in Pounds",
                               font=('arial', 15, 'bold'), width=27, bd=2, justify=LEFT)
        self.lb_weight.grid(row=2, column=0, padx=5)
        self.txt_inches = Entry(leftframe4, textvariable=weight, font=('arial', 15, 'bold'), bd=5, width=10,
                                justify=LEFT)
        self.txt_inches.grid(row=2, column=1, pady=5)

        # ===== LEFT FRAME 5 =====

        # ===== LEFT FRAME 6 =====

        self.btnBMI = Button(leftframe6, text="Calulate BMI", padx=4, pady=2, bd=4, width=38,
                             font=('arial', 17, 'bold'), height=1, bg='dodgerblue', command=Calulate_BMI)
        self.btnBMI.bind('<Return>', Calulate_BMI)
        self.btnBMI.grid(row=0, column=0)

        # ===== LEFT FRAME 7 =====

        self.lbBMIResult = Label(leftframe7, text="Your BMI Result is:", font=('arial', 17, 'bold'), bd=2)
        self.lbBMIResult.grid(row=1, column=0, padx=4)
        self.txtBMIResult = Text(leftframe7, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=7, height=1,
                                 relief='sunk')
        self.txtBMIResult.grid(row=1, column=1)

        self.btnExport = Button(leftframe7, text="Export Results", padx=4, pady=2, bd=4, width=11,
                                font=('arial', 17, 'bold'), height=1, bg='goldenrod', command=export)
        self.btnExport.grid(row=1, column=2)

        # ===== LEFT FRAME 8 =====

        self.btnReset = Button(leftframe8, text="Reset", padx=4, pady=2, bd=4, width=19, font=('arial', 17, 'bold'),
                               height=1, command=reset)
        self.btnReset.grid(row=0, column=1, )
        self.btnExit = Button(leftframe8, text="Exit", padx=4, pady=2, bd=4, width=19, font=('arial', 17, 'bold'),
                              height=1, command=exit)
        self.btnExit.grid(row=0, column=2)

        # ===========================    LEFT FRAME BUTTONS  ==================================

        # ===========================    LEFT FRAME BUTTONS  ==================================

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

        self.lbBMIClassResult = Label(rightframe4, text="Your BMI Class is:", state=DISABLED,  font=('arial', 17, 'bold'), bd=2)
        self.lbBMIClassResult.grid(row=1, column=0, padx=4)
        self.txtBMIClassResult = Text(rightframe4, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=20,
                                      height=1, bg='lime green', relief='sunk')
        self.txtBMIClassResult.grid(row=1, column=1)

        # ===========================================================================


if __name__ == '__main__':
    root = Tk()
    application = BMI(root)
    root.mainloop()
