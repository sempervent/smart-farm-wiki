---
title: "Halowlink User Guide 2 11 2 (extracted from PDF)"
source_pdf: raw/processed/2026/halowlink-user-guide-2-11-2.pdf
extracted: 2026-04-18
page_count: 57
note: Machine-extracted text; verify against the PDF for tables, figures, and typography.
---

# Halowlink User Guide 2 11 2

**Source PDF:** [`halowlink-user-guide-2-11-2.pdf`](./halowlink-user-guide-2-11-2.pdf) — repo path `/raw/processed/2026/halowlink-user-guide-2-11-2.pdf`


## Page 1

Copyright © 2025 Morse Micro 
Refer to the online version for up-to-date content

## Page 2

Refer to the online version for up-to-date content 
 
  
Table of Contents 
1 What is a HaLowLink?​
4 
1.1 HaLowLink Models​
5 
1.2 Important Security Notice​
6 
1.2.1 HTTPS-Only Access​
6 
1.2.2 SSH Disabled by Default​
7 
1.2.3 Software Updates​
7 
1.3 Preset Configurations​
8 
1.3.1 Router With a Wi-Fi HaLow Access Point​
8 
1.3.2 Wi-Fi HaLow Access Point (AP)​
8 
1.3.3 Wi-Fi HaLow Extender​
8 
2 Getting Started​
9 
2.1 Initial Connection​
9 
2.1.1 Using Ethernet​
9 
2.1.2 Using Wi-Fi​
9 
2.1.3 Using USB-C​
9 
2.1.4 Connecting to an Existing Network Using Ethernet​
10 
2.2 Login Page​
10 
2.3 Getting the Latest Software​
11 
2.4 Home Page​
11 
2.5 Wizard​
12 
2.5.1 Wi-Fi HaLow Modes​
12 
2.5.2 Network Modes​
13 
3 HaLow Extender​
15 
3.1 Pairing​
15 
3.2 Manual Extender Configuration (Alternative)​
16 
3.3 Using Your Extender’s Connection​
17 
4 Mesh (Advanced)​
18 
4.1 Should I Use a Mesh?​
18 
4.1.1 HaLowLink Mesh Comparison​
19 
4.2 EasyMesh​
20 
4.3 802.11s Mesh (beta)​
21 
4.4 Pairing Extenders to a Mesh​
22 
4.4.1 EasyMesh​
22 
4.4.2 11s Mesh​
22 
5 Restoring Factory Settings​
23 
6 Use Cases​
24 
6.1 Adding a HaLow Access Point to Your Existing Network via Ethernet​
24 
6.2 Adding a HaLow Access Point to a Network via 2.4 GHz Wi-Fi​
25 
6.3 Using HaLow to Extend an Existing Network - Virtual Wire​
26 
6.4 Connect Your Computer to a HaLow Network via USB-C​
27 
6.5 Connect an Ethernet Device to a HaLow Network​
27 
 
 
morsemicro.com  |  2

## Page 3

Refer to the online version for up-to-date content 
 
  
6.6 Connect a Non-HaLow Wi-Fi Device to a HaLow Network​
28 
6.7 Experimenting with HaLow​
29 
7 Quick Config​
30 
7.1 Network Interfaces​
30 
7.2 Wireless​
31 
7.3 Advanced Usage​
31 
8 Advanced Config​
32 
9 Exploring HaLow Connectivity​
33 
9.1 Status​
33 
9.1.1 Channel Analysis​
33 
9.1.2 Realtime Graphs​
33 
9.2 Network​
33 
9.2.1 Diagnostics​
33 
9.3 Statistics​
33 
9.3.1 Graphs​
33 
9.4 Services​
34 
9.4.1 Terminal​
34 
9.4.2 Range Test​
34 
10 Configuring With the Command Line​
37 
10.1 Making Changes​
37 
10.2 File/Service Structure​
38 
10.3 Debugging​
38 
10.4 Applying Configurations​
39 
11 Software Updates​
40 
12 Device Features​
41 
12.1 LED Indicators​
41 
12.1.1 Status LED​
41 
12.1.2 Wi-Fi HaLow LED​
41 
12.1.3 Wi-Fi 2.4 GHz LED​
42 
12.2 Ethernet/USB Ports​
43 
12.2.1 Access Point Mode (Green Status LED)​
43 
12.2.2 Extender Mode (Aqua Status LED)​
43 
13 Frequently Asked Questions​
44 
14 Troubleshooting​
49 
14.1 Recovering From Failed Updates​
51 
15 Licensing and source​
53 
16 FCC Compliance Statement​
54 
17 IC Compliance Statement​
55 
18 Simplified EU Declaration of Conformity​
56 
 
 
 
morsemicro.com  |  3

## Page 4

Refer to the online version for up-to-date content 
 
  
1 What is a HaLowLink? 
Your HaLowLink allows you to use Morse Micro’s HaLow Wi-Fi to: 
●​ easily set up a Router with a HaLow Access Point to create a new network which supports 
HaLow 
●​ let other HaLow-enabled devices to connect to your existing network through a HaLow 
Access Point 
●​ add a HaLow Extender so that existing non-HaLow devices (i.e. 2.4 GHz Wi-Fi and Ethernet 
Computers) can benefit from HaLow’s range 
It’s flexible and powerful enough that it can perform all these roles. For more information on how 
these roles can be useful, see the Use Cases section below. 
 
Figure: HaLowLink diagram 
 
 
 
morsemicro.com  |  4

## Page 5

Refer to the online version for up-to-date content 
 
  
1.1 HaLowLink Models 
 
 
Figure: HaLowLink 1 product image 
 
 
Figure: HaLowLink 2 product image 
This guide applies to both the HaLowLink 1 and the HaLowLink 2 models (pictured above). Both 
devices share the same core functionality and run the same HaLowLink variant of Morse Micro 
OpenWrt software (open-source versions are available at github.com/MorseMicro/openwrt). 
The only critical differences between the two models are in the hardware. The primary upgrade is a 
transition from the Morse Micro MM6108 HaLow chip in the HaLowLink 1 to the next generation 
MM8108 chip in the HaLowLink 2. 
The purpose of this guide is to provide a unified set of user instructions which apply equally to both 
models. If at any point in the future this guide is updated to include model-specific instructions, they 
will be explicitly identified. In all other cases, the term HaLowLink (without a model number suffix) 
will be used to refer to all models equally.
 
 
 
morsemicro.com  |  5

## Page 6

Refer to the online version for up-to-date content 
 
  
1.2 Important Security Notice 
There have been some significant updates to the Morse Micro OpenWrt software in order to remain 
compliant with international cybersecurity requirements. 
1.2.1 HTTPS-Only Access 
The HaLowLink web interface, from Morse Micro OpenWrt 2.11.x onwards, is accessible only via 
HTTPS. Any attempt to connect using HTTP will automatically redirect to https://192.168.12.1. 
When you first connect, your browser may display warnings about the page being insecure. This is 
expected, because the HaLowLink uses an encrypted HTTPS session without a signed certificate. You 
must proceed through these warnings in order to continue accessing the device. This is safer than 
HTTP as all traffic will be encrypted. 
 
Figure: Chrome HTTPS warning page 
 
Figure: Safari HTTPS warning page 
 
Figure: Edge HTTPS warning page 
 
Figure: Firefox HTTPS warning page 
 
 
morsemicro.com  |  6

## Page 7

Refer to the online version for up-to-date content 
 
  
1.2.2 SSH Disabled by Default 
To enable SSH, navigate to the SSH Access tab on the Administration Page in Advanced Config. 
 
Figure: The SSH Access page 
1.2.3 Software Updates 
To maintain compliance with evolving cybersecurity requirements, updates for this device may be 
released more frequently and it is strongly recommended to regularly check for new updates via the 
Software Updates page. 
 
 
 
morsemicro.com  |  7

## Page 8

Refer to the online version for up-to-date content 
 
  
1.3 Preset Configurations 
Below are high-level descriptions of common configuration “presets”, which are combinations of 
HaLow Mode and Network Mode, and can be configured via the Wizard page. 
1.3.1 Router With a Wi-Fi HaLow Access Point 
This is the default mode of operation for the HaLowLink. It has an IP address of 192.168.12.1, and 
hands out addresses to devices connected to the LAN side via Ethernet, 2.4 GHz Wi-Fi or Wi-Fi 
HaLow in this range. The WAN Ethernet port is the default uplink connection, and will obtain an 
address as a DHCP client. In this mode the HaLowLink is most similar to a typical home 
router/gateway, and it is not possible to access the web interface via the uplink connection. 
1.3.2 Wi-Fi HaLow Access Point (AP) 
Similar to access points (APs) available on the market, this allows you to add a HaLow Access Point to 
your existing network. You still use your WAN Ethernet port (which is more appropriately considered 
the “Uplink Ethernet Port” in this scenario) for the uplink connection, but any attached HaLow 
devices will use DHCP to obtain addresses on your existing network (i.e. home router) subnet. This 
means no traffic forwarding/NAT is required. This is the most appropriate mode for most use 
cases, as it makes it straightforward for anyone on your network to interact with HaLow connected 
devices. 
It will also be possible to access the web interface via your existing local network by determining 
which IP is assigned to the HaLowLink. However, the 192.168.12.1/24 network will remain 
accessible on the LAN Ethernet port. This functions as a separate management interface 
independent of the existing network which makes it simpler to reconfigure. 
Note: if you want to ensure that the AP is fully bridged exactly like a normal Access Point product see 
Frequently Asked Questions. 
1.3.3 Wi-Fi HaLow Extender 
Extenders generally receive a Wi-Fi signal and rebroadcast it. In Wi-Fi jargon, these devices are 
clients/stations rather than APs in regards to the HaLow network. 
The goal of this mode of operation is to help get another device connected to a HaLow network. That 
device might be connected to the HaLowLink via Ethernet or 2.4 GHz Wi-Fi, and then the HaLowLink 
passes that traffic via HaLow, effectively extending the range of the non-HaLow device. 
 
 
morsemicro.com  |  8

