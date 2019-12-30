import uuid


class connection:
    def __init__(self, **kwargs):
        self.connection_id = "c_" + str(uuid.uuid4())
        self.src_node = None
        self.src_vnode = None
        self.src_ant = None
        self.src_ch = None
        self.des_node = None
        self.des_vnode = None
        self.des_ant = None
        for key, value in kwargs.items():
            setattr(self, key, value)
