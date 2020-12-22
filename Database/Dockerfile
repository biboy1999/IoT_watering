FROM mariadb:latest

ENV TZ=Asia/Taipei
EXPOSE 3306

COPY schema.sql /docker-entrypoint-initdb.d/schema.sql