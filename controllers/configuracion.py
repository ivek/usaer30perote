# coding: utf8
# intente algo como
def index(): return dict(message="hello from configuracion.py")

def books():
    formulario = SQLFORM.grid(db.books)
    return locals()

def prestbook():
    formulario = SQLFORM.smartgrid(db.prestbook)
    return locals()
