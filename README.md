# Ansible role drunomics.drush
[![Build Status](https://travis-ci.org/drunomics/ansible-role-drush.svg?branch=master)](https://travis-ci.org/drunomics/ansible-role-drush)

Ansible role that installs drush.

Distribution: Ubuntu

## Requirements

- PHP must be installed.

## Usage
Note that this role can be used as root or on a per user basis by not specifying
become: yes on the playbook level. To configure drush for a certain user, enable
become at playbook level and specify the become_user as following:

  roles:
    - { role: drunomics.drush, tags: drush, become_user: jenkins }

For that to work with passwordless sudo access sudo needs to be configured
appropriately in addition to allowing passwordless root access. For example:

  %sudo   ALL=(jenkins) NOPASSWD: ALL


## License
MIT License
(c) 2015 drunomics GmbH.