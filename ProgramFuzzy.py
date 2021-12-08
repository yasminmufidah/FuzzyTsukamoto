from tkinter import *

root = Tk()
root.geometry("1280x900")
root.title(" Prediksi Pelayaran ")
defaultcolor = '#FFFFFF'
root.configure(bg=defaultcolor)

def Inference():
	inp1 = inputtxt1.get(1.0, "end-1c")
	inp1 = int(inp1)

	
	if inp1 <= 20:
		if inp1 <= 20:
			myu1 = 1
		elif inp1 > 20 and inp1 < 25:
			myu1 = (25 - inp1)/(25-20)
		elif inp1 >= 25:
			myu1 = 0
		Output.insert(END,'Ringan')
	elif inp1 > 20 and inp1 < 55 :
		if inp1 <= 20:
			myu1 = 1
		elif inp1 > 20 and inp1 <= 37.5:
			myu1 = (inp1-20)/(37.5-20)
		elif inp1 > 37.5 and inp1 < 55:
			myu1 = (55-inp1)/(55-37.5)
		elif inp1 >= 55:
			myu1 = 0
		Output.insert(END,'Sedang')
	elif inp1 > 50 and inp1 < 85 :
		if inp1 <= 50:
			myu1 = 0
		elif inp1 > 50 and inp1 < 85:
			myu1 = (inp1-50)/(85-50)
		elif inp1 >= 85:
			myu1 = 1
		Output.insert(END,'Kencang')

	
	inp2 = inputtxt2.get(1.0, "end-1c")
	inp2 = int(inp2)

	if inp2 > 0.1 and inp2 < 1.5:
		Kategori = 'Rendah'
		if inp2 <= 1:
			myu2 = 1
		elif inp2 > 1 and inp2 < 1.7:
			myu2 = ( 1.5 - inp2 ) / ( 1.5 - 1 )
		elif inp2 >= 1.5:
			myu2 = 0

	if inp2 > 1 and inp2 < 2.5:
		Kategori = 'Sedang'
		if inp2 <= 1:
			myu2 = 1
		elif inp2 > 1 and inp2 <=1.75:
			myu2 = ( inp2 - 1 ) / ( 1.75 - 1)
		elif inp2  > 1.5 and inp2  < 2.5:
			myu2 = ( 2.5 - inp2 ) / ( 2.5 - 1.5 )
		elif inp2 >= 2.5:
			myu3 = 0

	if inp2 > 2 and inp2 < 5:
		Kategori = ' Tinggi'
		if inp2 <= 2:
			myu3 = 0
		elif inp2 > 2 and inp2 < 5:
			myu3 = ( inp2 - 2 ) - ( 5 - 2 )
		elif inp2 >= 5:
			myu3 = 1

	inp3 = inputtxt3.get(1.0, "end-1c")
	inp3 = int(inp3)

	if inp3 >= 0 and inp3 <= 20 :
		if inp3 <= 15:
			myu3 = 1
		elif inp3 > 15 and inp3 < 20:
			myu3 = (20 - inp3)/(20-15)
		elif inp3 >= 20:
			myu3 = 0
		Output2.insert(END,'Ringan')
	elif inp3 >= 15 and inp3 <= 50 :
		if inp3 <= 15:
			myu3 = 0
		elif inp3 > 15 and inp3 <= 32.5:
			myu3 = (inp3-15)/(32.5-15)
		elif inp3 > 32.5 and inp3 < 50:
			myu3 = (50-inp3)/(50-32.5)
		elif inp3 >= 50:
			myu3 = 0
		Output2.insert(END,'Sedang')
	elif inp3 >=45 and inp3 <= 100 :
		if inp3 <= 45:
			myu3 = 0
		elif inp3 > 45 and inp3 < 100:
			myu3 = (inp3-45)/(100-45)
		elif inp3 >= 100:
			myu3 = 1
		Output2.insert(END,'Lebat')

	alpha = min(myu1, myu2, myu3)
	Output3.insert(END, alpha)


def rule1(var1='ringan', var2 ='rendah', var3='ringan', out='aman'):
	
		return

		# def kecepatanAngin():
		# 	return 
		# def KetinggianGelombang():
		# 	return
		# def CurahHujan():
		# 	return
l1 = Label(text = "Input Kecepatan Angin (km/jam)")
l1.configure(bg=defaultcolor, font='helvetica')
inputtxt1 = Text(root, height = 2,
				width = 25,
				bg = "light yellow", font='helvetica')
l2 = Label(text = "Input Ketinggian Gelombang (m)")
l2.configure(bg=defaultcolor, font='helvetica')
inputtxt2 = Text(root, height = 2,
				width = 25,
				bg = "light yellow", font='poppins')
l3 = Label(text = "Input Curah Hujan (mm/hari)")
l3.configure(bg=defaultcolor, font='poppins')
inputtxt3 = Text(root, height = 2,
				width = 25,
				bg = "light yellow", font='poppins')
l4 = Label(text = "Kategori Kecepatan Angin")
l4.configure(bg=defaultcolor, font='poppins')
Output = Text(root, height = 3,
			width = 25,
			bg = "light cyan", font='poppins')
l5 = Label(text = "Kategori Ketinggian Gelombang")
l5.configure(bg=defaultcolor, font='poppins')
Output1 = Text(root, height = 3,
			width = 25,
			bg = "light cyan", font='poppins')
l6 = Label(text = "Kategori Curah Hujan")
l6.configure(bg=defaultcolor, font='poppins')
Output2 = Text(root, height = 3,
			width = 25,
			bg = "light cyan", font='poppins')
Output3 = Text(root, height = 3,
			width = 25,
			bg = "light cyan", font='poppins')
Display = Button(root, height = 2,
				width = 20,
				text ="Show",
				command = lambda:Inference())

l1.pack()
inputtxt1.pack()
l2.pack()
inputtxt2.pack()
l3.pack()
inputtxt3.pack()
Display.pack()
l4.pack()
Output.pack()
l5.pack()
Output1.pack()
l6.pack()
Output2.pack()
Output3.pack()

mainloop()
