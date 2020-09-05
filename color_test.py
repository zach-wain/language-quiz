# See: https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Simple text joining
print("What is " + bcolors.OKGREEN + "Si" + bcolors.ENDC + " multiplied by " + bcolors.FAIL + "San" + bcolors.ENDC + "?")

# Format statement
print("What is {}Si{} multiplied by {}San{}?".format(bcolors.OKGREEN, bcolors.ENDC, bcolors.BOLD, bcolors.ENDC))

# Format statement with vars
si = bcolors.BOLD + bcolors.FAIL + "Si" + bcolors.ENDC
san = bcolors.BOLD + bcolors.OKGREEN + "San" + bcolors.ENDC
print("What is {} multiplied by {}?".format(si, san))

# emoji and kaomoji
print("This rocks ❤❤❤😎🤞")
print("This still rocks ¯\_(ツ)_/¯")



