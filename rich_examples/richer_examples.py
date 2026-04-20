from rich.console import Console
from rich.theme import Theme
import time


custom_theme = Theme({
    "success": "green",
    "error": "bold red",
    "warning": "yellow"
})
console = Console(theme=custom_theme)


console.print(f"I wonder what this looks like 1 + 1 = {1 + 1}")
console.print({"a": [1, 2, 3], "b" : {"c" : 1}})

console.print("This is [bold magenta]rich[/bold magenta]!", ":thumbs_up:")
console.print("This is some text!", ":thumbs_up:", style="bold underline")
console.print("This is some text!", ":thumbs_up:", style="bold underline red")
console.print("This is some text!", ":thumbs_up:", style="bold underline red on white")
console.print("[bold]This [underline]is[/] some text![/]")

console.print("This is a success message!", style="success")
console.print("This is an error message!", style="error")
console.print("This is a warning message!", style="warning")

console.print(":thumbs_up: File uploaded successfully!", style="success")

for i in range(10):
    console.log(f"I am about to sleep={i}")
    time.sleep(.3)
    console.log(f"But I am briefly awake now.")
