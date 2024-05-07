class User:
    def __init__(self, u_id: int, name: str):
        self.u_id = u_id
        self.name = name

    @staticmethod
    def get_by_id(u_id: int):
        return User(u_id, "John Doe")
