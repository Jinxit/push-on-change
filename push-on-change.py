#!/usr/bin/python

import sys
import time
import subprocess
import httplib
import urllib

from tokens import *

def notify(title, message):
	post = {
		"token": app_token,
		"user": user_token,
		"message": message,
		"title": title
	}

	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
		urllib.urlencode(post),
		{ "Content-type": "application/x-www-form-urlencoded" })
	conn.getresponse()

command = sys.argv[1]
delay = float(sys.argv[2])
title = sys.argv[3]

lastOutput = ""
while True:
	output = subprocess.Popen(command.split(), stdout=subprocess.PIPE).communicate()[0]
	if lastOutput != output:
		notify(title, output)
		lastOutput = output
	time.sleep(delay)
