import requests
from bs4 import BeautifulSoup

def define(term):
    term = term.lower()
    website_1 = 'https://en.wikipedia.org/wiki/'
    website_2 = 'https://dictionary.cambridge.org/dictionary/english/'
    try:
        res = requests.get(f'{website_1}{term}').text
        soup = BeautifulSoup(res, 'html.parser')
        title = soup.h1.text.lower()
        meaning = soup.find('div', class_='shortdescription nomobile noexcerpt noprint searchaux').text
        link1 = soup.find('a', class_='extiw')['href']
        #link2 = f'https://en.wiktionary.org/wiki/{term}'
        #value = f'Meaning of {title}:\n{meaning}.\n\n\nYou can find more information on that here:\n{link2}\n{link1}\n'
        if meaning.startswith('Disambiguation'):
            return "Sorry, couldn't find. If you try being more specific next time, it may be found"
        else:
            return meaning.lower()

    except Exception as e:
        res = requests.get(f'{website_2}{term}').text
        soup = BeautifulSoup(res, 'html.parser')
        title = soup.find('span', class_='hw dhw').text.lower()
        meaning = soup.find('div', class_="def ddef_d db").text
        #link = f'https://www.merriam-webster.com/dictionary/{term}'
        #value = f'Meaning of {title}:\n{meaning}.\n\n\nYou can find more information on that here:\n{link}\n'
        return meaning.lower()



if __name__ == '__main__':
    print(define('Animal'))


