# flask-crate-transit-data
A flask app that inserts transit data into CrateDB.

# Installation instructions CrateDB

1) Run Docker on a Unix-system
2) If you run Docker on a Linux system, you may need to adjust the memory map limit on your host system before booting Crate.

``sh$ sudo sysctl -w vm.max_map_count=262144``

Or, if you run docker machine VirtualBox "default" on Windows:

``sh$ docker-machine ssh default "sudo sysctl -w vm.max_map_count=262144"``

3) Set up the official CrateDB Docker image:

``sh$ docker run -p "4200:4200" crate``

4) You can visit the admin UI in your browser with this URL: 

``http://localhost:4200/``

If CrateDB is not running locally, replace localhost with the hostname CrateDB is running on. 
Run ``sh$ hostname -i`` to detect your host ip.

