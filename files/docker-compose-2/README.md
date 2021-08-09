# docker-compose-2

Running this docker-compose deployment should create a miniature application stack consisting of:

- load balancer (Nginx)
- backend server (Python Flask)
- database server (MongoDB)
- database administration web server (mongo-express)

To start this little stack up, run `docker-compose up` from inside this directory. NB you'll need Docker (and 
    docker-compose, if not bundled with Docker) installed!

When up and running:
 
- When you connect to `http://localhost/`, the client should be redirected to `http://localhost/app`
- When you connect to `http://localhost/app`, the response should be `Hello World!`
- You can connect to `http://localhost/mongo` and view the `mongo-express` database administration UI 

... but there are configuration errors present!
