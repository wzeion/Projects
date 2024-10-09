import tkinter as tk
import time, threading, random

def action(canvas, ball, base, W, H, ball_w, ball_h, base_w, base_h, xVel, yVel):
    while True:
        coordinates = canvas.coords(ball) #This gives the coordinates of the ball, and the below one of the base
        base_coords = canvas.coords(base)

        #Ball-Bouncing-off-Walls
        if coordinates[0] >= (W - ball_w) or coordinates[0] <= 0:
            xVel = -xVel
        if coordinates[1] <= 0:
            yVel = -yVel
        
        #Ball-bouncing-off-the-base
        if (coordinates[1] + ball_h >= base_coords[1] and
            base_coords[0] <= coordinates[0] <= base_coords[0] + base_w):
            yVel = -yVel
        
        #Reseting ball's position if it hits below
        if coordinates[1] >= H:
            canvas.coords(ball, W // 2, H // 2)
            xVel = random.choice([-3, 3])
            yVel = random.choice([-3, 3])

        canvas.move(ball, xVel, yVel)
        time.sleep(0.01)

def main():  #The main function
    def Move_Right(event):
        canvas.move(Bounce, 60, 0)

    def Move_Left(event):
        canvas.move(Bounce, -60, 0)

    WIDTH = 600
    HEIGHT = 400

    #This is to give ball random velocity at different times to make the game harder
    xVelo = random.choice([-3, 3])
    yVelo = random.choice([-3, 3])

    window = tk.Tk()
    window.title("Bouncing Ball Game")

    #All Images
    Icon=tk.PhotoImage(file="assets//icon.png")
    PokeB = tk.PhotoImage(file='assets//Pokeball.png')
    PokeBG = tk.PhotoImage(file='assets//PokeBG.png')
    base = tk.PhotoImage(file='assets//BaseBlue.png')

    window.iconphoto(True,Icon)

    canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
    canvas.pack()

    #Background
    canvas.create_image(0, 0, image=PokeBG, anchor='nw')

    #This is to make the start of the ball from centre
    initial_x = WIDTH // 2
    initial_y = HEIGHT // 2
    ball = canvas.create_image(initial_x, initial_y, image=PokeB, anchor='center')
    ball_w = PokeB.width()
    ball_h = PokeB.height()

    #Base object
    Bounce = canvas.create_image(250, 350, image=base, anchor='nw')
    base_w = base.width()
    base_h = base.height()

    #Start ball movement in a separate thread
    threading.Thread(target=action, args=(canvas, ball, Bounce, WIDTH, HEIGHT, ball_w, ball_h, base_w, base_h, xVelo, yVelo), daemon=True).start()

    #Key binding
    window.bind("<Right>", Move_Right)
    window.bind("<Left>", Move_Left)
    window.mainloop()

if __name__ == "__main__":
    main()