## Page 9

Refer to the online version for up-to-date content 
 
  
2 Getting Started 
2.1 Initial Connection 
Connect the provided antenna to the antenna connector first. Then connect your device to the 
HaLowLink. 
 
Figure: HaLowLink diagram 
2.1.1 Using Ethernet 
1.​ Connect your HaLowLink to power via the USB-C port using the provided power supply. 
2.​ Connect your computer to the LAN port of the HaLowLink using the provided Ethernet 
cable. 
2.1.2 Using Wi-Fi 
1.​ Connect your HaLowLink to power via the USB-C port using the provided power supply. 
2.​ Once the device is fully booted connect your computer or phone to the Wi-Fi network of the 
HaLowLink by scanning the QR-Code or using the Wi-Fi SSID/password on the label. 
2.1.3 Using USB-C 
Connect your HaLowLink to your computer directly using the USB-C cable provided. Ensure that the 
USB port on your computer can provide sufficient power. 
 
 
morsemicro.com  |  9

## Page 10

Refer to the online version for up-to-date content 
 
  
2.1.4 Connecting to an Existing Network Using Ethernet 
Optionally, if you want your downstream devices to have access to an existing network via your 
HaLowLink, connect an Ethernet cable from the WAN port of your HaLowLink to your home router 
(or any network with a DHCP server). 
2.2 Login Page 
Once you’re connected to the HaLowLink, you can then use a web browser to connect to 
https://192.168.12.1. To login, use the Device Username and Password on the label; we recommend 
letting your browser save the password. 
 
Figure: The Login page 
You should now be able to see the Home page, where initially, you will see 0 Connected Devices on 
your HaLow network. 
 
 
morsemicro.com  |  10

## Page 11

Refer to the online version for up-to-date content 
 
  
2.3 Getting the Latest Software 
In order to get the latest features, fixes and security upgrades we recommend checking for any 
updates as soon as you log in for the first time (see the Software Update section). 
2.4 Home Page 
 
Figure: The Home page 
The Home page will automatically update if changes occur in your network. To view more 
information, click on the large numbers on the card or on the 
 icon in the top right. Make sure the 
Uplink card does not show as disconnected if you want your HaLow devices to have access to an 
existing network or the internet. 
 
 
 
morsemicro.com  |  11

## Page 12

Refer to the online version for up-to-date content 
 
  
2.5 Wizard 
As described in What is a HaLowLink? When you first power on your HaLowLink it will be a Router 
with a HaLow Access Point. If you’d like to change this mode, navigate to the Wizard page using the 
sidebar menu. 
 
Figure: The Wizard page 
You should see that the option Wi-Fi HaLow devices will get an IP on this device’s local network is 
selected. This means that the device is acting as a router. 
If you would like to change this, the wizard is the simplest way. It automatically handles the many 
underlying changes needed to switch between different common device configurations. 
Note: using the wizard assumes default config as a starting point, so it will overwrite  customizations made 
outside of the wizard.  
2.5.1 Wi-Fi HaLow Modes 
The Wi-Fi HaLow Mode options in the wizard control how the Wi-Fi HaLow network operates. By 
default, the device runs as an Access Point which is sufficient for most use cases thanks to Wi-Fi 
 
 
morsemicro.com  |  12

## Page 13

Refer to the online version for up-to-date content 
 
  
HaLow’s long range. If your particular scenario requires even greater coverage or more redundancy 
you can also use the wizard to configure a mesh, either EasyMesh or 802.11s Mesh, with multiple 
HaLowLink devices. 
2.5.2 Network Modes 
The Network Mode settings define how the HaLowLink will connect to the other networks (uplinks) 
such as your home’s internet and how it will provide access to the downstream HaLow devices.  
Wi-Fi HaLow devices will get an IP on your existing router’s network (recommended) 
In this mode the HaLowLink acts as an Access Point with an Ethernet uplink via the WAN Ethernet 
Port. HaLow devices will receive IP addresses from your existing network’s DHCP server, allowing 
seamless integration with other devices on that LAN. The firewall will be effectively inactive and your 
existing router should handle security and routing. 
If possible, we recommend selecting this option on your device. This will effectively change your 
device from a Router with a HaLow Access Point to a HaLow Access Point (AP) as described in What 
is a HaLowLink?  
This option will only work, however, if you have connected your WAN port to your existing router and 
your HaLowLink has obtained an IP address. To confirm this is true, go to the Home page and make 
sure you have been assigned an IP on the Uplink card: 
 
Figure: The Uplink card, with an active Ethernet connection 
Note: if you want to ensure your device is fully bridged in this Network Mode, see Frequently Asked 
Questions. 
Use this option when you have a wired Ethernet connection to your HaLowLink WAN port and want HaLow 
devices to join your main network directly like normal devices. 
Wi-Fi HaLow devices will get an IP on this device’s local network (default) 
In this mode, the HaLowLink creates its own local subnet and DHCP service for HaLow devices. If 
connected to the WAN Ethernet port, devices may still reach the internet, but IP addresses come 
 
 
morsemicro.com  |  13

## Page 14

Refer to the online version for up-to-date content 
 
  
from the HaLowLink itself rather than the upstream router. In this mode, the firewall is active and will 
block incoming connections on the wan interface whilst forwarding traffic originating from the lan 
out through that same wan interface. 
Use this for new or standalone HaLow networks rather than extending an existing network, for isolated test 
setups, or when you want control over the IP range. 
Wi-Fi HaLow devices will get an IP on this device's local network and use 2.4 GHz Wi-Fi for an 
uplink (not an Ethernet cable) 
In this mode, the HaLowLink acts as a router with a 2.4 GHz Wi-Fi uplink instead of an Ethernet 
connection to the WAN port. HaLow devices receive IP addresses from your existing Wi-Fi router.   
In this mode, the firewall is active and will block incoming connections on the wan interface whilst 
forwarding traffic originating from the lan out through that same wan interface. Once you have 
clicked Save & Apply in the wizard you will still need to provide the Wi-Fi credentials: 
1.​ Navigate to the Home page and click the Disconnected cross on the Uplink card. 
 
Figure: The Uplink card on the Home page, in a disconnected state 
2.​ Search for your Wi-Fi network and enter your password, then save the credentials. 
 
Figure: The expanded Uplink card on the Home page, in a disconnected state 
3.​ Wait for Connected to change to yes. You should now see a tick on the Uplink card.  
Use this when Ethernet cabling to the external network is unavailable, but you still want HaLow devices to 
join your existing Wi-Fi LAN. 
 
 
morsemicro.com  |  14

## Page 15

Refer to the online version for up-to-date content 
 
  
3 HaLow Extender 
Note: you don’t need to use the web interface to switch to Extender mode — this can be done directly with 
the Mode button. 
By default, your HaLowLink comes configured as a HaLow Access Point. However, it can also be used 
as a HaLow Extender when you have more than one HaLowLink device. This will let existing Wi-Fi and 
Ethernet devices make use of HaLow’s long range. 
To switch your HaLowLink into Extender mode: 
1.​ Power on your HaLowLink and wait until the Status LED is solid (green or aqua). 
2.​ Hold down the Mode button (pictured in The HaLowLink device Figure). The Status LED will 
first start flashing slowly green, and then start flashing quickly aqua. Release the button when 
it’s flashing aqua. 
3.​ Wait until the Status LED is solid aqua to indicate it’s loaded and running in Extender mode. 
3.1 Pairing 
Pairing is designed to make connecting your HaLowLink Extender to a HaLowLink Access Point as 
simple as possible. When using this method, the Access Point automatically pushes the correct 
configurations to the Extender so you don’t need to manually repeat settings on each Extender you 
add to the network. 
For example, if you’ve used the Access Point Wizard to configure the AP as an EasyMesh Controller, 
every extender you pair will automatically be set up as an EasyMesh Agent. This eliminates the need 
to manually enter credentials or specify operating modes on each device, reducing errors and 
ensuring consistent, reliable configuration across your network. 
In Extender mode your device will not be accessible at https://192.168.12.1. Instead, you should pair 
it to an existing HaLowLink by: 
1.​ Pressing and immediately releasing the mode button on your HaLowLink Access Point (with a 
green Status LED). The Wi-Fi HaLow LED will begin slowly flashing to indicate it’s ready to 
pair. 
2.​ Pressing and immediately releasing the mode button on your HalowLink Extender (with an 
aqua Status LED). The Wi-Fi HaLow LED will begin slowly flashing to indicate it’s searching 
for an Access Point to pair with. 
3.​ Wait until the Wi-Fi HaLow LED on your HaLowLink Extender is solid purple. Your Extender 
has now stored the Wi-Fi credentials, and is ready to use! 
If pairing fails, the HaLow LEDs will begin to flash quickly for 120 seconds to indicate the retry delay, 
a security feature to prevent brute force attempts and limit radio noise. After the HaLow LEDs stop 
flashing on both the Access Point and Extender, you can attempt the pairing again, beginning from 
Step 1 above. 
 
 
morsemicro.com  |  15

