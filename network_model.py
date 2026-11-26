from ipaddress import ip_address, ip_network

class NetworkModel:
    def __init__(self, config):
        self.branches = config["branches"]
        self.routes = config["routes"]

    def get_branch_for_ip(self, address):
        ip = ip_address(address)
        for branch in self.branches:
            if ip in ip_network(branch["subnet"]):
                return branch
        return None

    def lookup_route(self, destination):
        target = ip_address(destination)
        matches = []
        for route in self.routes:
            network = ip_network(route["destination"], strict=False)
            if target in network:
                matches.append((network.prefixlen, route))
        return max(matches, key=lambda x: x[0])[1] if matches else None

    def simulate_connectivity(self, source, destination):
        src_branch = self.get_branch_for_ip(source)
        dst_branch = self.get_branch_for_ip(destination)
        if src_branch is None:
            return {"status":"UNREACHABLE", "reason":"Source IP is outside configured branch subnets."}
        if dst_branch is None:
            return {"status":"UNREACHABLE", "reason":"Destination IP is outside configured branch subnets."}
        if src_branch["name"] == dst_branch["name"]:
            return {"status":"REACHABLE (LOCAL)", "reason":"Both endpoints are in the same branch subnet."}
        route = self.lookup_route(destination)
        if route is None:
            return {"status":"UNREACHABLE", "reason":"No matching route found."}
        if route.get("status") != "ACTIVE":
            return {"status":"UNREACHABLE", "reason":f"Route {route['route_id']} is inactive."}
        return {"status":"SIMULATED REACHABLE", "reason":f"{route['route_id']} forwards toward next hop {route['next_hop']} via {route['link']}."}
