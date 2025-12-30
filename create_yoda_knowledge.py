import os
import sys
from scraper import WebScraper
from rich.console import Console
from rich.panel import Panel

console = Console()

# Configuration mapping URLs to the Yoda knowledge base structure
YODA_KNOWLEDGE_CONFIG = {
    "programming/languages/python": [
        "https://docs.python.org/3/tutorial/index.html",
        "https://peps.python.org/pep-0008/"
    ],
    "programming/languages/javascript": [
        "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
        "https://react.dev/learn"
    ],
    "programming/best-practices": [
        "https://clean-code-developer.com/",
        "https://refactoring.guru/refactoring/what-is-refactoring"
    ],
    "programming/architecture": [
        "https://12factor.net/"
    ],
    "persona/yoda-style": [
        "https://starwars.fandom.com/wiki/Yoda",
        "https://starwars.com/news/the-star-wars-wisdom-of-yoda"
    ]
}

MAX_FILES = 20

class YodaKnowledgeBuilder:
    def __init__(self, base_output_dir="knowledge-base"):
        self.base_output_dir = base_output_dir
        self.total_scraped = 0

    def build(self):
        console.print(Panel("[bold green]Master Yoda Knowledge Base Builder[/bold green]\n"
                             "Initializing knowledge gathering...", title="Force Awakening"))

        # Sort categories to prioritize personality if needed, but let's just go through them.
        for category, urls in YODA_KNOWLEDGE_CONFIG.items():
            if self.total_scraped >= MAX_FILES:
                break
                
            category_dir = os.path.join(self.base_output_dir, category)
            console.print(f"\n[bold blue]Building category: {category}[/bold blue]")
            
            # Allocate budget: 2 pages per URL of personality, 1 for others or as remaining
            for url in urls:
                if self.total_scraped >= MAX_FILES:
                    break
                
                remaining_budget = MAX_FILES - self.total_scraped
                # Smart allocation: Persona gets more detail (2 pages), others 1
                page_limit = 2 if "persona" in category else 1
                page_limit = min(page_limit, remaining_budget)
                
                console.print(f"[yellow]Sensing the Force in:[/yellow] {url} (Limit: {page_limit})")
                
                # Use recursion for persona to get more depth if limit > 1
                is_recursive = page_limit > 1
                
                scraper = WebScraper(url, recursive=is_recursive, output_dir=category_dir, max_pages=page_limit)
                scraper.start()
                
                # Check how many were actually scraped by looking at scraper.visited_urls
                scraped_count = len(scraper.visited_urls)
                self.total_scraped += scraped_count

        console.print(Panel(f"[bold green]Knowledge Base Construction Complete![/bold green]\n"
                             f"Total files gathered: {self.total_scraped}\n"
                             f"Location: {os.path.abspath(self.base_output_dir)}", title="Wisdom Acquired"))

        console.print(Panel(f"[bold green]Knowledge Base Construction Complete![/bold green]\n"
                             f"Total files gathered: {self.total_scraped}\n"
                             f"Location: {os.path.abspath(self.base_output_dir)}", title="Wisdom Acquired"))

def main():
    builder = YodaKnowledgeBuilder()
    builder.build()

if __name__ == "__main__":
    main()
