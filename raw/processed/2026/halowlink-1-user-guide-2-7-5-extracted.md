---
title: "Halowlink 1 User Guide 2 7 5 (extracted from PDF)"
source_pdf: raw/processed/2026/halowlink-1-user-guide-2-7-5.pdf
extracted: 2026-04-18
page_count: 43
note: Machine-extracted text; verify against the PDF for tables, figures, and typography.
---

# Halowlink 1 User Guide 2 7 5

**Source PDF:** [`halowlink-1-user-guide-2-7-5.pdf`](./halowlink-1-user-guide-2-7-5.pdf) — repo path `/raw/processed/2026/halowlink-1-user-guide-2-7-5.pdf`


## Page 1

HaLowLink 1 
User Guide

## Page 2

Table of Contents 
 
1 What is the HaLowLink 1?​
4 
1.1 Router with HaLow Access Point​
4 
1.2 HaLow Access Point (AP)​
4 
1.3 HaLow Extender​
5 
2 Getting started​
6 
2.1 Initial connection​
6 
2.1.1 Via Ethernet​
6 
2.1.2 Via Wi-Fi​
6 
2.1.3 Via USB-C​
6 
2.1.4 Connecting to an existing network/internet​
6 
2.2 Home Page​
7 
2.3 Wizard​
8 
2.3.1 Network Mode - HaLow Access Point​
9 
2.3.2 Network Mode - Router with HaLow Access Point and a 2.4 GHz Wi-Fi 
Uplink​
9 
2.3.3 HaLow Mode - 802.11s Mesh and EasyMesh​
10 
3 HaLow Extender​
11 
3.1 Pairing​
12 
3.2 Using your Extender​
13 
4 Restoring Factory Settings​
14 
5 Use Cases​
15 
5.1 Adding a HaLow Access Point to your existing network via Ethernet​
15 
5.2 Adding a HaLow Access Point to a network via 2.4 GHz Wi-Fi​
16 
5.3 Using HaLow to extend an existing network - ‘Virtual Wire’​
17 
5.4 Connect your computer to a HaLow network via USB-C​
18 
5.5 Connect an Ethernet device to a HaLow network​
19 
5.6 Connect a non-HaLow Wi-Fi device to a HaLow network​
20 
5.7 Experimenting with HaLow​
21 
6 Quick Config​
22 
6.1 Network Interfaces​
22 
6.2 Wireless​
22 
2 | morsemicro.com.au​

## Page 3

6.3 Advanced Usage​
22 
7 Advanced Config​
23 
8 Exploring HaLow Connectivity​
24 
8.1 Status -> Channel Analysis​
24 
8.2 Status -> Realtime Graphs​
24 
8.3 Network -> Diagnostics​
24 
8.4 Statistics -> Graphs​
24 
8.5 Services -> Terminal​
25 
9 Configuring via the Command Line​
26 
9.1 Making changes​
26 
9.2 File/service structure​
27 
9.3 Debugging​
28 
9.4 Applying configurations​
28 
10 Software Upgrades​
29 
11 Device Features​
30 
11.1 LED indicators​
30 
11.1.1 Status LED​
30 
11.1.2 Wi-Fi HaLow LED​
31 
11.1.3 Wi-Fi 2.4 GHz LED​
31 
11.2 Ethernet/USB ports​
32 
11.2.1 HaLow Access Point mode (green status LED)​
32 
11.2.2 HaLow Extender mode (aqua status LED)​
33 
12 Troubleshooting​
34 
12.1 Recovering From Failed Upgrades​
37 
13 Licensing and Source​
38 
14 FCC compliance statement​
39 
15 IC compliance statement​
40 
3 | morsemicro.com.au​

## Page 4

1 What is the HaLowLink 1? 
Your HaLowLink 1 allows you to use Morse Micro’s HaLow Wi-Fi chip to: 
●​ easily set up a new network that supports HaLow​
-> Router with HaLow Access Point (green Status LED) 
●​ let other HaLow-enabled devices connect to your existing network​
-> HaLow Access Point (green Status LED) 
●​ let existing non-HaLow (i.e. 2.4 GHz Wi-Fi and Ethernet) devices, including 
normal computers, use HaLow’s range​
-> HaLow Extender (aqua Status LED) 
It’s flexible and powerful enough that it  can perform all these roles. For more 
information on how these roles can be useful, see the Use Cases section below. 
 
 
4 | morsemicro.com.au​

## Page 5

1.1 Router with HaLow Access Point 
This is the default mode of operation for HaLowLink. It has an IP address of 
192.168.12.1, and hands out addresses to devices connected to the LAN side via 
Ethernet, Wi-Fi or HaLow in this range. The WAN Ethernet port is the default uplink 
connection, and will obtain an address as a DHCP client. In this mode the HaLowLink is 
most similar to a typical home router/gateway, and it is not possible to access the web 
interface except via the local network. 
1.2 HaLow Access Point (AP) 
Similar to access points (APs) available on the market, this allows you to add a HaLow 
Access Point to your existing network. You still use your WAN Ethernet port for the 
uplink connection, but any attached HaLow devices will use DHCP to obtain addresses 
on your existing network subnet. This means no traffic forwarding/NAT is required. This 
is the most appropriate mode for most use cases, as it makes it straightforward for 
anyone on your network to interact with HaLow connected devices. 
It will also be possible to access the web interface via your existing local network by 
determining which IP is assigned to the HaLowLink. However, the 192.168.12.1/24 
network will remain accessible on the LAN port. This functions as a separate 
management interface independent of the existing network which makes it simpler to 
reconfigure. 
1.3 HaLow Extender 
Extenders generally receive a Wi-Fi signal and rebroadcast it. In Wi-Fi jargon, these 
devices are stations/clients rather than APs in regards to the HaLow network. 
The goal of this mode of operation is to help get another device connected to a HaLow 
network. That device might be connected to the HaLowLink via Ethernet or 2.4 GHz 
Wi-Fi, and then the HaLowLink passes that traffic via HaLow, effectively extending the 
range of the non-HaLow device. 
5 | morsemicro.com.au​

