# flask-crate-transit-data
A flask app that inserts transit data into CrateDB.

# Requirements

Project requires Docker, Docker Toolbox and docker-compose in your development environment.

# Installation instructions CrateDB

1) If you run Docker on a Linux system, you may need to adjust the memory map limit on your host system before running the images.

Linux:
``sh$ sudo sysctl -w vm.max_map_count=262144`

Windows running a Linux VirtualBox on docker-machine: 
``sh$ docker-machine ssh default "sudo sysctl -w vm.max_map_count=262144"``

2) From the project directory, start up your application by running:

``docker-compose up``

3) Navigate to ``http://localhost:4200/`` to see the app running.

4) You can visit the CrateDB admin UI in your browser with this URL: 

``http://localhost:4200/``

If CrateDB is not running locally, replace localhost with the hostname CrateDB is running on. 
Run ``sh$ docker-machine -i`` to detect your host ip.

5) If you hit the button on the Home page, the app will start inserting the data into CrateDB.
Once, it is finished, you will be routed to Success.

You can track the status of the insertion on your terminal and on the CrateDB UI. 

# Running tests

To run the tests, run the pytest module:

``sh$ pytest``

<!-- 3) Set up the official CrateDB Docker image:

``sh$ docker run -p "4200:4200" crate`` -->


<!-- If CrateDB is not running locally, replace localhost with the hostname CrateDB is running on. 
Run ``sh$ docker-machine -i`` to detect your host ip. -->

<!-- docker-machine ip -->

<!-- 5) Activate your virtual environment:

If you are a Mac user, activate your environment by running 
``sh$ source myenv/bin/activate``
If you are a Windows user, activate your environment by running 
``sh$ source myenv/Scripts/activate``

# Run the docker image -->
<!-- 
``docker-compose up``
``docker run -it -d -p 5000:5000 transitdata`` -->


