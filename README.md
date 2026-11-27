# IN PROGRESS

## Future Plans:
Network honeypot using HTTP OR SSH connection all built using Python and containerized using Docker.

Plans to train a ML model to identify the traffic and acts on it similar to an IPS + IDS or GuardDuty + Lambda type of function.

Start with HTTP honeypot and later transition to track SSH traffic once I'm more skilled

## Progress:
Created and configured socket as a server, used local host port 127.0.0.1 and a free port (2222)
Binded opened socket to the host and port and configured it to listen on the port and accept the traffic

Keep learning the socket library as I go 