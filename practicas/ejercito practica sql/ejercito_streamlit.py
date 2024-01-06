import mysql.connector
import streamlit as st
from datetime import datetime
from connection_data import data
from sqlite3 import IntegrityError

# establecer conexion
connection = mysql.connector.connect(
    host=data["host"],
    user=data["user"],
    password=data["password"],
    database=data["database"],
    port=data["port"]
)


def insertar_soldados():
    st.subheader("Por favor inserte los datos")
    codigo_soldado = st.text_input("Código del Soldado")
    nombre_soldado = st.text_input("Nombre")
    apellidos_soldado = st.text_input("Apellidos")
    grado_soldado = st.text_input("Grado")
    codigo_cuerpo_soldado = st.text_input("Código del Cuerpo para el soldado")
    numero_compania_soldado = st.text_input("Número de Compañía para el soldado")
    codigo_cuartel_soldado = st.text_input("Código del Cuartel para el soldado")
    if st.button("Insertar Soldado"):
        try:
            query = """
                INSERT INTO Soldados 
                    (codigo_soldado, nombre, apellidos, grado, codigo_cuerpo1, numero_compania1, codigo_cuartel1)
                VALUES ({codigo_soldado}, '{nombre}', '{apellidos}', '{grado}', {codigo_cuerpo}, {numero_compania}, {codigo_cuartel})
            """
            query = query.format(codigo_soldado=codigo_soldado, nombre=nombre_soldado, apellidos=apellidos_soldado,
                                 grado=grado_soldado,codigo_cuerpo= codigo_cuerpo_soldado, numero_compania=numero_compania_soldado,
                                 codigo_cuartel=codigo_cuartel_soldado)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            st.success("Soldado insertado con éxito.")
            return True
        except Exception as e:
            print(e)
            st.error("Ya existe un Soldado con ese código.")
            return False


def insertar_cuerpo():
    # Formulario para insertar datos en Cuerpos
    codigo_cuerpo = st.text_input("Código del Cuerpo")
    denominacion_cuerpo = st.text_input("Denominación del Cuerpo")

    if st.button("Insertar Cuerpo"):
        try:
            query = """
            INSERT INTO Cuerpos
            (codigo_cuerpo, denominacion) 
            VALUES
                ({codigo_cuerpo}, '{denominacion}')
            """
            query = query.format(codigo_cuerpo=codigo_cuerpo, denominacion=denominacion_cuerpo)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            st.success("Cuerpo insertado con éxito.")
        except:
            st.error("Ya existe un Cuerpo con ese código.")


def insertar_compania():
    # Formulario para insertar datos en Companias
    st.subheader("Por favor inserte los datos")
    numero_compania = st.text_input("Número de Compañía")
    actividad_compania = st.text_input("Actividad Principal")
    if st.button("Insertar Compañía"):
        try:
            query = """
                INSERT INTO Companias
                (numero_compania, actividad_principal) 
                VALUES
                    ({numero_compania}, '{actividad_principal}')
            """
            query = query.format(numero_compania=numero_compania, actividad_principal=actividad_compania)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            st.success("Compañia insertado con éxito.")
        except:
            st.error("Ya existe una Compania con ese código.")


# Función para insertar datos en la tabla Cuarteles
def insertar_cuartel():
    st.subheader("Por favor inserte los datos")
    codigo_cuartel = st.text_input("Código del Cuartel")
    nombre_cuartel = st.text_input("Nombre del Cuartel")
    ubicacion_cuartel = st.text_input("Ubicación del Cuartel")
    if st.button("Insertar Cuartel"):
        try:
            query =  """
            INSERT INTO Cuarteles
                (codigo_cuartel, nombre_cuartel, ubicacion)
            VALUES ({codigo_cuartel}, '{nombre_cuartel}', '{ubicacion}')
            
            """
            query = query.format(codigo_cuartel=codigo_cuartel, nombre_cuartel=nombre_cuartel, ubicacion=ubicacion_cuartel)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            st.success("Cuartel insertado con éxito.")
        except:
            st.error("Ya existe un Cuartel con ese código.")


def insertar_servicio():
    st.subheader("Por favor inserte los datos")
    codigo_servicio = st.text_input("Código del servicio")
    actividad = st.text_input("Actividad")
    if st.button("Insertar Servicio"):
        try:
            query = """
            INSERT INTO Servicios 
                (codigo_servicio, actividad)
            VALUES ({codigo_servicio}, '{actividad}')
            """
            query = query.format(codigo_servicio=codigo_servicio, actividad=actividad)
            print(query)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            st.success("Servicio insertado con éxito.")
        except Exception as e:
            print(e)
            st.error("Ya existe un Servicio con ese código.")


