from flask import Flask, render_template, request, redirect, url_for
import configparser
import subprocess
import shlex
import psutil
import os
import json,urllib.request

running=False
runningServer="None"

def startProgramm(cmd):
	stopProgramm()
	command = "./lan-play --netif eth0 --relay-server-addr "+cmd
	logfile = open('output', 'w', 1)
	proc = subprocess.Popen(shlex.split(command), stdout=logfile, bufsize=1)
	return True
	
def stopProgramm():
	global runningServer
	os.system("killall -9 lan-play")
	runningServer = "None"
	return False
    	
def getServers():
	servers = []
	config = configparser.ConfigParser()
	config.read('config.ini')
	
	for server in config['Servers']:
		dummy = []
		dummy.append(server)
		#ping server
		dummy.append(config['Servers'][server])
		server_address = config['Servers'][server][:-6]

		# Checking a different port for a specific server
		if server == 'joinsg':
   		 	port_to_check = 11453  # Replace with the specific port for this server
		else:
    			port_to_check = 11451  # Replace with the default port for other servers

		# Using os.system nc to check if the port is open
		up = True if os.system(f"nc -zv -w 1 {server_address} {port_to_check}") == 0 else False
		dummy.append(up)
		#get online count
		data = urllib.request.urlopen("http://"+config['Servers'][server]+"/info").read()
		output = json.loads(data)
		dummy.append(output["online"])
		servers.append(dummy)

	return servers

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/', methods=['POST', 'GET'])
def index():
	global runningServer
	servers = getServers()
	return render_template('index.html', servers=servers, runningServer=runningServer)

@app.route("/run/", methods=['POST', 'GET'])
def execute():
	global running
	global runningServer
	if running==True:
		pass
	else:
		cmd =request.form['serverAddr']
		running = startProgramm(cmd)
		runningServer = cmd
	return redirect('/')

@app.route("/stop/")
def stop():
	global running
	running = stopProgramm()
	return redirect('/')

@app.route("/logs/")
def logs():
	global running
	running = stopProgramm()
	return redirect('/')
