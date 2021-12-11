from tkinter import *
import tkinter as tk
import numpy as np

class RefiEval:
    def __init__(self):
        master = Tk()
        master.title("Prediksi Resiko Pelayaran")
        master.configure(background='antiquewhite1')
        master.geometry("700x400")
 
       
        heading = Label(master, text='Prediksi Resiko Pelayaran', font = ('Helvetica', 15, 'bold'), background="antiquewhite1").grid(row=0, column=3, ipady=8, pady=10)
        
         # input
        Label(master, text='Kecepatan Angin (km/jam)', font = ('Helvetica', 10), background="antiquewhite1").grid(row=3,column=2, ipadx= 5)
        Label(master, text='Ketinggian Gelombang (m)', font = ('Helvetica', 10),background="antiquewhite1").grid(row=4,column=2, ipadx= 5)
        Label(master, text='Curah Hujan (mm/hari)', font = ('Helvetica', 10),background="antiquewhite1").grid(row=5,column=2, ipadx= 5)

        self.d1 = StringVar()
        self.d2 = StringVar()
        self.d3 = StringVar()
        self.d4 = StringVar()
        self.out = StringVar()
        self.out1 = StringVar()
        self.out2 = StringVar()

        # variable for input
        e1 = Entry(master, textvariable=self.d1, font=('Helvetica', 10))
        e2 = Entry(master,  textvariable=self.d2, font = ('Helvetica', 10))
        e3 = Entry(master,  textvariable=self.d3, font = ('Helvetica', 10))

        # grid input
        e1.grid(row=3, column=3, sticky=W, ipadx=100, ipady=6)
        e2.grid(row=4, column=3, sticky=W, ipadx=100, ipady=6)
        e3.grid(row=5, column=3, sticky=W, ipadx=100, ipady=6)
        
        # Button
        btn = tk.Button(master, text="Submit",font = ('Helvetica', 10), background="coral1",command=self.submit, justify="left")
        btn.place(x=220, y=220) 
        btn2 = tk.Button(master, text="Reset",font = ('Helvetica', 10), background="coral1",command=self.reset, justify="right") 
        btn2.place(x=275, y=220)
        
        # Output
        Output = tk.Label(master, font = ('Helvetica', 13, 'bold'), textvariable=self.out ,background="antiquewhite1" ).place(x=50, y=280)
        Output1 = tk.Label(master, font = ('Helvetica', 13, 'bold'),textvariable=self.out1,background="antiquewhite1").place(x=50, y=310)
        Output2 = tk.Label(master, font = ('Helvetica', 13, 'bold'),textvariable=self.out2,background="antiquewhite1").place(x=50, y=340)
        
        master.mainloop()

    def submit(self):
		# mengambil nilai input
        d1 = self.d1.get()
        d2 = self.d2.get()
        d3 = self.d3.get()
        d4 = self.d4.get()
        d1 = int(d1)
		# kategori kecepatan angin pada setiap rule
		# nilai 0 = ringan, nilai 1 = sedang, nilai 2 = kencang 
        var1 = [0,0,0,0,0,0,0,1,1,1,1,1,1,1,2]
        myu_1 = []
		
		# perhitungan nilai myu pada variabel kecepatan angin
        for i in var1:
            if i == 0:
                if d1 <= 20:
                    myu1 = 1
                elif d1 > 20 and d1 < 25:
                    myu1 = (25 - d1)/(25-20)
                elif d1 >= 25:
                    myu1 = 0
            elif i == 1:
                if d1 <= 20:
                    myu1 = 1
                elif d1 > 20 and d1 <= 37.5:
                    myu1 = (d1-20)/(37.5-20)
                elif d1 > 37.5 and d1 < 55:
                    myu1 = (55-d1)/(55-37.5)
                elif d1 >= 55:
                    myu1 = 0
            elif i == 2:
                if d1 <= 50:
                    myu1 = 0
                elif d1 > 50 and d1 < 85:
                    myu1 = (d1-50)/(85-50)
                elif d1 >= 85:
                    myu1 = 1
            myu_1.append(myu1)
        d2 = float(d2)

		# kategori ketinggian gelombang pada setiap rule
		# nilai 0 = rendah, nilai 1 = sedang, nilai 2 = tinggi 
        var2 = [0,0,0,1,1,1,2,0,0,0,1,1,1,2,3]
        myu_2 = []
        for i in var2:
            if i == 0:
                if d2 <= 1:
                    myu2 = 1
                elif d2 > 1 and d2 < 1.7:
                    myu2 = ( 1.5 - d2 ) / ( 1.5 - 1 )
                elif d2 >= 1.5:
                    myu2 = 0
            elif i == 1:
                if d2 <= 1:
                    myu2 = 1
                elif d2 > 1 and d2 <=1.75:
                    myu2 = ( d2 - 1 ) / ( 1.75 - 1)
                elif d2  > 1.5 and d2  < 2.5:
                    myu2 = ( 2.5 - d2 ) / ( 2.5 - 1.5 )
                elif d2 >= 2.5:
                    myu2 = 0
            elif i == 2:
                if d2 <= 2:
                    myu2 = 0
                elif d2 > 2 and d2 < 5:
                    myu2 = ( d2 - 2 )/( 5 - 2 )
                elif d2 >= 5:
                    myu2 = 1
            elif i == 3 :
                myu2 = 0
            myu_2.append(myu2)

			# kategori curah hujan pada setiap rule
			# nilai 0 = ringan, nilai 1 = sedang, nilai 2 = lebat 
            d3 = int(d3)
            var3 = [0,1,2,0,1,2,3,0,1,2,0,1,2,3,3]
            myu_3 = []
            for i in var3:
                if i == 0 :
                    if d3 <= 15:
                        myu3 = 1
                    elif d3 > 15 and d3 < 20:
                        myu3 = (20 - d3)/(20-15)
                    elif d3 >= 20:
                        myu3 = 0
                elif i == 1:
                    if d3 <= 15:
                        myu3 = 0
                    elif d3 > 15 and d3 <= 32.5:
                        myu3 = (d3-15)/(32.5-15)
                    elif d3 > 32.5 and d3 < 50:
                        myu3 = (50-d3)/(50-32.5)
                    elif d3 >= 50:
                        myu3 = 0
                elif i == 2 :
                    if d3 <= 45:
                        myu3 = 0
                    elif d3 > 45 and d3 < 100:
                        myu3 = (d3-45)/(100-45)
                    elif d3 >= 100:
                        myu3 = 1
                elif i == 3 :
                    myu3 = 0
                myu_3.append(myu3)

        # perhitungan nilai alpha
        # mencari nilai minimum dari setiap rule
        alpha_out = []
        for i in range(0,15):
            if i == 6 :
                alpha = min(myu_1[i], myu_2[i])
            elif i == 13 :
                alpha = min(myu_1[i], myu_2[i])
            elif i == 14 :
                alpha = myu_1[i]
            else:
                alpha = min(myu_1[i], myu_2[i], myu_3[i])
            alpha_out.append(alpha)

        # perhitungan nilai z
        var_out = [0,0,1,0,0,1,2,0,1,1,1,2,2,2,2]
        z_out = []
        for i in range(0,15):
            if var_out[i] == 0 :
                # Kategori = 'Aman'
                z = 50 - (alpha_out[i]*10)
            elif var_out[i] == 1 :
                # Kategori = 'Waspada'
                z1 = (alpha_out[i]*10) + 40
                z2 = 60 - (alpha_out[i]*10)
                z = (z1+z2)/2
            else:
                # Kategori = 'Bahaya'
                z = (alpha_out[i]*50) + 50
            z_out.append(z)

        # Defuzzifikasi
        nilai_defuzzifikasi = 0
        x = float(nilai_defuzzifikasi)
        for i in range(0,15):
            x += (alpha_out[i]*z_out[i])
        a = (x / np.sum(alpha_out))

		# perhitungan kategori resiko dan derajat keanggotaannya
        dk = 0
        if a > 0 and a < 50 :
            Kategori = 'Aman'
            if a <= 40:
                dk = 1 
            elif a > 40 and a < 50:
                dk = (50 - a)/(50-40)
            elif a >= 50:
                dk = 0
        elif a > 40 and a < 60 :
            Kategori = 'Waspada'
            if a <= 40:
                dk = 0
            elif a > 40 and a <= 50:
                dk = (a - 40)/(50-40)
            elif a > 50 and a < 60:
                dk = (60 - a)/(60-50)
            elif a >= 60:
                dk = 0
        if a > 50 and a < 100 :
            Kategori = 'Bahaya'
            if a <= 50:
                dk = 0
            elif a > 40 and a < 50:
                dk = (a - 50)/(100-50)
            elif a >= 50:
                dk = 1

		# output
        self.out.set("Nilai Fuzzy : " + str(a))
        self.out1.set("Derajat keanggotaan : " + str(dk))
        self.out2.set("Risiko Pelayaran : " + Kategori)
        
	# reset program
    def reset(self):
        self.d1.set('')
        self.d2.set('')
        self.d3.set('')
        self.d4.set('')
        self.out.set('')
        self.out1.set('')
        self.out2.set('')

RefiEval()