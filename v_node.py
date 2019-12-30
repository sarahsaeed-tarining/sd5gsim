import uuid
import node
import basestation
import resource


class v_node:
    def __init__(self, **kwargs):
        self.v_node_id = "v_" + str(uuid.uuid4())
        self.active = False
        self.alloc_res_list = []
        self.parent_nd = None
        self.parent_bs = None

        for key, value in kwargs.items():
            setattr(self, key, value)

    def add_res(self, **kwargs):  # kwargs = {"channel": channel,"ant": ant, "power": power, "time": time}
        res = resource(**kwargs)
        self.alloc_res_list.append(res)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def request_res(self):
        pass

    def vacate_res(self):
        pass
