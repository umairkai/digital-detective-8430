# Mission 7 — How computers communicate

## 1. Task / objective
The objective of Mission 7 is to understand how computers communicate across networks:
- Define and explain fundamental computer networking concepts, scopes, hardware, and architectures.
- Use macOS Terminal networking utilities (`ping` and `nslookup`) to test network connectivity and perform domain name resolution on a public website.
- Explain the precise purpose and limitations of connectivity and DNS lookup tests.
- Trace the step-by-step lifecycle of opening a website in a browser using standard networking terminology.

---

## 2. Work completed

### Task 7.1 — Network concepts table

| Concept | Explain it in your own words | Example |
|---|---|---|
| **LAN (Local Area Network)** | A network connecting computers and devices across a small, localized physical area, typically sharing high bandwidth and common local equipment. | A home Wi-Fi network connecting laptops, phones, and a smart printer, or a college computer lab. |
| **MAN (Metropolitan Area Network)** | A network covering a larger geographic region than a LAN, such as an entire city, municipal area, or sprawling university campus. | A city-wide fiber network connecting municipal government offices, traffic cameras, and public libraries. |
| **WAN (Wide Area Network)** | A large-scale network connecting multiple smaller networks across vast geographic regions, countries, or continents. | The global Internet, or a multinational bank connecting branch offices worldwide. |
| **DNS (Domain Name System)** | A decentralized naming system that translates human-memorable domain names into machine-readable numeric IP addresses. | Translating `example.com` into the IP address `172.66.147.243`. |
| **Router** | A networking hardware device that connects distinct networks, inspects incoming data packet headers, and forwards them along the best path to their destination. | A home Wi-Fi broadband router connecting local home devices to the Internet Service Provider's network. |
| **Protocol** | A standardized set of rules and conventions that govern how devices format, transmit, verify, and receive data across a network. | HTTP/HTTPS for web browsing, TCP for reliable packet delivery, and IP for network addressing. |
| **Packet switching** | A data transmission method where digital messages are broken into smaller chunks (packets), routed independently across the network, and reassembled at the receiver. | Sending an image or email across the Internet where each packet may take different routes before arriving intact. |
| **Client-server** | A distributed computing architecture where user devices (clients) request services, data, or web pages from central host computers (servers). | A web browser (client) requesting a web page from a web hosting machine (server). |

---

### Task 7.2 — Observe network information

#### 1. Connectivity Test (`ping`):
Executed `ping -c 3 example.com` to test round-trip communication:
```text
$ ping -c 3 example.com
PING example.com (172.66.147.243): 56 data bytes
64 bytes from 172.66.147.243: icmp_seq=0 ttl=59 time=42.505 ms
64 bytes from 172.66.147.243: icmp_seq=1 ttl=59 time=47.481 ms
64 bytes from 172.66.147.243: icmp_seq=2 ttl=59 time=43.245 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 42.505/44.410/47.481/2.192 ms
```

#### 2. DNS Lookup (`nslookup`):
Executed `nslookup example.com` to resolve the IP address:
```text
$ nslookup example.com
Server:     [redacted-local-dns]
Address:    [redacted-local-dns]#53

Non-authoritative answer:
Name:   example.com
Address: 172.66.147.243
Name:   example.com
Address: 104.20.23.154
```

#### Observations and Questions:
- **What a connectivity test helps check:**  
  `ping` uses the ICMP (Internet Control Message Protocol) echo request/reply mechanism. It confirms whether the destination computer is reachable over the network, calculates round-trip latency in milliseconds, and detects packet loss.
- **What a connectivity test cannot establish:**  
  Ping operates at the Network Layer (Layer 3). It does not test whether an application service (such as an HTTP/HTTPS web server or database) is running or healthy. Additionally, many secure servers and corporate firewalls intentionally block ICMP pings for security reasons, so a ping may fail even when the website itself is fully operational.
- **What information a DNS lookup displays:**  
  `nslookup` shows the IP addresses (IPv4 / IPv6) assigned to a domain name, the specific DNS resolver that answered the request, and whether the answer came directly from the primary authoritative nameserver or from an intermediate cache (non-authoritative).
- **The role of DNS when entering a website name in a browser:**  
  DNS acts as the phonebook of the Internet. Because humans find domain names like `example.com` easy to remember while computers and network routers require numeric IP addresses (like `172.66.147.243`), DNS translates human names into the IP addresses required to establish a connection.

---

### Task 7.3 — What happens when you open a website?
A 6-step walkthrough describing what happens when a user opens `https://example.com`:

1. **User Request & URL Parsing (Client):**  
   The user types `https://example.com` into the web browser (**client**). The browser parses the URL to identify the application **protocol** (`HTTPS`), the domain name (`example.com`), and the requested resource path (`/`).
2. **Domain Name Resolution (DNS):**  
   The client checks its browser and operating system DNS caches. If the address is not cached, the client sends a lookup request to a recursive **DNS** server. The DNS server resolves `example.com` into the server's numeric IP address (`172.66.147.243`) and returns it to the client.
3. **Establishing Network Connection (Protocol & Router):**  
   Using the IP address, the client initiates a reliable TCP connection (via a 3-way handshake) and performs a TLS handshake to negotiate end-to-end encryption. Data packets travel from the client device through local Wi-Fi and intermediary network **routers** across the Internet to the destination.
4. **Sending HTTP Request (Client to Server):**  
   Once the encrypted channel is established, the client sends an `HTTP GET` request message over the network asking the **server** for the home page document.
5. **Processing & Response (Server):**  
   The web **server** receives the incoming packets, processes the request, locates the requested HTML file, and transmits an `HTTP 200 OK` response packet stream back across the network to the client.
6. **Rendering the Web Page (Client):**  
   The client's browser receives the response packets, checks for errors, parses the HTML, CSS, and JavaScript, and renders the visual web page on the user's screen.

---

## 3. Commands / tools used
- `ping -c 3 example.com`: Sent 3 ICMP echo request packets to measure latency and packet loss.
- `nslookup example.com`: Queried the DNS system to resolve domain IP addresses.
- macOS Network stack: Handled packet transmission and DNS queries.

---

## 4. My understanding
- Computer networks rely on hierarchical layers and standardized protocols to allow hardware from different manufacturers across the world to communicate seamlessly.
- DNS is a fundamental internet service; without it, navigating the web would require memorizing long, changing numeric IP strings.
- Packet switching makes the Internet resilient because packets can navigate around congested or broken network paths and reassemble cleanly at their destination.

---

## 5. Difficulties faced
- Running network commands inside restricted execution sandboxes blocked network queries until proper network access was verified.
- Ensuring local private IP addresses (such as local gateway/router addresses) were redacted from the `nslookup` output to protect network privacy.

---

## 6. How I resolved them
- Executed network testing with active network access enabled.
- Replaced local network addresses in the logs with privacy-safe placeholders (`[redacted-local-dns]`).

---

## 7. Evidence / files
- Mission documentation: `mission-07-networking/README.md`
- Network logs: Privacy-safe outputs of `ping -c 3 example.com` and `nslookup example.com`.

---

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Target branch:** `main`
- **Remote status:** Ready to stage, commit, and push to GitHub origin.