## Page 6

2 Getting started 
2.1 Initial connection 
Connect the provided antenna to the antenna connector first. Then connect your 
device to the HaLowLink 1. 
2.1.1 Via Ethernet 
1.​ Connect your HaLowLink 1 to power via the USB-C port with the power supply 
provided. 
2.​ Connect your computer to the LAN port of the HaLowLink 1 with the Ethernet 
cable provided. 
2.1.2 Via Wi-Fi 
1.​ Connect your HaLowLink 1 to power via the USB-C port with the power supply 
provided. 
2.​ Connect your computer or phone to the Wi-Fi network of the HaLowLink 1 by 
scanning the QR-Code or using the Wi-Fi SSID/password on the label. 
2.1.3 Via USB-C 
1.​ Connect your HaLowLink 1 to your computer directly with the USB-C cable 
provided. Make sure to use a USB-C port to ensure sufficient power. 
2.1.4 Connecting to an existing network/internet 
Optionally, if you want your HaLow devices to access the  internet or an existing 
network, connect an Ethernet cable from the WAN port of the HaLowLink 1 to a 
network with a DHCP server. 
6 | morsemicro.com.au​

## Page 7

2.2 Home Page 
Once you’ve connected to the HaLowLink’s network, you can then use your web 
browser to connect to http://192.168.12.1. To login, use the Device Username and 
Password on the bottom of the HaLowLink; we recommend letting your browser save 
the password. 
You should now be able to see the Home page, where initially, you will have ‘0 
Connected Devices’ on your HaLow network. 
 
The Home Page will automatically update if changes happen to your network. To view 
more information, click on the large numbers on the card or on the ‘expand’ icon in the 
top right. Make sure the ‘Uplink’ card has a tick if you want your HaLow devices to have 
access to an existing network or the internet. 
7 | morsemicro.com.au​

## Page 8

2.3 Wizard 
As described in What is the HaLowLink 1?  above, when you first start your HaLowLink 
1 it will be a Router with HaLow Access Point. If you’d like to change this mode, go to 
the Wizard option in the menu on the left hand side: 
 
You should see that the option ‘HaLow Wi-Fi devices will get an IP on this device’s local 
network’ is selected; i.e. this device is acting as a router. 
The wizard helps you quickly switch between different device modes, making many 
configuration changes for you automatically. Because it has to make many changes, 
using the wizard may remove some of your customisations. 
8 | morsemicro.com.au​

## Page 9

2.3.1 Network Mode - HaLow Access Point 
If possible, we recommend changing your device to ‘HaLow Wi-Fi devices will get an IP on 
your existing router’s network’. That is, change from Router with HaLow Access Point to 
HaLow Access Point. As described above in What is the HaLowLink 1?, this ensures 
that HaLow devices are a seamless part of your existing network. 
This option will only work, however, if you have connected your WAN port to your 
existing router and your HaLowLink 1 has obtained an IP address. To confirm this is 
true, go to the Home page and make sure you have tick on the Uplink card: 
 
2.3.2 Network Mode - Router with HaLow Access Point and a 2.4 GHz 
Wi-Fi Uplink 
If you do not have easy access to an Ethernet port on your existing network, but do have 
access to Wi-Fi, you should select the final network mode, ‘HaLow Wi-Fi devices will get 
an IP on this device's local network and use 2.4 GHz Wi-Fi for an uplink (not an Ethernet 
cable)’. Once you’ve clicked Save & Apply, however, you will need to provide credentials: 
●​ Go to the Home page, and click the ‘Disconnected’ cross on the uplink card​
 
9 | morsemicro.com.au​

## Page 10

●​ Search for your Wi-Fi network and enter  your password, then save the 
credentials:​
 
●​ Wait for ‘connected’ to change to ‘yes’ (and green). You should now see that the 
Home page has a tick on the Uplink, and your HaLowLink 1 will have access to 
your existing network. 
2.3.3 HaLow Mode - 802.11s Mesh and EasyMesh 
By default, your device is configured as an Access Point. Because of HaLow’s incredible 
range, for most purposes this is sufficient. However, to achieve even more range, or if 
there are physical barriers between devices, it’s possible to use multiple HaLowLinks to 
create a mesh. 
1.​ Configure your Access Point as a mesh device (either 802.11s Mesh or 
EasyMesh) via the wizard. 
2.​ Configure additional mesh devices in Extender mode (aqua status LED) by 
pairing them to the original device. For more details, see 3 HaLow Extender 
below. When it pairs, it will automatically configure itself as a mesh device. 
However, if it was previously connected to a normal Access Point, make sure to 
reset your Extender and re-pair it to ensure it is configured as a Mesh Extender. 
If you simply change the configuration on the Access Point your Extenders will 
connect but will not form a mesh. 
If you have configured your device in one of the mesh modes we do not recommend 
making significant networking changes in the UI as it is very easy to misconfigure the 
mesh. In particular, for EasyMesh, not all settings are visible in the web interface. 
10 | morsemicro.com.au​

## Page 11

