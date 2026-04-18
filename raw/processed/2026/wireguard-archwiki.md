From the [WireGuard](https://www.wireguard.com/) project homepage:

WireGuard is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable.

A rough introduction to the main concepts used in this article can be found on [WireGuard's](https://www.wireguard.com/) project homepage. WireGuard has been included in the [Linux kernel](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=e7096c131e5161fa3b8e52a650d7719d2857adfd) since late 2019.

## Installation

[Install](https://wiki.archlinux.org/title/Install "Install") the [wireguard-tools](https://archlinux.org/packages/?name=wireguard-tools) package for userspace utilities.

Alternatively, various network managers provide support for WireGuard, provided that peer keys are available. See [#Persistent configuration](#Persistent_configuration) for details.

### Graphical clients

- **wireguird** — A linux GTK GUI client for WireGuard.

[https://github.com/UnnoTed/wireguird](https://github.com/UnnoTed/wireguird) || [wireguird](https://aur.archlinux.org/packages/wireguird/) <sup><small>AUR</small></sup>

- **wireguard-gui** — A wireguard client GUI for Linux made with nextauri.

[https://github.com/0xle0ne/wireguard-gui](https://github.com/0xle0ne/wireguard-gui) || [wireguard-gui-bin](https://aur.archlinux.org/packages/wireguard-gui-bin/) <sup><small>AUR</small></sup>

### Command-line tools

- **wg\_tool** — Tool to manage wireguard configs for server and users.

[https://github.com/gene-git/wg\_tool](https://github.com/gene-git/wg_tool) || [wg\_tool](https://aur.archlinux.org/packages/wg_tool/) <sup><small>AUR</small></sup>

- **wg-client** — Linux client with both command line and GUI.

[https://github.com/gene-git/wg-client](https://github.com/gene-git/wg-client) || [wg-client](https://aur.archlinux.org/packages/wg-client/) <sup><small>AUR</small></sup>

- **wg2nd** — A tool to convert WireGuard configurations from [wg-quick(8)](https://man.archlinux.org/man/wg-quick.8) format into [systemd-networkd](https://wiki.archlinux.org/title/Systemd-networkd "Systemd-networkd") compatible configurations.

[https://git.flu0r1ne.net/wg2nd/about](https://git.flu0r1ne.net/wg2nd/about) || [wg2nd](https://aur.archlinux.org/packages/wg2nd/) <sup><small>AUR</small></sup>

## Usage

The commands below demonstrate how to set up a basic tunnel between two or more peers with the following settings:

<table><tbody><tr><th rowspan="2"></th><th colspan="3">External (public) addresses</th><th colspan="2">Internal IP addresses</th><th rowspan="2">Port</th></tr><tr><th>Domain name</th><th>IPv4 address</th><th>IPv6 address</th><th>IPv4 address</th><th>IPv6 address</th></tr><tr><th>Peer A</th><td></td><td>198.51.100.101</td><td>2001:db8:a85b:70a:ffd4:ec1b:4650:a001</td><td>10.0.0.1/24</td><td>fdc9:281f:04d7:9ee9::1/64</td><td>UDP/51871</td></tr><tr><th>Peer B</th><td>peer-b.example</td><td>203.0.113.102</td><td>2001:db8:40f0:147a:80ad:3e88:f8e9:b002</td><td>10.0.0.2/24</td><td>fdc9:281f:04d7:9ee9::2/64</td><td>UDP/51902</td></tr><tr><th>Peer C</th><td></td><td><i>dynamic</i></td><td><i>dynamic</i></td><td>10.0.0.3/24</td><td>fdc9:281f:04d7:9ee9::3/64</td><td>UDP/51993</td></tr></tbody></table>

**Tip** The same UDP port can be used for all peers.

The external addresses should already exist. For example, if ICMP echo requests are not blocked, peer A should be able to [ping](https://wiki.archlinux.org/title/Ping "Ping") peer B via its public IP address(es) and vice versa.

The internal addresses will be new addresses, created either manually using the [ip(8)](https://man.archlinux.org/man/ip.8) utility or by network management software, which will be used internally within the new WireGuard network. The following examples will use [10.0.0.0/24](https://tools.ietf.org/html/rfc1918#section-3 "rfc:1918") and [fdc9:281f:04d7:9ee9::/64](https://wiki.archlinux.org/title/Router#Unique_Local_Addresses "Router") as the internal network. The `/24` and `/64` in the IP addresses is the [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation "wikipedia:Classless Inter-Domain Routing").

### Key generation

Create a private and public key for each peer. If connecting dozens of peers optionally consider a vanity keypair to personalize the Base64 encoded public key string. See [#Vanity keys](#Vanity_keys).

To create a private key run:

```
$ (umask 0077; wg genkey > peer_A.key)
```

**Note** It is recommended to only allow reading and writing access for the owner. The above alters the [umask](https://wiki.archlinux.org/title/Umask "Umask") temporarily within a sub-shell to ensure that access (read/write permissions) is restricted to the owner.

To create a public key:

```
$ wg pubkey < peer_A.key > peer_A.pub
```

Alternatively, do this all at once:

```
$ wg genkey | (umask 0077 && tee peer_A.key) | wg pubkey > peer_A.pub
```

One can also generate a pre-shared key to add an additional layer of symmetric-key cryptography to be mixed into the already existing public-key cryptography, for post-quantum resistance. A pre-shared key should be generated for each peer pair and should not be reused. For example, three interconnected peers, A, B, and, C will need three separate pre-shared keys, one for each peer pair.

Generate a pre-shared key for each peer pair using the following command (make sure to use `umask 0077` for this as well):

```
$ wg genpsk > peer_A-peer_B.psk
$ wg genpsk > peer_A-peer_C.psk
$ wg genpsk > peer_B-peer_C.psk
```

#### Vanity keys

Currently, WireGuard does not support comments or attaching human-memorable names to keys. This makes identifying the key's owner difficult particularly when multiple keys are in use. One solution is to generate a public key that contains some familiar characters (perhaps the first few letters of the owner's name or of the hostname etc.). [wireguard-vanity-address](https://archlinux.org/packages/?name=wireguard-vanity-address), or alternatively [wicuvanity](https://aur.archlinux.org/packages/wicuvanity/) <sup><small>AUR</small></sup>, do this.

For example:

```
$ wireguard-vanity-address --in 8 leslie
```
```
searching for 'leslie' in pubkey[0..10], one of every 214748364 keys should match
one core runs at 2.69e6 keys/s, CPU cores available: 16
est yield: 5.0 seconds per key, 200.10e-3 keys/s
hit Ctrl-C to stop
private wEoVMj92P+E3fQXVf9IixWJqpCqcnP/4OfvrB1g3zmY=  public LEsliEny+aMcWcRbh8Qf414XsQHSBOAFk3TaEk/aSD0=
private EAOwlGGqpHVbZ9ehaCspdBJt+lkMcCfkwiA5T5a4JFs=  public VlesLiEB5BFd//OD2ILKXviolfz+hodG6uZ+XjoalC8=
private UDWG4VWI+RzAGzNSnlC+0X4d3nk9goWPs/NRC5tX524=  public 9lESlieIFOlJFV6dG7Omao2WS+amWgshDdBYn8ahRjo=
```

### Manual configuration

#### Peer setup

Manual setup is accomplished by using [ip(8)](https://man.archlinux.org/man/ip.8) and [wg(8)](https://man.archlinux.org/man/wg.8).

**Note** These examples use the pre-shared keys which were introduced as *optional* in [#Key generation](#Key_generation). If not using them, simply ignore the corresponding parts in the commands.

**Peer A setup:**

In this example, peer A will listen on UDP port 51871 and will accept connection from peers B and C.

```
# ip link add dev wg0 type wireguard
# ip addr add 10.0.0.1/24 dev wg0
# ip addr add fdc9:281f:04d7:9ee9::1/64 dev wg0
# wg set wg0 listen-port 51871 private-key /path/to/peer_A.key
# wg set wg0 peer PEER_B_PUBLIC_KEY preshared-key /path/to/peer_A-peer_B.psk endpoint peer-b.example:51902 allowed-ips 10.0.0.2/32,fdc9:281f:04d7:9ee9::2/128
# wg set wg0 peer PEER_C_PUBLIC_KEY preshared-key /path/to/peer_A-peer_C.psk allowed-ips 10.0.0.3/32,fdc9:281f:04d7:9ee9::3/128
# ip link set wg0 up
```

`*PEER_X_PUBLIC_KEY*` should be the contents of `*peer_X*.pub`.

The keyword `allowed-ips` is a list of addresses that will get routed to the peer. Make sure to specify at least one address range that contains the WireGuard connection's internal IP address(es).

**Peer B setup:**

```
# ip link add dev wg0 type wireguard
# ip addr add 10.0.0.2/24 dev wg0
# ip addr add fdc9:281f:04d7:9ee9::2/64 dev wg0
# wg set wg0 listen-port 51902 private-key /path/to/peer_B.key
# wg set wg0 peer PEER_A_PUBLIC_KEY preshared-key /path/to/peer_A-peer_B.psk endpoint 198.51.100.101:51871 allowed-ips 10.0.0.1/32,fdc9:281f:04d7:9ee9::1/128
# wg set wg0 peer PEER_C_PUBLIC_KEY preshared-key /path/to/peer_B-peer_C.psk allowed-ips 10.0.0.3/32,fdc9:281f:04d7:9ee9::3/128
# ip link set wg0 up
```

**Peer C setup:**

```
# ip link add dev wg0 type wireguard
# ip addr add 10.0.0.3/24 dev wg0
# ip addr add fdc9:281f:04d7:9ee9::3/64 dev wg0
# wg set wg0 listen-port 51993 private-key /path/to/peer_C.key
# wg set wg0 peer PEER_A_PUBLIC_KEY preshared-key /path/to/peer_A-peer_C.psk endpoint 198.51.100.101:51871 allowed-ips 10.0.0.1/32,fdc9:281f:04d7:9ee9::1/128
# wg set wg0 peer PEER_B_PUBLIC_KEY preshared-key /path/to/peer_B-peer_C.psk endpoint peer-b.example:51902 allowed-ips 10.0.0.2/32,fdc9:281f:04d7:9ee9::2/128
# ip link set wg0 up
```

**Tip** To cleanly tear down the connection as well as deleting the interface, run
```
# ip link delete dev wg0
```
everywhere the previous commands were used.

#### Additional routes

To establish connections more complicated than point-to-point, additional setup is necessary.

##### Point-to-site

To access the network of a peer, specify the network subnet(s) in `allowed-ips` in the configuration of the peers who should be able to connect to it. E.g. `allowed-ips 10.0.0.2/32,fdc9:281f:04d7:9ee9::2/128,**192.168.35.0/24,fd7b:d0bd:7a6e::/64**`.

Make sure to also set up the [routing table](https://wiki.archlinux.org/title/Network_configuration#Routing_table "Network configuration") with [ip-route(8)](https://man.archlinux.org/man/ip-route.8). E.g.:

```
# ip route add 192.168.35.0/24 dev wg0
# ip route add fd7b:d0bd:7a6e::/64 dev wg0
```

##### Site-to-point

If the intent is to connect a device to a network with WireGuard peer(s), set up routes on each device so they know that the peer(s) are reachable via the device.

**Tip** Deploy routes network-wide by configuring them in the router. E.g., using [DHCP option](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol#Options "wikipedia:Dynamic Host Configuration Protocol") 121.

After that, [enable IP forwarding](https://wiki.archlinux.org/title/Internet_sharing#Enable_packet_forwarding "Internet sharing") on the peer through which other devices on the network will connect to WireGuard peer(s).

##### Site-to-site

To connect two (or more) networks, apply both [#Point-to-site](#Point-to-site) and [#Site-to-point](#Site-to-point) on all *sites*.

##### Routing all traffic over WireGuard

To route everything over the WireGuard tunnel, use:

```
# ip route add default dev wg0 table 2468
# wg set wg0 fwmark 1234
# ip rule add not fwmark 1234 table 2468 pref 10
```

In the first line, the default route is added to an alternative routing table (table 2468). The only purpose of this alternative routing table is to hand packets over to the wg0 interface.

In the second line, all outgoing packets handled by the wg0 interface are marked with a firewall mark.

In the third line, packets lacking this firewall mark are directed to the alternative routing table 2468, which routes them to the wg0 interface. `pref 10` indicates that this rule has priority 10. To list all rules with their corresponding priority, use `ip rule show`. These rules determine which routing table will be employed for a certain packets.

This implementation's main strength lies in its avoidance of using any endpoint. This is advantageous because WireGuard endpoints can roam. It is possible to define WireGuard peers without an endpoint.

The local access network will be inaccessible in this implementation. To whitelist LAN use:

```
# ip rule add suppress_prefixlength 0 table main pref 5
```

It's fairly straightforward to add things to the whitelist using [ip-rule(8)](https://man.archlinux.org/man/ip-rule.8). For instance, to give a certain user permission to send queries outside the WireGuard tunnel, use:

```
# ip rule add uidrange 955-955 table main pref 5
```

955 is the user ID of the user. The user IDs of all users can be found in `/etc/passwd`.

#### DNS

To use a peer as a DNS server, add its WireGuard tunnel IP address(es) to [/etc/resolv.conf](https://wiki.archlinux.org/title//etc/resolv.conf "/etc/resolv.conf"). For example, to use peer B as the DNS server:

```
/etc/resolv.conf
```
```
nameserver fdc9:281f:04d7:9ee9::2
nameserver 10.0.0.2
```

**Note** If a peer will act as a DNS server, make sure to use its WireGuard tunnel address(es) as the DNS server address(es) instead of another of its addresses from allowed IPs. Otherwise DNS lookups may fail.

### Basic checkups

Invoking the [wg(8)](https://man.archlinux.org/man/wg.8) command without parameters will give a quick overview of the current configuration.

As an example, when peer A has been configured we are able to see its identity and its associated peers:

```
# wg
```
```
interface: wg0
  public key: UguPyBThx/+xMXeTbRYkKlP0Wh/QZT3vTLPOVaaXTD8=
  private key: (hidden)
  listening port: 51871

peer: 9jalV3EEBnVXahro0pRMQ+cHlmjE33Slo9tddzCVtCw=
  endpoint: 203.0.113.102:51902
  allowed ips: 10.0.0.2/32, fdc9:281f:04d7:9ee9::2

peer: 2RzKFbGMx5g7fG0BrWCI7JIpGvcwGkqUaCoENYueJw4=
  endpoint: 192.0.2.103:51993
  allowed ips: 10.0.0.3/32, fdc9:281f:04d7:9ee9::3
```

At this point one could reach the end of the tunnel. If the peers do not block ICMP echo requests, try [pinging](https://wiki.archlinux.org/title/Ping "Ping") a peer to test the connection between them.

Using ICMPv4:

```
$ ping 10.0.0.2
```

Using ICMPv6:

```
$ ping fdc9:281f:04d7:9ee9::2
```

After transferring some data between peers, the `wg` utility will show additional information:

```
# wg
```
```
interface: wg0
  public key: UguPyBThx/+xMXeTbRYkKlP0Wh/QZT3vTLPOVaaXTD8=
  private key: (hidden)
  listening port: 51871

peer: 9jalV3EEBnVXahro0pRMQ+cHlmjE33Slo9tddzCVtCw=
  endpoint: 203.0.113.102:51902
  allowed ips: 10.0.0.2/32, fdc9:281f:04d7:9ee9::2
  latest handshake: 5 seconds ago
  transfer: 1.24 KiB received, 1.38 KiB sent

peer: 2RzKFbGMx5g7fG0BrWCI7JIpGvcwGkqUaCoENYueJw4=
  allowed ips: 10.0.0.3/32, fdc9:281f:04d7:9ee9::3
```

### Persistent configuration

Persistent configuration can be achieved using `wg-quick@.service`, which is shipped with [wireguard-tools](https://archlinux.org/packages/?name=wireguard-tools), or using a network manager. Network managers that support WireGuard are [systemd-networkd](https://wiki.archlinux.org/title/Systemd-networkd "Systemd-networkd"), [netctl](https://wiki.archlinux.org/title/Netctl "Netctl") [\[1\]](https://gitlab.archlinux.org/archlinux/netctl/blob/master/docs/examples/wireguard), [NetworkManager](https://wiki.archlinux.org/title/NetworkManager "NetworkManager") and [ConnMan](https://wiki.archlinux.org/title/ConnMan "ConnMan") [\[2\]](https://git.kernel.org/pub/scm/network/connman/connman.git/tree/doc/vpn-config-format.txt).

#### wg-quick

[wg-quick(8)](https://man.archlinux.org/man/wg-quick.8) configures WireGuard tunnels using configuration files from `/etc/wireguard/*interfacename*.conf`.

The current WireGuard configuration can be saved by utilizing the [wg(8)](https://man.archlinux.org/man/wg.8) utility's `showconf` command. For example:

```
# wg showconf wg0 > /etc/wireguard/wg0.conf
```

To start a tunnel with a configuration file, use

```
# wg-quick up interfacename
```

or use the systemd service— `wg-quick@*interfacename*.service`. To start the tunnel at boot, [enable](https://wiki.archlinux.org/title/Enable "Enable") the unit.

**Note**
- Users configuring the WireGuard interface using *wg-quick*, should make sure that no other [network management](https://wiki.archlinux.org/title/Network_management "Network management") software tries to manage it. To use [NetworkManager](https://wiki.archlinux.org/title/NetworkManager "NetworkManager") and to not configure WireGuard interfaces with it, see [#Routes are periodically reset](#Routes_are_periodically_reset).
- *wg-quick* adds additional configuration options to the configuration file format thus making it incompatible with [wg(8) § CONFIGURATION FILE FORMAT](https://man.archlinux.org/man/wg.8#CONFIGURATION_FILE_FORMAT). See the [wg-quick(8) § CONFIGURATION](https://man.archlinux.org/man/wg-quick.8#CONFIGURATION) man page for the configuration values in question. A *wg* -compatible configuration file can be produced by using `wg-quick strip`.
- *wg-quick* does not provide a way to instruct [resolvconf](https://wiki.archlinux.org/title/Resolvconf "Resolvconf") to set the WireGuard interface as *private*. Even if there are search domains specified, all DNS queries from the system, not just those that match the search domains, will be sent to the DNS servers which are set in the WireGuard configuration.

**Peer A setup:**

```
/etc/wireguard/wg0.conf
```
```
[Interface]
Address = 10.0.0.1/24, fdc9:281f:04d7:9ee9::1/64
ListenPort = 51871
PrivateKey = PEER_A_PRIVATE_KEY

[Peer]
PublicKey = PEER_B_PUBLIC_KEY
PresharedKey = PEER_A-PEER_B-PRESHARED_KEY
AllowedIPs = 10.0.0.2/32, fdc9:281f:04d7:9ee9::2/128
Endpoint = peer-b.example:51902

[Peer]
PublicKey = PEER_C_PUBLIC_KEY
PresharedKey = PEER_A-PEER_C-PRESHARED_KEY
AllowedIPs = 10.0.0.3/32, fdc9:281f:04d7:9ee9::3/128
```
- To *route all traffic* through the tunnel to a specific peer, add the [default route](https://en.wikipedia.org/wiki/Default_route "wikipedia:Default route") (`0.0.0.0/0` for IPv4 and `::/0` for IPv6) to `AllowedIPs`. E.g. `AllowedIPs = 0.0.0.0/0, ::/0`. wg-quick will automatically take care of setting up correct routing and fwmark [\[4\]](https://www.wireguard.com/netns/#routing-all-your-traffic) so that networking still functions.
- To use a peer as a DNS server, set `DNS = *wireguard_internal_ip_address_of_peer*` in the `[Interface]` section. [Search domains](https://en.wikipedia.org/wiki/Search_domain "wikipedia:Search domain") are also set with the `DNS =` option. Separate all values in the list with commas.

**Peer B setup:**

```
/etc/wireguard/wg0.conf
```
```
[Interface]
Address = 10.0.0.2/24, fdc9:281f:04d7:9ee9::2/64
ListenPort = 51902
PrivateKey = PEER_B_PRIVATE_KEY

[Peer]
PublicKey = PEER_A_PUBLIC_KEY
PresharedKey = PEER_A-PEER_B-PRESHARED_KEY
AllowedIPs = 10.0.0.1/32, fdc9:281f:04d7:9ee9::1/128
Endpoint = 198.51.100.101:51871

[Peer]
PublicKey = PEER_C_PUBLIC_KEY
PresharedKey = PEER_B-PEER_C-PRESHARED_KEY
AllowedIPs = 10.0.0.3/32, fdc9:281f:04d7:9ee9::3/128
```

**Peer C setup:**

```
/etc/wireguard/wg0.conf
```
```
[Interface]
Address = 10.0.0.3/24, fdc9:281f:04d7:9ee9::3/64
ListenPort = 51993
PrivateKey = PEER_C_PRIVATE_KEY

[Peer]
PublicKey = PEER_A_PUBLIC_KEY
PresharedKey = PEER_A-PEER_C-PRESHARED_KEY
AllowedIPs = 10.0.0.1/32, fdc9:281f:04d7:9ee9::1/128
Endpoint = 198.51.100.101:51871

[Peer]
PublicKey = PEER_B_PUBLIC_KEY
PresharedKey = PEER_B-PEER_C-PRESHARED_KEY
AllowedIPs = 10.0.0.2/32, fdc9:281f:04d7:9ee9::2/128
Endpoint = peer-b.example:51902
```

#### systemd-networkd

[systemd-networkd](https://wiki.archlinux.org/title/Systemd-networkd "Systemd-networkd") has native support for setting up WireGuard interfaces. An example is provided in the [systemd.netdev(5) § EXAMPLES](https://man.archlinux.org/man/systemd.netdev.5#EXAMPLES) man page.

**Note** Routing all DNS over WireGuard (i.e. `Domains=~.`) will prevent the DNS resolution of endpoints. Unless the peer domain is configured to be resolved on a specific network link.

**Peer A setup:**

```
/etc/systemd/network/99-wg0.netdev
```
```
[NetDev]
Name=wg0
Kind=wireguard
Description=WireGuard tunnel wg0

[WireGuard]
ListenPort=51871
PrivateKey=PEER_A_PRIVATE_KEY
RouteTable=main

[WireGuardPeer]
PublicKey=PEER_B_PUBLIC_KEY
PresharedKey=PEER_A-PEER_B-PRESHARED_KEY
AllowedIPs=10.0.0.2/32,fdc9:281f:04d7:9ee9::2/128
Endpoint=peer-b.example:51902

[WireGuardPeer]
PublicKey=PEER_C_PUBLIC_KEY
PresharedKey=PEER_A-PEER_C-PRESHARED_KEY
AllowedIPs=10.0.0.3/32,fdc9:281f:04d7:9ee9::3/128
```
```
/etc/systemd/network/99-wg0.network
```
```
[Match]
Name=wg0

[Network]
Address=10.0.0.1/24
Address=fdc9:281f:04d7:9ee9::1/64
```
- To use a peer as a DNS server, specify its WireGuard tunnel's IP address(es) in the *.network* file using the `DNS=` option. For [search domains](https://en.wikipedia.org/wiki/Search_domain "wikipedia:Search domain") use the `Domains=` option. See [systemd.network(5) § \[NETWORK\] SECTION OPTIONS](https://man.archlinux.org/man/systemd.network.5#%5BNETWORK%5D_SECTION_OPTIONS) for details.
- To use a peer as the **only** DNS server set `DNSDefaultRoute=true` and `Domains=~.` in the `[Network]` section of *.network* file's.
- To automatically create routes for everything in `AllowedIPs`, add `RouteTable=main` to the `[WireGuard]` or `[WireGuardPeer]` sections in the *.netdev* file. Alternatively, additional routes can be specified manually using `[Route]` sections in the *.network* file.

**Warning** In order to prevent the leaking of private and preshared keys, it is recommended to set the permissions of the *.netdev* file:
```
# chown root:systemd-network /etc/systemd/network/99-wg*.netdev
# chmod 0640 /etc/systemd/network/99-wg*.netdev
```

Alternatively, the keys can be stored in separate files and referenced with `PrivateKeyFile=`, `PresharedKeyFile=` and `PublicKeyFile=`, or they can be stored encrypted using [systemd-creds](https://wiki.archlinux.org/title/Systemd-creds "Systemd-creds"). See [#Using systemd credentials for private keys (systemd-networkd)](#Using_systemd_credentials_for_private_keys_\(systemd-networkd\)).

**Tip** To use the WireGuard interface name or IP addresses in [nftables rules via systemd-networkd's NFTSet option](https://wiki.archlinux.org/title/Nftables#Dynamic_named_sets_using_systemd-networkd "Nftables"), specify the addresses in `[Address]` sections instead of the `[Network]` section. E.g.:
```
/etc/systemd/network/99-wg0.network
```
```
...
[Address]
Address=10.0.0.1/24
NFTSet=address:inet:my_table:wg_ipv4_address
NFTSet=prefix:inet:my_table:wg_ipv4_prefix
NFTSet=ifindex:inet:my_table:wg_ifindex

[Address]
Address=fdc9:281f:04d7:9ee9::1/64
NFTSet=address:inet:my_table:wg_ipv6_address
NFTSet=prefix:inet:my_table:wg_ipv6_prefix
NFTSet=ifindex:inet:my_table:wg_ifindex
```

**Peer B setup:**

```
/etc/systemd/network/99-wg0.netdev
```
```
[NetDev]
Name=wg0
Kind=wireguard
Description=WireGuard tunnel wg0

[WireGuard]
ListenPort=51902
PrivateKey=PEER_B_PRIVATE_KEY
RouteTable=main

[WireGuardPeer]
PublicKey=PEER_A_PUBLIC_KEY
PresharedKey=PEER_A-PEER_B-PRESHARED_KEY
AllowedIPs=10.0.0.1/32,fdc9:281f:04d7:9ee9::1/128
Endpoint=198.51.100.101:51871

[WireGuardPeer]
PublicKey=PEER_C_PUBLIC_KEY
PresharedKey=PEER_B-PEER_C-PRESHARED_KEY
AllowedIPs=10.0.0.3/32,fdc9:281f:04d7:9ee9::3/128
```
```
/etc/systemd/network/99-wg0.network
```
```
[Match]
Name=wg0

[Network]
Address=10.0.0.2/24
Address=fdc9:281f:04d7:9ee9::2/64
```

**Peer C setup:**

```
/etc/systemd/network/99-wg0.netdev
```
```
[NetDev]
Name=wg0
Kind=wireguard
Description=WireGuard tunnel wg0

[WireGuard]
ListenPort=51993
PrivateKey=PEER_C_PRIVATE_KEY
RouteTable=main

[WireGuardPeer]
PublicKey=PEER_A_PUBLIC_KEY
PresharedKey=PEER_A-PEER_C-PRESHARED_KEY
AllowedIPs=10.0.0.1/32,fdc9:281f:04d7:9ee9::1/128
Endpoint=198.51.100.101:51871

[WireGuardPeer]
PublicKey=PEER_B_PUBLIC_KEY
PresharedKey=PEER_B-PEER_C-PRESHARED_KEY
AllowedIPs=10.0.0.2/32,fdc9:281f:04d7:9ee9::2/128
Endpoint=peer-b.example:51902
```
```
/etc/systemd/network/99-wg0.network
```
```
[Match]
Name=wg0

[Network]
Address=10.0.0.3/24
Address=fdc9:281f:04d7:9ee9::3/64
```

#### systemd-networkd: routing all traffic over WireGuard

In this example, Peer B connects to Peer A with a public IP address. Peer B routes all its traffic over the WireGuard tunnel and uses Peer A for handling DNS requests.

**Peer A setup**

```
/etc/systemd/network/99-wg0.netdev
```
```
[NetDev]
Name=wg0
Kind=wireguard
Description=WireGuard tunnel wg0

[WireGuard]
ListenPort=51871
PrivateKey=PEER_A_PRIVATE_KEY
RouteTable=main

[WireGuardPeer]
PublicKey=PEER_B_PUBLIC_KEY
PresharedKey=PEER_A-PEER_B-PRESHARED_KEY
AllowedIPs=10.0.0.2/32
AllowedIPs=fd31::2/128
```
```
/etc/systemd/network/99-wg0.network
```
```
[Match]
Name=wg0

[Network]
Address=10.0.0.1/32
Address=fd31::1/128
IPMasquerade=both
```

**Note** The `IPMasquerade=both` option enables IP forwarding on the WireGuard interface for both IPv4 and v6, sets up firewall rules for IP masquerading for it in order for Peer A to provide working internet to Peer B. Additionally:
- Enable [IP forwarding](https://wiki.archlinux.org/title/Internet_sharing#Enable_packet_forwarding "Internet sharing") for the interface that is used for connecting to the Internet (i.e. add `IPv4Forwarding=yes` to its *.network* file).
- Make sure that [the firewall does not block forwarding](https://wiki.archlinux.org/title/Internet_sharing#Enable_NAT "Internet sharing").
- Configure the local DNS server to accept connections to the WireGuard interface IP address. For systemd-resolved see [systemd-resolved#Additional listening interfaces](https://wiki.archlinux.org/title/Systemd-resolved#Additional_listening_interfaces "Systemd-resolved").
- To automatically create routes for everything in `AllowedIPs`, add `RouteTable=main` to the `[WireGuard]` or `[WireGuardPeer]` sections in the *.netdev* file.

**Peer B setup:**

```
/etc/systemd/network/99-wg0.netdev
```
```
[NetDev]
Name=wg0
Kind=wireguard
Description=WireGuard tunnel wg0

[WireGuard]
ListenPort=51902
PrivateKey=PEER_B_PRIVATE_KEY
FirewallMark=0x8888

[WireGuardPeer]
PublicKey=PEER_A_PUBLIC_KEY
PresharedKey=PEER_A-PEER_B-PRESHARED_KEY
AllowedIPs=0.0.0.0/0
AllowedIPs=::/0
# Endpoint=[2a01::1]:51871
Endpoint=198.51.100.101:51871
RouteTable=1000
```

  
In the netdev configuration, the most interesting lines are `RouteTable=1000` and `FirewallMark=0x8888`. The RouteTable line specifies that a new routing table with id 1000 is created for the wireguard interface, and no rules are set on the main routing table.

The FirewallMark simply marks all packets send and received by this wireguard interface with the number 0x8888, which can be used to define policy rules on these packets.

```
/etc/systemd/network/50-wg0.network
```
```
[Match]
Name=wg0

[Network]
Address=10.0.0.2/32
Address=fd31::2/128
DNS=10.0.0.1
DNS=fd31::1
DNSDefaultRoute=true
Domains=~.

[RoutingPolicyRule]
Family=both
FirewallMark=0x8888
InvertRule=true
Table=1000
Priority=10

# Exempt the endpoint IP address so that wireguard can still connect to it.
[RoutingPolicyRule]
#To = "2a01::1/128";
To=198.51.100.101/32
Priority=5
```

We define two routing policies here. For all packets \*not\* marked with 0x8888 (i.e. all non-wireguard/normal traffic), we specify that the routing table 1000 must be used (which is the wireguard routing table). This rule routes all traffic through wireguard.

We exempt our endpoint with a higher priority by routing it through the main table (`Table=main` is default).

**Exempting specific addresses**

In order to exempt specific addresses (such as private LAN addresses) from routing over the WireGuard tunnel, add them to another RoutingPolicyRule with higher priority.

```
/etc/systemd/network/50-wg0.network
```
```
...
[RoutingPolicyRule]
To=192.168.0.0/24
Priority=9
...
```

**Route for specific user**

It may be desirable to route WAN traffic over the tunnel only for a specific user, for example, the [transmission](https://wiki.archlinux.org/title/Transmission "Transmission") user in order to use the tunnel for torrent traffic.

```
/etc/systemd/network/99-wg0.network
```
```
...
[RoutingPolicyRule]
Table=1000
User=transmission
Priority=30001
Family=both

[RoutingPolicyRule]
Table=main
User=transmission
SuppressPrefixLength=0
Priority=30000
Family=both
...
```

The higher priority rule (30000), matches all traffic generated by the transmission user and routes it through the main table (no wireguard) BUT only using rules with a prefix length larger than 0. This excludes the default catch-all rule. Therefore, only traffic matching specific rules (such as those defining the subnet of your local home network) of the main table are routed through the main table.

The lower priority rule (30001), matches all traffic generated by the transmission user and routes it through table 1000 which is the wireguard table.

Note: these rules are to be put *instead* of the two rules defined at the start of this section to route all traffic through wireguard.

**Testing**

Test the proxy with

```
# ipv4
$ curl -4 zx2c4.com/ip

# ipv6
$ curl -6 zx2c4.com/ip
```

Check systemd-networkd log for any error and warning messages.

```
$ journalctl -u systemd-networkd.service
```

Invoke `wg` command from `wireguard-tools`.

#### Netctl

[Netctl](https://wiki.archlinux.org/title/Netctl "Netctl") has native support for setting up WireGuard interfaces. A typical set of WireGuard netctl profile configuration files would look like this:

**Peer A setup:**

```
/etc/netctl/wg0
```
```
Description="WireGuard tunnel on peer A"
Interface=wg0
Connection=wireguard
WGConfigFile=/etc/wireguard/wg0.conf

IP=static
Address=('10.0.0.1/24')
```
```
/etc/wireguard/wg0.conf
```
```
[Interface]
ListenPort = 51871
PrivateKey = PEER_A_PRIVATE_KEY

[Peer]
PublicKey = PEER_B_PUBLIC_KEY
AllowedIPs = 10.0.0.2/32
Endpoint = peer-b.example:51902

[Peer]
PublicKey = PEER_C_PUBLIC_KEY
AllowedIPs = 10.0.0.3/32
```

**Peer B setup:**

```
/etc/netctl/wg0
```
```
Description="WireGuard tunnel on peer B"
Interface=wg0
Connection=wireguard
WGConfigFile=/etc/wireguard/wg0.conf

IP=static
Address=('10.0.0.2/24')
```
```
/etc/wireguard/wg0.conf
```
```
[Interface]
ListenPort = 51902
PrivateKey = PEER_B_PRIVATE_KEY

[Peer]
PublicKey = PEER_A_PUBLIC_KEY
AllowedIPs = 10.0.0.1/32
Endpoint = peer-a.example:51871

[Peer]
PublicKey = PEER_C_PUBLIC_KEY
AllowedIPs = 10.0.0.3/32
```

**Peer C setup:**

```
/etc/netctl/wg0
```
```
Description="WireGuard tunnel on peer C"
Interface=wg0
Connection=wireguard
WGConfigFile=/etc/wireguard/wg0.conf

IP=static
Address=('10.0.0.3/24')
```
```
/etc/wireguard/wg0.conf
```
```
[Interface]
ListenPort = 51993
PrivateKey = PEER_C_PRIVATE_KEY

[Peer]
PublicKey = PEER_A_PUBLIC_KEY
AllowedIPs = 10.0.0.1/32
Endpoint = peer-a.example:51871

[Peer]
PublicKey = PEER_B_PUBLIC_KEY
AllowedIPs = 10.0.0.2/32
Endpoint = peer-b.example:51902
```

Then start and/or enable the wg0 interface on every participating peer as needed, i.e.

```
# netctl start wg0
```

To implement persistent site-to-peer, peer-to-site or site-to-site type of connection with WireGuard and Netctl, just add appropriate `Routes=` line into the netctl profile configuration file and add this network to `AllowedIPs` in the WireGuard profile, e.g. `Routes=('192.168.10.0/24 dev wg0')` in the `/etc/netctl/wg0` and `AllowedIPs=10.0.0.1/32, 192.168.10.0/24` in `/etc/wireguard/wg0.conf` and then do not forget to enable [IP forwarding](https://wiki.archlinux.org/title/Internet_sharing#Enable_packet_forwarding "Internet sharing").

#### NetworkManager

[NetworkManager](https://wiki.archlinux.org/title/NetworkManager "NetworkManager") has native support for setting up WireGuard interfaces. For all details about WireGuard usage in NetworkManager, read Thomas Haller's blog post— [WireGuard in NetworkManager](https://blogs.gnome.org/thaller/2019/03/15/wireguard-in-networkmanager/).

**Tip** NetworkManager can import a wg-quick configuration file. E.g.:
```
# nmcli connection import type wireguard file /etc/wireguard/wg0.conf
```

**Note** nmcli can create a WireGuard connection profile, but it does not support configuring peers. See [NetworkManager issue 358](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/issues/358).

The following examples configure WireGuard via the keyfile format *.nmconnection* files. See [nm-settings-keyfile(5)](https://man.archlinux.org/man/nm-settings-keyfile.5) and [nm-settings(5)](https://man.archlinux.org/man/nm-settings.5) for an explanation on the syntax and available options.

**Peer A setup:**

```
/etc/NetworkManager/system-connections/wg0.nmconnection
```
```
[connection]
id=wg0
type=wireguard
interface-name=wg0

[wireguard]
listen-port=51871
private-key=PEER_A_PRIVATE_KEY
private-key-flags=0

[wireguard-peer.PEER_B_PUBLIC_KEY]
endpoint=peer-b.example:51902
preshared-key=PEER_A-PEER_B-PRESHARED_KEY
preshared-key-flags=0
allowed-ips=10.0.0.2/32;fdc9:281f:04d7:9ee9::2/128;

[wireguard-peer.PEER_C_PUBLIC_KEY]
preshared-key=PEER_A-PEER_C-PRESHARED_KEY
preshared-key-flags=0
allowed-ips=10.0.0.3/32;fdc9:281f:04d7:9ee9::3/128;

[ipv4]
address1=10.0.0.1/24
method=manual

[ipv6]
address1=fdc9:281f:04d7:9ee9::1/64
method=manual
```
- To *route all traffic* through the tunnel to a specific peer, add the [default route](https://en.wikipedia.org/wiki/Default_route "wikipedia:Default route") (`0.0.0.0/0` for IPv4 and `::/0` for IPv6) to `wireguard-peer.*PEER_X_PUBLIC_KEY*.allowed-ips`. E.g. `wireguard-peer.*PEER_B_PUBLIC_KEY*.allowed-ips=0.0.0.0/0;::/0;`. Special handling of the default route in WireGuard connections is supported since NetworkManager 1.20.0.
- To use a peer as a DNS server, specify its WireGuard tunnel's IP address(es) with the `ipv4.dns` and `ipv6.dns` settings. [Search domains](https://en.wikipedia.org/wiki/Search_domain "wikipedia:Search domain") can be specified with the `ipv4.dns-search=` and `ipv6.dns-search=` options. See [nm-settings(5)](https://man.archlinux.org/man/nm-settings.5) for more details. For example, using the keyfile format:
```
...
[ipv4]
...
dns=10.0.0.2;
dns-search=corp;
...
[ipv6]
...
dns=fdc9:281f:04d7:9ee9::2;
dns-search=corp;
...
```

To use a peer as the **only** DNS server, set a negative DNS priority (e.g. `dns-priority=-1`) and add `~.` to the `dns-search=` settings.

**Peer B setup:**

```
/etc/NetworkManager/system-connections/wg0.nmconnection
```
```
[connection]
id=wg0
type=wireguard
interface-name=wg0

[wireguard]
listen-port=51902
private-key=PEER_B_PRIVATE_KEY
private-key-flags=0

[wireguard-peer.PEER_A_PUBLIC_KEY]
endpoint=198.51.100.101:51871
preshared-key=PEER_A-PEER_B-PRESHARED_KEY
preshared-key-flags=0
allowed-ips=10.0.0.1/32;fdc9:281f:04d7:9ee9::1/128;

[wireguard-peer.PEER_C_PUBLIC_KEY]
preshared-key=PEER_B-PEER_C-PRESHARED_KEY
preshared-key-flags=0
allowed-ips=10.0.0.3/32;fdc9:281f:04d7:9ee9::3/128;

[ipv4]
address1=10.0.0.2/24
method=manual

[ipv6]
address1=fdc9:281f:04d7:9ee9::2/64
method=manual
```

**Peer C setup:**

```
/etc/NetworkManager/system-connections/wg0.nmconnection
```
```
[connection]
id=wg0
type=wireguard
interface-name=wg0

[wireguard]
listen-port=51993
private-key=PEER_C_PRIVATE_KEY
private-key-flags=0

[wireguard-peer.PEER_A_PUBLIC_KEY]
endpoint=198.51.100.101:51871
preshared-key=PEER_A-PEER_C-PRESHARED_KEY
preshared-key-flags=0
allowed-ips=10.0.0.1/32;fdc9:281f:04d7:9ee9::1/128;

[wireguard-peer.PEER_B_PUBLIC_KEY]
endpoint=peer-b.example:51902
preshared-key=PEER_B-PEER_C-PRESHARED_KEY
preshared-key-flags=0
allowed-ips=10.0.0.2/32;fdc9:281f:04d7:9ee9::2/128;

[ipv4]
address1=10.0.0.3/24
method=manual

[ipv6]
address1=fdc9:281f:04d7:9ee9::3/64
method=manual
```

## Specific use-case: VPN server

**Note** Usage of the terms "server" and "client" were purposefully chosen in this section specifically to help new users/existing OpenVPN users become familiar with the construction of WireGuard's configuration files. WireGuard documentation simply refers to both of these concepts as "peers."

The purpose of this section is to set up a WireGuard "server" and generic "clients" to enable access to the server/network resources through an encrypted and secured tunnel like [OpenVPN](https://wiki.archlinux.org/title/OpenVPN "OpenVPN") and others. The "server" runs on Linux and the "clients" can run on any number of platforms (the WireGuard Project offers apps on both iOS and Android platforms in addition to Linux, Windows and MacOS). See the official project [install link](https://www.wireguard.com/install/) for more.

**Tip** Instead of using [wireguard-tools](https://archlinux.org/packages/?name=wireguard-tools) for server/client configuration, one may also use [systemd-networkd](#systemd-networkd) native WireGuard support.

### Server

On the peer that will act as the "server", first [enable IPv4 forwarding](https://wiki.archlinux.org/title/Internet_sharing#Enable_packet_forwarding "Internet sharing").

If the server has a public IP configured, be sure to:

- Allow UDP traffic on the specified port(s) on which WireGuard will be running (for example allowing traffic on `51820/UDP`).
- Setup the forwarding policy for the firewall if it is not included in the WireGuard configuration for the interface itself `/etc/wireguard/wg0.conf`. The example below should have the iptables rules and work as-is.

If the server is behind NAT, be sure to forward the specified port(s) on which WireGuard will be running (for example, `51820/UDP`) from the router to the WireGuard server.

### Key generation

Generate key pairs for the server and for each client as explained in [#Key generation](#Key_generation).

### Server configuration

Create the "server" configuration file:

```
/etc/wireguard/wg0.conf
```
```
[Interface]
Address = 10.200.200.1/24
ListenPort = 51820
PrivateKey = SERVER_PRIVATE_KEY

# substitute eth0 in the following lines to match the Internet-facing interface
# the FORWARD rules will always be needed since traffic needs to be forwarded between the WireGuard
# interface and the other interfaces on the server.
# if the server is behind a router and receives traffic via NAT, specify static routing back to the
# 10.200.200.0/24 subnet, the NAT iptables rules are not needed but the FORWARD rules are needed.
# if the server is behind a router and receives traffic via NAT but one cannot specify static routing back to
# 10.200.200.0/24 subnet, both the NAT and FORWARD iptables rules are needed. 
PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -A FORWARD -o %i -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -D FORWARD -o %i -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
# foo
PublicKey = PEER_FOO_PUBLIC_KEY
PresharedKey = PRE-SHARED_KEY
AllowedIPs = 10.200.200.2/32

[Peer]
# bar
PublicKey = PEER_BAR_PUBLIC_KEY
PresharedKey = PRE-SHARED_KEY
AllowedIPs = 10.200.200.3/32
```

Additional peers ("clients") can be listed in the same format as needed. Each peer requires the `PublicKey` to be set. However, specifying `PresharedKey` is optional.

Notice that the `Address` has a netmask of `/24` and the clients on `AllowedIPs` `/32`. The clients only use their IP and the server only sends back their respective addresses.

The interface can be managed manually using [wg-quick(8)](https://man.archlinux.org/man/wg-quick.8) or using a [systemd](https://wiki.archlinux.org/title/Systemd "Systemd") service managed via [systemctl(1)](https://man.archlinux.org/man/systemctl.1).

The interface may be brought up using `wg-quick up wg0` respectively by [starting](https://wiki.archlinux.org/title/Start "Start") and potentially [enabling](https://wiki.archlinux.org/title/Enable "Enable") the interface via `wg-quick@*interface*.service`, e.g. `wg-quick@wg0.service`. To close the interface use `wg-quick down wg0` respectively [stop](https://wiki.archlinux.org/title/Stop "Stop") `wg-quick@*interface*.service`.

### Client configuration

Create the corresponding "client" configuration file(s):

```
foo.conf
```
```
[Interface]
Address = 10.200.200.2/32
PrivateKey = PEER_FOO_PRIVATE_KEY
DNS = 10.200.200.1

[Peer]
PublicKey = SERVER_PUBLICKEY
PresharedKey = PRE-SHARED_KEY
Endpoint = my.ddns.example.com:51820
AllowedIPs = 0.0.0.0/0, ::/0
```
```
bar.conf
```
```
[Interface]
Address = 10.200.200.3/32
PrivateKey = PEER_BAR_PRIVATE_KEY
DNS = 10.200.200.1

[Peer]
PublicKey = SERVER_PUBLICKEY
PresharedKey = PRE-SHARED KEY
Endpoint = my.ddns.example.com:51820
AllowedIPs = 0.0.0.0/0, ::/0
```

Using the catch-all `AllowedIPs = 0.0.0.0/0, ::/0` will forward all IPv4 (`0.0.0.0/0`) and IPv6 (`::/0`) traffic over the VPN.

**Note** Users of [NetworkManager](https://wiki.archlinux.org/title/NetworkManager "NetworkManager"), may need to [enable](https://wiki.archlinux.org/title/Enable "Enable") the `NetworkManager-wait-online.service` and users of [systemd-networkd](https://wiki.archlinux.org/title/Systemd-networkd "Systemd-networkd") may need to [enable](https://wiki.archlinux.org/title/Enable "Enable") the `systemd-networkd-wait-online.service` to wait until devices are network-ready before attempting a WireGuard connection.

## Testing the tunnel

Once a tunnel has been established, one can use [netcat](https://wiki.archlinux.org/title/Netcat "Netcat") to send traffic through it to test out throughput, CPU usage, etc. On one side of the tunnel, run `nc` in listen mode and on the other side, pipe some data from `/dev/zero` into `nc` in sending mode.

In the example below, port 2222 is used for the traffic (be sure to allow traffic on port 2222 if using a firewall).

On one side of the tunnel listen for traffic:

```
$ nc -vvlnp 2222
```

On the other side of the tunnel, send some traffic:

```
$ dd if=/dev/zero bs=1024K count=1024 | nc -v 10.0.0.203 2222
```

Status can be monitored using `wg` directly.

```
# wg
```
```
interface: wg0
  public key: UguPyBThx/+xMXeTbRYkKlP0Wh/QZT3vTLPOVaaXTD8=
  private key: (hidden)
  listening port: 51820

peer: 9jalV3EEBnVXahro0pRMQ+cHlmjE33Slo9tddzCVtCw=
  preshared key: (hidden)
  endpoint: 192.168.1.216:53207
  allowed ips: 10.0.0.0/0
  latest handshake: 1 minutes, 17 seconds ago
  transfer: 56.43 GiB received, 1.06 TiB sent
```

## Tips and tricks

### Store private keys in encrypted form (wg-quick)

It may be desirable to store private keys in encrypted form, such as through use of [pass](https://archlinux.org/packages/?name=pass). Just replace the `PrivateKey` line under `[Interface]` in the WireGuard configuration file with:

```
PostUp = wg set %i private-key <(su user -c "export PASSWORD_STORE_DIR=/path/to/your/store/; pass WireGuard/private-keys/%i")
```

where *user* is the Linux username of interest. See the [wg-quick(8)](https://man.archlinux.org/man/wg-quick.8) man page for more details.

Alternatively, [systemd-creds](https://wiki.archlinux.org/title/Systemd-creds "Systemd-creds") can be used. This can be helpful to create encrypted private keys that are bound to the system's [TPM](https://wiki.archlinux.org/title/TPM "TPM"). See [systemd-creds(1)](https://man.archlinux.org/man/systemd-creds.1) for more details.

First, create an encrypted credential:

```
# echo -n your_wg_private_key | systemd-creds --tpm2-device=auto encrypt - /etc/credstore.encrypted/wg-private-key.cred
```

Finally, replace the `PrivateKey` line under `[Interface]` in the WireGuard configuration file with:

```
PostUp = wg set %i private-key <(systemd-creds decrypt /etc/credstore.encrypted/wg-private-key.cred)
```

### Using systemd credentials for private keys (systemd-networkd)

You can use [systemd-creds](https://wiki.archlinux.org/title/Systemd-creds "Systemd-creds") to store your private keys encrypted.

```
# echo -n your_wg_private_key | systemd-creds encrypt - /etc/credstore.encrypted/network.wireguard.private.wg0
# echo -n your_pre_shared_key | systemd-creds encrypt - /etc/credstore.encrypted/network.wireguard.psk.wg0
```

**Note** The name of the store must match `network.wireguard.*`. See [systemd.netdev(5) § \[WIREGUARD\]\_SECTION\_OPTIONS](https://man.archlinux.org/man/systemd.netdev.5#%5BWIREGUARD%5D_SECTION_OPTIONS).

Modify your *.netdev* file to use

```
PrivateKey = @network.wireguard.private.wg0
PresharedKey = @network.wireguard.psk.wg0
```

### Endpoint with changing IP

After resolving a server's domain, WireGuard [will not check for changes in DNS again](https://lists.zx2c4.com/pipermail/wireguard/2017-November/002028.html).

If the WireGuard server is frequently changing its IP-address due DHCP, [Dyndns](https://wiki.archlinux.org/title/Dyndns "Dyndns"), IPv6, etc., any WireGuard client is going to lose its connection, until its endpoint is updated via something like `wg set "$INTERFACE" peer "$PUBLIC_KEY" endpoint "$ENDPOINT"`.

Also be aware, if the endpoint is ever going to change its address (for example when moving to a new provider/datacenter), just updating DNS will not be enough, so periodically running reresolve-dns might make sense on any DNS-based setup.

Luckily, [wireguard-tools](https://archlinux.org/packages/?name=wireguard-tools) provides an example script `/usr/share/wireguard-tools/examples/reresolve-dns/reresolve-dns.sh`, that parses WG configuration files and automatically resets the endpoint address.

One needs to run the `/usr/share/wireguard-tools/examples/reresolve-dns/reresolve-dns.sh /etc/wireguard/wg.conf` periodically to recover from an endpoint that has changed its IP.

One way of doing so is by updating all WireGuard endpoints once every thirty seconds [\[5\]](https://git.zx2c4.com/WireGuard/tree/contrib/examples/reresolve-dns/README) via a systemd timer:

```
/etc/systemd/system/wireguard_reresolve-dns.timer
```
```
[Unit]
Description=Periodically reresolve DNS of all WireGuard endpoints

[Timer]
OnCalendar=*:*:0/30

[Install]
WantedBy=timers.target
```
```
/etc/systemd/system/wireguard_reresolve-dns.service
```
```
[Unit]
Description=Reresolve DNS of all WireGuard endpoints
Wants=network-online.target
After=network-online.target nss-lookup.target

[Service]
Type=oneshot
ExecStart=/bin/sh -c 'for i in /etc/wireguard/*.conf; do /usr/share/wireguard-tools/examples/reresolve-dns/reresolve-dns.sh "$i"; done'
```

Afterwards [enable](https://wiki.archlinux.org/title/Enable "Enable") and [start](https://wiki.archlinux.org/title/Start "Start") `wireguard_reresolve-dns.timer`

If the client is a mobile device such as a phone, [qrencode](https://archlinux.org/packages/?name=qrencode) can be used to generate client's configuration QR code and display it in terminal:

```
$ qrencode -t ansiutf8 -r client.conf
```

### Enable debug logs

When using the Linux kernel module on a kernel that supports [dynamic debug](https://docs.kernel.org/admin-guide/dynamic-debug-howto.html), debugging information can be written into the kernel ring buffer (viewable with [dmesg](https://wiki.archlinux.org/title/Dmesg "Dmesg") and [journalctl](https://wiki.archlinux.org/title/Journalctl "Journalctl")) by running:

```
# modprobe wireguard
# echo module wireguard +p > /sys/kernel/debug/dynamic_debug/control
```

### Reload peer (server) configuration

In case the WireGuard peer (mostly server) adding or removing another peers from its configuration and wants to reload it without stopping any active sessions, one can execute the following command to do it:

```
# wg syncconf ${WGNET} <(wg-quick strip ${WGNET})
```

Where `$WGNET` is WireGuard interface name or configuration base name, for example `wg0` (for server) or `client` (without the *.conf* extension, for client).

Users of `wg-quick@.service` can simply [reload](https://wiki.archlinux.org/title/Reload "Reload") the service.

### Workaround for some public Wi-Fi networks seemingly blocking WireGuard connections

**Note** This workaround will only be an option if a cellular connection is available on the device.

Some Wi-Fi networks can be configured to actively identify and block WireGuard's handshake thus preventing the initial connection and preventing the establishment of the secure tunnel.

This strategy works for blocking *new* WireGuard connections but it is useless against *existing* connections. Therefore, to use WireGuard on such a network, simply connect to the WireGuard peer over cellular before joining the Wi-Fi network thus allowing the handshake to take place before the active blocking can occur. WireGuard will keep this tunnel open as the devices transitions from cellular to Wi-Fi.

## Troubleshooting

### Routes are periodically reset

Users of [NetworkManager](https://wiki.archlinux.org/title/NetworkManager "NetworkManager") should make sure that it [is not managing](https://wiki.archlinux.org/title/NetworkManager#Ignore_specific_devices "NetworkManager") the WireGuard interface(s). For example, create the following configuration file:

```
/etc/NetworkManager/conf.d/unmanaged.conf
```
```
[keyfile]
unmanaged-devices=type:wireguard
```

### Broken DNS resolution

When tunneling all traffic through a WireGuard interface, the connection can become seemingly lost after a while or upon new connection. This could be caused by a [network manager](https://wiki.archlinux.org/title/Network_manager "Network manager") or [DHCP](https://wiki.archlinux.org/title/DHCP "DHCP") client overwriting `/etc/resolv.conf`.

By default *wg-quick* uses *resolvconf* to register new [DNS](https://wiki.archlinux.org/title/DNS "DNS") entries (from the `DNS` keyword in the configuration file). This will cause issues with [network managers](https://wiki.archlinux.org/title/Network_manager "Network manager") and [DHCP](https://wiki.archlinux.org/title/DHCP "DHCP") clients that do not use *resolvconf*, as they will overwrite `/etc/resolv.conf` thus removing the DNS servers added by wg-quick.

The solution is to use networking software that supports [resolvconf](https://wiki.archlinux.org/title/Resolvconf "Resolvconf").

**Note** Users of [systemd-resolved](https://wiki.archlinux.org/title/Systemd-resolved "Systemd-resolved") should make sure that [systemd-resolvconf](https://archlinux.org/packages/?name=systemd-resolvconf) is [installed](https://wiki.archlinux.org/title/Install "Install").

Users of [NetworkManager](https://wiki.archlinux.org/title/NetworkManager "NetworkManager") should know that it does not use resolvconf by default. It is recommended to use [systemd-resolved](https://wiki.archlinux.org/title/Systemd-resolved "Systemd-resolved"). If this is undesirable, [install](https://wiki.archlinux.org/title/Install "Install") [openresolv](https://archlinux.org/packages/?name=openresolv) and configure NetworkManager to use it: [NetworkManager#Use openresolv](https://wiki.archlinux.org/title/NetworkManager#Use_openresolv "NetworkManager").

### Adjusting the MTU value

A default Wireguard maximum transmission unit (MTU) value is `1420`.

Due to a too low MTU (lower than `1280`), wg-quick may have failed to create the WireGuard interface. This can be solved by setting the MTU value in WireGuard configuration in Interface section on client.

```
foo.config
```
```
[Interface]
Address = 10.200.200.2/24
MTU = 1420
PrivateKey = PEER_FOO_PRIVATE_KEY
DNS = 10.200.200.1
```

Depending on your network, a lower MTU value can also make your WireGuard connection work.

In certain cases larger MTU values can lead to unstable or intermittent connection because of unreliable [Path MTU discovery (PMTU)](https://tldp.org/HOWTO/Adv-Routing-HOWTO/lartc.cookbook.mtu-mss.html) along the route. Which may lead to situations where ICMP ping works because of its low packet size, but most of TCP connections fail because of full MTU size utilization. For example, an IPv6 connection has a higher packet overhead than IPv4, hence fragmentation may occur earlier with the same MTU value.

It is worth checking the links MTU size on both peers and other routers involved to determine the minimum value.

```
# ip link show
```
```
5: wg0: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 1400 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
link/none
```

Another option is falling back to a MTU of `1280` and finding appropriate value for given path with a trial/error approach.

An MTU of `1420` and above can lead to partially broken links which could be interpreted as a firewall or routing issue instead of actual MTU size.

### Key is not the correct length or format

To avoid the following error, put the key value in the configuration file and not the path to the key file.

```
# wg-quick up wg0
```
```
[#] ip link add wg0 type wireguard
[#] wg setconf wg0 /dev/fd/63
Key is not the correct length or format: \`/path/example.key'
Configuration parsing error
[#] ip link delete dev wg0
```

### Unable to establish a persistent connection behind NAT / firewall

By default, WireGuard peers remain silent while they do not need to communicate, so peers located behind a NAT and/or [firewall](https://wiki.archlinux.org/title/Firewall "Firewall") may be unreachable from other peers until they reach out to other peers themselves (or the connection may time out). Adding `PersistentKeepalive = 25` to the `[Peer]` settings of a peer located behind a NAT and/or firewall can ensure that the connection remains open.

To temporarily set the persistent-keepalive setting via command line, run the following command:

```
# wg set wg0 peer public_key persistent-keepalive 25
```

### Loop routing

Adding the endpoint IP to the allowed IPs list, the kernel will attempt to send handshakes to said device binding, rather than using the original route. This results in failed handshake attempts.

As a workaround, the correct route to the endpoint needs to be manually added using

```
# ip route add endpoint_ip via gateway dev network_interface
```

E.g. for peer B from above in a standard LAN setup:

```
# ip route add 203.0.113.102 via 192.168.0.1 dev eth0
```

To make this route persistent, the command can be added as `PostUp = ip route ...` to the `[Interface]` section of `wg0.conf`. However, on certain setups (e.g. using `wg-quick@.service` in combination with NetworkManager) this might fail on resume. Furthermore, this only works for a static network setup and fails if gateways or devices change (e.g. using Ethernet or Wi-Fi on a laptop).

Using NetworkManager, a more flexible solution is to start WireGuard using a dispatcher script. As root, create

```
/etc/NetworkManager/dispatcher.d/50-wg0.sh
```
```
#!/bin/sh
case $2 in
  up)
    wg-quick up wg0
    ip route add <endpoint ip> via $IP4_GATEWAY dev $DEVICE_IP_IFACE
    ;;
  pre-down)
    wg-quick down wg0
    ;;
esac
```

If not already running, start and enable `NetworkManager-dispatcher.service`. Also make sure that NetworkManager is not managing routes for `wg0`, see [#Routes are periodically reset](#Routes_are_periodically_reset).

### Connection lost after sleep using systemd-networkd

[systemd](https://wiki.archlinux.org/title/Systemd "Systemd") version 253 introduced a change in how network interfaces are reconfigured when resuming from a suspended state [\[6\]](https://github.com/systemd/systemd/commit/a39a9ac8065c29330207838b70fe388bde2bc254). In doing so, network connections managed by [systemd-networkd](https://wiki.archlinux.org/title/Systemd-networkd "Systemd-networkd") will lose connection to the WireGuard interface. Unless a kill switch is configured, this risks exposing the public IP address after resuming from suspension. To fix this, uncomment and change the value to `no` for `ManageForeignRoutingPolicyRules` in `/etc/systemd/networkd.conf`.[\[7\]](https://github.com/systemd/systemd/issues/26665#issuecomment-1454353725) If your WireGuard interface uses the `fwmark` setting, you may also need to set `ManageForeignRoutes` to `no`.