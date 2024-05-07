from customtkinter import *
import customtkinter
from PIL import Image


FONT = ("Arial", 24, "bold")
BWIDTH, BHEIGHT = 300, 70



def get_screen_resolution():
    w, h = app.winfo_screenwidth(), app.winfo_screenheight()
    # return in this format: wxh
    return str(w) + "x" + str(h)




if __name__ == "__main__":

    app = CTk()
    app.geometry(get_screen_resolution())
#    app.set_appearance_mode("dark")

    # set window fullscreen
    app.attributes("-fullscreen", True)


    # put a picture on the screen
    image = Image.open("assets/Darts-24.png")  # Corrected the path separator
    tk_image = CTkImage(light_image=image, dark_image=image, size=(400, 300))

    image_label = CTkLabel(app, text="", image=tk_image)
    image_label.place(relx=0.5, rely=0.2, anchor="center")



    start_game_button = CTkButton(app, text="Start Game", width=BWIDTH, height=BHEIGHT, fg_color="green", font=FONT)
    start_game_button.place(relx=0.5, rely=0.5, anchor="center")

    add_player_button = CTkButton(app, text="Add a new player", width=BWIDTH, height=BHEIGHT, fg_color="purple", font=FONT)
    add_player_button.place(relx=0.5, rely=0.6, anchor="center")

    app.mainloop()


