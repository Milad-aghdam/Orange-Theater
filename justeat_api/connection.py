from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://gholi_pour__:2024data_Wee%25159159gholipour%25$%@p3nlmysql165plsk.secureserver.net/ph15928026353_"

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Connected to the database successfully!")
    connection.close()
except Exception as e:
    print("Error connecting to the database:", e)
