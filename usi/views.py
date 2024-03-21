from django.shortcuts import render
from neo4j import GraphDatabase

# Information de connexion à la base de données Neo4j
NEO4J_URI = "neo4j+s://83a44375.databases.neo4j.io"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "yxN0aKhhIPtHp71Na77Y4soZMGdFNuqoVDo34cp3h18"
AURA_INSTANCEID = "83a44375"
AURA_INSTANCENAME = "Instance01"


def accueil(request):
    return render(request, 'accueil.html')


def recherche(request):
    # Driver instantiation
    driver = GraphDatabase.driver(
        NEO4J_URI,
        auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
    )

    print(driver.session())

    # # Requêtage des données
    # cypher_query = """
    #     MATCH (n:emploi) RETURN n LIMIT 25;
    # """
    #
    # # Query
    # with driver.session() as session:
    #     result = session.run(cypher_query).data()
    #     for record in result:
    #         print(record)

    return render(request, 'recherche.html', context={'driver': 'driver'})
