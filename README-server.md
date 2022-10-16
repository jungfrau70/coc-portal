

#############################################################################################
# 1. Setup backend server development env
#############################################################################################

# create folder - server
mkdir server && cd server

# create virtualenv
python -m venv venv
.\venv\Scripts\activate

# install lib dependencies
(venv) pip install -r requirements.txt

alembic
fastapi
sqlalchemy
psycopg2
uvicorn

-----------
hypercorn
requestsls
jinja2
sqlmodel


#############################################################################################
# 2. Configure vscode
#############################################################################################

# Install vscode extension
Pylance
Python - IntelliSense

# Add below to ./.vscode/settings.json
{
    "python.pythonPath": "C:\\work\\lenz\\backend\\venv\\Scripts\\python.exe",
    "python.analysis.completeFunctionParens": true,
    "python.languageServer": "Pylance"
}

#############################################################################################
# 3. Add folders and files
#############################################################################################

# Add folders and files

index.py

config
config\db.py

models
models\user.py

schemas
schemas\user.py

routes
routes\user.py


#############################################################################################
# 4. 
#############################################################################################


