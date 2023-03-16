import tkinter 
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

count = 0

result = messagebox.showwarning("DEUS TE AMA", "VOCÊ FOI HACKEADO(A)")

if result == 'ok':
     result = messagebox.showwarning("PERA AI!", "PARA SER DESHACKEADO(A) PRECISO QUE ME RESPONDA UMA PERGUNTA...") #titulo, conteudo

if result == 'ok':
     result = messagebox.askquestion("O QUE ACHA?", "SABIA QUE JESUS TE AMA?") #titulo, conteudo

while result == 'no':
     count += 1
     if (count == 5):
          result = messagebox.showerror("NAAAO!", "ELE TE AMA SIM :)")
          break
     result = messagebox.askquestion("O QUE ACHA?", "SABIA QUE JESUS TE AMA?") #titulo, conteudo

if result == 'yes':
     messagebox.showinfo("BOA!", "SABIA ESCOLHA")
