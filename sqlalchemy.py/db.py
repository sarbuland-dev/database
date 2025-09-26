from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
database_url= "mysql+pymysql://root:@localhost/quiz_task"

engine=create_engine(database_url)
sessionlocal=sessionmaker(bind=engine,autoflush=False, autocommit=False)