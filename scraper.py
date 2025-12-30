import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
from markdownify import markdownify as md
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.panel import Panel
from rich.table import Table

console = Console()

class WebScraper:
    def __init__(self, base_url, recursive=False, output_dir="scraped_data"):
        self.base_url = base_url
        self.recursive = recursive
        self.output_dir = output_dir
        self.visited_urls = set()
        self.domain = urlparse(base_url).netloc

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

    def is_valid_url(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and parsed.netloc == self.domain

    def get_filename(self, url):
        path = urlparse(url).path
        if not path or path == "/":
            return "index.md"
        filename = path.strip("/").replace("/", "_")
        if not filename.endswith(".md"):
            filename += ".md"
        return filename

    def scrape_url(self, url, progress, task_id):
        if url in self.visited_urls:
            return []
        
        self.visited_urls.add(url)
        progress.update(task_id, description=f"[cyan]Scraping:[/cyan] {url}")
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            html_content = response.text
            
            # Convert to Markdown
            markdown_content = md(html_content, heading_style="ATX")
            
            # Determine directory and filename
            parsed_url = urlparse(url)
            site_name = parsed_url.netloc
            site_dir = os.path.join(self.output_dir, site_name)
            if not os.path.exists(site_dir):
                os.makedirs(site_dir, exist_ok=True)
            
            filename = self.get_filename(url)
            filepath = os.path.join(site_dir, filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            
            subpages = []
            if self.recursive:
                soup = BeautifulSoup(html_content, 'html.parser')
                for a_tag in soup.find_all('a', href=True):
                    link = urljoin(url, a_tag['href'])
                    if self.is_valid_url(link) and link not in self.visited_urls:
                        subpages.append(link)
            
            return subpages
        except Exception as e:
            console.print(f"[bold red]Error scraping {url}:[/bold red] {str(e)}")
            return []

    def start(self):
        console.print(Panel(f"[bold blue]Web Scraper Started[/bold blue]\n[yellow]Base URL:[/yellow] {self.base_url}\n[yellow]Recursive:[/yellow] {self.recursive}", title="Status"))
        
        urls_to_scrape = [self.base_url]
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console
        ) as progress:
            main_task = progress.add_task("[green]Total Progress...", total=None)
            
            while urls_to_scrape:
                current_url = urls_to_scrape.pop(0)
                new_links = self.scrape_url(current_url, progress, main_task)
                
                if self.recursive:
                    urls_to_scrape.extend(new_links)
                
                progress.update(main_task, advance=1, description=f"[green]Scraped {len(self.visited_urls)} pages[/green]")

        console.print(f"\n[bold green]Scraping completed![/bold green] Total pages: {len(self.visited_urls)}")
        console.print(f"[yellow]Files saved in:[/yellow] {os.path.abspath(self.output_dir)}")

def main():
    parser = argparse.ArgumentParser(description="A simple web scraper with progress visualization.")
    parser.add_argument("url", help="The URL to scrape")
    parser.add_argument("--subpages", action="store_true", help="Enable recursive subpages scraping")
    parser.add_argument("--output", default="scraped_data", help="Output directory for scraped files")
    
    args = parser.parse_args()
    
    scraper = WebScraper(args.url, recursive=args.subpages, output_dir=args.output)
    scraper.start()

if __name__ == "__main__":
    main()