## Page 16

Refer to the online version for up-to-date content 
 
  
3.2 Manual Extender Configuration (Alternative) 
We recommend using standard Pairing whenever possible. However, manual configuration of a 
HaLow network SSID/password may be required in certain cases and we have provided a special 
portal for this purpose. 
1.​ Factory reset the device and switch it into Extender Mode. 
2.​ Connect to the device using one of the methods described in Initial Connection and navigate 
to https://192.168.12.1. You should see the special HaLow Extender Configuration portal 
(pictured). 
 
Figure: HaLow Extender Configuration portal 
3.​ Fill out the form as necessary with the details of the HaLow network you intend to connect 
to. 
4.​ (Optional) Modify the name of the 2.4 GHz Access Point hosted by the Extender. 
5.​ Click Save and you should see a page telling you that the configuration is complete and that 
this portal will no longer be accessible, as the device has begun trying to connect to the 
HaLow network which you specified (pictured). 
 
 
morsemicro.com  |  16

## Page 17

Refer to the online version for up-to-date content 
 
  
 
Figure: HaLow Extender Configuration Complete page 
If the credentials are correct and the network is within range, your Extender should successfully 
connect to it and the HaLow LED will turn on. If the HaLow LED does not light up as expected, 
consider performing a factory reset and trying again. 
3.3 Using Your Extender’s Connection 
You can connect devices to your Extender via an Ethernet cable or via 2.4 GHz Wi-Fi, and this will let 
them use the Extender’s HaLow connection. For the Wi-Fi credentials, refer to the label on your 
Extender. These will not be the same as the credentials on your Access Point. 
 
 
morsemicro.com  |  17

## Page 18

Refer to the online version for up-to-date content 
 
  
4 Mesh (Advanced) 
WARNING: this is not currently supported in the EU or UK because regulatory rules require dynamic 
channel changing during operation. This is currently implemented on a per-device basis, but mesh devices in 
the same mesh must all have the same channel. 
Mesh technology allows the creation of multi-hop networks which can extend coverage and improve 
redundancy. 
To set up a mesh simply configure your Access Point mode (green Status LED) HaLowLink as an 
EasyMesh Controller or a 802.11s Mesh peer by applying the relevant HaLow Mode option in the 
Wizard. When you pair additional HaLowLinks it will automatically push the corresponding 802.11s 
Mesh Point or EasyMesh Agent configurations to the Extender being paired with. 
If you have configured your device in one of the mesh modes, avoid making significant networking 
changes in the UI as it is very easy to misconfigure. For EasyMesh specifically, some settings are 
managed automatically and are not made visible in the web interface. 
4.1 Should I Use a Mesh? 
 
 
Figure: Default Access Point topology 
 
 
Figure: Mesh topology (conceptual) 
Mesh networks allow the use of multiple HaLowLink devices to extend network coverage but are 
complex and often misunderstood and can even degrade network performance if deployed 
improperly. For most use cases, a single HaLow Access Point should provide more than enough 
coverage. 
The limitations of mesh networks are: 
●​ Each additional hop reduces the throughput by half 
●​ The number of hops are limited 
●​ There is a large amount of beaconing and control traffic overhead 
You likely do not need a mesh if: 
●​ Your existing AP + STA HaLow network already provides sufficient coverage 
 
 
morsemicro.com  |  18

## Page 19

Refer to the online version for up-to-date content 
 
  
●​ You only have two (2) HaLowLink devices 
You can use a mesh when: 
●​ You have dead zones or unreachable areas. 
●​ You need a reliable and redundant network with multiple paths more than you need speed. 
4.1.1 HaLowLink Mesh Comparison 
Feature 
EasyMesh 
802.11s Mesh 
Best For 
Smaller fixed networks which require 
greater coverage for end devices 
Larger or complex topologies requiring 
advanced routing and redundancy 
Example Use Case Expanding coverage within a single 
building or site 
Multi-building, industrial, or outdoor 
deployments needing fault tolerance 
Controller & 
Topology 
Controller-managed tree 
Distributed peer-to-peer 
Redundancy 
Partial support with STA steering 
Designed for multiple paths 
Node Mobility 
Designed for fixed devices only 
Supported 
Standards 
Wi-Fi Alliance EasyMesh Standard 
IEEE 802.11s 
Co-located HaLow 
Access Points 
HaLow STAs can connect to any AP 
node in network 
802.11s Mesh Gates can be manually 
configured with an AP 
Maximum Peer 
Nodes 
4 
10 
Maximum Hops 
2 
4 
Performance  
Lower latency single backhaul per 
tree 
Slower due to higher overhead on 
multiple peer links 
Table 1: HaLowLink mesh comparison 
 
 
morsemicro.com  |  19

## Page 20

Refer to the online version for up-to-date content 
 
  
4.2 EasyMesh 
 
Figure: Example EasyMesh diagram 
EasyMesh is a Wi-Fi Alliance Multi-AP solution for meshing together Access Points in a tree 
structure to extend coverage (but with reduced bandwidth available to clients). Configured as a 
HaLow Mode from the Wizard page, EasyMesh Controllers (green Status LED) discover, configure 
and monitor EasyMesh Agents (aqua Status LEDs), ensuring consistent SSIDs and channel 
information across the mesh.  
Agents connect upstream towards the Controller as normal clients while simultaneously serving 
downstream clients as normal Access Points themselves, allowing any HaLow device with the correct 
credentials to connect. Agents can also onboard client devices onto the mesh via Ethernet (any 
method) and the built-in 2.4 GHz AP. 
You can use the EasyMesh visualizer by clicking on the EasyMesh Controller card on the Home 
page of the Access Point Mode device (green status LED), which will display the connected nodes: 
 
Figure: The EasyMesh visualizer 
 
 
morsemicro.com  |  20

## Page 21

Refer to the online version for up-to-date content 
 
  
4.3 802.11s Mesh (beta) 
Note: 802.11s Mesh is a beta feature for experimental use, but not intended for production use yet. 
 
Figure: 802.11s Mesh diagram 
802.11s Mesh is an IEEE Wi-Fi mesh which forms a truly distributed peer-to-peer multi hop Mesh 
Basic Service Set (MBSS). Configured as a HaLow Mode via the Wizard page, 802.11s Mesh 
networks aim to increase coverage, redundancy and range by establishing self-healing links between 
neighboring 802.11s Mesh nodes in the topology. Only mesh capable devices can join or make use of 
the functionality provided by the MBSS. 
802.11s Mesh HaLowLink networks can be accessed via the Ethernet (any port) or the 2.4 GHz 
Wi-Fi AP on the devices. Units with a green Status LED also run a co-located HaLow Access Point 
which can allow the mesh to be bridged to external HaLow networks. 
You can use the 802.11s Mesh visualizer by clicking on the 802.11s Mesh Topology card on the 
Home page of any 802.11s mesh devices, which will display the topology as seen by that node. 
 
Figure: 802.11s Mesh visualizer 
 
 
morsemicro.com  |  21

## Page 22

Refer to the online version for up-to-date content 
 
  
4.4 Pairing Extenders to a Mesh 
As mentioned in the introduction, if you pair a HaLowLink Extender to a Mesh-enabled ‘green’ 
HaLowLink it will automatically become part of the mesh. That is, it will not be just a client, but either 
a Mesh Point or an EasyMesh Agent. 
If you instead want to configure an Extender as a normal station/client device instead of a mesh peer, 
then you should do so via the Manual Extender Configuration (Alternative). The other implication of 
this is that a manually configured device will not automatically become part of the mesh. That is: 
●​ Pair Extender (aqua) via push button -> becomes part of mesh 
●​ Enter manual credentials on Extender via web interface -> normal client Extender mode 
 
There are also some aspects to the default mesh configurations that may not be intuitive, as the role 
of the device changes. 
4.4.1 EasyMesh 
Once a device is configured as an Agent, the role of the mode button is now to onboard new devices 
to the mesh. This means that you can easily add more devices to your mesh from any of the already 
configured devices, but if you want to reconfigure your Extender entirely you should reset it before 
repairing. Also, the SSID of the original ‘green’ HaLowLink is propagated to all devices in the Mesh 
both for the 2.4 WiFi and the HaLow WiFi, such that the QRCode on your Extenders will no longer 
work to connect to the device but you will have a consistent SSID. 
4.4.2 11s Mesh 
Unlike EasyMesh, any Extender will NOT have an additional HaLow Access Point, as the HaLow 
interface will be exclusively used for the Mesh. The 2.4GHz  Access Point on the Extender is 
unmodified, so that all Extenders will have a distinct SSID and key (by default the one encoded on the 
QRCode). In this mode, Extenders will not support any further pairing actions, and so must be reset 
to be repaired. 
 
