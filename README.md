Note that this role can be used as root or on a per user basis by not specifying
sudo: yes on the playbook level. To configure drush for a certain user, enable
sudo at playbook level and specify the sudo_user as following:

  roles:
    - { role: drunomics.drush, tags: drush, sudo_user: jenkins }

For that to work with passwordless sudo access sudo needs to be configured
appropriately in addition to allowing passwordless root access. For example:

  %sudo   ALL=(jenkins) NOPASSWD: ALL
