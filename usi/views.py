from django.shortcuts import render

from usi.neo4jdb import Neo4jConnection


def accueil(request):
    return render(request, 'accueil.html')

def requete(request):
    db = Neo4jConnection(uri='bolt://localhost:7687', user='neo4j', password='Aaron23032015')
    connected = db.check_connection()
    query = "MATCH (n) RETURN n LIMIT 30"
    resultats_bruts = db.execute_query(query)

    # Transformer les résultats en un format plus convivial
    resultats = [{
        'id': record['n'].id,
        'labels': list(record['n'].labels),
        'properties': dict(record['n'].items()),
        'description': Neo4jConnection.generer_description({'labels': list(record['n'].labels), 'properties': dict(record['n'].items())})
    } for record in resultats_bruts]

    context = {
        'connected': connected,
        'resultats': resultats,
    }

    return render(request, 'requete.html', context)
