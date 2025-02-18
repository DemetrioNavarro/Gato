import tkinter as tk
import os
from tkinter import messagebox
from functools import partial

class GUI:
    #atributos
    root = tk.Tk()
    menuframe = tk.Frame(root)
    gameframe = tk.Frame(root)
    boardframe = tk.Frame(root)
    turn = 0
    used = 0
    botones = []
    board = ['0','0','0','0','0','0','0','0','0']

    #métodos
    def __init__(self):
        self.root.geometry("600x600")
        self.root.title("Gato")
        #configurar frames
        self.menuframe.columnconfigure(0, weight=1)
        self.menuframe.columnconfigure(1, weight=1)
        self.menuframe.columnconfigure(2, weight=1)

        self.boardframe.columnconfigure(0, weight=1)
        self.boardframe.columnconfigure(1, weight=1)
        self.boardframe.columnconfigure(2, weight=1)

        self.gameframe.columnconfigure(0, weight=1)
        self.gameframe.columnconfigure(1, weight=1)
        self.gameframe.columnconfigure(2, weight=1)
        self.gameframe.config(pady = 10)
        #configurar botones
            #botones tablero
        for i in range(9):
            self.botones.append(tk.Button(self.boardframe, height = 8, command = partial(self.selected, i)))
        for i in range(9):
            self.botones[i].grid(row=i//3, column = i%3, sticky = "WE")
            #botones menu
        self.load()
        btnStart = tk.Button(self.menuframe, height = 4, text = "Jugar partida", command = self.play)
        btnStart.grid(row = 0, column = 1, sticky = "WE")
            #botones game
        btnMenu = tk.Button(self.gameframe, height = 4, text = "Volver al menu", command = self.mainMenu)
        btnMenu.grid(row = 0, column = 0, sticky = "WE")
        btnRestart = tk.Button(self.gameframe, height = 4, text = "Reiniciar", command = self.delete)
        btnRestart.grid(row = 0, column = 2, sticky = "WE")
        #loop
        self.root.mainloop()

    def load(self):
        line = ""
        if os.path.exists("hst.txt"):
            with open("hst.txt", "r") as file:
                line = file.readline()
        else:
            line = "-"
        if line == '-':
            self.mainMenu()
        else:
            self.used = 9
            for i in range(9):
                self.board[i] = line[i]
                if line[i] == 'X':
                    self.botones[i].config(text = "X", font = ("Arial", 10),fg = "black", bg = "red", height = 8, state = "disabled")
                    self.botones[i].grid(row = i//3, column = i%3, sticky = "WE")
                elif line[i] == 'O':
                    self.botones[i].config(text = "O", font = ("Arial", 10),fg = "black", bg = "blue", height = 8, state = "disabled")
                    self.botones[i].grid(row = i//3, column = i%3, sticky = "WE")
                else:
                    self.used -= 1
                    self.botones[i].config(height = 8, state = "normal", bg = "beige", text = "")
                    self.botones[i].grid(row=i//3, column = i%3, sticky = "WE")
            self.turn = int(line[9])
            self.boardframe.pack_forget()
            self.gameframe.pack_forget()
            self.boardframe.pack(fill = 'x')
            self.gameframe.pack(fill = 'x')
    
    def mainMenu(self):
        self.gameframe.pack_forget()
        self.boardframe.pack_forget()
        self.menuframe.pack(fill = "x")

    def selected(self, cell):
        if self.turn == 0:
            self.board[cell] = 'X'
            self.botones[cell].config(text = "X", font = ("Arial", 10),fg = "white", bg = "red", height = 8, state = "disabled")
            self.botones[cell].grid(row = cell//3, column = cell%3, sticky = "WE")
        else:
            self.board[cell] = 'O'
            self.botones[cell].config(text = "O", font = ("Arial", 10),fg = "white", bg = "blue", height = 8, state = "disabled")
            self.botones[cell].grid(row = cell//3, column = cell%3, sticky = "WE")
        self.used += 1
        self.turn = self.turn + 1
        self.turn = self.turn % 2
        
        with open("hst.txt", "w") as file:
            for e in self.board:
                file.write(e)
            file.write(str(self.turn))
            file.close()
        self.boardframe.pack_forget()
        self.gameframe.pack_forget()
        self.boardframe.pack(fill = 'x')
        self.gameframe.pack(fill = 'x')
        self.check()
        
    def check(self):
        if self.board[0] != '0' and self.board[0] == self.board[1] and self.board[0] == self.board[2]:
            messagebox.showinfo(title = "Ganador", message = "Ganaron las "+self.board[0]+"s")
            self.delete()
        elif self.board[3] != '0' and self.board[3] == self.board[4] and self.board[3] == self.board[5]:
            messagebox.showinfo(title = "Ganador", message = "Ganaron las "+self.board[3]+"s")
            self.delete()
        elif self.board[6] != '0' and self.board[6] == self.board[7] and self.board[6] == self.board[8]:
            messagebox.showinfo(title = "Ganador", message = "Ganaron las "+self.board[6]+"s")
            self.delete()

        elif self.board[0] != '0' and self.board[0] == self.board[3] and self.board[0] == self.board[6]:
            messagebox.showinfo(title = "Ganador", message = "Ganaron las "+self.board[0]+"s")
            self.delete()
        elif self.board[1] != '0' and self.board[1] == self.board[4] and self.board[1] == self.board[7]:
            messagebox.showinfo(title = "Ganador", message = "Ganaron las "+self.board[1]+"s")
            self.delete()
        elif self.board[2] != '0' and self.board[2] == self.board[5] and self.board[2] == self.board[8]:
            messagebox.showinfo(title = "Ganador", message = "Ganaron las "+self.board[2]+"s")
            self.delete()
        
        elif self.board[0] != '0' and self.board[0] == self.board[4] and self.board[0] == self.board[8]:
            messagebox.showinfo(title = "Ganador", message = "Ganaron las "+self.board[0]+"s")
            self.delete()
        elif self.board[2] != '0' and self.board[2] == self.board[4] and self.board[2] == self.board[6]:
            messagebox.showinfo(title = "Ganador", message = "Ganaron las "+self.board[2]+"s")
            self.delete()
        elif self.used == 9:
            messagebox.showinfo(title = "Empate", message = "Empataron las Xs y las Os")
            self.delete()
        else:
            return
        self.delete()

    def delete(self):
        with open("hst.txt", "w") as file:
            file.write("-")
            file.close()
        self.used = 0
        self.turno = 0
        for i in range(9):
            self.board[i] = '0'
        self.mainMenu()
    

    def play(self):
        self.menuframe.pack_forget()
        self.boardframe.pack_forget()
        self.gameframe.pack_forget()
        

        for i in range(9):
            self.botones[i].config(height = 8, state = "normal", bg = "beige", text = "")
        for i in range(9):
            self.botones[i].grid(row=i//3, column = i%3, sticky = "WE")

        

        

        self.boardframe.pack(fill = "x")
        self.gameframe.pack(fill = "x")






def main():
    GUI()

if __name__ == "__main__":
    main()