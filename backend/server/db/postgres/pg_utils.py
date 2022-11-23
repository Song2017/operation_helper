import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

pg_sql_str = "postgresql://user:admin123@139.196.213.108:9002/app"
assert pg_sql_str is not None, "PG_CONNECTION is not found"
engine = create_engine(pg_sql_str)
session_class = sessionmaker(bind=engine)
session: Session = session_class()

def pg_run_codegen():
    """
        pip install sqlacodegen
    """
    args = f'sqlacodegen --outfile ./test_model.py {pg_sql_str} ' \
           f'--tables app_user'
    os.system(args)


if __name__ == "__main__":
    pg_run_codegen()