def registro_campos():
    section_cuerpos = st.session_state.section_cuerpos if "section_cuerpos" in st.session_state else True
    section_cuarteles = st.session_state.section_cuarteles if "section_cuarteles" in st.session_state else False
    section_companias = st.session_state.section_companias if "section_companias" in st.session_state else False
    section_servicios = st.session_state.section_servicios if "section_servicios" in st.session_state else False
    section_soldados = st.session_state.section_soldados if "section_soldados" in st.session_state else False

    # Botón "Siguiente" para avanzar al siguiente formulario
    if st.button("Siguiente a Cuarteles"):
        section_cuerpos = False
        section_cuarteles = True

    if section_cuerpos:
        st.header("Agregar Cuerpos del Ejército")
        insertar_cuerpo()

    if section_cuarteles:
        st.header("Agregar Cuarteles del Ejército")
        insertar_cuartel()
        # Botón "Siguiente" para avanzar al siguiente formulario
        if st.button("Siguiente a Compañias"):
            section_cuarteles = False
            section_companias = True

    # Mostrar el formulario de Compañías
    if section_companias:
        st.header("Agregar Compañías del Ejército")
        insertar_compania()
        # Botón "Siguiente" para avanzar al siguiente formulario
        if st.button("Siguiente a Servicios"):
            section_companias = False
            section_servicios = True

    # Mostrar el formulario de Servicios
    if section_servicios:
        st.header("Agregar Servicios del Ejército")
        insertar_servicio()
        # Botón "Siguiente" para avanzar al siguiente formulario
        if st.button("Siguiente a Soldados"):
            section_servicios = False
            section_soldados = True

    # Mostrar el formulario de Soldados
    if section_soldados:
        st.header("Agregar Soldados del Ejército")
        insertar_soldados()

        st.success("Fin del formulario")

    # Actualizar las variables de control en la sesión
    st.session_state.section_cuerpos = section_cuerpos
    st.session_state.section_cuarteles = section_cuarteles
    st.session_state.section_companias = section_companias
    st.session_state.section_servicios = section_servicios
    st.session_state.section_soldados = section_soldados


#def asignacion_datos():


def main():

    menu = ["Home", "Registro", "Asignaciones"]
    choice = st.sidebar.selectbox("Menu", menu, index=0)

    if choice == "Home":
        st.title("Bienvenido al formulario para el control de soldados que prestan el servicio militar ")
    elif choice == "Registro":
        registro_campos()
    elif choice == "Asignaciones":
        selector_formulario = st.selectbox("Selecciona un formulario:", ("Asignación de Servicios", "Asignación de Compañías a Cuarteles"))
        if selector_formulario == "Asignación de Servicios":
            st.subheader("Asignación de Servicios")
            def asignar_servicios ():
                st.title("Formulario de Soldados y Servicios")
                codigo_soldado = st.number_input("Código del soldado:")
                codigo_servicio = st.number_input("Código del servicio:")
                fecha_realizacion = st.date_input("Fecha de realización:")
                if st.button("Guardar"):
                    try:
                        query = """
                        INSERT INTO Soldados_Servicios 
                        (codigo_soldado1, codigo_servicio1, fecha_realizacion)
                        VALUES ({codigo_soldado}, {codigo_servicio}, {fecha_realizacion})
                        """, (codigo_soldado, codigo_servicio, fecha_realizacion)
                        query = query.format(codigo_soldado=codigo_soldado, codigo_servicio=codigo_servicio, fecha_realizacion=fecha_realizacion)
                        print(query)
                        cursor = connection.cursor()
                        cursor.execute(query)
                        connection.commit()
                        st.success("Servicio insertado con éxito.")
                    except Exception as e:
                        print(e)
                        st.error("Ya existe un Servicio con ese código.")
                    
        elif selector_formulario == "Asignación de Compañías a Cuarteles":
            def asignar_compañias ():
                st.title("Formulario de Cuarteles y Compañías")
                codigo_cuartel = st.number_input("Código del cuartel:")
                numero_compania = st.number_input("Número de la compañía:")
        #asignacion_datos()


if __name__ == "__main__":
    # lo que ahi de aca hacia abajo es la ejecucion inicial del codigo
    main()
