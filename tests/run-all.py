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

# Ensure the working directory is our directory.
os.chdir(os.path.dirname(sys.argv[0]))

# Install role dependencies only, so we do not require sudo.
print bcolors.HEADER + "Installing role dependencies" + bcolors.ENDC
subprocess.Popen(['ansible-playbook', 'install-dependencies.yml', '--tags=dependencies']).wait()

# Bail out if docker-py is missing.
result = subprocess.Popen(['bash', '-c', 'pip list | grep docker-py']).wait()
if result > 0:
  raise SystemExit(bcolors.FAIL + "Error: Missing the required python module docker-py. To install, run:\n  ansible-playbook install-dependencies.yml -K" + bcolors.ENDC)


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
