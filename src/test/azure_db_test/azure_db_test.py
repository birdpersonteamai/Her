import pyodbc


connectionString = 'Driver={ODBC Driver 13 for SQL Server};Server=tcp:herai.database.windows.net,1433;Database=HerAiDB;Uid=birdpersonteam@herai;Pwd={Kalekalekale247};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

connection = pyodbc.connect(connectionString)

# cursor is temp work are containing info retrieved from query
cursor = connection.cursor()

# example query: no data in db currently
# cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
#row = cursor.fetchone()
#while row:
#    print (str(row[0]) + " " + str(row[1]))
#    row = cursor.fetchone()