If you want to connect HaLow client devices that do not support 11s Mesh  to 11s Mesh Extenders, 
you can manually add a HaLow Access Point via the Quick Config interface. This will also re-enable 
the pairing function of the mode button, allowing you (as with EasyMesh) to onboard additional 
Extenders via this existing Extender. You will still need to reset the device if you want to repair the 
existing Extender. 
 
 
 
morsemicro.com  |  22

## Page 23

Refer to the online version for up-to-date content 
 
  
5 Restoring Factory Settings 
A factory reset is useful if you: 
●​ Don’t want to use your HaLowLink as an Extender anymore. 
●​ No longer have access to your device via the network after making configuration changes. 
●​ Want to start fresh by configuring your HaLowLink for a new purpose 
A factory reset always returns to Access Point mode (green Status LED), which is the default. To 
perform a factory reset: 
1.​ Power on your HaLowLink and wait until the Status LED is either solid green or solid aqua. 
2.​ Hold down the Mode button until the Status LED begins flashing slowly green, then release 
it. 
3.​ Wait until the device resets and the status LED changes to solid green, indicating that it is 
running in Access Point mode. 
4.​ You can now access your device at https://192.168.12.1 again, as described in Initial 
Connection. 
Warning: in Step 2, if you continue holding down the button until the status LED is flashing quickly aqua, the 
device will reset into Extender mode instead. (see the Extender section). 
 
 
morsemicro.com  |  23

## Page 24

Refer to the online version for up-to-date content 
 
  
6 Use Cases 
These are some common use cases for the HaLowLink with some pointers on how to set them up. If 
you have previously configured your HaLowLink in some way, you may want to Restore Factory 
Settings before following these instructions. 
6.1 Adding a HaLow Access Point to Your Existing 
Network via Ethernet 
 
Figure: Adding a HaLow Access Point to Your Existing Network via Ethernet use case diagram 
The primary use case for a HaLowLink is to add HaLow support to your existing network, 
allowing any HaLow-enabled client to work in the same way as any other Wi-Fi client. 
1.​ Make sure your HaLowLink is in Access Point mode (green Status LED). 
2.​ Connect the WAN port of your HaLowLink to your network; in the home, this usually means 
placing it next to your router and connecting the WAN port to a LAN port. 
3.​ HaLow devices can then connect via the SSID/password printed on the sticker. 
Although it will work as is for many use cases, for the best experience we recommend using the 
Wizard to set  Wi-Fi HaLow devices will get an IP on your existing router’s network, which will 
change it from a Router with HaLow Access Point to a HaLow Access Point. 
 
 
morsemicro.com  |  24

## Page 25

Refer to the online version for up-to-date content 
 
  
6.2 Adding a HaLow Access Point to a Network via 2.4 
GHz Wi-Fi 
 
Figure: Adding a HaLow Access Point to a Network via 2.4 GHz Wi-Fi use case diagram 
If it’s not possible to connect your HaLowLink via Ethernet, you can connect your HaLowLink via 2.4 
GHz Wi-Fi. You should only do this if Ethernet is not possible, as it will require your HaLowLink to act 
as a router, forwarding traffic from 192.168.12.x over the Wi-Fi link. 
1.​ Make sure your HaLowLink is in Access Point mode (green Status LED). See Restoring 
Factory Settings if it’s not. 
2.​ Go to the Wizard in at https://192.168.12.1 and set the Network Mode to Wi-Fi HaLow 
devices will get an IP on this device's local network and use 2.4 GHz Wi-Fi for an uplink 
(not an Ethernet cable), then go to the Home page to configure your credentials. For more 
details, see the Network Modes section above. 
3.​ HaLow devices can then connect via the SSID/password printed on the sticker. 
This may be particularly useful on networks you don’t have administrator access to, and in fact the 
HaLowLink can act as a travel router in this situation, providing your own private network not just 
HaLow Access Point but also a 2.4 GHz Wi-FI access point and Ethernet connectivity. 
 
 
 
morsemicro.com  |  25

## Page 26

Refer to the online version for up-to-date content 
 
  
6.3 Using HaLow to Extend an Existing Network - Virtual 
Wire 
 
Figure: Virtual Wire use case diagram 
This will require two (2) HaLowLink devices, and will make a HaLow link a transparent part of your 
network, functioning just like an Ethernet cable. 
First, you should add a HaLow Access Point to your network (see 1 or 2 above). Once your network 
supports HaLow, you should follow the instructions in the Extender section above. In summary: 
1.​ Make sure your HaLowLink is in Extender mode (aqua Status LED). 
2.​ Pair your Extender with your Access Point by pressing and releasing the mode button on your 
Access Point, then pressing and releasing the mode button on the Extender. The HaLow LED 
will slowly flash, usually for around 10 seconds, before turning a solid purple on the Extender 
to show it’s connected. 
3.​ Now any device connected to the Extender - via USB, 2.4 GHz Wi-Fi, or Ethernet - will make 
use of the HaLow link to connect to your network. See (4), (5) and (6) below for more 
instructions. 
 
 
 
morsemicro.com  |  26

## Page 27

Refer to the online version for up-to-date content 
 
  
6.4 Connect Your Computer to a HaLow Network via 
USB-C 
 
Figure: Connect Your Computer to a HaLow Network via USB-C use case diagram 
Follow the instructions above in (3) to set up an Extender, then: 
1.​ Connect your computer via the provided USB-C cable to your Extender (aqua status LED). 
2.​ A new Ethernet adapter should appear on your computer. Make sure it’s configured as a 
DHCP Client. 
3.​ You can now send traffic via the HaLow link. Note that because it’s an Ethernet connection, by 
default your computer will likely use it in preference to any existing Wireless connection. See 
the Troubleshooting section for more information. 
6.5 Connect an Ethernet Device to a HaLow Network 
 
Figure: Connect an Ethernet Device to a HaLow Network use case diagram 
Follow the instructions above in (3) to set up an Extender, then: 
1.​ Connect your device via an Ethernet cable to your Extender (aqua status LED). 
2.​ Your device should now acquire an address via DHCP. 
 
 
morsemicro.com  |  27

## Page 28

Refer to the online version for up-to-date content 
 
  
6.6 Connect a Non-HaLow Wi-Fi Device to a HaLow 
Network 
 
Figure: Connect a Non-HaLow Wi-Fi Device to a HaLow Network use case diagram 
This could be a computer, tablet, phone, or any IoT device. Follow the instructions above in (3) to set 
up an Extender, then: 
1.​ Set the SSID/password of the Extender (NOT the Access Point) via scanning the QR Code on 
the bottom of the Extender or copying the credentials from the same sticker. 
2.​ Your device should now acquire an address via DHCP. 
 
 
 
morsemicro.com  |  28

## Page 29

Refer to the online version for up-to-date content 
 
  
6.7 Experimenting with HaLow 
 
Figure: Experimenting with HaLow use case diagram 
If you’re currently just experimenting with HaLow’s amazing range and penetration, the easiest way 
to test this out with a HaLowLink is to have two devices and two laptops, where the laptops provide 
power to the HaLowLink. This allows you to easily move around. 
1.​ Connect one laptop via USB-C to your Router with HaLowLink Access Point (i.e. the factory 
default configuration), and go to https://192.168.12.1 (as described in Getting Started). 
2.​ Connect another laptop to an Extender via USB-C, then set up the Extender as described in 
(3). 
3.​ You should see the Extender appear on the Home page of the Access Point in the Connected 
Devices, and the Local Network card should show the IPs of both the Extender and your 
other laptop. 
 
Figure: The expanded Local Network card on the Home page 
4.​ You can now test out the connection from one laptop to the other via HaLow. For more 
information about how to do this, see Exploring HaLow Connectivity in the next section. 
Note: because the USB link is via Ethernet, by default your computer will likely use this in preference to any 
existing Wireless connection. See the Troubleshooting section for more information. If you’re familiar with 
OpenWrt, you can stop this happening by configuring the DHCP server to return nothing for Option 3 
(gateway). 
 
 
morsemicro.com  |  29

## Page 30

Refer to the online version for up-to-date content 
 
  
7 Quick Config 
For most users the Wizard page will be sufficient to configure a HaLow Access Point (green mode), 
and an Extender (aqua mode) can be configured via the Mode button as described above. However, if 
you want to make simple minor changes to your configuration - such as changing your Wi-Fi 
password or encryption method, or setting a Static IP - you can do so via the Quick Config page. To 
help you understand the changes you’re making, these will be reflected in the diagram at the top of 
the page as you make them. 
Warning: it is easy to change the configuration of your device here in a way that causes you to lose access to 
it, particularly if you’re changing network interfaces. If this happens, see the section above on Restoring 
Factory Settings.  
7.1 Network Interfaces 
 
