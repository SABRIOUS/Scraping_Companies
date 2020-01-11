from bs4 import BeautifulSoup
import requests


html = requests.get('https://www.inc.com/inc5000/2019/top-private-companies-2019-inc5000.html')
soup = BeautifulSoup(html.content, 'html.parser')
rows = soup.find('tbody')
all_links =  [link.find('a').attrs['href'] for link  in rows]

#second step
link_one = all_links[0]
get_one_page = requests.get(link_one)
soup_1 = BeautifulSoup(get_one_page.content, 'html.parser')
# all informations from article
rows_2 = soup_1.find('article')
# Name
company_name = rows_2.find('h1')
#RanK
company_rank = rows_2.find('dd').text.split(" ")[1]

#Industry
company_industry = rows_2.find('dd',{'class':'profileCss.singleIndustry'})


#Revenue
company_revenue = rows_2.find('dl',{'class':'undefined col-sm-6'}).text.split(" ")[3],rows_2.find('dl',{'class':'undefined col-sm-6'}).text.split(" ")[4]


#City
company_city = rows_2.find_all('dl',{'class':'undefined'})[4].text.split(",")[0].split(":")[1]

# Founded
company_year_founded = rows_2.find_all('dl',{'class':'undefined'})[5].text.split(":")[1]

# Employees
company_employees = rows_2.find_all('dl',{'class':'undefined'})[6].text.split(":")[1]

# Description
company_description = rows_2.find('p').text
