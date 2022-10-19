References
-. https://alembic.sqlalchemy.org/en/latest/tutorial.html

#################################################################################################
# 1. Install Python Package
#################################################################################################

pip install alembic sqlalchemy

#################################################################################################
# 2. Create an Environment
#################################################################################################

mkdir -p ~/lenz/backend/models && cd ~/lenz/backend/models
touch db.py incldent_models.py

cd ~/lenz/backend
alembic init migrations
<!-- touch db.py incldent_models.py
alembic init migrations -->

#################################################################################################
# 3. Editing the .ini File
#################################################################################################

vi alembic.ini
# sqlalchemy.url = driver://user:pass@localhost/dbname
sqlalchemy.url = sqlite:///database.db
sqlalchemy.url = postgresql+psycopg2://postgres:postgres@172.30.1.13/lenz

#################################################################################################
# 4. Create a Migration Script 
#################################################################################################

vi migrations/env.py
# add your model's MetaData object here
# for 'autogenerate' support
from database import Base
target_metadata = Base.metadata
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