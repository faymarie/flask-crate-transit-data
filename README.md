# flask-crate-transit-data
A flask app using CrateDB and Docker to inserts public transit data (VBB-Fahrplandaten via GTFS) into CrateDB.

# Requirements

Project requires Docker, Docker Toolbox and docker-compose in your development environment.

# Installation instructions CrateDB

1) If you run Docker on a Linux system, you may need to adjust the memory map limit on your host system before running the images.

Linux:
`sh$ sudo sysctl -w vm.max_map_count=262144`

Windows running a Linux VirtualBox on docker-machine: 
`sh$ docker-machine ssh default "sudo sysctl -w vm.max_map_count=262144"`

2) Navigate to the project directory and run the below command by replacing your host ip and assigning a secret key. The host ip is 'localhost'. If you are using VirtualBox/Docker Toolbox you need to assign the host ip of your virtualbox. Use `docker-machine ip <vm name>` to detect your host ip. Set a secure password.      

`DATABASE_URI=crate://crate@<host ip>:4200 SECRET=<secret> docker-compose up`

Example:
`DATABASE_URI=crate://crate@localhost:4200 SECRET=1supersecretpassword1 docker-compose up`

3) Navigate to `http://localhost:4200/` to see the app running.

4) You can visit the CrateDB admin UI in your browser with this URL: 

`http://localhost:4200/`

5) If you hit the button on the homepage, the app will start inserting the data into CrateDB.
Once, it is finished, you will be routed to success.

You can track the status of the insertion on your terminal and on the CrateDB UI. 

# Running tests

Run the pytest module:

`sh$ docker exec <transitdata container id> pytest'

