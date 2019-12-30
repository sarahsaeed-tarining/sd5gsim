import uuid


class antenna:
    def __init__(self, **kwargs):
        self.ant_id = "a_" + str(uuid.uuid4())
        self.active = None
        self.power = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.power = 0.0
        self.active = False
