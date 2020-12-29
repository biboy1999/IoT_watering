from sanic import Sanic
from sanic.response import json
from sanic.log import logger
from sanic_openapi import  swagger_blueprint, doc
import pymysql.cursors


app = Sanic("water")
app.blueprint(swagger_blueprint)
# db_conn = pymysql.Connect(host="db", user="root", password="superpapaya",
#                           db="auto_water", charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
db_conn = pymysql.Connect(host="db", user="water", password="no_water_for_you",
                          db="auto_water", cursorclass=pymysql.cursors.DictCursor)


@app.get("/temp")
async def test(request):
    result = None
    with db_conn.cursor() as cur:
        sql = "SELECT * FROM `record`"
        cur.execute(sql)
        result = cur.fetchall()
    return json(result)


@app.post("/temp")
@doc.consumes(
    doc.JsonBody(
        {
            "iot_id":doc.Integer("iot's id"),
            "temp":doc.Float("temperature"),
            "hum":doc.Float("hum")
        }
    ),
    location="body",
)
async def save_temp(request):
    iot_id = request.json["iot_id"]
    temp = request.json["temp"]
    hum = request.json["hum"]
    data  = (iot_id, temp, hum,)
    with db_conn.cursor() as cur:
        sql = "INSERT INTO `record` VALUES (null, %s, %s, %s, null)"
        cur.execute(sql,data)
    db_conn.commit()
    return  json({"status": "ok"}, status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