Figure: The Network Interfaces subsection on the Quick Config page. 
This section lists the logical interfaces available on your router, each of which can be configured with 
either a Static IP (and potentially a DHCP Server) or as a DHCP Client. If you have multiple Ethernet 
ports or Wireless interfaces on the same network, a bridge will automatically be created. Note that to 
attach new Wireless interfaces to the network, you will need to use the Wireless section. 
 
 
morsemicro.com  |  30

## Page 31

Refer to the online version for up-to-date content 
 
  
7.2 Wireless 
 
Figure: The Wireless subsection on the Quick Config page. 
This will allow you to configure the Wi-Fi interfaces on your HaLowLink. Note that it is possible to 
create multiple interfaces for a particular radio. 
7.3 Advanced Usage 
The Quick Config page is designed to correspond to the underlying text based configuration and 
connect with the pages accessible via Advanced Config. If you have Advanced Config enabled, you 
can use the cog icons on the Quick Config to access these pages, which will allow you more flexibility 
in your setup. It will also allow you to simply Save rather than Save & Apply, which will let you view 
and apply or revert the proposed changes by clicking on the Unsaved Changes indicator at the top 
right. 
For more about the underlying configuration format (known as UCI), see Configuring with the 
Command Line. 
 
 
morsemicro.com  |  31

## Page 32

Refer to the online version for up-to-date content 
 
  
8 Advanced Config 
The software running on your HaLowLink is based on OpenWrt, a Linux operating system targeting 
network connected devices. While the Wizard page provides basic preset configuration options, the 
Advanced Config section, accessible via the side menu, enables more advanced customizations. In the 
Advanced Config section (pictured below) the Quick Config page allows convenient access to 
frequently modified settings, whereas the other sub-menus within Advanced Config provide more 
granular and specific access to advanced functionalities. 
 
Figure: The Advanced Config menu. 
This will allow you to view detailed information about your device, change low-level configuration, 
install additional software if you have an internet connection (via the Software page under the 
System sub-menu), and even access the Linux terminal from the Terminal page. 
You can also directly connect to your device via ssh (must be enabled first) using the same username 
and password you used to login. This is printed on the label. 
For more information about OpenWrt, see openwrt.org/start. 
 
 
 
morsemicro.com  |  32

## Page 33

Refer to the online version for up-to-date content 
 
  
9 Exploring HaLow Connectivity 
Your HaLowLink comes packed with useful utilities and pages to make the most of your HaLow 
connection. In particular, we recommend the following pages, which are only accessible once 
Advanced Config has been enabled. 
9.1 Status 
9.1.1 Channel Analysis 
This will allow you to see the channels and signal strength of any other nearby HaLow networks. If 
there are many local HaLow networks, you may want to change the channel via the Quick Config 
page to avoid interference. 
9.1.2 Realtime Graphs 
This will show you a continuously updating graphical view of the link quality (see Wireless) as well as 
other critical system metrics while you have the page open. 
9.2 Network 
9.2.1 Diagnostics 
This allows you simple access to command line tools to evaluate your network, including iperf3 (to 
test bandwidth), ping and traceroute to explore connectivity, and arp-scan to discover all 
devices on the network. It also will show you the command it’s executing, as you may also want to do 
this via the command line (see Terminal). 
9.3 Statistics 
9.3.1 Graphs 
Your HaLowLink is running collectd to continuously monitor the behavior of the device. Some of 
the information here is similar to Realtime Graphs, but it’s updated at a lower frequency and stored 
while the device is running rather than just while you’re on the page. It’s also possible to configure 
other devices to point to this (e.g. Extenders) to aggregate all your statistics in a single place. 
 
 
morsemicro.com  |  33

## Page 34

Refer to the online version for up-to-date content 
 
  
9.4 Services 
9.4.1 Terminal 
For easy access to the Linux console, you can start a terminal on the device by going to Terminal. Note 
that you will have to re-enter your device password (refer to the sticker on the bottom of your 
HaLowLink). 
Note: The in-browser terminal does not work over HTTPS. To use it, follow the browser’s warning link to 
disable this security feature. 
From the command prompt, you will have access to the standard Linux utilities included in OpenWrt 
and those already mentioned via the Diagnostics page, as well as some other useful programs such 
as:  
Utility 
Purpose 
morse_cli 
Low level access to information from and settings on the Morse Micro 
HaLow chip. 
wavemon 
Terminal graphical program to monitor Wi-Fi signal strength and 
performance. 
nano 
Text editor, including syntax highlighting of UCI files. You may also use vi. 
tmux 
Terminal multiplexer, allowing persistent sessions and windows. 
Table 2: Useful Command Line Interface tools 
9.4.2 Range Test 
 
Figure: Range Test device setup 
The Range Test application is designed as a simple way to analyse HaLow network performance by 
automating iperf3 tests and collecting real-time statistics. It is a useful tool for quickly assessing 
signal strength, data throughput, and connection quality across different environments. 
Note: ensure that all devices under test are running the same version of Morse Micro OpenWrt. 
 
 
morsemicro.com  |  34

## Page 35

Refer to the online version for up-to-date content 
 
  
 
Figure: Range Test setup 
To use the range testing tool: 
1.​ Connect the devices being tested on the same HaLow network of any type outlined in this 
guide (Default AP/STA configurations are the most reliable). 
2.​ Set up the devices in the desired locations and select a local device to connect a laptop to. 
3.​ Select the IPv4 address from the Remote Device dropdown. If it does not appear on first 
load, click the 🔍icon to run another discovery. If this fails to find another device, you may 
enter a known IPv4 address into the custom field pictured.  
 
Figure: The Range Test setup Remote Device dropdown 
4.​ Fill in the Password field using the remote device password (not the Wi-Fi password). 
5.​ (Optional) Provide user notes about the test in the Description field. 
6.​ (Optional) If you want to log the coordinates of the local and remote devices and have the 
range calculated automatically enter the decimal degree values into the local and remote 
device coordinates fields respectively. Right-click a location in Google Maps to copy its 
coordinates to your clipboard in the correct format. 
 
 
morsemicro.com  |  35

## Page 36

Refer to the online version for up-to-date content 
 
  
7.​ Click Start Test and a progress bar will appear showing the status of the current test. This 
can be cancelled at any time by clicking the Stop button. 
After the test completes, a row in the Results Summary subsection should appear, as pictured below. 
This result can be deleted by clicking the trash icon, or a JSON file containing all the raw data can be 
downloaded via the Download button, which is intended to help engineers with remote debugging. 
The Download Results Summary (CSV) button yields a CSV file of all the data represented in the 
results summary. 
 
Figure: The Range Test results 
Note: test results are volatile to avoid overwhelming limited memory resources and will be deleted if power is 
removed or the device is rebooted. 
Warning: if the throughput numbers are returning ~40 Mbps for UDP and 900+ Mbps for TCP then the test 
is likely defaulting to run over an Ethernet connection. This should be avoided. 
By clicking the cog icon in the top left corner of the Test Configuration subsection, the data 
directions, test length and protocols which will be tested can be modified.  
The remote device will always act as the iperf3 server and use the same command: 
iperf3 -s -1 --json 
The local device will always act as the iperf3 client, running a command in the following format: 
iperf3 -c <ip> <protocol> <direction> -t <time> -O <omit> --json 
●​ Protocol: For UDP tests the protocol arguments become -u -b 40M/30 whereas for TCP 
tests only -Z is set.  
●​ Direction: For Send tests no arguments are set whilst Receive tests set the -R flag. 
●​ Time & Omit: If Quick Tests are selected in the Advanced Configuration dialog, these 
arguments will become -t 10 -O 2. By default the tests will run for longer with -t 70 
-O 10 to allow 10 seconds for rate control to settle and get 60 seconds worth of usable 
data. 
 
 
morsemicro.com  |  36

## Page 37

Refer to the online version for up-to-date content 
 
  
10 Configuring With the Command Line 
The HaLowLink is an open device running Linux, and it is straightforward to gain direct access via 
either SSH (must be enabled first) or the Terminal page (accessible after enabling Advanced Config). 
Because it’s based on OpenWrt, the primary mechanism of configuration is via UCI 
(openwrt.org/docs/guide-user/base-system/uci), which is fundamentally just a collection of files in 
/etc/config in a particular format. 
10.1 Making Changes 
This happens in 2 steps: 
1.​ Set new values in UCI 
2.​ reload_config to reload services 
You can make changes to UCI via the uci command or by editing the files in /etc/config. For 
example:  
nano /etc/config/wireless 
Or: 
uci show wireless 
uci set wireless.default_radio0.mode=sta 
uci commit 
Doing a uci commit will cause the change to appear in /etc/config/wireless. Once you've 
made changes (via either of those methods), to make them take effect use reload_config. Other 
files/services that are likely to be useful for network config are dhcp, network and firewall. 
Aside from the UCI documentation mentioned above, the most useful resource is clicking Save rather 
than Save & Apply in the UI, which is possible if you’ve enabled Advanced Config in the menu. This 
will allow you to go up the top right (Unsaved Changes) and view a sequence of uci set commands 
corresponding to the change you just made. For example, after setting a static IP: 
 
 
morsemicro.com  |  37

