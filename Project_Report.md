# Project Report: Branch Office Network Connectivity Simulator

## Abstract
A Python simulation of routing between two office LANs, with configurable subnets, gateways, an illustrative inter-office link, and routes. It displays route lookup and simulated reachability.

## Problem
Companies with multiple offices need networks to communicate. Each office may use a different private subnet; routing (and commonly a secure site-to-site VPN over WAN/Internet) connects them.

## Objectives
- Model two branch LANs and their IP ranges.
- Explain subnet, gateway, route, and next-hop concepts.
- Simulate communication in both directions.
- Demonstrate longest-prefix route matching and automated tests.

## Method
Load JSON topology, identify endpoint subnets, find the most specific matching route, and report simulated connectivity.

## Conclusion
This project is a learning/demo model, not a live network or VPN implementation.
