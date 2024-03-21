from neo4j import GraphDatabase


class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None, db=None):
        with self.driver.session(database=db) as session:
            return session.write_transaction(self._execute_query, query, parameters)

    def check_connection(self):
        try:
            with self.driver.session() as session:
                # Cette requête devrait être quelque chose de simple qui ne faille jamais si connecté
                session.run("RETURN 1")
            return True
        except Exception as e:
            print(f"Erreur lors de la vérification de la connexion: {e}")
            return False

    @staticmethod
    def generer_description(noeud):
        labels = noeud['labels']
        props = noeud['properties']

        if 'personnage' in labels:
            return f"{props.get('name', 'Un personnage mystérieux')} alias {props.get('nickname', 'sans surnom')} est un personnage emblématique."
        elif 'clan' in labels:
            return f"Le {props.get('clanname', 'clan inconnu')} est l'un des clans majeurs."
        else:
            return "Information non disponible."

    @staticmethod
    def _execute_query(tx, query, parameters):
        result = tx.run(query, parameters)
        return [record for record in result]