## Page 38

Refer to the online version for up-to-date content 
 
  
 
Figure: The Unsaved Changes dialog showing the incoming UCI modifications after setting a static IP 
10.2 File/Service Structure 
wireless contains the radio devices (wifi-device) and the interfaces connected to that (e.g. 
wlan0, wlan1 - caused by a wifi-iface). Any wifi-iface has a network, which refers to an 
interface in the network UCI file. This corresponds to the Wireless section on the Quick Config 
page. 
network contains a mix of switches/bridges and logical interfaces; an interface in a network 
may point to a bridge, in which case multiple Ethernet ports or wifi-ifaces might be attached to 
it. Confusingly, the wireless interfaces are not directly mentioned here, only in the wireless file. This 
means it’s possible to incorrectly configure a network interface by not having a bridge and having 
multiple wifi-ifaces refer to it. This corresponds to the Network Interfaces section on the Quick 
Config page. 
firewall controls nftables - i.e. forwarding/masquerading as well as simple accept/reject. 
Firewalls have another level of indirection - zones - such that you can potentially put multiple 
network interfaces in one zone. 
dhcp controls dnsmasq - i.e. DHCP and DNS. The usual setup is that there’s always dnsmasq 
running, but if you don’t want DHCP active on particular interfaces you set them to ignore. 
10.3 Debugging 
If you’ve made a change and it’s not working the way you expect this command is useful for following 
the logs as they are generated: 
 
 
morsemicro.com  |  38

## Page 39

Refer to the online version for up-to-date content 
 
  
logread -l 100 -f 
This is the primary mechanism OpenWrt of reporting that something went wrong, since you won’t 
see it running reload_config. 
Note that if you’ve manually edited the files rather than using uci set it’s possible you’ve made them 
invalid. Use uci show to confirm that the UCI library can still parse them. 
10.4 Applying Configurations 
As noted above, we recommend using reload_config to apply configurations. What this does is: 
●​ check to see if any of the config files have changed 
●​ trigger a reload on any services affected by these changes (i.e. not a restart) 
There are other ways to do this. 
●​ explicitly reloading a single service: service <service> reload 
●​ explicitly restarting a single service: service <service> restart 
●​ bringing down only the wifi interfaces and back up without restarting the network: wifi 
down && wifi up. 
Note: manually triggering a reload will pick up uncommitted changes. 
 
 
morsemicro.com  |  39

## Page 40

