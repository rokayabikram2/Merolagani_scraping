


# return render_template("merolagani.html",new=new)
from bs4 import BeautifulSoup
import requests
import lxml
import mysql.connector


#site url
url ="https://merolagani.com/LatestMarket.aspx"
#get request to fetch the raw gtml data
content= requests.get(url)
soup = BeautifulSoup(content.text,'lxml') #this is code of page
table = soup.find('table',class_="table table-hover live-trading sortable") #this is table withn its class
headers = [i.text for i in table.find_all('th')] #data of th tag
# print(headers)
data =[j for j in table.find_all('tr',{"class":["decrease-row","increase-row"]})] #data which are inside tr tag

#making  in the formate of list like[{'name':ADCL,'LTP':'450'}]
result =[{headers[index]:cell.text for index, cell in enumerate(row.find_all("td"))} for row in data]

print(result)


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="scrap",
    
)

# Create a cursor
cursor = conn.cursor()

# Assuming 'result' is the list of dictionaries you want to store in the database
for result_row in result:
    query = "INSERT INTO mero_stock(Symbol, LTP, Changes, Open,High, Low,Qty,PClose,Diff ) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
        result_row.get('Symbol', ''),
        result_row.get('LTP', ''),
        result_row.get('Changes', ''),  
        result_row.get('Open', ''),
        result_row.get('High', ''),
        result_row.get('Low', ''),
        result_row.get('Qty', ''),
        result_row.get('PClose', ''),
        result_row.get('Diff', '')
        
        
    )

    try:
        cursor.execute(query, values)
        conn.commit()  
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print(f"Query: {query}")
        print(f"Values: {values}")
        conn.rollback()  



