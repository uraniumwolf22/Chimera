#!/bin/bash
echo "Starting persistent serial client tunnel. Press Ctrl-C to exit."

while true
do
    socat PTY,link=/dev/ttyS10,raw,echo=0,wait-slave TCP:10.4.11.21:6666
    
    echo "Client script disconnected. Waiting for new connection..."
    sleep 1
done