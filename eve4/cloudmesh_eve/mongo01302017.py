# TODO: complete
# for executing shell commands please do not reinvent the whele but use

# https://github.com/cloudmesh/client/blob/master/cloudmesh_client/common/Shell.py
# if commands are missing or are not working we can fix that in cloudmesh_client

import subprocess
import commands
import os

class mongo(object):

    def start(portnumber):
        """starts the mongo service."""
        print("not yet implemented")
	#subprocess.call(mongod --port portnumber)
        os.system('sudo service mongod start')
	print 'mongod  ------  running'


    def stop():
        """stops the mongo service."""
        os.system('sudo service mongod stop')
        #subprocess.call(mongod --shutdown) 
	print 'mongodb  ------  stopped'


    def status(format=None):
        """returns the status of the service. if no parameter. if format
        is specified its returned in that fomat. txt, json, XML,
        allowed
        """
	output = commands.getoutput('ps -A')
	if 'mongod' in output :
	    print 'mongod  ------  running'
	else:
            print 'mongod  ------  stopped'


    def reset():
        """stops the service and deletes the database, restarts the service."""
	os.system('sudo service mongod stop')        
 	print 'mongodb  ------  stopped'
        
	#print("not yet implemented")
        pass


    def delete():
        """just deletes all data in the database"""
        print("not yet implemented")
        pass

    
    def pid():
        """returns the pid of the mongo db servier"""
	str= commands.getoutput("ps -A | grep mongod")
	charater = str.strip();
	print (charater.split(" ")[0])
        
	
    def log(path):
        """sets the log file to the given path"""
        print("not yet implemented")
        pass
    
#TODO: define test programs with nosetest


