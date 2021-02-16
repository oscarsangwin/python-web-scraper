# python-web-scraper

- A simple python project which scrapes web pages for connected pages and saves the content of any <title> tags to a text file.
- Uses the urllib and html.parser modules, as well as some other standard library modules.
- The user-agent can be changed, but it is there to bypass some websites (like google.com) which don't allow web scraping with the default urllib user-agent

It works by:
- Taking in a start url (e.g. https://www.bbc.co.uk/news)
- Getting the HTML from the page, and parsing it to:
    - Extract the href value of any <a> tag, and saving it to a list of unscraped urls if it hasn't already been found
    - Any <title> tags that are found are saved to a text file with the website url included
    - A summary of how many links found is printed out, then the program will, after the user presses enter, scrape a random unscraped url
    - The program will end when there are no more urls to scrape, or 'x' is pressed
