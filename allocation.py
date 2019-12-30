import uuid


class allocation:
    def __init__(self, **kwargs):
        self.alloc_id = "alloc_" + str(uuid.uuid4())
        self.alloc_node = None
        self.alloc_time = None
        self.alloc_power = None
        for key, value in kwargs.items():
            setattr(self, key, value)
