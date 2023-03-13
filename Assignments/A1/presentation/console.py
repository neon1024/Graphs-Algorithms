class Console:
    def __init__(self, service, repository):
        self.__service = service
        self.__repository = repository

        self.__console_options = {
            "1": self.__show_graph,
            "x": exit
        }

    def __show_graph(self):
        pass

    def print_console_options(self):
        print("1: show graph")
        print("x: exit")

    def run_console(self):
        while True:
            try:
                self.print_console_options()
            except Exception as error:
                print(error)
