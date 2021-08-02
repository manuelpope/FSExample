# FSExample
steps for running server side:


cd server_Flask/
python3 -m venv
pip install -r server/requirements.txt
cd server
python3 main.py




################################

steps for running ui:

cd uigraph/
npm install
npm start


... enjoy it...


#######
Tech Stack:

UI:
javascript
react js
react router
material ui - tabs
material ui - table
rechartsjs - graphs

Backend- API :
python3
Flask web framework
API Flask - resources API
SQL_Alchemy - orm


DB - SQLITE,
debido que hacer la migracion a MYSQL, ORACLE por ejemplo, puede ser muy facil con SQLALCHEMY.


NOTA: SI DESEA VOLVER A INICIALIZAR LA DB EN OTRO GESTOR DE BASE DE DATOS, HAY UNA FUNCION EN EL main.py, para 
hacer le mockeo de los valores, solo es descomentarla y cuando suceda el primer request a la API populara las tablas.

solo removiendo el # de 

# @app.before_first_request
conseguira que pueda correr la migracion.

