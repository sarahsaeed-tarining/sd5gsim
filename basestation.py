import uuid
from random import randrange
import matplotlib.pyplot as plt
from node import node
from channel import channel


class basestation:
    def __init__(self, **kwargs):
        self.bs_id = "b_" + str(uuid.uuid4())
        self.n_count = 6
        self.all_ch_count = 6

        self.coordinates = {"x": randrange(540, 590), "y": randrange(450, 500)}
        self.dimensions = {"x": 1000, "y": 1000}

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.bs_nodes = [node(**{"parent_bs": self}) for i in range(0, self.n_count)]
        self.global_pool = [channel(**{"availability": True, "power": 12000}) for i in range(0, self.all_ch_count)]

        self.ch_allocations = {}

        # Calculating Network Metrics
        self.channel_capacity = 5000
        self.num_of_reqs = 0
        self.num_of_blocked_reqs = 0
        self.num_of_transmitted_pkts = 0
        self.total_bandwidth = self.channel_capacity * self.all_ch_count
        self.utilized_channels = 0
        self.num_control_msg = 0
        self.packet_size = 500
        self.control_msg_size = 50

        self.throughput = 0.0
        self.blocking_rate = 0.0
        self.channel_utilization = 0.0

    def calculate_metrics(self, sim_time):
        try:
            thpt = (self.num_of_transmitted_pkts * self.packet_size) / sim_time
        except Exception as e:
            thpt = 0.0
        try:
            overhead = (self.num_control_msg * self.control_msg_size) / (self.num_of_transmitted_pkts * self.packet_size)
        except Exception as e:
            overhead = 0.0
        try:
            block_rate = self.num_of_blocked_reqs / self.num_of_reqs
        except Exception as e:
            block_rate = 0.0
        try:
            utilization = self.utilized_channels / (self.total_bandwidth)
        except Exception as e:
            utilization = 0.0

        return(thpt, overhead, block_rate, utilization)

    def assing_ch_to_node(self, **kwargs):
        ch_to_assign = None
        for ch in self.global_pool:
            if ch.availability:
                ch.availability = False
                kwargs["src_ch"] = ch
                self.establish_connection(**kwargs)
                return ch
        return ch_to_assign

    def establish_connection(self, **kwargs):
        # kwargs = {"src_node": src_node, "src_vnode": src_vnode, "src_ant": src_ant, "src_ch": src_ch, "des_node": des_node, "des_vnode": des_vnode, "des_ant": des_ant}
        cnt = connection(**kwargs)
        self.ch_allocations[cnt.src_ch.ch_id] = cnt.src_node

    def terminate_connection(self, **kwargs):
        src_node = kwargs["src_node"]
        src_vnode = kwargs["src_vnode"]
        src_ant = kwargs["src_ant"]
        des_node = kwargs["des_node"]
        des_vnode = kwargs["des_vnode"]
        des_ant = kwargs["des_ant"]
        src_ch = kwargs["src_ch"]
        num_of_pkts = kwargs["num_of_pkts"]

        self.num_of_transmitted_pkts += num_of_pkts
        src_node.deactivate_v_node(src_vnode)
        des_node.deactivate_v_node(des_vnode)
        src_node.deactivate_ant(src_ant)
        des_node.deactivate_ant(des_ant)
        src_ch.availability = True

        self.ch_allocations[src_ch.ch_id] = None

    def calculate_tx_time(self, num_pckts):
        return (num_pckts * self.packet_size) / self.channel_capacity

    def plot_network(self):
        x_coordinates = []
        y_coordinates = []
        for nd in self.bs_nodes:
            x_coordinates.append(nd.coordinates["x"])
            y_coordinates.append(nd.coordinates["y"])
        plt.scatter(x_coordinates, y_coordinates)
        plt.show()
