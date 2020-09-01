import uuid
from pprint import pprint
from random import randrange
import basestation
from v_node import v_node
import channel
from antenna import antenna


class node:
    def __init__(self, **kwargs):
        self.node_id = "n_" + str(uuid.uuid4())
        self.vn_count = 6
        self.ant_count = 6
        self.ch_count = 0
        self.coordinates = {"x": randrange(1, 1125), "y": randrange(1, 950)}
        self.parent_bs = None
        self.local_channels = []

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.local_antennas = [antenna(**{"active": False, "power": 0.0}) for i in range(0, self.ant_count)]
        self.local_v_nodes = [v_node(**{"parent_nd": self, "parent_bs": self.parent_bs}) for i in range(0, self.vn_count)]

    def add_to_local_channels(self, **kwargs):
        pass

    def get_channel_from_LP(self, des_nd):
        pass

    def activate_v_node(self):
        found_vn = None
        for vn in self.local_v_nodes:
            if vn.active is False:
                vn.activate()
                found_vn = vn
        return found_vn

    def deactivate_v_node(self, v_node):
        v_node.deactivate()

    def activate_ant(self):
        found_ant = None
        for ant in self.local_antennas:
            if ant.active is False:
                ant.activate()
                found_ant = ant
        return found_ant

    def deactivate_ant(self, ant):
        ant.deactivate()

    def set_local_channels(self):
        chs = {}
        for i in range(0, self.ch_count):
            ch = channel()
            chs[ch.ch_id] = {"availability": True, "power": 12000}
        return chs

    def set_local_antennas(self):
        ants = {}
        for i in range(0, self.ant_count):
            ant = antenna()
            ants[ant.ant_id] = {"availability": True, "power": 12000}
        return ants

    def request_ch(self, rec_node):
        pass

    def print_info(self):
        pprint(vars(self))
