#!/usr/bin/env python
# Small launcher to run tests as specified in .travis.yml.
# Written by Wolfgang Ziegler // fago.

import subprocess, os, sys, yaml;

# Assume ANSI colors and used colored shell output.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

exit_code = 0
stream = open("../.travis.yml", "r")
travis = yaml.load(stream)
for env_vars in travis.get('env'):
  for script in travis.get('script'):
    # Prepare an environment for running the script as travis does.
    env = os.environ.copy()
    env.update(env_vars)

    # Output the script executed while evaluating bash variables used.
    script_evaled = subprocess.check_output(['bash', '-c', 'echo "' + script + '"'], env=env)
    print ""
    print bcolors.HEADER + "RUNNING: " + script_evaled + bcolors.ENDC

    # Run the script.
    exit_code_script = subprocess.Popen(['bash', '-c', script], env=env).wait()
    if exit_code_script != 0:
      exit_code = 1
      print ""
      print bcolors.FAIL + "SCRIPT FAILED: " + script_evaled + bcolors.ENDC
      print ""

print "-------------"
if int(exit_code) > 0:
  print bcolors.FAIL + "Tests FAILED!" + bcolors.ENDC
  sys.exit(1)
else:
  print bcolors.OKGREEN + "Tests PASSED!" + bcolors.ENDC
  sys.exit(0)
