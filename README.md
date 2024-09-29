# Network Layer Practical Exercise: Distance Vector Routing Simulation

This project simulates real-time routing using the Distance Vector Routing algorithm. The program processes input commands such as adding/removing links, updating distance vectors, routing new packets, and printing the router's current distance vector. The simulation assumes no overlapping subnets in the input.

## Key Features
- Adding/removing links between routers
- Handling distance vector updates from neighbors
- Routing packets based on the current distance vector
- Real-time simulation of router behavior

## Input Types
The program accepts several types of input commands:

1. **Adding a link:**  
   Format:  
   `add link <id> <neighbor-ip-address>/<subnet-mask-bits-number> <distance-estimate>`  
   Example:  
   `add link 2 1.2.3.4/24 12`

2. **Removing a link:**  
   Format:  
   `remove link <id>`  
   Example:  
   `remove link 2`

3. **Updating distance vector:**  
   Format:  
   `update <link-id> <distance-vector-length>`  
   Followed by the next `<distance-vector-length>` lines, each containing:  
   `<ip-address>/<subnet-mask-bits-number> <distance-estimate>`  
   Example:  
   ```plaintext
   update 2 3
   1.2.4.1/24 30
   1.2.5.1/24 32
   1.3.8.1/16 45

   Sample Input and Output
Sample Input 1:

   ```plaintext
add link 1 192.168.1.0/24 5
add link 2 192.168.2.0/24 10
print
route 192.168.1.15
route 192.168.2.20
remove link 1
print
route 192.168.1.15
exit
```
Sample Output 1:

```plaintext
192.168.1.0/24 5
192.168.2.0/24 10
1
2
192.168.2.0/24 10
No route found
```

Sample Input 2:
   ```plaintext
add link 1 192.168.1.0/24 5
add link 2 192.168.3.0/24 15
update 2 2
192.168.4.0/24 7
192.168.5.0/24 10
print
route 192.168.4.25
route 192.168.5.30
exit
```
Sample Output 2:
   ```plaintext
192.168.1.0/24 5
192.168.3.0/24 15
192.168.4.0/24 22
192.168.5.0/24 25
2
2
```
   


