from bs4 import BeautifulSoup
import requests

print("Enter skills you're not familiar with")
unfam_skills = input(">")
print("Filtering out jobs for you")


html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for index, job in enumerate(jobs):
     posdate = job.find('span', class_="sim-posted").span.text

     if 'few' in posdate:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(" ", '')
            skills = job.find('span', class_="srp-skills").text.replace(" ", "")
            moreinfo = job.header.h2.a['href']

            if unfam_skills not in skills:
                with open(f'files/{index}','w') as f:
                  f.write(f"Company Name    : {company_name.strip()}")
                  f.write(f"Skills Required : {skills.strip()}")
                  f.write(f"More info       : {moreinfo}")







