import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred_obj = credentials.Certificate("calculadora-grupo-5-firebase-adminsdk-unu5r-69dc4419da.json")
default_app = firebase_admin.initialize_app(cred_obj, {"databaseURL":"https://calculadora-grupo-5-default-rtdb.firebaseio.com/"})


def crear(n,i,j):
	
	ecuacion = j.get()
	ref = db.reference(f"/{n}")
	ref.set({i:ecuacion})



def leerBok(n):

	ref = db.reference(f"/{n}")
	return ref.get()



def act(n,i,j):

	ref = db.reference(f"/{n}")
	m = {i:j}
	ref.update(m)



def borrar(n,i):

	ref = db.reference(f"/{n}")
	ref.child(i).delete()



def nodo():

    ref = db.reference('/')
    all_nodes = ref.get()
    lista = []

    for node_name in all_nodes:
        lista.append(node_name)

    return lista



def subnodos (n):

	ref = db.reference(f'/{n}')
	nodo = ref.get()
	lista = list(nodo.keys())
	
	return lista



def valor (n,j):

	ref = db.reference(f'/{n}')
	nodo_valor = ref.child(j).get()

	return nodo_valor
