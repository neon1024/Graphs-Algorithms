class EdgeAlreadyExistError(BaseException):
    def __init__(self):
        print("[!] Edge already exists")


class EdgeDoesNotExistError(BaseException):
    def __init__(self):
        print("[!] Edge does not exists")


class VertexAlreadyExistError(BaseException):
    def __init__(self):
        print("[!] Vertex already exists")


class VertexDoesNotExistError(BaseException):
    def __init__(self):
        print("[!] Vertex does not exists")


class InvalidNumberOfVerticesError(BaseException):
    def __init__(self):
        print("[!] Invalid number of vertices")


class InvalidNumberOfEdgesError(BaseException):
    def __init__(self):
        print("[!] Invalid number of edges")


class NodesMustBeDifferentError(BaseException):
    def __init__(self):
        print("[!] Nodes must be different")
