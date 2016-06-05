# Provides methods for manipulating text styling in specific terminals.
# Uses a basic chaining method where text properties are added by calling
# methods with related names.
# 
# For example, to print "Hello, world!" in red:
#   print pyfancy().red("Hello, world!").get()
#
# Styles can be changed for different text components. Example:
#   print pyfancy().red("Hello").raw(", ").blue("world!").get()
#
# No output text is necessary when calling a styling method. This allows
# styles to be stacked:
#   print pyfancy().red().bold("Hello, world!").get()
#
# There are two provided ways to access the modified text. The first is
# direct access to the string object called "out". However, accessing this
# object will not reset the style, so any text outputted after will have
# the same style as whatever the text was at the end of the chain.
# 
# The get() method is better for accessing text because it resets the text
# style so no new text will have unwanted styling.

class pyfancy:

    # Stores output text, for reset use get()
    out = ""

    # Returns output text and resets properties
    def get(self):
        return self.out + "\033[0m"

    # Outputs text using print (should work in Python 2 and 3)
    def output(self):
        print(self.get())

    # Adds new text without changing the styling
    def add(self,addition):
        self.out += addition;
        return self;

    # Raw text - i.e. default styling
    def raw(self,addition=""):
        self.out += "\033[0m" + addition + + "\033[0m"
        return self

    # Bold text
    def bold(self,addition=""):
        self.out += "\033[1m" + addition + + "\033[0m"
        return self

    # Dim text
    def dim(self,addition=""):
        self.out += "\033[2m" + addition + + "\033[0m"
        return self

    # Underlined text
    def underlined(self,addition=""):
        self.out += "\033[4m" + addition + "\033[0m"
        return self

    # Blinking text
    def blink(self,addition=""):
        self.out += "\033[5m" + addition + "\033[0m"
        return self

    # Foreground / background inverted
    def invert(self,addition=""):
        self.out += "\033[7m" + addition + "\033[0m"
        return self

    # Hidden text
    def hidden(self,addition=""):
        self.out += "\033[8m" + addition + "\033[0m"
        return self

    # Black text
    def black(self,addition=""):
        self.out += "\033[30m" + addition + "\033[0m"
        return self

    # Red text
    def red(self,addition=""):
        self.out += "\033[31m" + addition + "\033[0m"
        return self

    # Green text
    def green(self,addition=""):
        self.out += "\033[32m" + addition + "\033[0m"
        return self
    
    # Yellow text
    def yellow(self,addition=""):
        self.out += "\033[33m" + addition + "\033[0m"
        return self

    # Blue text
    def blue(self,addition=""):
        self.out += "\033[34m" + addition + "\033[0m"
        return self

    # Magenta text
    def magenta(self,addition=""):
        self.out += "\033[35m" + addition + "\033[0m"
        return self

    # Cyan text
    def cyan(self,addition=""):
        self.out += "\033[36m" + addition + "\033[0m"
        return self

    # Light gray text
    def lightGray(self,addition=""):
        self.out += "\033[37m" + addition + "\033[0m"
        return self

    # Dark gray text
    def darkGray(self,addition=""):
        self.out += "\033[90m" + addition + "\033[0m"
        return self

    # Light red text
    def lightRed(self,addition=""):
        self.out += "\033[91m" + addition + "\033[0m"
        return self

    # Light green text
    def lightGreen(self,addition=""):
        self.out += "\033[92m" + addition + "\033[0m"
        return self

    # Light yellow text
    def lightYellow(self,addition=""):
        self.out += "\033[93m" + addition + "\033[0m"
        return self

    # Light blue text
    def lightBlue(self,addition=""):
        self.out += "\033[94m" + addition + "\033[0m"
        return self

    # Light magenta text
    def lightMagenta(self,addition=""):
        self.out += "\033[95m" + addition + "\033[0m"
        return self

    # Light cyan text
    def lightCyan(self,addition=""):
        self.out += "\033[96m" + addition + "\033[0m"
        return self

    # White text
    def white(self,addition=""):
        self.out += "\033[97m" + addition + "\033[0m"
        return self
