from platform import system


class SystemOp:
    def __init__(self):
        self.__str__()

    def __str__(self):
        return system()  # Returns in str the operating system. ('Linux', 'Windows')
