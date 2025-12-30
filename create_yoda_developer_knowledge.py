import os
from scraper import WebScraper
from rich.console import Console
from rich.panel import Panel

console = Console()

# Mapping of subjects to their source URLs
DEVELOPER_KNOWLEDGE_CONFIG = {
    "languages": {
        "python": "https://docs.python.org/3/tutorial/index.html",
        "javascript": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
        "typescript": "https://www.typescriptlang.org/docs/handbook/intro.html",
        "go": "https://go.dev/doc/tutorial/getting-started",
        "rust": "https://doc.rust-lang.org/book/title-page.html",
        "java": "https://dev.java/learn/",
        "cpp": "https://en.cppreference.com/w/",
    },
    "frameworks": {
        "react": "https://react.dev/learn",
        "nextjs": "https://nextjs.org/docs",
        "vue": "https://vuejs.org/guide/introduction.html",
        "django": "https://docs.djangoproject.com/en/stable/",
        "spring": "https://spring.io/guides",
        "flutter": "https://docs.flutter.dev/get-started/install",
        "nodejs": "https://nodejs.org/en/docs/guides/",
    },
    "patterns_architecture": {
        "design_patterns": "https://refactoring.guru/design-patterns",
        "clean_architecture": "https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html",
        "solid": "https://en.wikipedia.org/wiki/SOLID",
        "best_practices": "https://12factor.net/",
    }
}

class DeveloperKnowledgeBuilder:
    def __init__(self, base_output_dir="knowledge-base/developer"):
        self.base_output_dir = base_output_dir
        self.total_scraped = 0

    def consolidate(self, category, subject, scraped_dir):
        output_file = os.path.join(self.base_output_dir, f"{subject}.md")
        console.print(f"[bold magenta]Consolidating {subject} into:[/bold magenta] {output_file}")
        
        with open(output_file, "w", encoding="utf-8") as f_out:
            f_out.write(f"# {subject.capitalize()} Knowledge\n\n")
            f_out.write(f"> Category: {category}\n\n")
            
            for root, dirs, files in os.walk(scraped_dir):
                for file in sorted(files):
                    if file.endswith(".md"):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, "r", encoding="utf-8") as f_in:
                                content = f_in.read()
                                f_out.write(f"\n## Source: {file}\n\n")
                                f_out.write(content)
                                f_out.write("\n\n---\n")
                        except Exception as e:
                            console.print(f"[red]Error reading {file_path}: {e}[/red]")

    def build(self):
        console.print(Panel("[bold green]Master Yoda Developer Knowledge Builder[/bold green]\n"
                             "Scanning the galaxy for programming wisdom...", title="Force Search"))

        if not os.path.exists(self.base_output_dir):
            os.makedirs(self.base_output_dir, exist_ok=True)

        temp_dir = "temp_scraping"
        
        try:
            for category, subjects in DEVELOPER_KNOWLEDGE_CONFIG.items():
                for subject, url in subjects.items():
                    console.print(f"\n[bold blue]Acquiring knowledge: {subject} ({category})[/bold blue]")
                    console.print(f"[yellow]Sensing the Force in:[/yellow] {url}")
                    
                    subject_temp_dir = os.path.join(temp_dir, subject)
                    
                    # We use recursion for better depth but limit max pages for lean search
                    scraper = WebScraper(url, recursive=True, output_dir=subject_temp_dir, max_pages=5)
                    scraper.start()
                    
                    self.total_scraped += len(scraper.visited_urls)
                    
                    # Consolidate after each subject
                    self.consolidate(category, subject, subject_temp_dir)
                    
        except KeyboardInterrupt:
            console.print("\n[bold yellow]Interrupting the search, we are. Saving what we have...[/bold yellow]")
        finally:
            console.print(Panel(f"[bold green]Developer Knowledge Gathering Complete![/bold green]\n"
                                 f"Subjects processed: {sum(len(v) for v in DEVELOPER_KNOWLEDGE_CONFIG.values())}\n"
                                 f"Total pages scanned: {self.total_scraped}\n"
                                 f"Knowledge base: {os.path.abspath(self.base_output_dir)}", title="Wisdom Found"))

def main():
    builder = DeveloperKnowledgeBuilder()
    builder.build()

if __name__ == "__main__":
    main()
