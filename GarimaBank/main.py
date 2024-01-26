import requests
from bs4 import BeautifulSoup
import mysql.connector

url = "https://merolagani.com/CompanyDetail.aspx?symbol=GBBL"

content = requests.get(url)
print(content)
soup = BeautifulSoup(content.text, 'lxml')

span = soup.find('span', id="ctl00_ContentPlaceHolder1_CompanyDetail1_companyName")
table = soup.find('table', class_="table table-striped table-hover table-zeromargin")
# print(table)
t_body = table.find('tbody', class_='panel panel-default')
print(t_body)
tr =table.find_all('tr')
print(tr)
headers = [i.text for i in t_body.find_all('th')]

# Find all td elements within the table body
t_d = t_body.find_all('td')
# print(t_d)
for cell in t_d:
  print(cell.text)

result =[{headers[index]:cell.text for index, cell in enumerate(row.find_all("td"))} for row in tr]


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="garima bank"
)

# Create a cursor
cursor = conn.cursor()

# Define your INSERT query
query = "INSERT INTO company_detail(Sector, Share_Out, Market_Price, Changes, Last_Trade_On, 52_Weeks_High_Low, 120_Day_Average, 1_Year_Yield, EPS, P_E_Ratio, Book_Value, PBV, Dividend, Bonus, Right_Share, 30_Day_Avg_Volume, Market_Capitalization) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for cell in t_d:
    values = (
        cell.get('Sector', ''),
        cell.get('Share_Out', ''),
        cell.get('Market_Price', ''),
        cell.get('Changes', ''),
        cell.get('Last_Trade_On', ''),
        cell.get('52_Weeks_High_Low', ''),
        cell.get('120_Day_Average', ''),
        cell.get('1_Year_Yield', ''),
        cell.get('EPS', ''),
        cell.get('P_E_Ratio', ''),
        cell.get('Book_Value', ''),
        cell.get('PBV', ''),
        cell.get('Dividend', ''),
        cell.get('Bonus', ''),
        cell.get('Right_Share', ''),
        cell.get('30_Day_Avg_Volume', ''),
        cell.get('Market_Capitalization', ''),
    )

    try:
        cursor.execute(query, values)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print(f"Query: {query}")
        print(f"Values: {values}")
        conn.rollback()

# Close the cursor and connection
cursor.close()
conn.close()
