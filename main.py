from concurrent.futures import ThreadPoolExecutor
import threading
from random import randrange
import random
import basestation
import node
import v_node
import antenna
import channel
import ToolTip
import SD5GSim_GUI
from tkinter import *


def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


def run_io_tasks_in_parallel(tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()


def start_simulation(bs):
    MIN_PACKET_COUNT = 100
    MAX_PACKET_COUNT = 500
    REQUEST_PROBABILITY = 0.85

    req_prob = random.uniform(0, 1)
    if req_prob < REQUEST_PROBABILITY:
        (sen_nd, rec_nd) = random.choices(bs.bs_nodes, k=2)
        sen_vn = sen_nd.activate_v_node()
        rec_vn = rec_nd.activate_v_node()
        src_ant = sen_nd.activate_ant()
        des_ant = rec_nd.activate_ant()
        num_of_pkts = randrange(MIN_PACKET_COUNT, MAX_PACKET_COUNT)
        bs.num_control_msg += 1

        if all(instance is not None for instance in [sen_vn, rec_vn, src_ant, des_ant]):
            req_attrs = {
                "src_node": sen_nd,
                "src_vnode": sen_vn,
                "src_ant": src_ant,
                "des_node": rec_nd,
                "des_vnode": rec_vn,
                "des_ant": des_ant
            }
            bs.num_of_reqs += 1
            src_ch = bs.assing_ch_to_node(**req_attrs)
            req_attrs["src_ch"] = src_ch
            req_attrs["num_of_pkts"] = num_of_pkts
            if src_ch is not None:
                bs.utilized_channels += 1
                curr_attrs = req_attrs
                tx_time = bs.calculate_tx_time(num_of_pkts)
                timer = threading.Timer(tx_time, lambda: bs.terminate_connection(**curr_attrs))
                timer.start()
            else:
                bs.num_of_blocked_reqs += 1
                pass


def main():
    root = Tk()
    my_gui = SD5GSim_GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
