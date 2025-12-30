import os
import re

def optimize_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Markdown Image links: ![alt](url) -> ""
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)

    # 2. Remove Markdown links: [label](url) -> label
    content = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', content)
    content = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', content)

    # 3. Remove leftover image markers or empty links
    content = re.sub(r'!\[.*?\]', '', content)
    content = re.sub(r'\[\]\(.*?\)', '', content)

    # 4. Remove bare URLs
    content = re.sub(r'https?://\S+', '', content)
    
    # 5. Remove relative paths in parentheses
    content = re.sub(r'\((/[\w\.\-\/]+|#[\w\-\.]+)\)', '', content)

    # 6. Remove specific noise patterns
    noise_patterns = [
        r'Legal Terms of Service.*',
        r'Cookie Preferences.*',
        r'Privacy Information.*',
        r'Responsible Disclosure.*',
        r'Trust Contact.*',
        r'Your Privacy Choices.*',
        r'Contents\s*\* \d+.*',
        r'\| Contents.*',
        r'\* \d+ Unexpected behaviour.*',
        r'© Copyright.*',
        r'Salesforce Tower.*',
        r'Written by .* • Last updated .*',
        r'Next »',
        r'« Previous',
        r'read on…',
        r'.* \(\w{2}\) \| .* \(\w{2}\) \| .* \(\w{2}\).*',
    ]
    for pattern in noise_patterns:
        content = re.sub(pattern, '', content)

    # 7. Clean up lines
    lines = content.split('\n')
    cleaned_lines = []
    
    # Menu items to remove (common in these scraped files)
    menu_items = {'Blog', 'Community', 'App', 'GitHub', 'Download ePub Book', 'Sourcecode'}
    
    for line in lines:
        stripped = line.strip()
        
        # Remove empty bullets or numbers
        if re.match(r'^[\*\-\+]\s*$', stripped) or re.match(r'^\d+\.\s*$', stripped):
            continue
            
        # Remove menu item bullets
        if stripped.startswith('* ') and stripped[2:] in menu_items:
            continue
            
        # Remove lines that are just artifacts like "!GitHub logoGitHub" or "!Vish Abrams"
        # We look for a line that has a "!" and is short
        temp = re.sub(r'[\*\-\+\d\.\s]', '', stripped)
        if temp.startswith('!') and len(temp) < 40:
            continue
            
        cleaned_lines.append(line)
    
    content = '\n'.join(cleaned_lines)

    # 8. Final clean up
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    content = re.sub(r'#+\s*$', '', content, flags=re.MULTILINE)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

def main():
    directory = '/var/www/apps/personal_projects/web_scraper/knowledge-base/developer'
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            print(f'Optimizing {filename}...')
            optimize_markdown(file_path)
            print(f'Done {filename}.')

if __name__ == "__main__":
    main()
