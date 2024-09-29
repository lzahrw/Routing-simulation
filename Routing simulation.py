import ipaddress
import sys

class Router:
    def __init__(self):
        self.links = {}
        self.distance_vector = {}
        self.link_subnets = {}  # Maps subnets to their respective links

    def add_link(self, link_id, subnet, distance):
        subnet = ipaddress.ip_network(subnet)
        self.links[link_id] = (subnet, distance)
        self.link_subnets[subnet] = link_id
        self.update_distance_vector()

    def remove_link(self, link_id):
        if link_id in self.links:
            subnet, _ = self.links[link_id]
            del self.links[link_id]
            if subnet in self.link_subnets:
                del self.link_subnets[subnet]
            self.update_distance_vector()

    def update_distance_vector(self):
        self.distance_vector.clear()
        for link_id, (subnet, distance) in self.links.items():
            self.distance_vector[subnet] = distance

    def receive_distance_vector(self, link_id, received_vector):
        if link_id not in self.links:
            return
        _, base_distance = self.links[link_id]
        for subnet, distance in received_vector.items():
            total_distance = base_distance + distance
            self.distance_vector[subnet] = total_distance
            self.link_subnets[subnet] = link_id  # Update the link_subnets dictionary

    def print_distance_vector(self):
        sorted_vector = sorted(self.distance_vector.items(), key=lambda x: (int(x[0].network_address), x[0].prefixlen))
        for subnet, distance in sorted_vector:
            print(f"{subnet} {distance}")

    def route_packet(self, destination_ip):
        dest_ip = ipaddress.ip_address(destination_ip)
        best_link = None
        best_distance = float('inf')
        for subnet, distance in self.distance_vector.items():
            if dest_ip in subnet and distance < best_distance:
                best_distance = distance
                best_link = self.link_subnets[subnet]
        if best_link is not None:
            print(best_link)
        else:
            print("No route found")

def main():
    router = Router()
    for line in sys.stdin:
        line = line.strip()
        if line.startswith("add link"):
            _, _, link_id, subnet, distance = line.split()
            router.add_link(int(link_id), subnet, int(distance))
        elif line.startswith("remove link"):
            _, _, link_id = line.split()
            router.remove_link(int(link_id))
        elif line.startswith("update"):
            _, link_id, vector_length = line.split()
            vector_length = int(vector_length)
            received_vector = {}
            for _ in range(vector_length):
                subnet, distance = sys.stdin.readline().strip().split()
                received_vector[ipaddress.ip_network(subnet)] = int(distance)
            router.receive_distance_vector(int(link_id), received_vector)
        elif line == "print":
            router.print_distance_vector()
        elif line.startswith("route"):
            _, destination_ip = line.split()
            router.route_packet(destination_ip)
        elif line == "exit":
            break

if __name__ == "__main__":
    main()
