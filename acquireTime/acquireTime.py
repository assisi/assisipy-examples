########################################################
######   read time from CASUs python script   ##########
#########         created: 06/13/16        #############
#########            D.M. LARICS           #############
######################################################## 



import zmq
from msg import dev_msgs_pb2
from msg import base_msgs_pb2
import threading
import yaml
import sys
from time import sleep

def main():

	# get script arguments
	if len(sys.argv) != 2:
		print("Invalid number of parameters!")
		return
	
	arenaFileName = str(sys.argv[1])

	# globals
	global zmqContext, zmqSub, casuTimes, timeThreadLock
	
	# ZMQ stuff
	zmqContext = zmq.Context(1)
	zmqSub = zmqContext.socket(zmq.SUB)
	zmqSub.setsockopt(zmq.SUBSCRIBE, '')

	# thread stuff
	timeThread = threading.Thread(target = receiveTime)	
	timeThread.daemon = True
	timeThreadLock = threading.Lock()
	
	# create casuTimes dictionary
	casuTimes = dict()
	
	# load *.arena yaml file
	with open(arenaFileName) as arenaFile:
		arena = yaml.safe_load(arenaFile)
		
	# iterate through CASU arena
	for casuName, casuInfo in arena['beearena'].iteritems():
		
		# connect to CASU sub address
		zmqSub.connect(casuInfo['sub_addr'])
		
		# populate casuTimes dicitonary with placeholder sec and nsec values
		casuTimes[casuName] = {'sec' : -1, 'nsec' : -1};

	timeThread.start()
	
	while True:
	
		# print casu times, this is just a placeholder for your code
		with timeThreadLock:
			for casuName, casuTime in casuTimes.iteritems():
		 		print "%s\n    sec:  %d\n    nsec: %d\n\n" % (casuName, casuTime['sec'], casuTime['nsec'])
		sleep(0.25)
		
		# your code goes here
		
		
		


# thread function for ZMQ receive
def receiveTime():
	
	temperatures = dev_msgs_pb2.TemperatureArray()
	
	while True:
	
		# receive zmq message
		[casuName, device, measurement, data] = zmqSub.recv_multipart()
		
		# use only temperatures messages
		if device == 'Temp':
			
			# parse ZMQ message
			temperatures.ParseFromString(data)
			
			# update casuTimes dictionary with received time values
			with timeThreadLock:
				casuTimes[casuName]['sec'] = temperatures.header.stamp.sec
				casuTimes[casuName]['nsec'] = temperatures.header.stamp.nsec
			
			
			
if __name__ == '__main__':
    main()
	
	
	
