import sys
from subprocess import Popen

if sys.argv[1] == '--execute':
	payload = sys.stdin.read()
	config = json.loads(payload)
	params = config.get('configuration')
	remote_cmd = 'service %s restart' % params['service']
	command = ['ssh', params['user'] + '@' + params['host'], remote_cmd]
	#logging
	print >> sys.stderr, config
	Popen(command)


# to test alert from search:
# |sendalert custom_alert_action param.host=<host> param.user=<user> param.service=<service>
# inspect job, check search.log for details, search for "alert"
