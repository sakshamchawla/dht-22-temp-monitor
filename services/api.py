from flask import Flask
from flask_restful import Resource, Api
import json
import services.database as database
import datetime
import decimal

app = Flask(__name__)
api = Api(app)
conn = database.set_up_db()

def to_json(cols, data):    
    resp = {}
    for c in range(len(cols)):        
        col = cols[c]
        resp[col] = []
        for d in data:
            if isinstance(d[c], datetime.datetime):
                resp[col].append(str(d[c]))
            elif  isinstance(d[c], decimal.Decimal):
                resp[col].append(float(d[c]))                
            else:
                resp[col].append(d[c])
                
    return resp

class current(Resource):
    def get(self):
        cols, data = database.get_current(conn)
        return to_json(cols, data)

class last24h(Resource):
    def get(self):
        cols, data = database.get_last24h(conn)
        return to_json(cols, data)   

class last1week(Resource):
    def get(self):
        cols, data = database.get_last1week(conn)
        return to_json(cols, data)        

def go():
    api.add_resource(current, '/current')
    api.add_resource(last24h, '/last24h')
    api.add_resource(last1week, '/last1week')
    app.run(host='0.0.0.0')
