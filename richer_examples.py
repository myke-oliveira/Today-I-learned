from rich.console import Console
from rich.theme import Theme


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
