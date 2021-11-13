
## Network Python Libraries

Network environments today consist of multiple devices from various vendors, each serving different roles. To automate repetitive tasks and enhance operational efficiency while minimizing human errors, network engineers rely on design and automation frameworks. Large enterprises and service providers often create workflows to automate network tasks, improving resiliency and agility. These workflows consist of a series of related tasks executed when changes are needed in the network.

### Common Tasks in Network Automation

A network automation framework can perform several tasks without human intervention, including:

- Root cause analysis for problems
- Checking and updating device operating systems
- Discovering network topology and relationships between nodes
- Conducting security audits and compliance reporting
- Installing and withdrawing routes based on application needs
- Managing device configurations and rollbacks

### Python Libraries for Network Automation

| Library            | Description                                                                                                           | Link                                                                                     |
|--------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Netmiko**        | A multi-vendor library supporting SSH and Telnet for network devices, executing commands across various vendors.     | [Netmiko](https://github.com/ktbyers/netmiko)                                         |
| **NAPALM**         | A wrapper for vendor APIs, providing abstraction methods to connect to devices and extract information in structured format. | [NAPALM](https://github.com/napalm-automation/napalm)                                 |
| **PyEZ**           | Manages and automates Juniper devices, performing CRUD operations and retrieving device facts in JSON or XML format. | [PyEZ](https://github.com/Juniper/py-junos-eznc)                                     |
| **infoblox-client**| Interacts with Infoblox NIOS over a REST interface called WAPI.                                                    | [infoblox-client](https://github.com/infobloxopen/infoblox-client)                    |
| **NX-API**         | Cisco Nexus API that exposes CLI commands via HTTP/HTTPS, returning output in JSON or XML format.                   | [NX-API](https://developer.cisco.com/docs/nx-os/#!working-with-nx-api-cli)            |
| **pyeapi**         | A wrapper around Arista EOS eAPI for configuring Arista devices, supporting eAPI calls over HTTP/HTTPS.             | [pyeapi](https://github.com/arista-eosplus/pyeapi)                                    |
| **netaddr**        | Works with network addresses (IPv4, IPv6, MAC), allowing iteration, slicing, sorting, and summarizing IP blocks.   | [netaddr](https://github.com/drkjam/netaddr)                                          |
| **ciscoconfparse** | Parses Cisco IOS-style configurations, returning structured output and supporting brace-delimited configurations.   | [ciscoconfparse](https://github.com/mpenning/ciscoconfparse)                          |
| **NSoT**           | A database for tracking network device inventory and metadata, with a Django-based frontend and SQLite backend.     | [NSoT](https://github.com/dropbox/nsot)                                              |
| **Nornir**         | A Python-based automation framework that runs tasks against devices in the inventory, supporting Ansible formats.    | [Nornir](https://github.com/nornir-automation/nornir)                                  |

These libraries facilitate the automation of network tasks, enhancing efficiency and reducing the potential for errors in network management.

<br/>

## System and Cloud Python Libraries

There are various Python packages that can be used for system and cloud administration. Public cloud providers such as Amazon Web Services (AWS) and Google tend to provide open and standard access to their resources to easily integrate with the organization's DevOps model. Phases like continuous integration, testing, and deployment require continuous access to infrastructure (either virtualized or bare metal servers) to complete the code life cycle. This cannot be done manually and needs to be automated.

### Python Libraries for System and Cloud Administration

| Library                       | Description                                                                                          | Link                                                                                     |
|-------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **ConfigParser**              | Python standard library to parse and work with INI files.                                           | [ConfigParser](https://github.com/python/cpython/blob/master/Lib/configparser.py)      |
| **Paramiko**                  | A Python (2.7, 3.4+) implementation of the SSHv2 protocol, providing both client and server functionality. | [Paramiko](https://github.com/paramiko/paramiko)                                      |
| **Pandas**                    | A library providing high-performance, easy-to-use data structures and data analysis tools.          | [Pandas](https://github.com/pandas-dev/pandas)                                        |
| **boto3**                     | Official Python interface that manages different AWS operations, such as creating EC2 instances and S3 storage. | [boto3](https://github.com/boto/boto3)                                                |
| **google-api-python-client**  | Google official API client library for Google Cloud Platform.                                       | [google-api-python-client](https://github.com/google/google-api-python-client)          |
| **pyVmomi**                   | The official Python SDK from VMware that manages ESXi and vCenter.                                  | [pyVmomi](https://github.com/vmware/pyvmomi)                                          |
| **PyMYSQL**                   | A pure Python MySQL driver to work with MySQL DBMS.                                                | [PyMYSQL](https://github.com/PyMySQL/PyMySQL)                                          |
| **Psycopg**                   | The PostgreSQL adapter for Python which conforms to DP-API 2.0 standard.                           | [Psycopg](http://initd.org/psycopg/)                                                  |
| **Django**                    | A high-level open source web framework based on Python, following the MVT architecture for building web applications. | [Django](https://www.djangoproject.com/)                                              |
| **Fabric**                    | A simple Python tool for executing commands and software deployments on remote devices based on SSH. | [Fabric](https://github.com/fabric/fabric)                                            |
| **SCAPY**                     | A brilliant Python-based packet manipulation tool that can handle a wide range of protocols and build packets with any combination of network layers. | [SCAPY](https://github.com/secdev/scapy)                                              |
| **Selenium**                  | A Python library used to automate web-browser tasks and web-acceptance testing.                     | [Selenium](https://pypi.org/project/selenium/)                                        |

You can find more Python packages categorized into different areas at the following link: [Awesome Python](https://github.com/vinta/awesome-python).
