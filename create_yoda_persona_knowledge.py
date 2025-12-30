import os
from scraper import WebScraper
from rich.console import Console
from rich.panel import Panel

console = Console()

# High-quality URLs focused on Yoda's philosophy, speech patterns, and wisdom
YODA_PERSONA_URLS = [
    "https://starwars.fandom.com/wiki/Yoda",
    "https://starwars.com/news/the-star-wars-wisdom-of-yoda",
    "https://www.starwars.com/databank/yoda",
    "https://en.wikipedia.org/wiki/Yoda",
    "https://www.mentalfloss.com/article/63200/15-powerful-quotes-yoda",
    "https://www.ign.com/articles/yoda-best-quotes-star-wars"
]

class YodaPersonaBuilder:
    def __init__(self, output_dir="knowledge-base/persona"):
        self.output_dir = output_dir
        self.total_scraped = 0

    def consolidate(self):
        master_file_path = os.path.join(self.output_dir, "yoda_persona_master.md")
        console.print(f"\n[bold magenta]Consolidating all wisdom into:[/bold magenta] {master_file_path}")
        
        with open(master_file_path, "w", encoding="utf-8") as master_file:
            master_file.write("# Master Yoda Persona Knowledge\n\n")
            master_file.write("> \"Much to learn, you still have.\"\n\n")
            
            for root, dirs, files in os.walk(self.output_dir):
                for file in sorted(files):
                    if file.endswith(".md") and file != "yoda_persona_master.md":
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, self.output_dir)
                        
                        master_file.write(f"\n\n## Source: {relative_path}\n\n")
                        try:
                            with open(file_path, "r", encoding="utf-8") as f:
                                # Add a bit of spacing and separate content
                                master_file.write(f.read())
                                master_file.write("\n\n---\n")
                        except Exception as e:
                            console.print(f"[red]Error reading {file_path}: {e}[/red]")

    def build(self):
        console.print(Panel("[bold green]Master Yoda Persona Knowledge Gathering[/bold green]\n"
                             "Deep into the Force, we must go...", title="Force Attunement"))

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

        try:
            for url in YODA_PERSONA_URLS:
                console.print(f"\n[bold blue]Seeking wisdom in:[/bold blue] {url}")
                
                scraper = WebScraper(url, recursive=True, output_dir=self.output_dir, max_pages=None)
                scraper.start()
                
                scraped_count = len(scraper.visited_urls)
                self.total_scraped += scraped_count
        except KeyboardInterrupt:
            console.print("\n[bold yellow]Interrupting the Force, we are. Consolidating what we have...[/bold yellow]")
        finally:
            # Consolidate after scraping (or interrupt)
            self.consolidate()

        console.print(Panel(f"[bold green]Persona Knowledge Gathering and Consolidation Complete![/bold green]\n"
                             f"Wisdom nuggets gathered: {self.total_scraped}\n"
                             f"Master file: {os.path.abspath(os.path.join(self.output_dir, 'yoda_persona_master.md'))}", title="Wisdom Consolidated"))

def main():
    builder = YodaPersonaBuilder()
    builder.build()

if __name__ == "__main__":
    main()
