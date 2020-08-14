class String:

    def __init__(self):
        self.str1 = ""

    def get_String(self, palabra):
        self.str1 = palabra

    def print_String(self):
        print(self.str1.upper())


str1 = String()
str1.get_String(input("escribe algo "))
str1.print_String()
