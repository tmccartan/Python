from PreClass.network import Network
from PreClass.host import Host
from PreClass.persister import Persister


class Runner():

    @staticmethod
    def add_network():
        net_input = str(input("Enter Network ->"))
        ps = Persister()
        if ps.validate_network_input(net_input):
            net_note = str(input("Enter note ->"))
            net = Network(net_input, net_note)
            ps = Persister()
            ps.save_network(net)
            print(net_input)
        else:

            print("Invalid format")
            return

    @staticmethod
    def add_host():
        host = str(input("Enter IPv4 Address ->"))
        ps = Persister()
        if ps.validate_host_input(host):
            host_note = str(input("Enter note ->"))
            host = Host(host, host_note)
            ps = Persister()
            ps.save_host(host)
        else:
            print("Invalid format")

    @staticmethod
    def show_hosts():
        network = str(input("Enter network ->"))
        ps = Persister()
        for net in ps.hosts:
            if network.split("/")[0] in net["ip"]:
                print(net["ip"] + " - " + net["note"])

    @staticmethod
    def flush_data():
        ps = Persister()
        ps.flush()