3 HaLow Extender 
By default, your HaLowLink 1 comes configured as a HaLow Access Point. However, as 
described in What is the HaLowLink 1?, it can also be used as an Extender when you 
have more than one HaLowLink 1 device. This will let existing Wi-Fi and Ethernet 
devices make use of HaLow’s long range. 
To switch your HaLowLink 1 device to Extender mode, you never need to use the web 
interface. Refer to the diagram in below, and switch modes as follows: 
1.​ Connect your HaLowLink 1 to mains power via the USB-C port with the power 
supply provided. 
2.​ Wait until the Status LED is solid green. 
3.​ Hold down the Mode button. The Status LED will first start flashing slowly 
green, and then start flashing quickly aqua. Release the button when it’s flashing 
aqua. 
4.​ Wait until the Status LED is solid aqua to indicate it’s loaded and running in 
Extender mode. 
 
 
11 | morsemicro.com.au​

## Page 12

3.1 Pairing 
In Extender mode your device will not be accessible at 192.168.12.1. Instead, you 
should pair it to an existing HaLowLink 1 by: 
1.​ Pressing and immediately releasing the mode button on your HalowLink 1 
Access Point (with a green Status LED). The Wi-Fi HaLow LED will begin slowly 
flashing to indicate it’s ready to pair. 
2.​ Pressing and immediately releasing the mode button on your HalowLink 1 
Extender (with an aqua Status LED). The Wi-Fi HaLow LED will begin slowly 
flashing to indicate it’s searching for an Access Point to pair with. 
3.​ Wait until the Wi-Fi HaLow LED is solid purple. Your Extender has now stored 
the Wi-Fi credentials, and is ready to use! 
If pairing hasn’t succeeded after 120 seconds, the Access Point Wi-Fi HaLow LED will 
stop flashing and the Extender Wi-Fi HaLow LED will turn off. You can now try pairing 
again from the beginning. 
3.2 Using your Extender 
You can connect devices to your Extender via an Ethernet cable or via 2.4 GHz Wi-Fi, 
and this will let them use the Extender’s HaLow connection. For the Wi-Fi credentials, 
refer to the label on your Extender. These will not be the same as the credentials on 
your Access Point. 
12 | morsemicro.com.au​

## Page 13

4 Restoring Factory Settings 
If you no longer want to use your HaLowLink 1 as an Extender, you’ve lost access to 
your device, or you simply want it to go back to the way it was, you can return it to 
Access Point mode (Green Status LED) by restoring factory settings: 
1.​ Connect your HaLowLink 1 to mains power via the USB-C port with the power 
supply provided. 
2.​ Wait until the Status LED is solid green or solid aqua. 
3.​ Hold down the Mode button. Once the Status LED starts flashing slowly green, 
release the button. 
4.​ Wait until the Status LED is solid green to indicate it’s running in Access Point 
mode. 
5.​ You can now access your device at http://192.168.12.1 again, as described in 
Initial Connection. 
Warning: if, at Step 3, you hold down the button until it’s flashing quickly aqua, the 
device will reset but change into Extender mode, as described in the Extender section. 
 
13 | morsemicro.com.au​

## Page 14

5 Use Cases 
These are some common use cases for the HaLowLink 1 with some pointers on how to 
achieve them. If you have previously configured your HaLowLink 1 in some way, you 
may want to Restore Factory Settings before following these instructions. 
5.1 Adding a HaLow Access Point to your existing 
network via Ethernet 
 
The primary use case for a HaLowLink 1 is to add HaLow support to your existing 
network, allowing any HaLow-enabled client to work in the same way as any other 
Wi-Fi client. 
●​ Make sure your HaLowLink is in Access Point mode (green status LED). 
●​ Connect the WAN port of your HaLowLink 1 to your network; in the home, this 
usually means placing it next to your router and connecting the WAN port to a 
LAN port. 
●​ HaLow devices can then connect via the SSID/password printed on the sticker. 
Although it will work as is for many use cases, for the best experience we recommend 
using the Wizard to set ‘HaLow Wi-Fi devices will get an IP on your existing router’s 
network’, which will change it from a Router with HaLow Access Point to a HaLow 
Access Point. See the Wizard section above for more details. 
14 | morsemicro.com.au​

## Page 15

5.2 Adding a HaLow Access Point to a network via 2.4 
GHz Wi-Fi 
 
If it’s not possible to connect your HaLowLink via Ethernet, you can connect your 
HaLowLink via 2.4 GHz Wi-Fi. You should only do this if Ethernet is not possible, as it 
will require your HaLowLink to act as a router, forwarding traffic from 192.168.12.x 
over the Wi-Fi link. 
●​ Make sure your HaLowLink is in Access Point mode (green status LED). See 
Restoring Factory Settings if it’s not. 
●​ Go to the Wizard in at http://192.168.12.1 and set the ‘Network Mode’ to 
‘HaLow Wi-Fi devices will get an IP on this device's local network and use 2.4 GHz 
Wi-Fi for an uplink (not an Ethernet cable)’, then go to the Home page to configure 
your credentials. For more details, see the Network Modes section above. 
●​ HaLow devices can then connect via the SSID/password printed on the sticker. 
This may be particularly useful on networks you don’t have administrator access to, and 
in fact the HaLowLink can act as a travel router in this situation, providing your own 
private network not just HaLow Access Point but also a 2.4 GHz Wi-FI access point and 
Ethernet connectivity. 
15 | morsemicro.com.au​

## Page 16

5.3 Using HaLow to extend an existing network - 
‘Virtual Wire’ 
 
