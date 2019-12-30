import uuid


class resource:
    def __init__(self, **kwargs):
        self.res_id = "r_" + str(uuid.uuid4())
        self.alloc_ch = None
        self.alloc_ant = None
        self.alloc_time = None
        self.alloc_power = None
        for key, value in kwargs.items():
            setattr(self, key, value)
