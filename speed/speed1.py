from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 3)) + " Mbps"
    up = str(round(sp.upload()/(10**6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("600x400")
sp.config(bg="#1e1e1e")


lab_title = Label(sp, text="Internet Speed Test", font=("Helvetica", 24, "bold"), bg="#1e1e1e", fg="white")
lab_title.place(x=150, y=60, height=50, width=300)


lab_down_label = Label(sp, text="Download Speed", font=("Helvetica", 18), bg="#1e1e1e", fg="lightblue")
lab_down_label.place(x=110, y=150, height=50, width=200)
lab_down = Label(sp, text="00 Mbps", font=("Helvetica", 18, "bold"), bg="#1e1e1e", fg="white")
lab_down.place(x=350, y=150, height=50, width=200)


lab_up_label = Label(sp, text="Upload Speed", font=("Helvetica", 18), bg="#1e1e1e", fg="lightblue")
lab_up_label.place(x=110, y=200, height=50, width=200)
lab_up = Label(sp, text="00 Mbps", font=("Helvetica", 18, "bold"), bg="#1e1e1e", fg="white")
lab_up.place(x=350, y=200, height=50, width=200)


button = Button(sp, text="Check Speed", font=("Helvetica", 18, "bold"), bg="#4caf50", fg="white", relief=RAISED, command=speedcheck)
button.place(x=200, y=330, height=50, width=200)

sp.mainloop()
