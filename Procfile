web: gunicorn main.wsgi --log-file -
web: java $JAVA_OPTS -jar tika-server/target/tika-server-1.13-SNAPSHOT.jar --host=0.0.0.0 --port=$PORT
