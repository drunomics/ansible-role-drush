# Ansible role drunomics.drush
[![Build Status](https://travis-ci.org/drunomics/ansible-role-drush.svg?branch=master)](https://travis-ci.org/drunomics/ansible-role-drush)

Ansible role that installs drush.

Distribution: Ubuntu

## Requirements

- PHP must be installed.

## Usage
Note that this role can be used as root or on a per user basis by not specifying
become: yes on the playbook level.


### System-wide installation
For a system wide installation, just add the role (as root) with the following vars:

  vars:
    drush_add_system_launcher: true
    composer_home_path: /opt/composer

This registers /opt/composer as root's composer path, which can be used for installing system-wide composer packages. In addition, it adds a small launcher script to a configurable bin directory, such that the `drush` command is available. Alternatively, composer bin directory may be added to the system $PATH variable.

### Per-user installation

To configure drush for a certain user, enable become at playbook level and specify the become_user as following:

  roles:
    - { role: drunomics.drush, tags: drush, become_user: drunomics }

Afterwards the drush launcher is available at ~/.composer/vendor/bin/drush. For putting the launcher in the path, it's suggested to add the user's composer bin directory to the user's $PATH variable (not covered by this role).

## License
MIT License
(c) drunomics GmbH.
