import nacos

# Both HTTP/HTTPS protocols are supported, if not set protocol prefix default is HTTP, and HTTPS with no ssl check(verify=False)
# "192.168.3.4:8848" or "https://192.168.3.4:443" or "http://192.168.3.4:8848,192.168.3.5:8848" or "https://192.168.3.4:443,https://192.168.3.5:443"
SERVER_ADDRESSES = "http://127.0.0.1:8848"
NAMESPACE = "public"

# no auth mode
client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE)
# auth mode
# client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, ak="{ak}", sk="{sk}")

# get config
data_id = "config.nacos"
group = "group"
print(client.get_config(data_id, group))

# register instance
service_name = "nacos-sdk-python"
ip="127.0.0.1"
port=9876
cluster_name = "DEFAULT"
weight = 1
metadata = {"version": "1.0"}
enable = True
healthy = True
ephemeral = True
group_name = "DEFAULT_GROUP"
heartbeat_interval = 5
NACOS_SERVER_ADDRESSES = "http://127.0.0.1:8848"
NACOS_NAMESPACE="aimark"
client = nacos.NacosClient(server_addresses=NACOS_SERVER_ADDRESSES, namespace=NACOS_NAMESPACE)
success = client.add_naming_instance(service_name, ip, port, cluster_name, weight, metadata, enable, healthy,ephemeral,group_name,heartbeat_interval)
print(success)
# TODO(吴方圆): add more examples