Refer to the online version for up-to-date content 
 
  
11 Software Updates 
To update your software, use your browser to access the web interface (usually at 
https://192.168.12.1) as described in Initial Connection. Then select Advanced Config, and you 
should see the Upgrade page: 
 
Figure: The Upgrade page 
●​ The Check for automatic upgrade button will attempt to obtain the new version of firmware 
from the Morse Micro servers. This requires an available internet connection — either 
through the browser you are using to access the HaLowLink GUI or through the HaLowLink 
device itself via an uplink or otherwise (see Network Modes). 
●​ The Manually upload firmware file button will let you upload any compatible firmware. 
Note: if your HaLowLink device has internet access, update notifications will appear automatically on the 
Home page within the Version card. 
 
 
 
morsemicro.com  |  40

## Page 41

Refer to the online version for up-to-date content 
 
  
12 Device Features 
12.1 LED Indicators 
 
Figure: The LED indicators on the front of a HaLowLink device 
12.1.1 Status LED 
Color & Behavior 
Meaning 
Yellow flashing 
Factory reset in progress. 
Yellow solid 
Bootloader running. 
Green flashing 
OpenWrt booting into Access Point mode. 
Green solid 
OpenWrt is loaded and running in Access Point mode. 
Aqua flashing 
OpenWrt is booting into Extender mode. 
Aqua solid 
OpenWrt is loaded and running in Extender mode. 
Blue flashing 
OpenWrt is executing a software update (do not disconnect power when 
this is happening). 
Table 3: Status LED explanations 
 
 
morsemicro.com  |  41

## Page 42

Refer to the online version for up-to-date content 
 
  
12.1.2 Wi-Fi HaLow LED 
Color & Behavior 
Meaning 
None 
If your device is in Access Point mode this means that HaLow is 
currently disabled.  
If your device is in Extender mode this means that your device is not 
associated via HaLow. 
Purple solid 
If your device is in Access Point mode this means that HaLow is 
currently enabled.  
If your device is in Extender mode this means that your device is 
currently associated via HaLow. 
Purple flickering 
On both the Access Point and Extender, the Wi-Fi HaLow LED flickers 
to show HaLow traffic activity. The busier the link, the faster the LED 
will flicker. 
Purple slow flashing 
Pairing is in progress. 
Table 4: Wi-Fi HaLow LED explanations 
 
12.1.3 Wi-Fi 2.4 GHz LED 
Color & Behavior 
Meaning 
Off 
Either the power is off or the 2.4 GHz Access Point is not active. It can 
be re-enabled via the management interface or restored via a Factory 
Reset. 
Green solid 
The 2.4 GHz Access Point on the HaLowLink is currently active and 
available for devices to discover and connect to. 
Green flickering 
On both the Access Point and Extender, the Wi-Fi 2.4 GHz LED flickers 
to show 2.4 GHz traffic activity. The busier the link, the faster the LED 
will flicker. 
Table 5: Wi-Fi 2.4 GHz LED explanations 
 
 
morsemicro.com  |  42

## Page 43

Refer to the online version for up-to-date content 
 
  
12.2 Ethernet/USB Ports 
 
Figure: The ports at the rear of a HaLowLink device 
12.2.1 Access Point Mode (Green Status LED) 
Regardless of whether the HaLowLink is configured as a Router or just an Access Point, these roles 
are correct. That is, USB-C and LAN will always be on a separate network to WAN, and the WAN port 
should be connected to your router. 
Port 
Role 
USB-C 
Either power only, or connect a computer to get a 192.168.12.x IP and access the 
management interface at https://192.168.12.1. 
LAN 
Connect a computer to get a 192.168.12.x IP and access the management 
interface at https://192.168.12.1. 
WAN 
Connect this to your existing network/router. 
Table 6: Access Point Mode port descriptions 
12.2.2 Extender Mode (Aqua Status LED) 
Port 
Role 
USB-C 
Either power only, or connect a computer to use the Extender’s HaLow 
connection. 
LAN 
Connect a computer to use the Extender’s HaLow connection. 
WAN 
Connect a computer to use the Extender’s HaLow connection. 
Table 7: Extender Mode port descriptions 
 
 
morsemicro.com  |  43

## Page 44

Refer to the online version for up-to-date content 
 
  
13 Frequently Asked Questions 
How can I make my HaLowLink Access Point behave exactly like a standard access point 
(fully bridged)? 
If you have used the Wizard to change your Network Mode to the recommended Wi-Fi HaLow 
devices will get an IP on your existing router's network setting you will have effectively setup a 
normal bridged Access Point — except for the lan management subnet which still hosts the GUI at 
https://192.168.12.1. This management network is maintained for ease of reconfiguration, but can 
be removed. 
If you want your HaLowLink Access Point to behave exactly like a consumer Access Point product 
(fully bridged), go to the Quick Config page and move all the devices and ports (LAN/2.4/USB) from 
the lan network onto the wlan network using the Network Interfaces section. This will allow you to 
connect devices to your normal network via the LAN Ethernet port, the 2.4 GHz Wi-Fi AP and even 
the USB-C port but will remove access to the separate lan management subnet. 
Ideally, you should do this from the address assigned from your upstream network (i.e. not 
192.168.12.1) to avoid losing access to the device. If you do use 192.168.12.1 you should use the 
Apply Unchecked option, as otherwise the changes will automatically revert unless you quickly 
access the UI via the other address in the same browser. 
How can I test mesh? (EasyMesh or 802.11s Mesh) 
There are two recommended ways to observe mesh operation using three (3) HaLowLink devices: 
1.​ Confirm relaying through an intermediate node: Move Device 1 and Device 2 far enough 
apart that they can no longer communicate directly before introducing Device 3 as a mesh 
peer. Successful communication between Device 1 and Device 2 in this state indicates that 
traffic is being relayed via Device 3. 
2.​ Demonstrate throughput improvement: Similar to the above method, increase the distance 
between Device 1 and Device 2 until their throughput decreases significantly, then introduce 
Device 3 as mesh peer. An improvement in throughput confirms that the mesh path has been 
established. 
How can I test 802.11s Mesh Self-Healing when my HaLowLink nodes are too close 
together? 
If you are unable to separate your HaLowLink 802.11s mesh devices sufficiently to observe the 
self-healing behaviour, this is expected. Wi-Fi HaLow’s primary strength is its range! 
To simulate greater distance between your HaLowLink 802.11s Mesh peers for testing purposes you 
can adjust the RSSI threshold for joining which prevents nodes from forming mesh links when the 
received signal strength is too weak. 
1.​ Setup your 802.11s Mesh  
 
 
morsemicro.com  |  44

## Page 45

Refer to the online version for up-to-date content 
 
  
2.​ In the Advanced Config menu, navigate to the Wireless page under the Network sub-menu. 
3.​ Click Edit on the Mesh Point (pictured below) 
 
Figure: The Wireless page 
4.​ Navigate to the Mesh Settings tab under the Interface Configuration sub-section. 
5.​ Update the RSSI threshold for joining field (pictured) to define an appropriate minimum 
signal strength (RSSI) a node must detect to establish a peer link in the mesh. 
 
Figure: The advanced mesh settings 
6.​ Click Save on the dialog and then Save & Apply on the Wireless page to apply these changes. 
How can I limit or increase the number of peers allowed in my 802.11s Mesh? 
Follow the exact same steps from the previous question up to Step 3 (pictured). From there you can 
adjust the Maximum number of mesh peers. If you set this value to 2, it will force the mesh to form a 
linear chain topology, which is likely not useful. 
 
 
morsemicro.com  |  45

## Page 46

Refer to the online version for up-to-date content 
 
  
I changed the mode of an interface on the Quick Config page, and it's refusing to save or 
not working as expected. 
Note: before attempting any significant interface modifications on the Quick Config page, you should check 
that none of the Wizard configurations do not already meet your needs. 
 
Figure: An example of the common WDS error message on the Quick Config page 
This usually happens when trying to attach a non-WDS (Wireless Distribution System / 4-address 
mode) interface to a WDS bridge (e.g. adding a 2.4 GHz Wi-Fi Client to a HaLowLink Access Point).  
For technical reasons, only one non-WDS interface (3-address mode) can exist on a bridge interface 
at a time. Any attempt to change this will cause errors to pop up on the Quick Config page when 
saving changes. 
To provide more context to this error we can expand upon the recommended actions described in the 
example error message: 
1. Remove the non-WDS Wi-Fi client: The error message describes the offending non-WDS Wi-Fi 
client which can be removed. In the example error message it specifies that the client on the wan 
network with the SSID “YourWifiNetwork” is causing problems (also pictured below). If this was just 
added/modified, we can reset the changes using the Reset button in the bottom right corner. 
 
Figure: The common WDS error message on the Quick Config page 
 
 
morsemicro.com  |  46

## Page 47

Refer to the online version for up-to-date content 
 
  
If the non-WDS client already existed before making the changes which caused the error message, 
you can simply delete the non-WDS client using the trash button (pictured above, not 
recommended) or move it to a new network where it is the only device. To create a new network 
interface, go to the Network Interfaces subsection on the same page and enter a new network 
interface name before clicking the Add button (pictured below): 
 
Figure: Creating a new network interface using the Quick Config page 
You should also click the Add Zone button to create a new permissive firewall zone. The created 
network interface will be an empty WDS bridge which will allow the attachment of a singular 
non-WDS Wi-Fi client interface. You can now safely remove the offending non-WDS Wi-Fi client 
onto this new interface without deleting it. For example, see the non-WDS “YourWifiNetwork” 2.4 
GHz Wi-Fi client moved to the newly created “24lan” network interface below. 
 
Figure: Assigning the non-WDS Wi-Fi as the only device on a new Network Interface 
 
 
morsemicro.com  |  47

## Page 48

Refer to the online version for up-to-date content 
 
  
 
2. Enable WDS for the Wi-Fi clients (if possible): From the Wireless subsection you should be able 
to select Client (WDS) as a Mode for your HaLow Wi-Fi client devices only. 
3. Remove the all other devices from this network to leave a single non-WDS Wi-Fi client: This 
option is simply the inverse of Remove the non-WDS Wi-Fi client and involves: 
●​ De-selecting the Ethernet ports from the relevant dropdown in the Network Interfaces 
subsection. You may also want to select them on another network interface row to keep them 
in use. 
●​ Moving the Wireless devices onto other network interfaces via the Wireless subsection. You 
can also delete them altogether if you want. 
 
 
 
morsemicro.com  |  48

## Page 49

Refer to the online version for up-to-date content 
 
  
14 Troubleshooting 
If you’re having trouble with your HaLowLink, we recommend resetting Restoring Factory Settings. 
You can also reach out on the Morse Micro Community Forum to share your issue and get help from 
our experts and other users. 
Problem 
Solution 
The Status LED is not 
Illuminated. 
There is a problem with power to the device. Check that the 
USB-C port on the HaLowLink is connected to the provided 
power supply or to a USB-C port on a computer. Do not use a 
USB-A to USB-C adapter. 
The Status LED is still yellow 
after some time, or never stops 
flashing green after boot. 
The flash partition is probably corrupt. To recover your 
HaLowLink, see Recovering from failed updates below. 
I can’t access the HaLowLink at 
https://192.168.12.1. 
If the status light is solid green and you can’t access your 
HaLowLink at https://192.168.12.1: 
●​ Make sure your computer is connected to either the LAN 
or USB port of the HaLowLink. 
●​ Check that your network connection is configured as a 
DHCP client, and has been allocated a 192.168.12.x IP. 
●​ If you’re failing to establish a network connection to your 
device, see Restoring factory settings. 
If the status light is solid aqua, your HaLowLink is in Extender 
mode and will only be useful if connected to an Access Point. 
Simply connect other devices to it via Ethernet or 2.4 GHz Wi-Fi 
to use your HaLow-enabled network. You should not need to 
access its Web UI, but you may find its address  in the DHCP 
lease table of your DHCP server. 
I changed a configuration 
setting and now I can’t access 
my HaLowLink, but I don’t want 
to reset it. 
If you need to access your HaLowLink as part of troubleshooting 
a complex configuration change, you can connect your computer 
to the LAN or WAN port and configure it with the following 
settings: 
●​ IP: 10.22.121.110 
●​ Netmask: 255.255.255.254 (if you can’t set 
255.255.255.254 due to OS limitations, use 
255.255.255.0) 
As long as your HaLowLink has a solid green or aqua light, it will 
be available at 10.22.121.111 (this is a secondary static IP 
 
 
morsemicro.com  |  49

## Page 50

Refer to the online version for up-to-date content 
 
  
Problem 
Solution 
assigned for diagnostic purposes). 
I can see that the Access Point 
card has connected devices, but 
the Local Network card doesn’t 
list them. 
If you have configured your device as an Access Point only (i.e. the 
wizard option Wi-Fi HaLow devices will get an IP on your 
existing router’s network), then these devices will appear in the 
DHCP lease table of the existing DHCP server on your network. 
The Local Network on the HaLowLink is being used primarily for 
easy access to the configuration, and will not have HaLow devices 
in it. 
Alternatively, if you have temporarily lost power to HaLowLink 
Access Point your devices may not yet have refreshed their 
DHCP leases. They will eventually renew their leases when their 
lease time expires. 
When I connect my computer to 
my HaLowLink Extender 
directly over Ethernet, my 
internet gets slower. 
Because your computer has a wired connection to the 
HaLowLink, most operating systems will prefer this connection 
over any wireless connection. However, if you’re using a 
HaLowLink Extender, this means you will be restricted to the 
maximum bandwidth over the HaLow link.  
For your particular operating system, you should determine how 
to prefer your existing Wi-FI connection (e.g. via setting the 
HaLowLink connection to local only, removing the default route 
from the HaLowLink, or changing the route priorities). 
When I connect my computer to 
my HaLowLink directly over 
Ethernet, my internet stops 
working. 
This is the same problem as above, where your computer will 
prefer the HaLowLink connection over any wireless connection, 
but in this case it’s probably your HaLowLink is not yet connected 
to the internet. For an Access Point, check the Uplink card on the 
homepage (which will report the WAN and 2.4 GHz state), and 
for an Extender check it has a purple light AND that the Access 
Point is correctly configured. 
I changed the HaLow Mode or 
Network Mode of my 
HaLowLink, and my Extenders 
no longer work. 
If you make significant changes to your Access Point 
configuration, any attached Extenders might not continue to 
function as you expect. If you’ve just changed the Network 
Mode, we recommend power cycling your Extender to force it to 
reinitialize. If you’ve changed the HaLow Mode, you should 
follow the instructions in the Extender section to reset your 
device to Extender mode and redo the pairing procedure. 
 
 
morsemicro.com  |  50

## Page 51

Refer to the online version for up-to-date content 
 
  
Problem 
Solution 
My connection isn’t performing 
as I expect. 
Check signal strengths on the Access Point by going to the Home 
page and clicking on the Connected Devices card. 
For more detailed information about the signal you can navigate 
to the Realtime Graphs page. 
To check if there are other HaLow networks interfering with your 
link, you can check the Channel Analysis page. 
To run iperf3 or ping tests you can also use the Diagnostics page. 
My Extender’s HaLow Status 
LED is flashing quickly all the 
time even when I’m not using it. 
Because the wireless and wired connection are bridged on the 
Extender, make sure you haven’t created a network loop by 
connecting a LAN/WAN port of your Extender to the same 
network as your Access Point. To solve this, disconnect the 
incorrect Ethernet link. 
I’m seeing strange or confusing 
behavior not mentioned above. 
Make sure you have the latest firmware by enabling Advanced 
Config, going to the Upgrade page and then clicking Check for 
automatic upgrade. 
If you would like to report an issue to Morse Micro, go to the 
Support page under the Help submenu, then click on Create 
Archive. You can then post this on the Morse Micro Community 
Forum and let us know what the problem was. 
Table 8: Troubleshooting common problems 
14.1 Recovering From Failed Updates 
If for some reason the software is corrupted or not booting - this is most often caused by loss of  
power during an update - the following procedure will allow a new image to be written to flash. 
1.​ Remove all cables from the device. 
2.​ Attach an Ethernet from the HaLowLink directly to your computer. 
3.​ While powered off, press and hold the mode button on the HaLowLink. 
4.​ Attach the power cable and turn on power and watch for the Status LED to turn yellow, then 
blink white 5 times. 
5.​ Release the button, the LED should remain yellow. 
6.​ Configure your network connection with the following static IP and netmask: 
a.​ IP address: 192.168.12.2 
b.​ Netmask: 255.255.255.0 
7.​ Open a web browser on the computer and navigate to http://192.168.12.1. 
 
 
morsemicro.com  |  51

## Page 52

Refer to the online version for up-to-date content 
 
  
a.​ Warning: if you get a Page Not Found error message during this step, ensure that your URL 
only contains the IP address, clear your cache and/or use an Incognito browser. 
8.​ Upload a firmware file and press update firmware. A progress screen similar to the figure 
below should appear. 
a.​ Note: despite what the bold text and animated spinner might suggest, you can safely 
navigate away from this page. 
 
Figure: u-boot recovery upgrade screen 
9.​ Do not remove the power until the device has installed the firmware and fully booted. You will 
see the following Status LED patterns to show the progress, in order: 
a.​ solid purple 
b.​ red/purple flashing 
c.​ solid purple 
d.​ solid red 
e.​ off (rebooting) 
f.​
flashing yellow 
g.​ solid yellow (the start of the normal boot process) 
Note: the entire process can take a while to complete (10+ minutes). 
 
 
morsemicro.com  |  52

## Page 53

Refer to the online version for up-to-date content 
 
  
15 Licensing and source 
Much of the software included in the HaLowLink is covered by open source licenses, including the 
GPLv2. For complete licensing information, and access to the source code, go to 
morsemicro.com/halowlink. 
 
 
morsemicro.com  |  53

## Page 54

Refer to the online version for up-to-date content 
 
  
16 FCC Compliance Statement 
FCC ID: 2A74O-9A6140 
FCC compliance statement  
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) this device may not 
cause harmful interference, and (2) this device must accept any interference received, including interference that may cause 
undesired operation.  
changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to 
operate the equipment.  
This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC 
Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This 
equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the 
instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not 
occur in a particular installation.  
If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the 
equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:  
-- Reorient or relocate the receiving antenna.  
-- Increase the separation between the equipment and receiver.  
-- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.  
-- Consult the dealer or an experienced radio/TV technician for help.  
FCC Radiation Exposure statement  
This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment. This equipment should 
be installed and operated with minimum distance 20cm between the radiator and your body. This transmitter must not be 
co-located or operating in conjunction with any other antenna or transmitter.  
 
