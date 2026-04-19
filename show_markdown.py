from rich.markdown import Markdown
from rich.console import Console


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
console.print(Markdown(md1))
console.print(Markdown(md2))