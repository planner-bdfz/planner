from subprocess import Popen, PIPE
from shlex import split


def run_it(cmd):
	"""
	type in your command as a simple string.
	I will fix any other things.
	"""
	# split the command via shlex.split
	cmd_wrun = split(cmd)
	if cmd_wrun == []:
		print("please do not use nothing in your command!!!!!!!!!!")
		return
	print('command in list format:',cmd_wrun,'\n')

	try:
		cmd_running = Popen(
		cmd_wrun,
		shell=False,
		stdout=PIPE,
		stderr=PIPE,
		universal_newlines=True,
		encoding="UTF-8"
		)
		rc = cmd_running.wait()
		out,err = cmd_running.communicate()
		print('Return Code:',rc,'\n')
		print('output is: \n', out)
		print('error is: \n', err)
	except FileNotFoundError:
		print("Error: your command is not found")
		print("please review your command:","\n","$",cmd)
	except OSError:
		print("Error: your command caused OSError")
		print("please review your command:","\n","$",cmd)