This will require two HaLowLink devices, and will make a HaLow link a transparent part 
of your network, functioning just like an Ethernet cable. 
First, you should add a HaLow Access Point to your network (see 1 or 2 above). Once 
your network supports HaLow, you should follow the instructions in the Extender 
section above. In summary: 
1.​ Make sure your HaLowLink is in Extender mode (aqua status LED). 
2.​ Pair your Extender with your Access Point by pressing and releasing the mode 
button on your Access Point, then pressing and releasing the mode button on 
the Extender. The HaLow LED will slowly flash, usually for around 10 seconds, 
before turning a solid purple on the Extender to show it’s connected. 
3.​ Now any device connected to the Extender - via USB, 2.4 GHz Wi-Fi, or 
Ethernet - will make use of the HaLow link to connect to your network. See (4), 
(5) and (6) below for more instructions. 
16 | morsemicro.com.au​

## Page 17

5.4 Connect your computer to a HaLow network via 
USB-C 
 
Follow the instructions above in (3) to set up an Extender, then: 
1.​ Connect your computer via the provided USB-C cable to your Extender (aqua 
status LED). 
2.​ A new Ethernet adapter should appear on your computer. Make sure it’s 
configured as a DHCP Client. 
3.​ You can now send traffic via the HaLow link. Note that because it’s an Ethernet 
connection, by default your computer will likely use it in preference to any 
existing Wireless connection. See the Troubleshooting section for more 
information. 
17 | morsemicro.com.au​

## Page 18

5.5 Connect an Ethernet device to a HaLow network 
 
Follow the instructions above in (3) to set up an Extender, then: 
1.​ Connect your device via an Ethernet cable to your Extender (aqua status LED). 
2.​ Your device should now acquire an address via DHCP. 
18 | morsemicro.com.au​

## Page 19

5.6 Connect a non-HaLow Wi-Fi device to a HaLow 
network 
 
This could be a computer, tablet, phone, or any IoT device. 
Follow the instructions above in (3) to set up an Extender, then: 
1.​ Set the SSID/password of the Extender (NOT the Access Point) via scanning the 
QRCode on the bottom of the Extender or copying the credentials from the 
same sticker. 
2.​ Your device should now acquire an address via DHCP. 
19 | morsemicro.com.au​

## Page 20

5.7 Experimenting with HaLow 
 
If you’re currently just experimenting with HaLow’s amazing range and penetration, the 
easiest way to test this out with a HaLowLink 1 is to have two devices and two laptops, 
where the laptops provide power to the HaLowLink. This allows you to easily move 
around. 
1.​ Connect one laptop via USB-C to your Router with HaLowLink 1 Access Point 
(i.e. the factory default configuration), and go to http://192.168.12.1 (as 
described in Getting Started). 
2.​ Connect another laptop to an Extender via USB-C, then set up the Extender as 
described in (3). 
3.​ You should see the Extender appear on the Home page of the Access Point in 
the ‘Connected Devices’, and the ‘Local Network’ card should show the IPs of 
both the Extender and your other laptop.​
 
4.​ You can now test out the connection from one laptop to the other via HaLow. 
For more information about how to do this, see Exploring HaLow Connectivity 
in the next section. 
Note that because the USB link is via Ethernet, by default your computer will likely use 
this in preference to any existing Wireless connection. See the Troubleshooting section 
for more information. If you’re familiar with OpenWrt, you can stop this happening by 
configuring the DHCP server to return nothing for Option 3 (gateway). 
20 | morsemicro.com.au​

## Page 21

6 Quick Config 
For most users the Wizard page will be sufficient to configure a HaLow Access Point 
(green mode), and an Extender (aqua mode) can be configured via the button as 
described above. However, if you want to make simple minor changes to your 
configuration - such as changing your Wi-Fi password or encryption method, or setting 
a Static IP - you can do so via the Quick Config page. To help you understand the 
changes you’re making, these will be reflected in the diagram at the top of the page as 
you make them. 
WARNING: it is easy to change the configuration of your device here in a way that 
causes you to lose access to it, particularly if you’re changing network interfaces. If this 
happens, see the section above on Restoring Factory Settings. 
6.1 Network Interfaces 
This section lists the logical networks available on your router, each of which can be 
configured with either a Static IP (and potentially a DHCP Server) or as a DHCP Client. 
If you have multiple ‘Ethernet’ ports or WIreless interfaces on the same network, a 
bridge will automatically be created. Note that to attach new Wireless interfaces to the 
network, you will need to use the Wireless section. 
6.2 Wireless 
This will allow you to configure the Wi-Fi interfaces on your HaLowLink. Note that it is 
possible to create multiple interfaces for a particular radio. 
6.3 Advanced Usage 
The Quick Config page is designed to correspond to the underlying text based 
configuration and connect with the pages accessible via Advanced Config (see below). 
If you have Advanced Config enabled, you can use the ‘cog’ icons on the Quick Config 
to access these pages, which will allow you more flexibility in your setup. It will also 
allow you to simply ‘Save’ rather than ‘Save & Apply’, which will let you view and apply or 
revert the proposed changes by clicking on the ‘Unsaved Changes’ indicator at the top 
right. 
For more about the underlying configuration format (known as UCI), see Configuring 
via the Command Line. 
21 | morsemicro.com.au​

## Page 22

7 Advanced Config 
The software running on your HaLowLink 1 is based on OpenWrt, a Linux operating 
system targeting network connected devices. Minor configuration changes are 
accessible via the Quick Config page, but for full access click the Advanced Config 
menu option on the left hand side. 
 
This will allow you to view detailed information about your device, change low-level 
configuration, install additional software if you have an internet connection (via System 
-> Software), and even access the Linux terminal (via Services -> Terminal). 
You can also directly connect to your device via ssh using the same username and 
password you used to login. This is printed on the label. 
For more information about OpenWrt, see https://openwrt.org/start. 
22 | morsemicro.com.au​

