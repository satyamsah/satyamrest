# TODO: complete
# for executing shell commands please do not reinvent the whele but use

# https://github.com/cloudmesh/client/blob/master/cloudmesh_client/common/Shell.py
# if commands are missing or are not working we can fix that in cloudmesh_client


import commands
import os
from pymongo import MongoClient

class mongo(object):

	# def __init__(self):
	# 	client = MongoClient(host='localhost', port=27017)

    def start(self,portnumber):

		os.system('sudo service mongod start')
		output1 = commands.getoutput('ps -A')
		if 'mongod' in output1 :
			print 'mongod  ------  running'
		else:
			os.system("systemctl start mongod");
			output2 = commands.getoutput('ps -A')
			if 'mongod'  in output2:
			print 'mongod  ------  running'
			else:
			print 'mongod  ------  stopped'


    def stop(self):
		os.system('sudo service mongod stop')
		output1 = commands.getoutput('ps -A')
		if 'mongod' in output1 :
			os.system("systemctl stop mongod");
			output2 = commands.getoutput('ps -A')
			if 'mongod' in output2:
				print 'mongod  ------  running'
			else:
				print 'mongod  ------  stopped'
		else:
			status="stopped"
			print 'mongod  ------  stopped'



    def status(self,format=None):
		"""returns the status of the service. if no parameter. if format
        is specified its returned in that fomat. txt, json, XML,
        allowed
        """
		output = commands.getoutput('ps -A')
		if 'mongod' in output :
			print 'mongod  ------  running'
		else:
			print 'mongod  ------  stopped'


    def reset(self ,databasename):
		""" Starts the database service  if shut down.
		Delete the given database  and then restarts the db services """
		client= MongoClient(host='localhost',port=27017)

		try:
			output = commands.getoutput('ps -A')
			if 'mongod' in output:
				print 'mongod  ------  running'
			else:
				print 'mongod  ------  stopped'
				os.system('sudo service mongod start')
				output = commands.getoutput('ps -A')
				if 'mongod' in output:
					print 'mongod  ------  running'
				else:
					os.system("systemctl start mongod");
					output = commands.getoutput('ps -A')
					if 'mongod' in output:
						print 'mongod  ------  running'
					else:
						print 'mongod  ------  stopped'

			client.drop_database(databasename);

			#restarting the service
			# os.system('sudo service mongod restart')
			# output1 = commands.getoutput('ps -A')
			# if 'mongod' in output1 :
			#     print 'mongod  ------  running'
			# else:
			#     print 'mongod  ------  stopped'


			#stopping the service
			os.system('sudo service mongod stop')
			output2= commands.getoutput('ps -A')
			if 'mongod' in output2 :
				os.system("systemctl stop mongod");
				output21 = commands.getoutput('ps -A')
				if 'mongod' in output21:
					print 'mongod  ------  running'
				else:
					print 'mongod  ------  stopped'
			else:
				status="stopped"
				print 'mongod  ------  stopped'

			#starting the service
			os.system('sudo service mongod start')
			output3 = commands.getoutput('ps -A')
			if 'mongod' in output3 :
				print 'mongod  ------  running'
			else:
				os.system("systemctl start mongod");
				output31 = commands.getoutput('ps -A')
				if 'mongod'  in output31:
					print 'mongod  ------  running'
				else:
					print 'mongod  ------  stopped'
			client.close();
		except:
			print "something went wroing , either database does not exist or database connection issue"


    def delete(self,database):
		"""just deletes all data from all collections
		in a particular database and leave the collection only with schema """
		try:

			client = MongoClient(host='localhost', port=27017)
			db=client.get_database(database)
			collectionsnames=db.collection_names()

			for singlecollectionname in collectionsnames:
				print "deleting",singlecollectionname," ..."
				db.get_collection(singlecollectionname).remove({})
		except:
			print "connection is down or the database does not exist"


    def pid(self):
		"""returns the pid of the mongo db servier"""
		str= commands.getoutput("ps -A | grep mongod")
		charater = str.strip();
		print (charater.split(" ")[0])
        

    def log(self,path):
        """sets the log file to the given path"""
        print("not yet implemented")
        pass
    
#TODO: define test programs with nosetest

if __name__=="__main__":
	"""nosetest function"""
	m= mongo()
	m.start(27017);
	m.stop();
	m.start(27017);
	m.status()
	m.pid()
	m.delete("eatables") # test database
	m.reset("eatables") # testdatabase


