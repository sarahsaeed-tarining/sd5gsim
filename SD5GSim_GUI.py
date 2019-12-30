from tkinter import *
from PIL import Image, ImageTk
import time
from tkinter import ttk
from collections import defaultdict
import random
from statistics import mean
import basestation
import node
import v_node
import channel
import antenna


class SD5GSim_GUI:
    def __init__(self, root):
        self.root = root
        self.root.wm_title("Network Simulator")
        self.root.geometry("1500x1000")
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.submenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.submenu)
        self.submenu.add_command(label="New Project")
        self.submenu.add_separator()
        self.submenu.add_command(label="Exit", command=self.root.destroy)

        self.run_menu = Menu(self.menu)
        self.menu.add_cascade(label="Run", menu=self.run_menu)
        self.run_menu.add_command(label="Generate Environment", command=lambda: self.generate_environment_2(self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get()))
        self.run_menu.add_command(label="Start Simulation", command=lambda: self.get_sim_args(self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get()))

        self.about_menu = Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.about_menu)
        self.about_menu.add_command(label="About", command=self.doNothing)
        #############################

        self.left_frame = Frame(self.root, bg='#20B2AA')
        self.left_frame.place(relx=0, rely=0.05, relwidth=0.25, relheight=0.95)

        self.right_frame = LabelFrame(self.root, highlightbackground="black", highlightthickness=1, text="Simulation Environment")
        self.right_frame.place(relx=0.25, rely=0.05, relwidth=0.75, relheight=0.95)

        ###################

        self.box1 = LabelFrame(self.left_frame, borderwidth=1, relief="solid", text="Simulation Parameters", bg='#20B2AA')
        self.box2 = LabelFrame(self.left_frame, borderwidth=1, relief="solid", text="Simulation Results", bg='#20B2AA')
        self.box1.pack(expand=True, fill="both", padx=5, pady=5)
        self.box2.pack(expand=True, fill="both", padx=5, pady=5)

        ###################

        self.label1 = Label(self.box1, text="Number of cells", bg='#20B2AA')
        self.label1.grid(row=1, column=0, sticky=E)
        self.entry1 = Entry(self.box1, bg='white', relief=SUNKEN, width=6)
        self.entry1.grid(row=1, column=1)
        self.label2 = Label(self.box1, text="Number of channels/cell", bg='#20B2AA')
        self.label2.grid(row=2, column=0, sticky=E)
        self.entry2 = Entry(self.box1, bg='white', relief=SUNKEN, width=6)
        self.entry2.grid(row=2, column=1)
        self.label3 = Label(self.box1, text="Number of PNs/cell", bg='#20B2AA')
        self.label3.grid(row=3, column=0, sticky=E)
        self.entry3 = Entry(self.box1, bg='white', relief=SUNKEN, width=6)
        self.entry3.grid(row=3, column=1)
        self.label4 = Label(self.box1, text="Number of VNs/PN", bg='#20B2AA')
        self.label4.grid(row=4, column=0, sticky=E)
        self.entry4 = Entry(self.box1, bg='white', relief=SUNKEN, width=6)
        self.entry4.grid(row=4, column=1)
        self.label5 = Label(self.box1, text="Number of RIs/PN", bg='#20B2AA')
        self.label5.grid(row=5, column=0, sticky=E)
        self.entry5 = Entry(self.box1, bg='white', relief=SUNKEN, width=6)
        self.entry5.grid(row=5, column=1)
        self.label6 = Label(self.box1, text="Simulation Time", bg='#20B2AA')
        self.label6.grid(row=6, column=0, sticky=E)
        self.entry6 = Entry(self.box1, bg='white', relief=SUNKEN, width=6)
        self.entry6.grid(row=6, column=1)

        self.label7 = Label(self.box2, text="Average Network Throughput", bg='#20B2AA')
        self.label7.grid(row=11, column=0, sticky=E)
        self.label8 = Label(self.box2, bg='white', text='', relief=SUNKEN, width=6)
        self.label8.grid(row=11, column=1)

        self.label9 = Label(self.box2, text="Average Network Blocking Rate", bg='#20B2AA')
        self.label9.grid(row=12, column=0, sticky=E)
        self.label10 = Label(self.box2, bg='white', text='', relief=SUNKEN, width=6)
        self.label10.grid(row=12, column=1)

        self.label13 = Label(self.box2, text="Average Network Overhead", bg='#20B2AA')
        self.label13.grid(row=14, column=0, sticky=E)
        self.label14 = Label(self.box2, bg='white', text='', relief=SUNKEN, width=6)
        self.label14.grid(row=14, column=1)

        #############################
        self.toolbar = Frame(self.root, bd=4, bg='#20B2AA')

        self.run_img = Image.open("run.png")
        # self.run_img = self.run_img.resize((25, 23), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        self.render2 = ImageTk.PhotoImage(self.run_img)

        self.gen_img = Image.open("gen.png")
        # self.gen_img = self.gen_img.resize((25, 28), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        self.render3 = ImageTk.PhotoImage(self.gen_img)

        self.exit_img = Image.open("exit.png")
        self.render4 = ImageTk.PhotoImage(self.exit_img)

        self.clear_img = Image.open("clear.png")
        self.render5 = ImageTk.PhotoImage(self.clear_img)
        ##############################################################

        self.gen_butt = Button(self.toolbar, image=self.render3, text="Generate Envirnment", command=lambda: self.generate_environment_2(self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get()), bg='#008080')
        self.gen_butt.pack(side=LEFT, padx=2, pady=2)
        CreateToolTip(self.gen_butt, text='Generate Envirnment')
        self.run_butt = Button(self.toolbar, image=self.render2, text="Start Simulation", command=lambda: self.get_sim_args(self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get()), bg='#008080')
        self.run_butt.pack(side=LEFT, padx=2, pady=2)
        CreateToolTip(self.run_butt, text='Start Simulation')
        self.clear_butt = Button(self.toolbar, image=self.render5, text="Clear Environment", command=lambda: self.clear_frame(self.right_frame), bg='#008080')
        self.clear_butt.pack(side=LEFT, padx=2, pady=2)
        CreateToolTip(self.clear_butt, text='Clear Environment')

        self.exit_butt = Button(self.toolbar, image=self.render4, text="Exit", command=self.root.destroy, bg='#008080')
        self.exit_butt.pack(side=LEFT, padx=2, pady=2)
        CreateToolTip(self.exit_butt, text='Exit Simulator')

        self.toolbar.pack(side=TOP, fill=X)
        ############################
        self.status = Label(self.root, text=" ", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def doNothing():
        print("Works!!")

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            if widget != self.toolbar:
                widget.destroy()

    def generate_environment_2(self, cell_count, ch_count, node_count, vn_count, ant_count, sim_time):
        global bss
        ####################
        tabControl = ttk.Notebook(self.right_frame)          # Create Tab Control
        ####################
        ss_img = Image.open("icon3.png")
        ss_img = ss_img.resize((20, 20), Image.ANTIALIAS)  # The (250, 250) is (height, width)
        render = ImageTk.PhotoImage(ss_img)

        ss1_img = Image.open("icon2.png")
        ss1_img = ss1_img.resize((20, 20), Image.ANTIALIAS)  # The (250, 250) is (height, width)
        render3 = ImageTk.PhotoImage(ss1_img)

        ss2_img = Image.open("icon5.png")
        ss2_img = ss2_img.resize((20, 20), Image.ANTIALIAS)  # The (250, 250) is (height, width)
        render5 = ImageTk.PhotoImage(ss2_img)

        ss_icon_list = [render, render3, render5]

        bs_img = Image.open("icon4.png")
        bs_img = bs_img.resize((50, 50), Image.ANTIALIAS)  # The (250, 250) is (height, width)
        render1 = ImageTk.PhotoImage(bs_img)

        ####################
        bs_args = {
            "n_count": int(node_count),
            "all_ch_count": int(ch_count),
            "dimensions": {
                "x": 2000,
                "y": 2000
            }
        }
        bss = [basestation(**bs_args) for i in range(0, int(cell_count))]
        cell_num = 0
        for bs in bss:
            cell_num += 1
            tab1 = ttk.Frame(tabControl)            # Create a tab
            cell_name = 'Cell ' + str(cell_num)
            tabControl.add(tab1, text=cell_name)      # Add the tab
            tabControl.pack(expand=1, fill="both")  # Pack to make visible
            img0 = Label(tab1, image=render1)
            img0.image = render1
            img0.place(x=bs.coordinates['x'], y=bs.coordinates['y'])
            for node in bs.bs_nodes:
                temp_render = random.choice(ss_icon_list)
                img = Label(tab1, image=temp_render)
                img.image = temp_render
                img.place(x=node.coordinates['x'], y=node.coordinates['y'])

    def get_sim_args(self, cell_count, ch_count, node_count, vn_count, ant_count, sim_time):
        global bss

        max_time = int(sim_time)
        start_time = time.time()  # remember when we started
        while (time.time() - start_time) < max_time:
            run_io_tasks_in_parallel([
                lambda: start_simulation(bss[0]),
                lambda: start_simulation(bss[1]),
                lambda: start_simulation(bss[2]),
                lambda: start_simulation(bss[3]),
                lambda: start_simulation(bss[4]),
            ])

        metrics = defaultdict(list)

        for bs in bss:
            (thpt, overhead, block_rate, utilization) = bs.calculate_metrics(int(sim_time))
            metrics['throughput'].append(thpt)
            metrics['overhead'].append(overhead)
            metrics['blocking'].append(block_rate)

        avg_throughput = round(mean(metrics['throughput']), 2)
        avg_blocking_rate = round(mean(metrics['blocking']), 2)
        avg_overhead = round(mean(metrics['overhead']), 2)

        self.label8['text'] = str(avg_throughput)
        self.label10['text'] = str(avg_blocking_rate)
        self.label14['text'] = str(avg_overhead)
