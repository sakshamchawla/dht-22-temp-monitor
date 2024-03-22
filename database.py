import psycopg2
import psycopg2.extras

config_file = "keys"

def set_up_db():
    with open(config_file, 'r') as dbconffile:
        configVals = [line.rstrip('\n') for line in dbconffile]
    conn_string = "host=%s dbname=%s user=%s password=%s" % (
        configVals[0], configVals[1], configVals[2], configVals[3])

    conn = psycopg2.connect(conn_string)   
    with conn.cursor() as cursor: 
        with open('init.sql', 'r') as initfile:
            setup_queries = initfile.read()
            cursor.execute(setup_queries)    
        cursor.execute("prepare ins_query as insert into sensor_data(temp_c, temp_f, humidity, sensor_id) values($1,$2,$3,$4)")
    return conn


def save_data(conn, temp_c, temp_f, humidity, sensor_id):
    cursor = conn.cursor()
    ins = "execute ins_query(%s,%s,%s,%s)"
    cursor.execute(ins, (temp_c, temp_f, humidity, sensor_id))
    conn.commit()