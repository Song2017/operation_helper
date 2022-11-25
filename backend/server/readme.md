## Backend server

### Guide
change directory to ./backend/server
1. replace db uri: core/config.py:SQLALCHEMY_DATABASE_URI
   ```
     docker volume create pgvolume
     docker run -itd --restart always -p 9002:5432 --volume pgvolume:/var/lib/postgresql -e POSTGRES_PASSWORD=admin123 -e POSTGRES_USER=user -e POSTGRES_DB=app -e POSTGRES_HOST_AUTH_METHOD=trust postgres:13.0-alpine
   ```
2. run server
   ```
   docker build -t songgs/operation-helper -f backend.dockerfile ./
   docker run -it -p 9003:80 -e SQLALCHEMY_DATABASE_URI=postgresql://user:admin123@172.17.0.1:9002/app songgs/operation-helper
   ```
3. swagger UI: http://localhost:9002/api/docs