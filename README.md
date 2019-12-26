# flask-crate-transit-data
A flask app using CrateDB and Docker to inserts public transit data (VBB-Fahrplandaten via GTFS) into CrateDB.

# Requirements

Project requires Docker, Docker Toolbox and docker-compose in your development environment.

# Installation instructions CrateDB

If you run Docker on a Linux system, you may need to adjust the memory map limit on your host system before running the images.

Linux:  
`sh$ sudo sysctl -w vm.max_map_count=262144`

Windows running a Linux VirtualBox on docker-machine:    
`sh$ docker-machine ssh default "sudo sysctl -w vm.max_map_count=262144"`

## Run the app

Navigate to the project directory and run the below command.  
  
`sh$ ./scripts/run`

## Stop the app

Stop the app by running the below command:
  
`sh$ ./scripts/stop`

## Settings
### Host

If your host for CrateDB differs from localhost (e.g. when using VirtualBox/Docker Toolbox) you need to assign the host ip to the database URI. Replace <vm name> by the name of your virtal machine. 
    
`export DATABASE_URI==crate://crate@$(docker-machine ip <vm name>):4200`

### Password  

You can set a secure password by exporting: 
  
`export SECRET=thisisasecurepassword` 

## Insert data

To see the app running, navigate to:  
  
`http://localhost:5000/` 
  
You can visit the CrateDB admin UI in your browser with this URL. Replace localhost by your host ip, if you are using a different host. 
  
`http://localhost:4200/`
  
If you hit the button on the homepage, the app will start inserting the data into CrateDB.
Once, it is finished, you will be routed to success.

You can track the status of the insertion on your terminal and on the CrateDB UI. 

# Running tests
The tests are using the pytest module. You need to have python, pip and virtualenv installed on your system.

1) Start and activate a virtual environment in the root directory using venv.
  
`python -m venv myenv`  
  
`source myenv/bin/activate`  
  
2) Install requirements.
   
`pip install -r requirements.txt`

3) Set the environment variables using localhost or host ip and choosing a password:
  
`sh$ export DATABASE_URI=crate://crate@localhost:4200`  
`sh$ export SECRET=supersecretpassword`  

4) Run the official CrateDB Docker image.  
    
`sh$ docker run -p "4200:4200" crate`    
  
5) Run the tests module.
  
`sh$ ./scripts/start.test`  

## Troubleshoot

You may need to reinstall numpy using conda as its dependencies may depend on your system.
  
``pip uninstall numpy``     
``conda install numpy``  

