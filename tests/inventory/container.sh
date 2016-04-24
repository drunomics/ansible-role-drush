#!/bin/bash
# When the "playbook" environment variable is set (via travis or run-all.py)
# we provider nicer container names, such that the test output is meaningful.

if [ "$playbook" == "" ]; then
  CONTAINER_NAME=ansible-run-test-playbook
else
  CONTAINER_NAME=ansible-run-$playbook
fi

cat <<end-of-json
{
    "container"   : {
        "hosts"   : [ "$CONTAINER_NAME" ],
        "vars"    : {
            "ansible_connection"   : docker,
            "ansible_user"         : root
        }
    }
}
end-of-json