import os
import kivy

from controllers.main_window import TPVApp
from controllers.auth_window import SessionApp
from kivy.lang import Builder

from seed import seed

from models.database import Database

DIR_TPV = os.path.dirname(__file__)

route_main_kv = os.path.join(DIR_TPV, 'views', 'MainRoot.kv')
route_login_kv = os.path.join(DIR_TPV, 'views', 'LoginRoot.kv')

Builder.load_file(route_main_kv)
Builder.load_file(route_login_kv)

if __name__ == '__main__':
    
    seed.run_seed()

    route_db = os.path.join(DIR_TPV, 'data', 'tpv.db')

    if not os.path.exists(route_db):
        print("Intentando conectar a la base de datos...")
        db = Database(db_name=route_db)
    else:
        print("Base de datos detectada.")

    user = True
    if user:
        TPVApp().run()
    else: 
        SessionApp().run()