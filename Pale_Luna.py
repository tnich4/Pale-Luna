import tkinter as tk
from PIL import Image, ImageTk
import os

class PaleLunaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Pale Luna")

        #SET BG TO BLACK
        self.master.config(bg="black")

        #DIRECTORY FOR IMAGES
        self.images_dir = os.path.join(os.path.dirname(__file__), r"C:\Users\tenic\Downloads\UIUC Spring 2024\BCOG 200\Pale Luna\images")

        #REQUIREMENTS FOR LEAVING PSG 1
        self.current_passage = 1
        self.items_collected = {
            "GOLD": False,
            "SHOVEL": False,
            "ROPE": False,
            "DOOR_OPEN": False
        }

        #DICTIONARY FOR IMAGES USED IN THE GAME. USE ONLY PNG!
        self.images = {
            0: "dark_room.png",
            1: "gold.png",
            2: "rope.png",
            3: "shovel.png",
            4: "open_door.png",
            5: "forest1.png",
            6: "forest2.png",
            7: "forest3.png",
            8: "forest4.png",
            9: "here.png",
            10: "hole.png",
            11: "bury_gold.png",
            12: "coords.png",
        }

        #ALL SCENARIOS IN GAME
        self.passages = {
            1: {"text": "You are in a dark room. Moonlight shines through the window. \nThere is GOLD in the corner, along with a SHOVEL and a ROPE. \nThere is a door to the EAST.",
                "choices": ["PICK UP GOLD", "PICK UP SHOVEL", "PICK UP ROPE", "OPEN DOOR", "GO EAST"]},
            2: {"text": "Reap your reward. \nPALE LUNA SMILES AT YOU. \nYou are in a forest. There are paths to the NORTH, WEST, AND EAST.",
                "choices": ["Go NORTH", "Go WEST", "Go EAST"]},
            3: {"text": "You traverse NORTH. \nReap your reward. \nPALE LUNA SMILES AT YOU. \nYou are in a forest. There are paths to the NORTH, WEST, AND SOUTH.",
                "choices": ["Go NORTH", "Go WEST", "Go SOUTH", "Use GOLD", "Use SHOVEL", "Use ROPE"]},
            4: {"text": "You traverse NORTH. \nReap your reward. \nPALE LUNA SMILES AT YOU. \nYou are in a forest. There are paths to the NORTH, EAST, AND SOUTH.",
                "choices": ["Go NORTH", "Go EAST", "Go SOUTH", "Use GOLD", "Use SHOVEL", "Use ROPE"]},
            5: {"text": "You traverse EAST. \nReap your reward. \nPALE LUNA SMILES AT YOU. \nYou are in a forest. There are paths to the NORTH, WEST, AND SOUTH.",
                "choices": ["Go NORTH", "Go WEST", "Go SOUTH", "Use GOLD", "Use SHOVEL", "Use ROPE"]},
            6: {"text": "Reap your reward. \nPALE LUNA SMILES AT YOU. \nYou are here.", 
                "choices": ["Use GOLD", "Use ROPE", "Use SHOVEL"]},
        }

        #FRAME FOR TEXT AND BUTTONS 
        self.frame = tk.Frame(master, bg="black")
        self.frame.pack(expand=True, fill="both")

        # SETS BACKGROUND AND TEXT COLOR
        self.passage_label = tk.Label(self.frame, text="", wraplength=400, bg="black", fg="white", font=("Arial", 16)) 
        self.passage_label.pack(expand=True, fill="both", padx=20, pady=10)

        #IMPLEMENTATION FOR DISPLAYING IMAGES
        self.image = Image.open(os.path.join(self.images_dir, self.images[0]))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.frame, image=self.photo, bg='black')
        self.image_label.pack(expand=True, fill="both", padx=20, pady=10)

        # CHOICE BUTTON CONFIG
        self.choice_buttons = []
        for i in range(len(self.passages[self.current_passage]["choices"])):
            choice_button = tk.Button(self.frame, text=self.passages[self.current_passage]["choices"][i], command=lambda i=i: self.make_choice(i), font=("Arial", 14))
            choice_button.pack(expand=True, fill="both", padx=20, pady=2)  # Reduce vertical padding to 2
            self.choice_buttons.append(choice_button)


        self.update_display()

    #CLEARS ALL BUTTONS/PASSAGES SO THAT NEXT PASSAGES AND BUTTONS ALIGN
    def update_display(self):
        passage_info = self.passages[self.current_passage]
        self.passage_label.config(text=passage_info["text"])

        for button in self.choice_buttons:
            button.destroy()

        self.choice_buttons = []
        for i, choice in enumerate(passage_info["choices"]):
            choice_button = tk.Button(self.master, text=choice, command=lambda i=i: self.make_choice(i))
            choice_button.pack(pady=5)
            self.choice_buttons.append(choice_button)

        if self.current_passage == 1:
            self.update_image(self.images[0])
        elif self.current_passage == 2:
            self.update_image(self.images[5])
        elif self.current_passage == 3:
            self.update_image(self.images[6])
        elif self.current_passage == 4:
            self.update_image(self.images[7])
        elif self.current_passage == 5:
            self.update_image(self.images[8])
        elif self.current_passage == 6:
            self.update_image(self.images[9])
        else:
            self.update_image(self.images[self.current_passage])

    def update_image(self, image_name):

        original_image = Image.open(os.path.join(self.images_dir, image_name))
        
        desired_width = 300  
        
        width_percent = (desired_width / float(original_image.size[0]))
        desired_height = int((float(original_image.size[1]) * float(width_percent)))
        
        resized_image = original_image.resize((desired_width, desired_height), Image.LANCZOS)
        
        self.photo = ImageTk.PhotoImage(resized_image)
        
        self.image_label.configure(image=self.photo)


    #EVERY DECISION THE PLAYER MAKES IS DONE HERE 
    def make_choice(self, choice):

        #PASSAGE ONE 
        if self.current_passage == 1:
            self.update_image(self.images[0])
            if choice == 0:
                if self.items_collected["GOLD"]:
                    self.passage_label.config(text="You already took this.")
                    return
                self.items_collected["GOLD"] = True
                self.update_image("gold.png")  #UPDATE TO SHOW GOLD
                self.display_intermediary_screen("GOLD")
                return
            elif choice == 1:
                if self.items_collected["SHOVEL"]:
                    self.passage_label.config(text="You already took this.")
                    return
                self.items_collected["SHOVEL"] = True
                self.update_image("shovel.png")
                self.display_intermediary_screen("SHOVEL")
                return

            elif choice == 2:
                if self.items_collected["ROPE"]:
                    self.passage_label.config(text="You already took this.")
                    return
                self.items_collected["ROPE"] = True
                self.update_image("rope.png")
                self.display_intermediary_screen("ROPE")
                return

            elif choice == 3:
                self.items_collected["DOOR_OPEN"] = True
                self.update_image("open_door.png")
                self.passage_label.config(text="The door is open.")

            elif choice == 4:
                if all(self.items_collected.values()) and self.items_collected["DOOR_OPEN"]:
                    self.current_passage = 2
                    self.update_display()  
                else:
                    self.passage_label.config(text="Not yet.")



        #PASSAGE TWO 
        elif self.current_passage == 2: 

            if choice == 0:
                self.current_passage = 3
                self.update_display()
            elif choice == 1 or choice == 2: 
                exit()



        #PASSAGE THREE 
        elif self.current_passage == 3:

            if choice == 0:
                self.current_passage = 4
                self.update_display()
            elif choice == 1 or choice == 2: 
                exit()
            elif choice == 3: 
                self.passage_label.config(text="Not here.")
            elif choice == 4: 
                self.passage_label.config(text="Not now.")
            elif choice == 5:
                self.passage_label.config(text="You already used this.")



        #PASSAGE FOUR
        elif self.current_passage == 4:

            if choice == 0:
                exit()
            elif choice == 1: 
                self.current_passage = 5
                self.update_display()
            elif choice == 2: 
                exit()
            elif choice == 3: 
                self.passage_label.config(text="Not here.")
            elif choice == 4: 
                self.passage_label.config(text="Not now.")
            elif choice == 5:
                self.passage_label.config(text="You already used this.")



        #PASSAGE FIVE
        elif self.current_passage == 5:

            if choice == 0:
                self.current_passage = 6
                self.update_display()
            elif choice == 1 or choice == 2: 
                exit()
            elif choice == 3: 
                self.passage_label.config(text="Not here.")
            elif choice == 4: 
                self.passage_label.config(text="Not now.")
            elif choice == 5:
                self.passage_label.config(text="You already used this.")



        #PASSAGE SIX - CURRENTLY WIP!!!
        elif self.current_passage == 6:

            if choice == 0:
                self.passage_label.config(text="Can't bury treasure without a hole.")
                return
            elif choice == 1: 
                self.passage_label.config(text="You already used this.")
                return
            elif choice == 2:
                self.passage_label.config(text="Used SHOVEL.")
                self.current_passage = 7
                self.update_display()
                
    #FOR EACH ITEM ATTAINED SO THAT DOING ALLAT DOESN'T GET REPETITIVE 
    def display_intermediary_screen(self, item):
        self.passage_label.config(text=f"You got the {item}.")

def main():
    root = tk.Tk()
    root.title("Pale Luna")
    root.attributes('-fullscreen', True)  
    app = PaleLunaGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
