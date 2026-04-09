from tkinter import * 

# creation de la fenetre
fenetre = Tk()

#caracteristiques de la fenetre
fenetre.attributes('-fullscreen',True)
fenetre.configure(bg="black")
label = Label(fenetre,text="Cyber-Toolkit")
label.pack()

#titre principal

titrep = Label(fenetre , text="CYBER TOOLKIT" , fg="white", font=("Arial",70) , bg=fenetre["bg"])
titrep.pack()







fenetre.mainloop()
