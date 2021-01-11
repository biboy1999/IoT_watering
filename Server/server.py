from sanic import Sanic
from sanic.response import json
from sanic.log import logger
from sanic_openapi import swagger_blueprint, doc
from json import dumps
import pymysql.cursors


app = Sanic("water")
app.blueprint(swagger_blueprint)
db_conn = pymysql.Connect(host="127.0.0.1", user="water", password="no_water_for_you",
                          db="auto_water", cursorclass=pymysql.cursors.DictCursor)


@app.get("/temp")
@doc.produces(
    {
        "ID": doc.Integer("record's id"),
        "IOT_ID": doc.Integer("iot's id"),
        "air_temp": doc.Float("air temperature"),
        "air_hum": doc.Float("air hum"),
        "dirt_hum": doc.Float("dirt hum"),
        "ts": doc.DateTime("timestamp")
    },
    content_type="application/json"
)
async def get_record(request):
    result = None
    with db_conn.cursor() as cur:
        sql = "SELECT * FROM `record` LIMIT 100"
        cur.execute(sql)
        result = cur.fetchall()

    for line in result:
        line["ts"] = line["ts"].strftime("%Y-%m-%d %H:%M:%S")
    return json(result)


@app.post("/temp")
@doc.consumes(
    doc.JsonBody(
        {
            "IOT_ID": doc.Integer("iot's id"),
            "air_temp": doc.Float("air temperature"),
            "air_hum": doc.Float("air hum"),
            "dirt_hum": doc.Float("dirt hum")
        }
    ),
    location="body",
    content_type="application/json"
)
async def save_record(request):
    # iot_id = request.json["IOT_ID"]
    iot_id = 1
    air_temp = request.json["air_temp"]
    air_hum = request.json["air_hum"]
    dirt_hum = request.json["dirt_hum"]
    data = (iot_id, air_temp, air_hum, dirt_hum)
    with db_conn.cursor() as cur:
        sql = "INSERT INTO `record` VALUES (null, %s, %s, %s, %s, null)"
        cur.execute(sql, data)
    db_conn.commit()
    return json({"status": "ok"}, status=200)


@app.get("schedule")
def get_water_schedule(request):
    result = None
    with db_conn.cursor() as cur:
        sql = "SELECT * FROM `setting` WHERE IOT_ID = 1"
        cur.execute(sql)
        result = cur.fetchone()

    return json(result)


@app.post("schedule")
@doc.consumes(
    doc.JsonBody(
        {
            "IOT_ID": doc.Integer("IOT's ID"),
            "water_schedule": doc.String("water schedule. Separate by ;")
        }
    ),
    location="body",
    content_type="application/json"
)
def change_water_schedule(request):
    IOT_ID = request.json["IOT_ID"]
    water_schedule = request.json["water_schedule"]
    data = (water_schedule, IOT_ID)
    with db_conn.cursor() as cur:
        sql = "UPDATE `setting` SET `water_schedule`=%s WHERE `IOT_ID` = %s"
        cur.execute(sql, data)
    db_conn.commit()
    return json({"status": "ok"}, status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
