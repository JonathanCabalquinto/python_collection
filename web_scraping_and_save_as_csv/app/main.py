from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_largest_banks_in_the_Philippines'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find_all('table')[0]
headers = table.find_all('tr')[0].find_all('th')
content = table.find_all('tr')

header_title = [title.text.strip() for title in headers]

df = pd.DataFrame(columns=header_title)
for row in content[1:]:
    row_data = row.find_all('th') + row.find_all('td')
    individual_row = []

    for data in row_data:
        span_element = data.find_all('span')
        if len(span_element) > 1:
            if data.find_all('span')[1] and 'title' in data.find_all('span')[1].attrs:
                title_attribute = data.find_all('span')[1]['title']
                individual_row.append(title_attribute)
        else:
            individual_row.append(data.text.strip())
    length = len(df)
    df.loc[length] = individual_row
    print(individual_row)


df.to_csv(r'C:\Users\jonathan.cabalquinto\research_development\web_scraping\ScrapedDataset\companies.csv', index=False)

