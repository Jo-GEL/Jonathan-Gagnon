import requests
from requests.api import request


def lister_parties(idul):
    req1 = 'https://python.gel.ulaval.ca/quoridor/api/parties/'
    rep = requests.get(f'{req1}parties/', params= {'idul': idul})
    if rep.status_code== 406:
        raise RuntimeError(f"Le GET sur {req1} a produit le code d'erreur {rep.status_code}.")

    rep = rep.json()
    if 'message' in rep.keys():
        raise RuntimeError(rep['message'])
    else:
        return rep['parties']
        


def initialiser_partie(idul):
    req2 = 'https://python.gel.ulaval.ca/quoridor/api/partie/'
    rep = requests.post(f'{req2}parties/', data= {'idul': idul})
    if rep.status_code== 406:
        raise RuntimeError(f"Le POST sur {req2} a produit le code d'erreur {rep.status_code}.")

    rep = rep.json()
    if 'message' in rep.keys():
        raise RuntimeError(rep['message'])
    else:
        return rep['id'], rep['état']
    


def jouer_coup(id_partie, type_coup, position):
    req3 = 'https://python.gel.ulaval.ca/quoridor/api/jouer/'
    rep = requests.put(f'{req3}jouer/', data= {'id': id_partie, 'type': type_coup, 'pos': position})
    
    if rep.status_code==200:
        return rep['état']
    
    if rep.status_code== 406:
        raise RuntimeError(f"Le PUT sur {req3} a produit le code d'erreur {rep.status_code}.")
    
    rep = rep.json()
    if 'message' in rep.keys():
        raise RuntimeError(rep['message'])
    
    if 'gagnant' in rep.keys():
        raise StopIteration(rep['gagnant'])
    else:
        return None