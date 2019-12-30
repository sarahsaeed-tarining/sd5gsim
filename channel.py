import uuid


class channel:
    def __init__(self, **kwargs):
        self.ch_id = "ch_" + str(uuid.uuid4())
        self.power = None
        self.availability = None
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.allocations = []

    def add_node_to_alloc(self, **kwargs):  # kwargs = {"alloc_node": alloc_node,"alloc_time": alloc_time,"alloc_power": alloc_power}
        alloc = allocation(**kwargs)
        self.alloc_res_list.append(alloc)
