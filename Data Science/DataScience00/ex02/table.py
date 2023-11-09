from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text, MetaData, Table


engine = create_engine("postgresql+psycopg2://nlesage:mysecretpassword@localhost:5432/piscineds", echo=False)

metadata = MetaData()
messages = Table(
	'messages', metadata,
	Column('id', Integer, primary_key=True),
	Column('message', Text),
)
messages.create(bind=engine)

insert_message = messages.insert().values(message='Hello, World!')
engine.execute(insert_message)

# with engine.connect() as conn:
  ##Effectuons une première requête : selection des 10 premières lignes
    # result = conn.execute(text("SELECT * from lieu LIMIT 10"))
    
# metadata = MetaData(bind=engine)
# metadata_obj = MetaData()


# Charge les noms des tables depuis la base de données
# metadata.reflect()

# Affiche les noms des tables
# print(metadata.tables.keys())




# import psycopg2

# try:
#     print('Connecting to the PostgreSQL database...')
#     conn = psycopg2.connect(
#         host="172.19.0.3",
#         database="piscineds",
#         user="nlesage",
#         password="mysecretpassword")
#     print('Connected to DB')
    
#     cur = conn.cursor()
    
#     print('PostgreSQL database version:')
#     cur.execute('SELECT version()')
    
#     db_version = cur.fetchone()
#     print(db_version)
    
#     cur.close()
# except (Exception, psycopg2.DatabaseError) as error:
#     print(error)
# finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')
