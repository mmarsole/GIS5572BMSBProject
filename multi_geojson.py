import os
import string
from flask import Flask, request
import psycopg2
app = Flask(__name__) # setup initial flask app; gets called throughout in routes

@app.route('/model_alpha2') #python decorator 
def hello_world(): #function that app.route decorator references
    connection = psycopg2.connect(host='spatialdb.gisandbox.org', database='marso093', user='marso093')
#     connection = psycopg2.connect(host='34.123.61.225', database='lab0', user='postgres', password='')
    cursor = connection.cursor()
    cursor.execute("SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(features.feature)::jsonb)"
            "FROM (SELECT jsonb_build_object('type', 'Feature', 'geometry', ST_AsGeoJSON(shape)::jsonb, 'properties', jsonb_build_object('gid', gid, 'CITY_SJ', CITY_SJ, 'Presence', Presence, 'Accuracy', Accuracy, 'overall_FP', overall_FP, 'overall_TN', overall_TN, 'overall_TP', overall_TP, 'overall_FN', overall_FN))::jsonb As feature FROM MN_Cities_Pts_WGS_norank) features;")
    returns =cursor.fetchall()
    connection.close()
    return returns[0][0]

@app.route('/model_alpha1_75') #python decorator 
def hello_world_1(): #function that app.route decorator references
    connection = psycopg2.connect(host='spatialdb.gisandbox.org', database='marso093', user='marso093')
    cursor = connection.cursor()
    cursor.execute("SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(features.feature)::jsonb)"
                "FROM (SELECT jsonb_build_object('type', 'Feature', 'geometry', ST_AsGeoJSON(shape)::jsonb, 'properties', jsonb_build_object('gid', gid, 'CITY_SJ', CITY_SJ, 'Presence', Presence, 'Accuracy', Accuracy, 'overall_FP', overall_FP, 'overall_TN', overall_TN, 'overall_TP', overall_TP, 'overall_FN', overall_FN))::jsonb As feature FROM MN_Cities_Pts_WGS_norank1_75) features;")
    returns =cursor.fetchall()
    connection.close()
    return returns[0][0]

@app.route('/model_alpha1_5') #python decorator
def hello_world_1_5():
    connection = psycopg2.connect(host='spatialdb.gisandbox.org', database='marso093', user='marso093')
    cursor = connection.cursor()
    cursor.execute("SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(features.feature)::jsonb)"
               "FROM (SELECT jsonb_build_object('type', 'Feature', 'geometry', ST_AsGeoJSON(shape)::jsonb, 'properties', jsonb_build_object('gid', gid, 'CITY_SJ', CITY_SJ, 'Presence', Presence, 'Accuracy', Accuracy, 'overall_FP', overall_FP, 'overall_TN', overall_TN, 'overall_TP', overall_TP, 'overall_FN', overall_FN))::jsonb As feature FROM MN_Cities_Pts_WGS_norank1_5) features;")
    returns =cursor.fetchall()
    connection.close()
    return returns[0][0]

@app.route('/ranked_cities') #python decorator
def rank_cities():
    connection = psycopg2.connect(host='spatialdb.gisandbox.org', database='marso093', user='marso093')
    cursor = connection.cursor()
    cursor.execute("SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(features.feature)::jsonb)"
               "FROM (SELECT jsonb_build_object('type', 'Feature', 'geometry', ST_AsGeoJSON(shape)::jsonb, 'properties', jsonb_build_object('gid', gid, 'City_name', City_name, 'Rank', Rank))::jsonb As feature FROM BMSB_City_Rank_alpha2) features;")
    returns =cursor.fetchall()
    connection.close()
    return returns[0][0]


if __name__ == "__main__":
    app.run(
      debug=True, #shows errors 
      host='0.0.0.0', #tells app to run exposed to outside world
      port=int(os.environ.get("PORT", 8080))) #port = '5000'
