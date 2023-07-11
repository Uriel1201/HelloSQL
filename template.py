# pip install pandas
# pip install SQLAlchemy
# pip install cxOracle

import pandas as pd 
import cx_Oracle
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)

tablename_sql = """select * from tablename""";
df_tablename = pd.read_sql(table_sql, engine)
print(df_tablename)
except SQLAlchemyError as e:
print(e)
