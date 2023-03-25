class EdgeAlreadyExistsError(BaseException):
    def __init__(self):
        print("[!] Edge already exists")


class EdgeDoesNotExistsError(BaseException):
    def __init__(self):
        print("[!] Edge does not exists")


class VertexAlreadyExistsError(BaseException):
    def __init__(self):
        print("[!] Vertex already exists")


class VertexDoesNotExistsError(BaseException):
    def __init__(self):
        print("[!] Vertex does not exists")
