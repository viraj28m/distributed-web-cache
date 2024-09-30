PKT_SIZE = 1024                 # size of packet
MAX_CACHE_SIZE = 5              # max entries per cache server
NUM_CACHE_SERVERS = 3           # number of cache servers
MASTER_PORT = 5001              # port for master server
TO_MASTER_FROM_NODES = 5002     # port for master to receive messages from nodes
CACHE1_PORT = 5003              # port for cache server 1, ports assigned in ascending order afterwards
HEARTBEAT_MSG_LEN = 9           # 1 byte for heartbeat, 8 bytes for node id
HEARTBEAT_EXPIRATION_TIME = 10  # seconds since last heartbeat that would necessiate removal of node
HEARTBEAT_INTERVAL = 1          # seconds between heartbeats 