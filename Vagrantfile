# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-18.04"
  config.ssh.insert_key = false

  config.vm.network "private_network", ip: "192.168.56.100"

  config.vm.synced_folder "vagrant", "/vagrant", :mount_options => ["ro"]
  config.vm.synced_folder "", "/www", owner: "vagrant", group: "vagrant", :mount_options => ["rw"]

  config.vm.provision "ansible_local" do |ansible|
     ansible.provisioning_path = "/vagrant/provision"
     ansible.inventory_path = "inventory"
     ansible.playbook = "playbook.yml"
     ansible.limit = "all"
  end
end
