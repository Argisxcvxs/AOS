"""
Proceso de registro de usuarios y login usando mysql y streamlit
"""

# pip install mysql-connector-python
# pip install streamlit

import mysql.connector
import streamlit as st
from datetime import datetime  # dates en python
from connection_data import data, tables
from queries.queries import query_insert, query_val_user

# establecer conexion
connection = mysql.connector.connect(
    host=data["host"],
    user=data["user"],
    password=data["password"],
    database=data["database"],
    port=data["port"]
)

# Definir la variable tables
table_estudiantes = tables["estudiantes"]
# Acceder a la tabla de estudiantes

def val_user_exist(documento):
    """
    Valida si un usuario existe e
    n la base de datos.

    Args:
        documento (int): docuemnto del estudiante.

    Returns:
        bool: True si el usuario existe, False si no existe.
    """
    query = query_val_user.format(table_estudiantes=table_estudiantes, documento=documento)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    resultado = cursor.fetchone()
    if resultado is None:
        return False  # Indica que no existe el documento del usuario en la base de datos
    return True  # Indica que existe el usuario en la base de datos


def insert_user(documento, nombre, apellido, grado, contraseña, fecha_registro):
    """
    Inserta un nuevo usuario en la base de datos.

    Args:
        documento (int): documento del estudiante
        nombre (str): Nombre del estudiante
        apeliido (str): Apellido del estudiante.
        grado (int): grado del estudiante.
        contraseña (int): Contraseña del estudiante
    """
    query = query_insert.format(
        table_estudiantes=table_estudiantes, documento=documento, nombre=nombre, 
        apellido=apellido, grado=grado, 
        contraseña=contraseña, fecha_registro=fecha_registro
    )
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


def val_login(documento, contraseña):
    """
    Valida el inicio de sesión de un estudiante.

    Args:
        documento (int): documento del estudiante
        contraseña (int): Contraseña del estudiante

    Returns:
        bool: True si el inicio de sesión es exitoso, False si no es exitoso.
    """
    query = """
        SELECT * 
        FROM {table_estudiantes}
        WHERE id_customer = {documento} and password_customer = {contraseña}
    """.format(table_estudiantes=table_estudiantes, documento=documento, contraseña=contraseña)

    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    resultado = cursor.fetchone()

    if resultado is None:
        return False  # Indica que el usuario o contraseña es incorrecto
    return True  # Indica que los datos son correctos


def login():
    """
    Sección de inicio de sesión.
    """
    st.subheader("Inicia sesión")
    documento = st.sidebar.text_input("Documento")
    contraseña = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        flag_login = val_login(documento, contraseña)
        if flag_login:
            st.success('Inicio de sesión exitoso')
            task = st.selectbox("Actividad", options=["Agregar Tareas", "Eliminar Tareas"])
        else:
            st.warning('Usuario/Contraseña incorrectos')


def signup():
    """
    Sección de registro de nuevos usuarios.
    """
    st.subheader("Regístrate")
    documento = st.sidebar.text_input("Documento")
    nombre = st.sidebar.text_input("Nombres")
    apellido = st.sidebar.text_input("Apellidos")
    email = st.sidebar.text_input("Email")
    contraseña = st.sidebar.text_input("Contrasena", type="password")
    fecha_registro = datetime.now()

    if st.sidebar.button("Create"):
        flag_exists = val_user_exist(documento)
        if flag_exists:
            st.info("Usuario ya registrado")
        else:
            insert_user(documento, nombre, apellido, email, contraseña, fecha_registro)
            st.success("Welcome {}".format(nombre))


def main():
    """Funcion principal que define la interfaz y maneja la navegacion.
    """
    st.title("Educalificaciones")
    menu = ["principal", "acceder", "registrarse"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "principal":
        st.subheader("principal")
    elif choice == "inicia sesion":
        login()
    elif choice == "registrate":
        signup()


if __name__ == "__main__":
    main()
