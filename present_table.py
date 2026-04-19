from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")
table.add_row("1977", "Star Wars: Episode IV - A New Hope", "$775,398,007")
table.add_row("1980", "Star Wars: Episode V - The Empire Strikes Back", "$547,969,004")
table.add_row("1983", "Star Wars: Episode VI - Return of the Jedi", "$475,106,177")

console = Console()
console.print(table)
