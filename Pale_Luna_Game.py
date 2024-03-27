import tkinter as tk
from Pale_Luna import PaleLunaGUI 

def main():
    root = tk.Tk()
    root.title("Pale Luna")
    root.attributes('-fullscreen', True)  
    app = PaleLunaGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
