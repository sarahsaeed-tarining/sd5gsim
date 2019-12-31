# SD5GSim
SD5GSim is a network simulator to simulate network performance under different circumstances using different simulation parameter.

# INSTALLATION AND RUNNING  
To install SD5GSim, you can use the following command:

**pip install sd5gsim==0.2**

**Important Note:** Make sure to download the following icons and put them in your project directory:
* run.png
* gen.png
* exit.png
* clear.png
* icon3.png
* icon2.png
* icon5.png
* icon4.png

**Then to run the simulator you can simply run the following commands:**

```python
from sd5gsim import main
main()
```

# SD5GGSim GUI Snapshots 

# Required Libraries:
* tkinter library
* threading  library
* concurrent.futures library
* pprint library
* datetime as dt library
* defaultdict library
* pandas as pd library
* random library
* uuid library
* PIL library
* time library
* ttk library
* matplotlib.pyplot as plt library

# Classes
## basestation: 
**This class is the instance of the network simulator that represents
the controller of the SDN network. and it has the following attributes:**
* bs_id: a unique identifier for each basestation in the network
* n_count: total number of nodes in each network
* channel_count: total number of channels available for each network
* coordinates: pair of x and y coordinates that specify the basestation location
in the network
* dimensions: total dimensions of the network that belongs to the current basestation
* bs_nodes: list of all nodes reside in the network
* global_pool: list of all channels available for the network
* ch_allocations: a data structure (Python dictionary) that stores tuples of
nodes and the corresponding allocated channels.
* channel_capacity: individual channel capacity
* num_of_reqs: total number of communication requests made by all PNs
throughout the simulation time.
* num_of_blocked_reqs: total number of blocked communication requests due
to channel unavailability throughout the simulation time.
* num_of_transmitted_pkts: total number of packets transmitted between all
PNs throughout the simulation time.
* total_bandwidth: total available bandwidth for the network
* overhead: the network overhead which is the ratio between the number of
control packets sent to the basestation and the total amount of packets sent
throughout the simulation.
* throughput: average rate that shows the amount of successful delivery of packets
between nodes in the network.
* blocking_rate: the ratio between the number of blocked requests and total
number of requests.
* channel_utilization: the ratio between the amount of packet transmitted successfully
for a specific time period and the peak amount that the network
resources can handle.

**The basestation class also has the following methods:**
* assing_ch_to_node: a method for assigning channels to a PNs
* establish_connection: a method for creating and saving connection parameters
* terminate_connection: a method for terminating and revoking the assigned
channels from a PN
* plot_network: a method for drwaing the network.
## node:
**This class is the instance of the network simulator that represents the PNs in the SDN network and it has the following attributes:**
* node_id: a unique identifier for each PN in the network.
* vn_count: number of VNs for each PN.
* ant_count: number of antennas installed on each PN.
* ch_count: number of local channels allocated for the PN.
* coordinates: pair of x and y coordinates that specify the PN location in the
network
* parent_bs: the basestaion that is controlling the cell.
* local_channels: list of all allocated channels.
* local_antennas: list of all installed antennas.
* local_v_nodes: list of all VNs in the PN.

**The node class also has various methods as follows:**
* add_to_local_channels: a method for inserting the new allocated channel to
the local pool.
* activate_v_node: a method for activating a VN to be used for the communication
with other nodes.
* deactivate_v_node: a method for deactivating the VN after finishing the
transmission.
* activate_ant: a method for activating a antenna to be used for the
connection.
* deactivate_ant: a method for deactivating the antenna after finishing
the transmission.
* request_ch: a method for requesting a channel from the basestation to establish
a connection with other node in the network.
* print_info: a method for diplaying the node information.
## v_node class: 
**This class is the instance of the network simulator that represents the virtual instance of the PN used for creating a connection with other nodes in the SDN network and it has the following attributes:**
* v_node_id: a unique identifier for each VN in the network
* active: boolean variable that indicates of the VN is active or not.
* alloc_res_list: a data structure (Python dictionary) that stores the channels
allocated for the VN
* parent_nd: the node that is controlling the VN.
* parent_bs: the basestaion that is controlling the cell that this VN belongs to.

**The v_node class has also various methods, as follows:**
* add_res: a method to add a new antenna and channel pair to the
allocation list
* activate: a method for activating the VN
* deactivate: a method for deactivating the VN
* request_res: a method for requesting resources to start a connection
* vacate_res: a method for vacating the allocated resoures after the transmission
is finished.
## connection:
**This class stores information about the connections in the SDN network and it has the following attributes:**
* connection_id: a unique identifier for each connection in the network
* src_node: the sender node side of the connection
* src_vnode: the sender VN side of the connection
* src_ant: the sender antenna side of the connection
* src_ch: the sender channel side of the connection
* des_node: the receiver node side of the connection
* des_vnode: the receiver VN side of the connection
* des_ant: the receiver antenna side of the connection
## channel:
**This class is the instance of the network simulator that represents the channels used for the connection between nodes in the SDN network and it has the following attributes:**
* ch_id: a unique identifier for each channel available in the network
* power: the transmission power for the channel
* availability: a boolean indicator that used to indicate if the channel is available
to be used for connection between nodes
* allocations: list of all nodes allocated the channel
## antenna:
**This class is the instance of the network simulator that represents the antennas used for the connection between nodes in the SDN network and it has the following attributes:**
* ant_id: a unique identifier for each antenna available in the network
* active: a boolean indicator that used to indicate if the antenna is being
used in the connections
* power: the transmission power for the antenna.
## SD5GSim_GUI:
**This class is the network simulator GUI. Where the interface includes the following components:**
![SD5GSim](https://user-images.githubusercontent.com/59348176/71614636-dce1a000-2b7a-11ea-9384-69d80c99e7df.png)
### Network parameters component:
In this component, the user can select different parameters to build the network simulation environment, including:
* Number of cells
* Number of channels for each cell
* Number of PNs for each cell
* Number of VNs for each cell
* Number of antennas for each PN
* Simulation time

### Simulation results component: 
This component shows the results after running the simulation according to the network performance metrics and it includes:
* Network Throughput
* Network Blocking Rate
* Network Overhead
### Menu bar Component: 
This component includes various menus that allow users to interact with the simulation interface, following are some of these options:
* File menu: it includes options to create new project and exit window options.
* Run menu: it includes options to generate simulation environment, clear simulation
environment, and start simulation.
### Toolbar Component: 
This component includes a strip of icons used to perform certain functions, as generate simulation environment, clear simulation environment, and start simulation. Also, it shows the various cells created for simulation, so users can navigate between different cells.
### Simulation environment component: 
This component used to visualize the network after building it using "Generate Environment" option. It includes icons for basestations and PNs and their coordinates (location) in the network.
### Status bar component: 
This status bar shows information for the current selected cell, like number of PNs, number of channels and basestation ID.

# Contributors:
* Sarah Saeed
* Yaser Jararweh
* Haythem Bany Salameh

