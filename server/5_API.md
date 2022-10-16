Generic single-database configuration.

#################################################################################################
# 1. Install Package
#################################################################################################

pip install alembic sqlalchemy

#################################################################################################
# 2. Initialize alembic(=database migration package)
#################################################################################################

touch models.py
alembic init migrations

#################################################################################################
# 3. Configure database in alembic.ini
#################################################################################################

# sqlalchemy.url = driver://user:pass@localhost/dbname
sqlalchemy.url = 'sqlite:///model.db'
# sqlalchemy.url = 'postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase'

#################################################################################################
# 4. Configure database in env.py
#################################################################################################

# add your model's MetaData object here
# for 'autogenerate' support
from app.models import Base
target_metadata = Base.metadata
# target_metadata = None

#################################################################################################
# 6. Coding
#################################################################################################
