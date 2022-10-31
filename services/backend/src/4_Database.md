References
-. https://alembic.sqlalchemy.org/en/latest/tutorial.html

#################################################################################################
# 1. Install sqlitebrowser
#################################################################################################

sudo apt-get install sqlitebrowser

#################################################################################################
# 2. Start sqlitebrowser
#################################################################################################

sqlitebrowser

#################################################################################################
# 3. Editing the .ini File
#################################################################################################

vi alembic.ini
# sqlalchemy.url = driver://user:pass@localhost/dbname
sqlalchemy.url = sqlite:///database.db
# sqlalchemy.url = 'postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase'

#################################################################################################
# 4. Create a Migration Script 
#################################################################################################

vi migrations/env.py
# add your model's MetaData object here
# for 'autogenerate' support
from models.incident_models import incidents
target_metadata = incidents.metadata
# target_metadata = None

alembic revision -m "create xxx table"

#################################################################################################
# 5. Running our First Migration
#################################################################################################

alembic upgrade heads


#################################################################################################
# 6. Running our Second Migration
#################################################################################################

alembic revision -m "Add a column"
alembic upgrade head

#################################################################################################
# 7. Partial Revision Identifiers
#################################################################################################

alembic upgrade ae1

...