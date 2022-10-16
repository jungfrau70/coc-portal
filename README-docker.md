
- Prerequities
  . Docker installed

#############################################################################################
# 1. Install vscode extension
#############################################################################################

Docker

#############################################################################################
# 1. Install postgresql database and admin
#############################################################################################

# database
docker run --name psqld -d -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_DATABASE=test postgres

docker run --name psqld2 -d -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_DATABASE=test postgres


# pgadmin4
docker run --rm -p 5050:5050 thajeztah/pgadmin4
