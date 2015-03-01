import json


class FileAccess(object):

    def __init__(self, net_file_name, host_file_name):
        self.network_file_name = net_file_name
        self.host_file_name = host_file_name

    def save_to_file(self, name, array):
        with open(name, "w") as datafile:
            json.dump(array, datafile, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def get_file_data(self, name):
        with open(name) as datafile:
            data = json.load(datafile)
            return data

    def load_networks(self):
        networks = self.get_file_data(self.network_file_name)
        return networks

    def load_hosts(self):
        hosts = self.get_file_data(self.host_file_name)
        return hosts
