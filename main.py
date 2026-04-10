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
titrep.pack(expand=True)
titrep.pack()

#saisie du login et du mdp
Champlogin = Text(fenetre, height=1, width=50)
titreLogin = Label(fenetre , text="votre login" , fg="white", font=("Arial",10) )
Champlogin.pack()
ChampMdp = Text(fenetre, height=1, width=50)
titreMdp = Label(fenetre , text="votre mdp" , fg="white", font=("Arial",10) , bg=fenetre["bg"])
ChampMdp.pack()















fenetre.mainloop()