FCC ID: 2A740-F24F90 
FCC compliance statement  
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) this device may not 
cause harmful interference, and (2) this device must accept any interference received, including interference that may cause 
undesired operation.  
changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to 
operate the equipment.  
This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC 
Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This 
equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the 
instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not 
occur in a particular installation.  
If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the 
equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:  
-- Reorient or relocate the receiving antenna.  
-- Increase the separation between the equipment and receiver.  
-- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.  
-- Consult the dealer or an experienced radio/TV technician for help.  
FCC Radiation Exposure statement  
This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment. This equipment should 
be installed and operated with minimum distance 20cm between the radiator and your body. This transmitter must not be 
co-located or operating in conjunction with any other antenna or transmitter.  
 
 
 
morsemicro.com  |  54

## Page 55

Refer to the online version for up-to-date content 
 
  
17 IC Compliance Statement 
ISED compliance statement  
This device contains licence-exempt transmitter(s)/receiver(s) that comply with Innovation, Science and Economic Development 
Canada’s licence-exempt RSS(s). Operation is subject to the following two conditions:  
(1) This device may not cause interference.  
(2) This device must accept any interference, including interference that may cause undesired operation of the device.  
L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et 
Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux 
conditions suivantes :  
(1) L’appareil ne doit pas produire de brouillage;  
(2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le 
fonctionnement.  
ISED Radiation Exposure statement  
This equipment complies with IC RSS-102 radiation exposure limits set forth for an uncontrolled environment. This equipment 
should be installed and operated with minimum distance 20 cm between the radiator and your body.  
Cet équipement est conforme aux limites d'exposition aux radiations IC CNR-102 établies pour un environnement non contrôlé. 
Cet équipement doit être installé et utilisé avec une distance minimale de 20 cm entre le radiateur et votre corps.  
This radio transmitter [6100A-HM593] has been approved by Innovation, Science and Economic Development Canada to 
operate with the antenna types listed below, with the maximum permissible gain indicated. Antenna types not included in this 
list that have a gain greater than the maximum gain indicated for any type listed are strictly prohibited for use with this device.  
Antenna Designation: Dipole Antenna, Gain: 2.34dBi 
Le présent émetteur radio [6100A-HM593] a été approuvé par Innovation, Sciences et Développement économique Canada 
pour fonctionner avec les types d'antenne énumérés ci-dessous et ayant un gain admissible maximal. Les types d'antenne non 
inclus dans cette liste, et dont le gain est supérieur au gain maximal indiqué pour tout type figurant sur la liste, sont strictement 
interdits pour l'exploitation de l'émetteur.  
Antenna Designation: Dipole Antenna, Gain: 2.34dBi 
 
ISED compliance statement  
This device contains licence-exempt transmitter(s)/receiver(s) that comply with Innovation, Science and Economic Development 
Canada’s licence-exempt RSS(s). Operation is subject to the following two conditions:  
(1) This device may not cause interference.  
(2) This device must accept any interference, including interference that may cause undesired operation of the device.  
L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et 
Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux 
conditions suivantes :  
(1) L’appareil ne doit pas produire de brouillage;  
(2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le 
fonctionnement.  
ISED Radiation Exposure statement  
This equipment complies with IC RSS-102 radiation exposure limits set forth for an uncontrolled environment. This equipment 
should be installed and operated with minimum distance 20 cm between the radiator and your body.  
Cet équipement est conforme aux limites d'exposition aux radiations IC CNR-102 établies pour un environnement non contrôlé. 
Cet équipement doit être installé et utilisé avec une distance minimale de 20 cm entre le radiateur et votre corps.  
This radio transmitter [29791-737B5B] has been approved by Innovation, Science and Economic Development Canada to 
operate with the antenna types listed below, with the maximum permissible gain indicated. Antenna types not included in this 
list that have a gain greater than the maximum gain indicated for any type listed are strictly prohibited for use with this device.  
Antenna Designation: Dipole Antenna, Gain: 2.34dBi 
Le présent émetteur radio [29791-737B5B] a été approuvé par Innovation, Sciences et Développement économique Canada 
pour fonctionner avec les types d'antenne énumérés ci-dessous et ayant un gain admissible maximal. Les types d'antenne non 
inclus dans cette liste, et dont le gain est supérieur au gain maximal indiqué pour tout type figurant sur la liste, sont strictement 
interdits pour l'exploitation de l'émetteur.  
Antenna Designation: Dipole Antenna, Gain: 2.34dBi 
 
 
morsemicro.com  |  55

## Page 56

Refer to the online version for up-to-date content 
 
  
18 Simplified EU Declaration of Conformity 
Hereby, Morse Micro Pty Ltd declares that the radio equipment type HaLowLink 2 is in compliance with Directive 2014/53/EU 
(RED). 
 
The full text of the EU declaration of conformity is available at:​
https://www.morsemicro.com/resources/declarations/EU Declaration of Conformity for MM-HL2-EXT.pdf 
 
 
 
morsemicro.com  |  56

## Page 57

Refer to the online version for up-to-date content 
 
  
Morse Micro provides this information "as is" without warranties of any kind, express or implied. No guarantee is made as to the 
accuracy, completeness, or suitability of this information or Morse Micro’s products for any specific purpose. Use of this information 
and products is at the user’s sole risk. Morse Micro products are not designed or tested for use in mission-critical systems, and should 
not be used in such applications. Performance specifications are based on internal testing and are believed to be reliable; however, they 
are not guaranteed. It is the Buyer’s responsibility to test and validate all product performance, compatibility, and compliance, both in 
isolation and within end applications. Morse Micro assumes no liability for the use or application of any product, circuit, or information 
described herein. No license or other rights—express or implied—are granted under Morse Micro’s intellectual property. This 
document contains proprietary information of Morse Micro and is subject to change without notice. 
 
 
 
 
 
 
 
 
Morse Micro Pty. Ltd. Corporate Headquarters 
Level 8, 10-14 Waterloo Street, Surry Hills, NSW 2010, AUSTRALIA 
Email: sales@morsemicro.com 
Copyright © Morse Micro Pty. Ltd.
