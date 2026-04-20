from rich.console import Console
from rich.traceback import install
import time

install()

def add_two(n1, n2):
    console.log("About to add two numbers", log_locals=True)
    return n1 + n2

console = Console(record=True)
try:
    for i in range(10):
        time.sleep(.3)
        add_two(1, i)
    add_two(1, 'a')
except:
    console.print_exception()

console.save_html("debug.html")