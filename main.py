from tkinter import tk

root = tk.Tk()
root.title('Крестики нолики')

buttons = [[None for _ in range(3)] for _ in range(3)]

def make_move(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        current_player = "O" if current_player == "X" else "X"


for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 24), width=5, height=2)
        buttons[i][j].grid(row=i, column=j)

root.mainloop()