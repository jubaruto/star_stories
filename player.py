from tkinter import*
from PIL import ImageTk, Image
import pygame
from pygame import mixer
import os

cor00 = "#f0f3f5"
cor01 = "#feffff"
cor02 = "#3fb5a3"
cor03 = "#2e2d2c"
cor04 = "#403d3d"
cor05 = "#4a88e8"

janela = Tk()
janela.title("Player")
janela.geometry("352x255")
janela.configure(background=cor01)
janela.resizable(width=FALSE, height=FALSE)

frame_esquerda = Frame(janela, width=150, height=150, bg=cor03)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_direita = Frame(janela, width=250, height=150, bg=cor03)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=404, height=100, bg=cor03)
frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)

img01 = Image.open(r"C:\Projetos\star_stories\icons\icon1.png")
img01 = img01.resize((130, 130))
img01 = ImageTk.PhotoImage(img01)

logo = Label(frame_esquerda, height=130, image=img01, compound=LEFT, padx=0, anchor="nw",
font=("ivy 16 bold"), bg=cor03, fg=cor03)
logo.place(x=14, y=15)

def play_musica():
    tocando = listbox.get(ACTIVE)
    mov["text"] = tocando
    mixer.music.load(tocando)
    mixer.music.play()

def stop_musica():
    mixer.music.stop()

def pausar_musica():
    mixer.music.pause()

def continuar_musica():
    mixer.music.unpause()

def voltar_musica():
    mixer.music.unpause()
    tocar = mov["text"]
    index = musicas_rg.index(tocar)
    novo_index = index - 1
    tocar = musicas_rg[novo_index]
    mixer.music.load(tocar)
    mixer.music.play()
    listbox.delete(0, END)
    mostrar()
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    mov["text"] = tocar

def proxima_musica():
    tocar = mov["text"]
    index = musicas_rg.index(tocar)
    novo_index = index + 1
    tocar = musicas_rg[novo_index]
    mixer.music.load(tocar)
    mixer.music.play()
    listbox.delete(0, END)
    mostrar()
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    mov["text"] = tocar

listbox = Listbox(frame_direita, width=22, height=10, selectmode=SINGLE, font=("arial 9 bold"), bg=cor03, fg=cor01)
listbox.grid(row=0, column=0)

s = Scrollbar(frame_direita)
s.grid(row=0, column=1, sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)


mov = Label(frame_baixo, text="Selecione a música na lista", width=44, justify=LEFT, anchor="nw",
font=("ivy 10"), bg=cor01, fg=cor04)
mov.place(x=0, y=1)

img04 = Image.open(r"C:\Projetos\star_stories\icons\icon4.png")
img04 = img04.resize((30, 30))
img04 = ImageTk.PhotoImage(img04)
play = Button(frame_baixo, command=play_musica, width=40, height=40, image=img04,
font=("ivy 10 bold"), relief=RAISED, overrelief=RIDGE, bg=cor03, fg=cor01)
play.place(x=38, y=35)

img02 = Image.open(r"C:\Projetos\star_stories\icons\icon2.png")
img02 = img02.resize((30, 30))
img02 = ImageTk.PhotoImage(img02)
stop = Button(frame_baixo, command=stop_musica, width=40, height=40, image=img02,
font=("ivy 10 bold"), relief=RAISED, overrelief=RIDGE, bg=cor03, fg=cor01)
stop.place(x=84, y=35)

img08 = Image.open(r"C:\Projetos\star_stories\icons\icon8.png")
img08 = img08.resize((30, 30))
img08 = ImageTk.PhotoImage(img08)
voltar = Button(frame_baixo, command=voltar_musica, width=40, height=40, image=img08,
font=("ivy 10 bold"), relief=RAISED, overrelief=RIDGE, bg=cor03, fg=cor01)
voltar.place(x=130, y=35)

img07 = Image.open(r"C:\Projetos\star_stories\icons\icon7.png")
img07 = img07.resize((30, 30))
img07 = ImageTk.PhotoImage(img07)
avancar = Button(frame_baixo, command=proxima_musica, width=40, height=40, image=img07,
font=("ivy 10 bold"), relief=RAISED, overrelief=RIDGE, bg=cor03, fg=cor01)
avancar.place(x=176, y=35)

img03 = Image.open(r"C:\Projetos\star_stories\icons\icon3.png")
img03 = img03.resize((30, 30))
img03 = ImageTk.PhotoImage(img03)
pausar = Button(frame_baixo, command=pausar_musica, width=40, height=40, image=img03,
font=("ivy 10 bold"), relief=RAISED, overrelief=RIDGE, bg=cor03, fg=cor01)
pausar.place(x=222, y=35)

img09 = Image.open(r"C:\Projetos\star_stories\icons\icon9.png")
img09 = img09.resize((30, 30))
img09 = ImageTk.PhotoImage(img09)
continuar = Button(frame_baixo, command=continuar_musica, width=40, height=40, image=img09,
font=("ivy 10 bold"), relief=RAISED, overrelief=RIDGE, bg=cor03, fg=cor01)
continuar.place(x=268, y=35)

os.chdir(r"C:\Projetos\star_stories\rg")
musicas_rg = os.listdir()

def mostrar():
    for i in musicas_rg:
        listbox.insert(END, i)

mostrar()

mixer.init()

janela.mainloop()