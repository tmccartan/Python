from PreClass.file_access import FileAccess
import re

class Persister(object):

    # taken from http://blog.markhatton.co.uk/2011/03/15/regular-expressions-for-ip-addresses-cidr-ranges-and-hostnames/
    IPV4_REGEX = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    IPV4_CIDR_REGEX ="^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(/([0-9]|[1-2][0-9]|3[0-2]))$"
    CIDR_REGEX = "[0-9]{1,3}(?:\.[0-9]{1,3}){0,3}/[0-9]+"

    def __init__(self):
        self.file_access = FileAccess("network.json", "hosts.json")
        self.networks = self.file_access.load_networks()
        self.hosts = self.file_access.load_hosts()

    def save_network(self, network):
        self.networks.append(network)
        self.file_access.save_to_file("network.json",  self.networks)

    def save_host(self, host):
        self.hosts.append(host)
        self.file_access.save_to_file("hosts.json",  self.hosts)

    def validate_host_input(self, host):
        # can validate here whether the host is already added
        ip4_match = re.match(self.IPV4_REGEX, host)
        if ip4_match:
            return ip4_match
        else:
            cidr_match = re.match(self.IPV4_CIDR_REGEX, host)
            return cidr_match

    def validate_network_input(self, network):
        # can validate here if network has already been added
        # or is overlapping another
        ip4_match = re.match(self.CIDR_REGEX, network)
        return ip4_match

    def flush(self):
        self.file_access.save_to_file("hosts.json",  [])
        self.file_access.save_to_file("network.json",  [])
        self.networks = self.file_access.load_networks()
        self.hosts = self.file_access.load_hosts()
