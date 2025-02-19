import pyeapi
import os
import yaml

pyeapi.load_config('eapi.conf')

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

# The lab had this be a static list, but a bonus is to load from a YAML file
# switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4', 'spine1', 'spine2', 'spine3', 'spine4', 'borderleaf1', 'borderleaf2']

switch_file = open('switches.yml', 'r')
switches = yaml.safe_load(switch_file)
switch_file.close()

for switch in switches:
    connect = pyeapi.connect_to(switch)
    running_config = connect.get_config(as_string=True)
    path = directory + '/' + switch + '.cfg'
    file = open(path, 'w')
    file.write(running_config)
    file.close()
    print(f"Backing up {switch}")
