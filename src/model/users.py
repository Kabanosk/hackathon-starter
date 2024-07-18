class User:
    def __init__(self, u_id: int, name: str):
        self.u_id = u_id
        self.name = name

    def __dict__(self):
        return {"u_id": self.u_id, "name": self.name}

    @staticmethod
    def get_by_id(u_id: int):
        return User(u_id, "John Doe")

    def save(self):
        raise NotImplementedError("Saving in database is not implemented yet.")
