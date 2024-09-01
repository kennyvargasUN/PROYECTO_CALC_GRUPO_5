import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred_obj = credentials.Certificate("CONTROLLER_calculadora-grupo-5-firebase-adminsdk-unu5r-b9ad1a988a.json")
default_app = firebase_admin.initialize_app(cred_obj, {"databaseURL":"https://calculadora-grupo-5-default-rtdb.firebaseio.com/"})


def crear(u,n,i,j):
	
	ecuacion = j.get()
	ref = db.reference(f"/{u}")
	ref.set({n:{i:ecuacion}})


def leerBok(usuario,n):

	ref = db.reference(usuario)
	return ref.child(n).get()


def act(usuario,n,i,j):

	ref = db.reference(usuario)
	m = {i:j}
	ref.child(n).update(m)


def borrar(usuario,n,i):

	ref = db.reference(usuario)
	ref.child(n).child(i).delete()


def nodo(usuario):

    ref = db.reference(usuario)
    all_nodes = ref.get()
    lista = []

    for node_name in all_nodes:
        lista.append(node_name)

    return lista


def subnodos (usuario,n):

	ref = db.reference(usuario)
	nodo = ref.child(n).get()
	lista = list(nodo.keys())
	
	return lista


def valor (usuario,n,j):

	ref = db.reference(usuario)
	nodo_valor = ref.child(n).child(j).get()

	return nodo_valor