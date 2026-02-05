import os
import kivy

from controllers.main_window import TPVApp
from controllers.auth_window import SessionApp
from kivy.lang import Builder
#Seed de datos para tests
from seed import seed
#Modelo de la base de datos
from models.database import Database
#Variable de Entorno para detectar la ruta del proyecto en otros dispositivos
DIR_TPV = os.path.dirname(__file__)
#routes para cada Ventana el formato join(env, carpeta, nombre del archivo)
route_main_kv = os.path.join(DIR_TPV, 'views', 'MainRoot.kv')
route_login_kv = os.path.join(DIR_TPV, 'views', 'LoginRoot.kv')
#Builder que carga cada ruta encontrada de los kivy
Builder.load_file(route_main_kv)
Builder.load_file(route_login_kv)

if __name__ == '__main__':
    #Detectando la ruta de la base de datos en el directorio
    route_db = os.path.join(DIR_TPV, 'data', 'tpv.db')
    #Condición de control para verificar si existe ya la base de datos, si no lanzar msg
    if not os.path.exists(route_db):
        #Iniciando el seed
        seed.run_seed()
        print("Intentando conectar a la base de datos...")
        db = Database(db_name=route_db)
    else:
        print("Base de datos detectada.")
    #Solo para test, posteriormente asignar la validación de inicio de sesión
    user = True
    if user:
        TPVApp().run()
    else: 
        SessionApp().run()