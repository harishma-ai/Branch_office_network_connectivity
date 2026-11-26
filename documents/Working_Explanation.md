# Working Explanation

**Branch office network:** Separate office LANs, each with its own subnet.

**LAN:** Local devices' network. **Subnet:** IP range. **Default gateway:** router a host uses to reach other networks. **Route:** destination network plus next hop. **Next hop:** forwarding neighbor. **Site-to-site VPN:** common secure real-world method for linking offices; not created by this simulation.

Scenario:
- Coimbatore Branch A: `192.168.10.0/24`
- Chennai Branch B: `192.168.20.0/24`
- Illustrative link: `10.10.10.0/30`

When a Branch A host targets Branch B, the simulator looks up the destination route and displays the chosen next hop and a simulated reachable result. This is not a live ping.

Use: learning routing, subnets, gateways, branch connectivity design, and network administrator concepts.
