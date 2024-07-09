import tkinter as tk
from tkinter import messagebox
import random
import time

class MemoryPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Puzzle Game")
        self.time_limit = 60  # Time limit in seconds
        
        self.initialize_game()

    def initialize_game(self):
        self.start_time = time.time()
        self.pairs = list("♠♠♥♥♦♦♣♣♤♤♡♡♢♢♧♧")
        random.shuffle(self.pairs)
        self.buttons = []
        self.flipped = []
        self.matched = []
        
        self.create_widgets()
        self.update_timer()
        
    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.time_label = tk.Label(self.root, text=f"Time Left: {self.time_limit} seconds", font=("Roboto", 14))
        self.time_label.pack(pady=10)

        for i in range(4):
            row = []
            for j in range(4):
                button = tk.Button(self.frame, text="", width=10, height=5, bg="lightgrey", font=("Roboto", 20),
                                   command=lambda i=i, j=j: self.flip_card(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
    
    def flip_card(self, i, j):
        index = i * 4 + j
        print(f"Flipping card at ({i}, {j}), index: {index}, pair: {self.pairs[index]}")  # Debugging line
        
        if (i, j) in self.matched or len(self.flipped) == 2:
            return
        
        button = self.buttons[i][j]
        button.config(text=self.pairs[index], bg="white", disabledforeground="black", state="disabled")
        button.update_idletasks()
        time.sleep(0.1)
        
        self.flipped.append((i, j))
        
        if len(self.flipped) == 2:
            self.root.after(500, self.check_match)
    
    def check_match(self):
        (i1, j1), (i2, j2) = self.flipped
        if self.pairs[i1*4 + j1] == self.pairs[i2*4 + j2]:
            self.matched.extend(self.flipped)
            self.buttons[i1][j1].config(bg="lightgreen")
            self.buttons[i2][j2].config(bg="lightgreen")
        else:
            self.buttons[i1][j1].config(text="", bg="lightgrey", state="normal")
            self.buttons[i2][j2].config(text="", bg="lightgrey", state="normal")
        self.flipped = []
        
        if len(self.matched) == len(self.pairs):
            self.end_game("You win!")
    
    def update_timer(self):
        time_left = self.time_limit - int(time.time() - self.start_time)
        self.time_label.config(text=f"Time Left: {time_left} seconds")
        
        if time_left <= 0:
            self.end_game("Time's up! You lose!")
        else:
            self.root.after(1000, self.update_timer)
    
    def end_game(self, message):
        if messagebox.askyesno("Game Over", f"{message}\nWould you like to play again?"):
            self.frame.destroy()
            self.initialize_game()
        else:
            self.root.destroy()

def main():
    root = tk.Tk()
    game = MemoryPuzzleGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
