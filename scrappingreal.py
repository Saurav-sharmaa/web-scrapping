from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
# print(html_text)


soup = BeautifulSoup(html_text,'lxml')
 
# jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx' )

jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx' )

for job in jobs:
    
    posdate = job.find('span',class_="sim-posted").text

    if 'few' in posdate:
    
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(" ", '')
        skills = job.find('span',class_="srp-skills").text.replace(" ","")
        moreinfo = job.header.h2.a['href']

        print(f"Company Name    : {company_name.strip()}")
        print(f"Skills Required : {skills.strip()}")
        print(f"More info       : {moreinfo}")
        print(" ")

    



# print(f'''
# Company Name    : {company_name}
# Skills Required : {skills}
# ''')

