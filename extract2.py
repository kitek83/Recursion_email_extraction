#extract2.py
"""This program extrtract emails from the web page."""
from extract_emails import EmailExtractor
from extract_emails.browsers import RequestsBrowser


with RequestsBrowser() as browser:
    email_extractor = EmailExtractor("https://virtualpeople.pl/", browser, depth=6)
    emails = email_extractor.get_emails()


for email in emails:
    print(email)
    print(email.as_dict())

"""
output:
Email(email="kontakt@virtualpeople.pl", source_page="https://virtualpeople.pl/")
{'email': 'kontakt@virtualpeople.pl', 'source_page': 'https://virtualpeople.pl/'}
Email(email="tech@virtualpeople.pl", source_page="https://virtualpeople.pl/kontakt")
{'email': 'tech@virtualpeople.pl', 'source_page': 'https://virtualpeople.pl/kontakt'}
Email(email="ksiegowosc@virtualpeople.pl", source_page="https://virtualpeople.pl/kontakt")
{'email': 'ksiegowosc@virtualpeople.pl', 'source_page': 'https://virtualpeople.pl/kontakt'}

"""