Install Mongo
-----------

::
   
   brew update
   brew install mongodb

   # brew install mongodb --with-openssl


Create db dir
----------

::

   mkdir -p ~/.cloudmesh/data/db
   mongod --dbpath ~/.cloudmesh/data/db --bind_ip 127.0.0.1


Try it out
-------

Just uses firt python environment::

  make deploy
  make test

testing validation
--------------

python schema.py


TO DO
-----

insert

curl -d '{"name": "myCLuster",	"label": "c0","ip": "127.0.0.1","memoryGB": 16}' -H 'Content-Type: application/json'  http://127.0.0.1:5000/computer  

add logger