## Page 23

8 Exploring HaLow Connectivity 
Your HaLowLink 1 comes packed with useful utilities and pages to make the most of 
your HaLow connection. In particular, we recommend the following pages, accessible 
once Advanced Config has been enabled: 
8.1 Status -> Channel Analysis 
This will allow you to see the channels and signal strength of any other nearby HaLow 
networks. If there are many local HaLow networks, you may want to change the channel 
via the Quick Config page to avoid interference. 
8.2 Status -> Realtime Graphs 
This will show you a continuously updating graphical view of the link quality (see 
Wireless section) as well as other critical system metrics while you have the page open. 
8.3 Network -> Diagnostics 
This allows you simple access to command line tools to evaluate your network, including 
iperf3 (to test bandwidth), ping and traceroute to explore connectivity, and arp-scan 
to discover all devices on the network. It also will show you the command it’s executing, 
as you may also want to do this via the command line (see Services -> Terminal). 
8.4 Statistics -> Graphs 
Your HaLowLink 1 is running collectd to continuously monitor the behaviour of the 
device. Some of the information here is similar to Realtime Graphs, but it’s updated at a 
lower frequency and stored while the device is running rather than just while you’re on 
the page. It’s also possible to configure other devices to point to this (e.g. Extenders) to 
aggregate all your statistics in a single place. 
23 | morsemicro.com.au​

## Page 24

8.5 Services -> Terminal 
For easy access to the Linux console, you can start a terminal on the device by going to 
Services -> Terminal. Note that you will have to re-enter your device password (refer 
to the sticker on the bottom of your HaLowLink). 
From the command prompt, you will have access to the standard Linux utilities included 
in OpenWrt and those already mentioned via the Diagnostics page, as well as some 
other programs we’ve added. Here are some extra programs we’ve included that are 
particularly useful: 
Utility 
Purpose 
morse_cli 
Low level access to information from and settings on the Morse 
Micro HaLow chip. 
wavemon 
Terminal graphical program to monitor Wi-Fi signal strength and 
performance. 
nano 
Text editor, including syntax highlighting of UCI files. You may also 
use vi. 
tmux 
Terminal multiplexer, allowing persistent sessions and windows. 
24 | morsemicro.com.au​

## Page 25

8.5 Services -> Range Test 
 
The Range Test application is designed as a simple way to analyse HaLow network 
performance by automating iPerf3 tests and collecting real-time statistics. It is a useful 
tool for quickly assessing signal strength, data throughput, and connection quality 
across different environments. 
 
Before using this application ensure that all devices under test are running the same 
version of Morse OpenWrt. This tool can run with different types of evaluation kit (i.e. 
between an HaLowLink 1 and an EKH01) but the software versions must be the same. 
To use the range testing tool: 
25 | morsemicro.com.au​

## Page 26

1.​ Connect the devices being tested on the same HaLow network of any type 
outlined in this guide (Default AP/STA configurations are the most reliable). 
2.​ Set up the devices in the desired locations and select a ‘local’ device to connect a 
laptop to. 
3.​ In the management interface navigate to Services -> Range Test. 
4.​ Select the HaLow IPv4 address from the ‘Remote Device’ dropdown. If it does 
not appear on first load, click the 🔍icon to run another discovery. If this fails ​
​
to find a device which is connected to the same network as the local HaLowLink 
1, a user may enter any IPv4 address into the ‘custom’ field pictured. 
5.​ Fill in the ‘Password’ field using the device password (not the Wi-Fi password) if 
the remote device has one. 
6.​ Optional - Provide user notes about the test in the ‘Description’ field. 
7.​ Optional - If you want to log the coordinates of the local and remote devices and 
have the range calculated automatically enter the decimal degree values into the 
local and remote device coordinates fields respectively. ​
​
These values can be easily found by right clicking the relevant locations on 
Google Maps and then selecting the coordinates which will automatically put 
them in your clipboard (pictured).  
8.​ If valid coordinates have been used from the previous step, the ‘Range (m)’ field 
should automatically populate, otherwise a range value must be supplied. 
9.​ Optional - By clicking the 
 icon in the top left corner of the Test 
Configuration subsection, the data directions and protocols which will be tested 
can be modified.​
​
Note: data directions are named relative to the local device. If a ‘Send’ test is running it 
26 | morsemicro.com.au​

## Page 27

means that the local device will send data to the remote device and vice versa with 
‘Receive’ tests.​
 
10.​Click ‘Start Test’ and a progress bar will appear showing the status of the current 
test. This can be cancelled at any time by clicking the Stop button. 
11.​After the test completes, a row in the Results Summary subsection should 
appear, as pictured below.
 ​
This result can be deleted by clicking the trash icon, or a JSON file containing all 
the raw data can be downloaded via the ‘Download’ button, which is intended to 
help engineers with remote debugging. The ‘Download Results Summary (CSV)’ 
button yields a CSV file of all the data represented in the results summary.​
​
Note: test results are volatile to avoid overwhelming limited memory resources and will 
be deleted if power is removed or the device is rebooted. 
Each sub-test is based around a 10 second iPerf3 test. The remote device will always 
act as the iPerf3 server and use the same command: iperf3 -s -1 --json. The local 
device will always act as the iPerf3 client, running a command in the following format:  
iperf3 -c <remote_IP> <protocol> <data_direction> -t 10 -O 2 --json 
For UDP tests the protocol arguments become -u -b 40M/30 whereas for TCP tests 
only -Z is set. For the data direction arguments ‘Receive’ tests set the -R flag.​
​
Note: if the throughput numbers are returning ~40 Mbps for UDP and 900+ Mbps for TCP 
then the test is likely defaulting to run over an Ethernet connection. This should be avoided. 
27 | morsemicro.com.au​

