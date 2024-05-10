from customtkinter import *
import customtkinter
from PIL import Image
import sys
import DBclass
from CTkMessagebox import CTkMessagebox


FONT = ("Arial", 24, "bold")
BWIDTH, BHEIGHT = 300, 70
myDB = DBclass.DBclass()



def get_screen_resolution():
    w, h = app.winfo_screenwidth(), app.winfo_screenheight()
    # return in this format: wxh
    return str(w) + "x" + str(h)

def on_exit(event):
    app.destroy()
    sys.exit()

def on_add_player(event):

    # each player have a name and a score, which is initially 0 by default
    dialog = CTkInputDialog(text="Enter player name", title="Add player")

    name = dialog.get_input()

    if name:
        if myDB.user_exists(name):
            # Show error message in a popup window
            CTkMessagebox(title="Error", message="Player already exists", icon="cancel")

        else:
            myDB.add_user(name)
            # Show success message in a popup window
            CTkMessagebox(title="Success", message="Player added successfully", icon="check")
    else:
        # otherwise we just do noting
        pass
    
def on_start_game(event):
    # clear current screen
    for widget in app.winfo_children():
        widget.destroy()

#    # add a combo box of players
#    players = myDB.get_all_users()
#    players = [player[0] for player in players]
#
#    player_combobox = CTkComboBox(app, values=players, font=FONT)
#    player_combobox.place(relx=0.5, rely=0.3, anchor="center")

    # choose number of players:
    label = CTkLabel(app, text="Choose number of players:", font=FONT)
    label.place(relx=0.5, rely=0.3, anchor="center")
    
    options = ["2", "3", "4", "5"]

    num_players = CTkComboBox(app, values=options, font=FONT)
    num_players.place(relx=0.5, rely=0.4, anchor="center")

    players_selection_button = CTkButton(app, text="Next", width=BWIDTH, height=BHEIGHT, fg_color="green", font=FONT)
    players_selection_button.place(relx=0.5, rely=0.5, anchor="center")

    players_selection_button.bind("<Button-1>", lambda event: on_players_selection(event, num_players.get()))



def on_players_selection(event, num_players):
    num_players = int(num_players)

    # clear current screen
    for widget in app.winfo_children():
        widget.destroy()

    for i in range(num_players):
        players = myDB.get_all_users()
        players = [player[0] for player in players]
        players = sorted(players)

        label = CTkLabel(app, text=f"Player {i+1}:", font=FONT)
        label.place(relx=0.4, rely=0.3 + 0.1 * i, anchor="center")

        player_combobox = CTkComboBox(app, values=players, font=FONT)
        player_combobox.place(relx=0.6, rely=0.3 + 0.1 * i, anchor="center")
    

if __name__ == "__main__":

    app = CTk()
    app.geometry(get_screen_resolution())
#    app.set_appearance_mode("dark")

    # set window fullscreen
    app.attributes("-fullscreen", True)


    # put a picture on the screen
#    image = Image.open("assets/Darts-24.png")  # Corrected the path separator
#    tk_image = CTkImage(light_image=image, dark_image=image, size=(400, 300))
#
#    image_label = CTkLabel(app, text="", image=tk_image)
#    image_label.place(relx=0.5, rely=0.2, anchor="center")


    start_game_button = CTkButton(app, text="Start Game", width=BWIDTH, height=BHEIGHT, fg_color="green", font=FONT)
    start_game_button.place(relx=0.5, rely=0.5, anchor="center")

    add_player_button = CTkButton(app, text="Add a new player", width=BWIDTH, height=BHEIGHT, fg_color="purple", font=FONT)
    add_player_button.place(relx=0.5, rely=0.6, anchor="center")

    exit_button = CTkButton(app, text="Exit", width=BWIDTH, height=BHEIGHT, fg_color="red", font=FONT)
    exit_button.place(relx=0.5, rely=0.8, anchor="center")


    #bind buttons
    start_game_button.bind("<Button-1>", on_start_game)
    add_player_button.bind("<Button-1>", on_add_player)
    exit_button.bind("<Button-1>", on_exit)

    app.mainloop()

