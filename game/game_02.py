from tkinter import *
import random

def start_game():
    global ball, paddle, score

    canvas.delete("all")

    score = 0
    update_score()

    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')

    game_loop()


def game_loop():
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        tk.update_idletasks()
        tk.update()
        tk.after(10, game_loop)
    else:
        restart_button.place(x=210, y=220)


def update_score():
    canvas.delete("score")
    canvas.create_text(
        50, 20,
        text=f"Score: {score}",
        font=("Helvetica", 14, "bold"),
        fill="black",
        tag="score"
    )


tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.paddle = paddle
        self.canvas.move(self.id, 245, 100)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        global score

        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(
                self.canvas_width / 2,
                self.canvas_height / 2,
                text="GAME OVER",
                font=("Helvetica", 32),
                fill="red"
            )
            return

        if self.hit_paddle(pos):
            self.y = -3
            score += 1
            update_score()

        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = 0


restart_button = Button(
    tk,
    text="Restart",
    font=("Helvetica", 14),
    command=lambda: [restart_button.place_forget(), start_game()]
)

start_game()

tk.mainloop()
