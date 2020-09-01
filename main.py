import random
import basestation
import node
import v_node
import antenna
import channel
from SD5GSim_GUI import SD5GSim_GUI
from tkinter import *

def main():
    root = Tk()
    my_gui = SD5GSim_GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
