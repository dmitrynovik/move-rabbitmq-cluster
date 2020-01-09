import sys, getopt, subprocess
from urllib.parse import urlparse
from rabbitmqadmin import Management

print("\nRabbitMQ Blue-Green Migration Script\n")

from_cluster = None
from_user = "admin"
from_password = "admin"
to_cluster = None
to_user = "admin"
to_password = "admin"
ssl = False

# Parse Command Line Arguments:
opts, arg = getopt.getopt(sys.argv[1:], "", 
    ["from-cluster=", "from-user=", "from-password=", "to-cluster=", "to-user=", "to-password=", "ssl="])

print("received arguments:")
for opt, arg in opts:
    print("\t", opt, " -> ", arg)
    if opt == "--from-cluster":
        from_cluster = arg
    elif opt == "--from-user":
        from_user = arg
    elif opt == "--from-password":
        from_password = arg
    elif opt == "--to-cluster":
        to_cluster = arg
    elif opt == "--to-user":
        to_user = arg
    elif opt == "--to-password":
        to_password = arg
    elif opt == "--ssl":
        ssl = arg
    
if from_cluster == None:
    raise Exception("Missing argument: --from-cluster")
if to_cluster == None:
    raise Exception("Missing argument: --to-cluster")
if to_cluster == from_cluster:
    raise Exception("Same source and destination, cannot proceed:", to_cluster)

print("\nSource cluster (url, user, pass):", from_cluster, from_user, from_password)
print("Destination cluster (url, user, pass):", to_cluster, to_user, to_password)

# export definitions:
defs_path = "rabbitmq.definitions.json"
export_return_code = subprocess.call(['python', './rabbitmqadmin.py', '-H', from_cluster, '-u', from_user, '-p', from_password, 'export', defs_path])
if export_return_code != 0:
    raise Exception('Failed to export definitions')

class RabbitMQAdminOptions:
    format = "raw_json"
    sort = sort_reverse = None
    path_prefix = ""
    request_timeout = 60

    def __init__(self, cluster, user, pwd, ssl):
        self.depth = 1
        self.username = user
        self.password = pwd

        url = urlparse(cluster)
        self.hostname = url.hostname or cluster
        self.port = url.port or "15672"
        self.ssl = ssl
        #print("url:", self.hostname, self.port, self.ssl)

opts = RabbitMQAdminOptions(from_cluster, from_user, from_password, ssl)
mgmt = Management(opts, ['vhosts'])
mgmt.invoke_list()
#print(result)





