from rich.markdown import Markdown
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel


md1 = """
# My Markdown Title

This is a paragraph with **bold** text and *italic* text.

- Item 1
- Item 2
- Item 3
"""

md2 = """
## Another Title

Here is a list of items:

1. First item
2. Second item
3. Third item
"""

console = Console()
markdown1 = Markdown(md1)
markdown2 = Markdown(md2)
console.print(Columns([Panel.fit(markdown1, title="panel 1", width=60), Panel.fit(markdown2, title="panel 2", width=60)]))