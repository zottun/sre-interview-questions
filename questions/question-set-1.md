# Interview Question Set #1

Applicable to _junior_ or _mid-level_ candidates.

NB we wouldn't want a candidate spending more than a few hours on this question set - but evidently nobody is 
    timing you, so take as long as you like! This is completely open-book; use whatever resources you want.

Please submit your answers to this question set in whatever format you like; this will most likely be a text document
    containing the more 'wordy' answers, and a collection of other accompanying files/images etc. all bundled into a 
    ZIP file.

### 1. Scripting
##### 1(a)

Using the file [months.json](../files/months.json) as input, write a script in a language of your choosing which prints
    out a list of the months in alphabetical order. Submit your script as your answer.

##### 1(b) 

Using the file [months.json](../files/months.json) as input, write a script in a language of your choosing which 
    calculates the number of days in a year excluding those from any month that contains the letter "y". 
    Submit your script as your answer.

##### 1(c)

Write a script, in a language of your choosing, that does the following:

- clones this repository
- creates a branch with a name of your choosing
- adds a blank line to the [README.md](../README.md)
- pushes the branch
- opens a Pull Request for your branch

Submit your script as your answer.

### 2. Containerised Applications

Please submit your modified copy of the [docker-compose-2](../files/docker-compose-2) directory as part of your answer 
    to part 2.

##### 2(a)

Referring to [docker-compose-2](../files/docker-compose-2) and the expected behaviour as defined in the 
    [README](../files/docker-compose-2/README.md), explain what the actual behaviour is (and why), and identify the 
    configuration errors that are causing defective behaviour. You may need to fix the configuration errors in order to 
    move on to the next questions.
    
##### 2(b)

Expose a route to the Mongo database so that you could connect to the database via a `mongodb` client on your local 
    machine on port `:27017`.
    
##### 2(c)

Add a default 404 page, served as static content by the Nginx load balancer, such that any unmatched request eg. 
    `http://localhost/chicken` returns this static page, and not the default Nginx 404 page. NB this is not a test of 
    your HTML/CSS/JS skills!

##### 2(d)

Referring to [docker-compose-2](../files/docker-compose-2), modify the Flask applciation. Here are your requirements:

- It should not return `Hello World!` on route: `/`, but instead should use the PyMongo client to retrieve something 
    from the Mongo database. You can use the MongoDB administration UI (`mongo-express`) to insert this value if you'd 
    like, or for bonus points you could add another route/method to the app that accepts a PUT/POST request to update 
    this value.


### 3. Infrastructure
##### 3(a)

In a language/framework/cloud-provider etc. of your choosing or simply with a diagram(s), produce something which 
    creates/depicts the following:

- a network with a reasonably broad CIDR range
- some subnets in this network with narrower CIDR ranges, one public and at least one private
- some basic routing for these subnets

##### 3(b)

Building on the answer given in part 3(a), add the following:

- an application server (of whatever type you want) in a private subnet capable of serving static content to a 
    client over HTTP, and accessible from the outside of the network

##### 3(c)

Building on the answer given in part 3(b), add one or more of the following:

- some HA for your application server
- a backend database for your application server
- caching layer(s)
- network security
- anything else that you feel improves your mini-stack!
