class Console:
    def __init__(self, service):
        self.__service = service

        self.__console_options = {
            "1": self.__read_graph_from_file,
            "": self.__show_graph,
            "x": exit
        }

    def __read_graph_from_file(self):
        file_name = input("file name: ")
        file_name = file_name.strip()

        self.__service.read_directed_graph_from_file_first_convention(file_name)

    def __show_graph(self):
        pass

    def print_console_options(self):
        print("1: read graph from file")
        print(": show graph")
        print("x: exit")

    def run_console(self):
        while True:
            try:
                self.print_console_options()

                chosen_option = input("> ")

                self.__console_options[chosen_option]()

            except Exception as error:
                print(error)