## Page 28

9 Configuring via the Command Line 
The HaLowLink 1 is an open device running Linux, and it is straightforward to gain 
direct access via either ssh or the Services -> Terminal page (accessible after enabling 
Advanced Config). Because it’s based on OpenWrt, the primary mechanism of 
configuration is via UCI (https://openwrt.org/docs/guide-user/base-system/uci), which 
is fundamentally just a collection of files in /etc/config in a particular format. 
9.1 Making changes 
This happens in two steps: 
●​ set new values in UCI 
●​ reload_config to reload services 
You can make changes to UCI via the uci command or by editing the files in 
/etc/config. 
For example: 
nano /etc/config/wireless 
OR 
uci show wireless​
​
uci set wireless.default_radio0.mode=sta​
​
uci commit 
Doing a uci commit will cause the change to appear in /etc/config/wireless. 
Once you've made changes (via either of those methods), to make them take effect use: 
reload_config 
Other files/services that are likely to be useful for network config are dhcp, network and 
firewall. 
Aside from the UCI documentation mentioned above, the most useful resource is 
clicking ‘Save’ rather than ‘Save & Apply’ in the UI, which is possible if you’ve enabled 
Advanced Config in the menu. This will allow you to go up the top right ('Unsaved 
28 | morsemicro.com.au​

## Page 29

Changes') and view a sequence of uci set commands corresponding to the change you 
just made. For example, after setting a static IP: 
 
9.2 File/service structure 
●​ wireless contains the radio devices (wifi-device) and the interfaces connected 
to that (e.g. wlan0, wlan1 - caused by a wifi-iface). Any wifi-iface has a 
network, which refers to an interface in the network UCI file. This corresponds 
to the Wireless section on the Quick Config page. 
●​ network contains a mix of switches/bridges and logical interfaces; an interface 
in network may point to a bridge, in which case multiple Ethernet ports or 
wifi-ifaces might be attached to it. 
○​ confusingly, the wireless interfaces are not directly mentioned here, only 
in the wireless file. This means it’s possible to incorrectly configure a 
network interface by NOT having a bridge and having multiple 
wifi-ifaces refer to it. 
○​ this corresponds to the Network Interfaces section on the Quick Config 
page. 
●​ firewall controls nftables - i.e. forwarding/masquerading as well as simple 
accept/reject. Firewalls have another level of indirection - zones - such that you 
can potentially put multiple network interfaces in one zone. 
29 | morsemicro.com.au​

## Page 30

●​ dhcp controls dnsmasq - i.e. DHCP and DNS. The usual setup is that there’s 
always dnsmasq running, but if you don’t want DHCP active on particular 
interfaces you set them to ‘ignore’. 
9.3 Debugging 
If you’ve made a change and it’s not working the way you expect: 
logread -l 100 -f 
will tail the logs. This is the primary mechanism OpenWrt of reporting that something 
went wrong, since you won’t see it running reload_config. 
Note that if you’ve manually edited the files rather than using uci set it’s possible you’ve 
made them invalid. Use uci show to confirm that the UCI library can still parse them. 
9.4 Applying configurations 
As noted above, we recommend using reload_config to apply configurations. What 
this does is: 
●​ check to see if any of the config files have changed 
●​ trigger a reload on any services affected by these changes (i.e. not a restart) 
There are other ways to do this. Notably, manually triggering a reload will pick up 
uncommitted changes: 
●​ explicitly reloading a single service: service network reload 
●​ explicitly restarting a single service: service network restart 
●​ bringing down only the wifi interfaces and back up without restarting the 
network: wifi down && wifi up 
 
30 | morsemicro.com.au​

## Page 31

10 Software Upgrades 
To upgrade your software, use your browser to access the web interface (usually at 
http://192.168.12.1) as described in Initial Connection. Then select Advanced Config, 
and you should see the Upgrade menu item: 
 
 
●​ Check for automatic upgrade will obtain the new version of firmware from the 
Morse servers. 
●​ Manually upload firmware file will let you upload any compatible firmware. 
31 | morsemicro.com.au​

## Page 32

11 Device Features 
11.1 LED indicators 
 
11.1.1 Status LED 
Color 
Meaning 
Yellow flashing 
factory reset in progress 
Yellow solid 
bootloader running 
Green flashing 
OpenWrt is booting 
Green solid 
OpenWrt is loaded and running 
32 | morsemicro.com.au​

## Page 33

Aqua flashing 
OpenWrt is booting into Extender mode 
Aqua solid 
OpenWrt is loaded and running in Extender mode 
Blue flashing 
OpenWrt is executing a software upgrade (do not 
disconnect power when this is happening) 
11.1.2 Wi-Fi HaLow LED 
Color 
Meaning 
Off 
Wi-Fi HaLow is disabled (or not associated if Extender) 
Purple solid 
Wi-Fi HaLow is enabled (and associated if Extender) 
Purple fast flash/flicker 
Data is being transferred over HaLow 
Purple slow flash 
Pairing is in progress 
11.1.3 Wi-Fi 2.4 GHz LED 
Color 
Meaning 
Off 
Wi-Fi 2.4 GHz Access Point is disabled 
Green solid 
Wi-Fi 2.4 GHz Access Point is enabled 
Green fast flash/flicker 
Data is being transferred over Wi-Fi 2.4 GHz 
33 | morsemicro.com.au​

## Page 34

11.2 Ethernet/USB ports 
 
11.2.1 HaLow Access Point mode (green status LED) 
Regardless of whether the HaLowLink is configured as a router or just an access point, 
these roles are correct. That is, USB-C and LAN will always be on a separate network to 
WAN, and the WAN port should be connected to your router. 
Port 
Role 
USB-C 
Either power only, or connect a computer to get a 
192.168.12.x IP and access the management interface at 
192.168.12.1. 
LAN 
Connect a computer to get a 192.168.12.x IP and access 
the management interface at 192.168.12.1. 
WAN 
Connect this to your existing network/router. 
34 | morsemicro.com.au​

## Page 35

​
11.2.2 HaLow Extender mode (aqua status LED) 
In Extender mode, all ports are bridged, and WAN has no special role. 
Port 
Role 
USB-C 
Either power only, or connect a computer to use the 
Extender’s HaLow connection. 
LAN 
Connect a computer to use the Extender’s HaLow 
connection. 
WAN 
Connect a computer to use the Extender’s HaLow 
connection. 
35 | morsemicro.com.au​

## Page 36

12 Troubleshooting 
If you’re having trouble with your HaLowLink 1, we recommend resetting the device by 
holding down the mode button, as described in Restoring Factory Settings. You can 
also contact Morse via https://morsemicro.com/halowlink1  
 
Problem 
Solution 
The status light is not 
illuminated. 
There is a problem with power to the device. Check 
that the USB-C port on the HaLowLink 1 is connected 
to the provided power supply or to a USB-C port on a 
computer. Do not use a USB-A to USB-C adapter. 
The status light is still yellow 
after some time, or never 
stops flashing green after 
boot. 
The flash partition is probably corrupt. To recover 
your HaLowLink, see Recovering From Failed 
Upgrades below. 
I can’t access the HaLowLink 
at 192.168.12.1. 
If the status light is solid green and you can’t access 
your HaLowLink at 192.168.12.1: 
●​ Make sure your computer is connected to 
either the LAN or USB port of the HaLowLink. 
●​ Check that your network connection is 
configured to use DHCP client, and has been 
allocated a 192.168.12.XXX IP. 
●​ If you’re failing to establish a network 
connection to your device, see Restoring 
Factory Settings. 
​
If the status light is solid aqua, your HaLowLink is in 
Extender mode and will only be useful if connected to 
an Access Point. Simply connect other devices to it via 
Ethernet or 2.4 GHz Wi-Fi to use your 
HaLow-enabled network. You should not need to 
access its Web UI, but you may find its address  in the 
DHCP lease table of your DHCP server. 
36 | morsemicro.com.au​

## Page 37

I changed a configuration 
setting and now I can’t 
access my HaLowLink 1, but 
I don’t want to reset it. 
If you need to access your HaLowLink 1 as part of 
troubleshooting a complex configuration change, you 
can connect your computer to the LAN or WAN port 
and configure it with the following settings: 
●​ IP: 10.22.121.110 
●​ Netmask: 255.255.255.254​
(if you can’t set 255.255.255.254 due to OS 
limitations, use 255.255.255.0) 
 
As long as your HaLowLink 1 has a solid green or aqua 
light, it will be available at 10.22.121.111 (this is a 
secondary static IP assigned for diagnostic purposes). 
I can see that the Access 
Point card has connected 
devices, but the Local 
Network card doesn’t list 
them. 
If you have configured your device as an Access Point 
only (i.e.  the wizard option HaLow Wi-Fi devices will get 
an IP on your existing router’s network), then these 
devices will appear in DHCP lease table of the existing 
DHCP server on your network. The Local Network 
on the HaLowLink 1 is being used primarily for easy 
access to the configuration, and will not have HaLow 
devices in it.. 
 
Alternatively, if you have temporarily lost power to 
HaLowLink 1 Access Point your devices may not yet 
have refreshed their DHCP leases. They will 
eventually renew their leases when their lease time 
expires. 
When I connect my 
computer to my HaLowLink 
Extender directly over 
Ethernet, my internet gets 
slower. 
Because your computer has a wired connection to the 
HaLowLink, most operating systems will prefer this 
connection over any wireless connection. However, if 
you’re using a HaLowLink Extender, this means you 
will be restricted to the maximum bandwidth over the 
HaLow link (~22mbps). For your particular operating 
system, you should determine how to prefer your 
existing Wi-FI connection (e.g. via setting the 
HaLowLink connection to ‘local only’, removing the 
default route from the HaLowLink, or changing the 
route priorities). 
37 | morsemicro.com.au​

## Page 38

When I connect my 
computer to my HaLowLink 
directly over Ethernet, my 
internet stops working. 
This is the same problem as above, where your 
computer will prefer the HaLowLink connection over 
any wireless connection, but in this case it’s probably 
your HaLowLink is not yet connected to the internet. 
For an Access Point, check the ‘Uplink’ on the 
homepage (which will report the WAN and 2.4 GHz 
state), and for an Extender check it has a purple light 
AND that the Access Point is correctly configured. 
I changed the HaLow Mode 
or Network Mode of my 
HaLowLink 1, and my 
Extenders no longer work. 
If you make significant changes to your configuration, 
any Extenders attached to your Access Point may no 
longer function as you expect. If you’ve just changed 
the Network Mode, we recommend plugging and 
unplugging your Extender to force it to reinitialise. If 
you’ve changed the HaLow Mode, you should follow 
the instructions in the Extender section to reset your 
device to Extender mode and redo the pairing 
procedure. 
My connection isn’t 
performing as I expect. 
Check signal strengths on the Access Point by going 
to the Home page and clicking on the ‘Connected 
Devices’. For more detailed information about the 
signal, go to Status -> Realtime Graphs (in Advanced 
Config). You can also see if there are other HaLow 
networks interfering by going to the Status -> 
Channel Analysis page, or go to Network -> 
Diagnostics to run iperf3 or ping tests. 
My Extender’s HaLow status 
LED is flashing quickly all the 
time even when I’m not using 
it. 
Because the wireless and wired connection are 
bridged on the Extender, make sure you haven’t 
created a network loop by connecting a LAN/WAN 
port of your Extender to the same network as your 
Access Point. To solve this, disconnect the incorrect 
Ethernet link. 
I’m seeing strange or 
confusing behaviour not 
mentioned above. 
Make sure you have the latest firmware by enabling 
Advanced Config, going to the Upgrade page and 
then clicking ‘Check for automatic upgrade’. 
 
If you would like to report an issue to Morse Micro, go 
to Help -> Support, then click on Create Archive. Go 
to https://morsemicro.com/halowlink1 and let us 
know what the problem was. 
38 | morsemicro.com.au​

## Page 39

12.1 Recovering From Failed Upgrades 
If for some reason the software is corrupted or not booting - this is most often caused 
by losing power during an upgrade - the following procedure will allow a new image to 
be written to flash. 
1.​ Remove all cables from the device. 
2.​ Attach an Ethernet from the HaLowLink 1 directly to your computer. 
3.​ While powered off, press and hold the mode button on the HaLowLink. 
4.​ Attach the power cable and turn on power. 
5.​ Watch for the Status LED to turn yellow, then blink white 5 times. 
6.​ Release the button, the LED should remain yellow. 
7.​ Configure your network connection with the following static IP and netmask: 
IP address: 192.168.12.2​
Netmask: 255.255.255.0 
8.​ Open a web browser on the computer and navigate to http://192.168.12.1 
9.​ Upload a firmware file and press ‘update firmware’. 
10.​Do not remove the power until the device has installed the firmware and fully 
booted.  You will see the following LED patterns to show progress: 
a.​ solid purple 
b.​ then red/purple flashing 
c.​ then solid purple 
d.​ then solid red 
e.​ then off (the device is rebooting) 
f.​ then yellow -> flashing -> solid (normal boot process) 
The entire process will take approximately 10 minutes to complete. 
39 | morsemicro.com.au​

## Page 40

13 Licensing and Source 
Much of the software included in the HaLowLink 1 is covered by open source licences, 
including the GPLv2. For complete licensing information, and access to the source code, 
go to http://morsemicro.com/halowlink1   
40 | morsemicro.com.au​

## Page 41

14 FCC compliance statement  
FCC ID: 2A74O-9A6140 
FCC compliance statement  
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) this device 
may not cause harmful interference, and (2) this device must accept any interference received, including interference 
that may cause undesired operation.  
changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority 
to operate the equipment.  
This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of 
the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential 
installation. This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in 
accordance with the instructions, may cause harmful interference to radio communications. However, there is no 
guarantee that interference will not occur in a particular installation.  
If this equipment does cause harmful interference to radio or television reception, which can be determined by turning 
the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following 
measures:  
-- Reorient or relocate the receiving antenna.  
-- Increase the separation between the equipment and receiver.  
-- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.  
-- Consult the dealer or an experienced radio/TV technician for help.  
FCC Radiation Exposure statement  
This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment. This equipment 
should be installed and operated with minimum distance 20cm between the radiator and your body. This transmitter 
must not be co-located or operating in conjunction with any other antenna or transmitter.  
41 | morsemicro.com.au​

## Page 42

15 IC compliance statement 
ISED compliance statement  
This device contains licence-exempt transmitter(s)/receiver(s) that comply with Innovation, Science and Economic 
Development Canada’s licence-exempt RSS(s). Operation is subject to the following two conditions:  
(1) This device may not cause interference.  
(2) This device must accept any interference, including interference that may cause undesired operation of the device.  
L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences 
et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée 
aux deux conditions suivantes :  
(1) L’appareil ne doit pas produire de brouillage;  
(2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre 
le fonctionnement.  
ISED Radiation Exposure statement  
This equipment complies with IC RSS-102 radiation exposure limits set forth for an uncontrolled environment. This 
equipment should be installed and operated with minimum distance 20 cm between the radiator and your body.  
Cet équipement est conforme aux limites d'exposition aux radiations IC CNR-102 établies pour un environnement non 
contrôlé. Cet équipement doit être installé et utilisé avec une distance minimale de 20 cm entre le radiateur et votre 
corps.  
This radio transmitter [29791-9A6140] has been approved by Innovation, Science and Economic Development 
Canada to operate with the antenna types listed below, with the maximum permissible gain indicated. Antenna types not 
included in this list that have a gain greater than the maximum gain indicated for any type listed are strictly prohibited for 
use with this device.  
Antenna Designation: Dipole Antenna, Gain: 2.34dBi 
Le présent émetteur radio [29791-9A6140] a été approuvé par Innovation, Sciences et Développement économique 
Canada pour fonctionner avec les types d'antenne énumérés ci-dessous et ayant un gain admissible maximal. Les types 
d'antenne non inclus dans cette liste, et dont le gain est supérieur au gain maximal indiqué pour tout type figurant sur la 
liste, sont strictement interdits pour l'exploitation de l'émetteur.  
Antenna Designation: Dipole Antenna, Gain: 2.34dBi 
 
42 | morsemicro.com.au​

## Page 43

43 | morsemicro.com.au​
