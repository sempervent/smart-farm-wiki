---
title: "Lorawan Specification V1 1 (extracted from PDF)"
source_pdf: raw/processed/2026/lorawan-specification-v1-1.pdf
extracted: 2026-04-18
page_count: 101
note: Machine-extracted text; verify against the PDF for tables, figures, and typography.
---

# Lorawan Specification V1 1

**Source PDF:** [`lorawan-specification-v1-1.pdf`](./lorawan-specification-v1-1.pdf) — repo path `/raw/processed/2026/lorawan-specification-v1-1.pdf`


## Page 1

©2017 LoRa Alliance™ 
Page 1 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
1 
LoRaWAN™ 1.1 Specification 
2 
Copyright © 2017 LoRa Alliance, Inc.  All rights reserved. 
3 
 
4 
NOTICE OF USE AND DISCLOSURE 
5 
Copyright © LoRa Alliance, Inc. (2017). All Rights Reserved.  
6 
 
7 
The information within this document is the property of the LoRa Alliance (“The Alliance”) and its use and disclosure are 
8 
subject to LoRa Alliance Corporate Bylaws, Intellectual Property Rights (IPR) Policy and Membership Agreements. 
9 
 
10 
Elements of LoRa Alliance specifications may be subject to third party intellectual property rights, including without 
11 
limitation, patent, copyright or trademark rights (such a third party may or may not be a member of LoRa Alliance). The 
12 
Alliance is not responsible and shall not be held responsible in any manner for identifying or failing to identify any or all 
13 
such third party intellectual property rights. 
14 
 
15 
This document and the information contained herein are provided on an “AS IS” basis and THE ALLIANCE DISCLAIMS 
16 
ALL WARRANTIES EXPRESS OR IMPLIED, INCLUDING BUT NOTLIMITED TO (A) ANY WARRANTY THAT 
17 
THE USE OF THE INFORMATION HEREINWILL NOT INFRINGE ANY RIGHTS OF THIRD PARTIES 
18 
(INCLUDING WITHOUTLIMITATION ANY INTELLECTUAL PROPERTY RIGHTS INCLUDING PATENT, 
19 
COPYRIGHT OR TRADEMARK RIGHTS) OR (B) ANY IMPLIED WARRANTIES OF MERCHANTABILITY, 
20 
FITNESS FOR A PARTICULAR PURPOSE,TITLE OR NONINFRINGEMENT. 
21 
 
22 
IN NO EVENT WILL THE ALLIANCE BE LIABLE FOR ANY LOSS OF PROFITS, LOSS OF BUSINESS, LOSS OF 
23 
USE OF DATA, INTERRUPTION OFBUSINESS, OR FOR ANY OTHER DIRECT, INDIRECT, SPECIAL OR 
24 
EXEMPLARY, INCIDENTIAL, PUNITIVE OR CONSEQUENTIAL DAMAGES OF ANY KIND, IN CONTRACT OR 
25 
IN TORT, IN CONNECTION WITH THIS DOCUMENT OR THE INFORMATION CONTAINED HEREIN, EVEN IF 
26 
ADVISED OF THE POSSIBILITY OF SUCH LOSS OR DAMAGE.  
27 
 
28 
 
29 
The above notice and this paragraph must be included on all copies of this document that are made. 
30 
 
31 
LoRa Alliance, Inc. 
32 
3855 SW 153rd Drive 
33 
Beaverton, OR  97003 
34 
 
35 
Note: All Company, brand and product names may be trademarks that are the sole property of their respective owners. 
36 
 
37 
 
38 
39

## Page 2

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 2 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
40 
 
41 
LoRaWAN™ 1.1 Specification 
42 
 
43 
Authored by the LoRa Alliance Technical Committee  
44 
 
45 
Chairs: 
46 
N.SORNIN (Semtech), A.YEGIN (Actility) 
47 
 
48 
Editor: 
49 
N.SORNIN (Semtech) 
50 
 
51 
Contributors: 
52 
A.BERTOLAUD (Gemalto), J.DELCLEF (ST Microelectronics), V.DELPORT (Microchip 
53 
Technology), P.DUFFY (Cisco), F.DYDUCH (Bouygues Telecom), T.EIRICH (TrackNet), 
54 
L.FERREIRA (Orange), S.GHAROUT(Orange), O.HERSENT (Actility), A.KASTTET 
55 
(Homerider Systems), D.KJENDAL (Senet), V.KLEBAN (Everynet), J.KNAPP (TrackNet), 
56 
T.KRAMP (TrackNet), M.KUYPER (TrackNet), P.KWOK (Objenious), M.LEGOURIEREC 
57 
(Sagemcom), C.LEVASSEUR (Bouygues Telecom), M.LUIS (Semtech), M.PAULIAC 
58 
(Gemalto), P.PIETRI (Orbiwise), D.SMITH (MultiTech), R.SOSS(Actility), T.TASHIRO (M2B 
59 
Communications), P.THOMSEN (Orbiwise), A.YEGIN (Actility) 
60 
 
61 
Version: 1.1 
62 
Date: October 11, 2017 
63 
Status: Final release 
64 
 
65 
 
66 
 
67

## Page 3

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 3 of 101 
The authors reserve the right to change 
specifications without notice. 
 
Contents 
68 
1 
Introduction .................................................................................................................. 8 
69 
1.1 
LoRaWAN Classes .................................................................................................. 8 
70 
1.2 
Conventions ............................................................................................................. 9 
71 
2 
Introduction on LoRaWAN options ............................................................................. 10 
72 
2.1 
LoRaWAN Classes ................................................................................................ 10 
73 
Class A – All end-devices ................................................................................................... 11 
74 
3 
Physical Message Formats ........................................................................................ 12 
75 
3.1 
Uplink Messages .................................................................................................... 12 
76 
3.2 
Downlink Messages ............................................................................................... 12 
77 
3.3 
Receive Windows................................................................................................... 13 
78 
3.3.1 First receive window channel, data rate, and start ............................................ 14 
79 
3.3.2 Second receive window channel, data rate, and start ....................................... 14 
80 
3.3.3 Receive window duration .................................................................................. 14 
81 
3.3.4 Receiver activity during the receive windows .................................................... 14 
82 
3.3.5 Network sending a message to an end-device ................................................. 14 
83 
3.3.6 Important notice on receive windows ................................................................ 14 
84 
3.3.7 Receiving or transmitting other protocols .......................................................... 15 
85 
4 
MAC Message Formats ............................................................................................. 16 
86 
4.1 
MAC Layer (PHYPayload) ...................................................................................... 16 
87 
4.2 
MAC Header (MHDR field) ..................................................................................... 17 
88 
4.2.1 Message type (MType bit field) ......................................................................... 17 
89 
4.2.2 Major version of data message (Major bit field) ................................................ 18 
90 
4.3 
MAC Payload of Data Messages (MACPayload) .................................................... 18 
91 
4.3.1 Frame header (FHDR) ...................................................................................... 18 
92 
4.3.2 Port field (FPort) ............................................................................................... 24 
93 
4.3.3 MAC Frame Payload Encryption (FRMPayload) ............................................... 25 
94 
4.4 
Message Integrity Code (MIC)................................................................................ 26 
95 
4.4.1 Downlink frames ............................................................................................... 26 
96 
4.4.2 Uplink frames ................................................................................................... 27 
97 
5 
MAC Commands........................................................................................................ 29 
98 
5.1 
Reset indication commands (ResetInd, ResetConf) ............................................... 32 
99 
5.2 
Link Check commands (LinkCheckReq, LinkCheckAns) ........................................ 33 
100 
5.3 
Link ADR commands (LinkADRReq, LinkADRAns) ................................................ 33 
101 
5.4 
End-Device Transmit Duty Cycle (DutyCycleReq, DutyCycleAns) .......................... 35 
102 
5.5 
Receive Windows Parameters (RXParamSetupReq, RXParamSetupAns) ............ 36 
103 
5.6 
End-Device Status (DevStatusReq, DevStatusAns) ............................................... 37 
104 
5.7 
Creation / Modification of a Channel (NewChannelReq, NewChannelAns, 
105 
DlChannelReq, DlChannelAns) .............................................................................. 38 
106 
5.8 
Setting delay between TX and RX (RXTimingSetupReq, RXTimingSetupAns) ...... 40 
107 
5.9 
End-device transmission parameters (TxParamSetupReq, TxParamSetupAns) .... 41 
108 
5.10 Rekey indication commands (RekeyInd, RekeyConf) ............................................. 42 
109 
5.11 ADR parameters (ADRParamSetupReq, ADRParamSetupAns) ............................ 43 
110 
5.12 DeviceTime commands (DeviceTimeReq, DeviceTimeAns) ................................... 44 
111 
5.13 Force Rejoin Command (ForceRejoinReq)............................................................. 44 
112 
5.14 RejoinParamSetupReq (RejoinParamSetupAns) ................................................... 45 
113 
6 
End-Device Activation ................................................................................................ 47 
114 
6.1 
Data Stored in the End-device................................................................................ 47 
115 
6.1.1 Before Activation .............................................................................................. 47 
116 
6.1.2 After Activation ................................................................................................. 49 
117 
6.2 
Over-the-Air Activation ........................................................................................... 52 
118

## Page 4

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 4 of 101 
The authors reserve the right to change 
specifications without notice. 
 
6.2.1 Join procedure.................................................................................................. 52 
119 
6.2.2 Join-request message ...................................................................................... 52 
120 
6.2.3 Join-accept message........................................................................................ 53 
121 
6.2.4 ReJoin-request message .................................................................................. 57 
122 
6.2.5 Key derivation diagram ..................................................................................... 61 
123 
6.3 
Activation by Personalization ................................................................................. 64 
124 
7 
Retransmissions back-off ........................................................................................... 65 
125 
Class B – Beacon ............................................................................................................... 66 
126 
8 
Introduction to Class B ............................................................................................... 67 
127 
9 
Principle of synchronous network initiated downlink (Class-B option) ......................... 68 
128 
10 
Uplink frame in Class B mode .................................................................................... 71 
129 
11 
Downlink Ping frame format (Class B option) ............................................................. 72 
130 
11.1 Physical frame format ............................................................................................ 72 
131 
11.2 Unicast & Multicast MAC messages ....................................................................... 72 
132 
11.2.1 Unicast MAC message format .......................................................................... 72 
133 
11.2.2 Multicast MAC message format ........................................................................ 72 
134 
12 
Beacon acquisition and tracking ................................................................................. 73 
135 
12.1 Minimal beacon-less operation time ....................................................................... 73 
136 
12.2 Extension of beacon-less operation upon reception ............................................... 73 
137 
12.3 Minimizing timing drift ............................................................................................. 73 
138 
13 
Class B Downlink slot timing ...................................................................................... 74 
139 
13.1 Definitions .............................................................................................................. 74 
140 
13.2 Slot randomization ................................................................................................. 75 
141 
14 
Class B MAC commands ........................................................................................... 76 
142 
14.1 PingSlotInfoReq ..................................................................................................... 76 
143 
14.2 BeaconFreqReq ..................................................................................................... 77 
144 
14.3 PingSlotChannelReq .............................................................................................. 78 
145 
14.4 BeaconTimingReq & BeaconTimingAns ................................................................. 79 
146 
15 
Beaconing (Class B option) ........................................................................................ 80 
147 
15.1 Beacon physical layer ............................................................................................ 80 
148 
15.2 Beacon frame content ............................................................................................ 80 
149 
15.3 Beacon GwSpecific field format .............................................................................. 81 
150 
15.3.1 Gateway GPS coordinate:InfoDesc = 0, 1 or 2 ................................................. 82 
151 
15.4 Beaconing precise timing ....................................................................................... 82 
152 
15.5 Network downlink route update requirements ......................................................... 82 
153 
16 
Class B unicast & multicast downlink channel frequencies ......................................... 84 
154 
16.1 Single channel beacon transmission ...................................................................... 84 
155 
16.2 Frequency-hopping beacon transmission ............................................................... 84 
156 
Class C – Continuously listening ......................................................................................... 85 
157 
17 
Class C: Continuously listening end-device................................................................ 86 
158 
17.1 Second receive window duration for Class C ......................................................... 86 
159 
17.2 Class C Multicast downlinks ................................................................................... 87 
160 
18 
Class C MAC command ............................................................................................. 88 
161 
18.1 Device Mode (DeviceModeInd, DeviceModeConf) ................................................. 88 
162 
Support information ............................................................................................................. 89 
163 
19 
Examples and Application Information ....................................................................... 90 
164 
19.1 Uplink Timing Diagram for Confirmed Data Messages ........................................... 90 
165 
19.2 Downlink Diagram for Confirmed Data Messages .................................................. 90 
166 
19.3 Downlink Timing for Frame-Pending Messages ..................................................... 91 
167 
20 
Recommendation on contract to be provided to the network server by the end-
168 
device provider at the time of provisioning .......................................................................... 93 
169 
21 
Recommendation on finding the locally used channels .............................................. 94 
170 
22 
Revisions ................................................................................................................... 95 
171

## Page 5

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 5 of 101 
The authors reserve the right to change 
specifications without notice. 
 
22.1 Revision 1.0 ........................................................................................................... 95 
172 
22.2 Revision 1.0.1 ........................................................................................................ 95 
173 
22.3 Revision 1.0.2 ........................................................................................................ 95 
174 
22.4 Revision 1.1 ........................................................................................................... 96 
175 
22.4.1 Clarifications ..................................................................................................... 96 
176 
22.4.2 Functional modifications ................................................................................... 96 
177 
22.4.3 Examples ......................................................................................................... 98 
178 
23 
Glossary .................................................................................................................... 99 
179 
24 
Bibliography ............................................................................................................. 100 
180 
24.1 References........................................................................................................... 100 
181 
25 
NOTICE OF USE AND DISCLOSURE ..................................................................... 101 
182 
 
183 
Tables 
184 
Table 1: MAC message types ............................................................................................. 17 
185 
Table 2: Major list ................................................................................................................ 18 
186 
Table 3: FPort list ................................................................................................................ 26 
187 
Table 4: MAC commands .................................................................................................... 31 
188 
Table 5: Channel state table ............................................................................................... 34 
189 
Table 6: LinkADRAns status bits signification ..................................................................... 35 
190 
Table 7: RXParamSetupAns status bits signification ........................................................... 37 
191 
Table 8: Battery level decoding ........................................................................................... 37 
192 
Table 9: NewChannelAns status bits signification ............................................................... 39 
193 
Table 10: DlChannelAns status bits signification ................................................................. 40 
194 
Table 11: RXTimingSetup Delay mapping table .................................................................. 40 
195 
Table 12 : TxParamSetup EIRP encoding table .................................................................. 41 
196 
Table 13 : JoinReqType values ........................................................................................... 55 
197 
Table 14 : Join-Accept encryption key ................................................................................. 55 
198 
Table 15 : summary of RejoinReq messages ...................................................................... 58 
199 
Table 18 : transmission conditions for RejoinReq messages ............................................... 60 
200 
Table 19 : Join-request dutycycle limitations ....................................................................... 65 
201 
Table 20: Beacon timing ..................................................................................................... 74 
202 
Table 21 : classB slot randomization algorithm parameters................................................. 75 
203 
Table 22 : classB MAC command table .............................................................................. 76 
204 
Table 23 : beacon infoDesc index mapping ......................................................................... 81 
205 
Table 24 : Class C MAC command table............................................................................. 88 
206 
Table 25 : DeviceModInd class mapping ............................................................................. 88 
207 
 
208 
Figures 
209 
Figure 1: LoRaWAN Classes .............................................................................................. 10 
210 
Figure 2: Uplink PHY structure ............................................................................................ 12 
211 
Figure 3: Downlink PHY structure ....................................................................................... 12 
212 
Figure 4: End-device receive slot timing. ............................................................................. 13 
213 
Figure 5: Radio PHY structure (CRC* is only available on uplink messages) ...................... 16 
214 
Figure 6: PHY payload structure ......................................................................................... 16 
215 
Figure 7: MAC payload structure ......................................................................................... 16 
216 
Figure 8: Frame header structure ........................................................................................ 16 
217 
Figure 9: PHY paylod format ............................................................................................... 16 
218 
Figure 10: MAC header field content ................................................................................... 17 
219

## Page 6

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 6 of 101 
The authors reserve the right to change 
specifications without notice. 
 
Figure 11 : Frame header format ........................................................................................ 18 
220 
Figure 12 : downlink FCtrl fields .......................................................................................... 19 
221 
Figure 13 : uplink FCtrl fields ............................................................................................... 19 
222 
Figure 14 : data rate back-off sequence example ................................................................ 20 
223 
Figure 15 : Encryption block format ..................................................................................... 24 
224 
Figure 16 : MACPayload field size ...................................................................................... 25 
225 
Figure 17 : Encryption block format ..................................................................................... 26 
226 
Figure 18 : downlink MIC computation block format ............................................................ 27 
227 
Figure 19 : uplink B0 MIC computation block format ............................................................ 27 
228 
Figure 20 :  uplink B1 MIC computation block format ........................................................... 27 
229 
Figure 34 : ResetInd payload format ................................................................................... 32 
230 
Figure 35 : ResetConf payload format ................................................................................. 33 
231 
Figure 21: LinkCheckAns payload format ............................................................................ 33 
232 
Figure 22 : LinkADRReq payload format ............................................................................. 33 
233 
Figure 23 : LinkADRAns payload format ............................................................................. 35 
234 
Figure 24 : DutyCycleReq payload format ........................................................................... 36 
235 
Figure 25 : RXParamSetupReq payload format .................................................................. 36 
236 
Figure 26 : RXParamSetupAns payload format ................................................................... 37 
237 
Figure 27 : DevStatusAns payload format ........................................................................... 37 
238 
Figure 28 : NewChannelReq payload format ....................................................................... 38 
239 
Figure 29 : NewChannelAns payload format ....................................................................... 38 
240 
Figure 30 : DLChannelReq payload format ......................................................................... 39 
241 
Figure 31 : DLChannelAns payload format .......................................................................... 39 
242 
Figure 32 : RXTimingSetupReq payload format .................................................................. 40 
243 
Figure 33 : TxParamSetupReq payload format ................................................................... 41 
244 
Figure 36 : RekeyInd payload format .................................................................................. 42 
245 
Figure 37 : RekeyConf payload format ................................................................................ 43 
246 
Figure 38 : ADRParamSetupReq payload format ................................................................ 43 
247 
Figure 39 : DeviceTimeAns payload format ......................................................................... 44 
248 
Figure 40 : ForceRejoinReq payload format ........................................................................ 44 
249 
Figure 41 : RejoinParamSetupReq payload format ............................................................. 45 
250 
Figure 42 : RejoinParamSetupAns payload format .............................................................. 46 
251 
Figure 43 : DevAddr fields ................................................................................................... 49 
252 
Figure 44 : Join-request message fields .............................................................................. 52 
253 
Figure 45 : Join-accept message fields ............................................................................... 53 
254 
Figure 46: Rejoin-request type 0&2 message fields ............................................................ 58 
255 
Figure 47: Rejoin-request type 1 message fields ................................................................. 59 
256 
Figure 48 : LoRaWAN1.0 key derivation scheme ................................................................ 62 
257 
Figure 49 : LoRaWAN1.1 key derivation scheme ................................................................ 63 
258 
Figure 50: Beacon reception slot and ping slots .................................................................. 70 
259 
Figure 51 : classB FCtrl fields ............................................................................................. 71 
260 
Figure 52 : beacon-less temporary operation ...................................................................... 73 
261 
Figure 53: Beacon timing .................................................................................................... 74 
262 
Figure 54 : PingSlotInfoReq payload format ........................................................................ 76 
263 
Figure 55 : BeaconFreqReq payload format ........................................................................ 77 
264 
Figure 56 : BeaconFreqAns payload format ........................................................................ 77 
265 
Figure 57 : PingSlotChannelReq payload format ................................................................. 78 
266 
Figure 58 : PingSlotFreqAns payload format ....................................................................... 78 
267 
Figure 59 : beacon physical format ..................................................................................... 80 
268 
Figure 60 : beacon frame content........................................................................................ 80 
269 
Figure 61 : example of beacon CRC calculation (1) ............................................................ 80 
270 
Figure 62 : example of beacon CRC calculation (2) ............................................................ 81 
271 
Figure 63 : beacon GwSpecific field format ......................................................................... 81 
272

## Page 7

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 7 of 101 
The authors reserve the right to change 
specifications without notice. 
 
Figure 64 : beacon Info field format ..................................................................................... 82 
273 
Figure 65: Class C end-device reception slot timing. ........................................................... 87 
274 
Figure 66 : DeviceModeInd payload format ......................................................................... 88 
275 
Figure 67: Uplink timing diagram for confirmed data messages .......................................... 90 
276 
Figure 68: Downlink timing diagram for confirmed data messages ...................................... 91 
277 
Figure 69: Downlink timing diagram for frame-pending messages, example 1 .................... 91 
278 
Figure 70: Downlink timing diagram for frame-pending messages, example 2 .................... 92 
279 
Figure 71: Downlink timing diagram for frame-pending messages, example 3 .................... 92 
280 
 
281

## Page 8

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 8 of 101 
The authors reserve the right to change 
specifications without notice. 
 
1 Introduction 
282 
This document describes the LoRaWAN™ network protocol which is optimized for battery-
283 
powered end-devices that may be either mobile or mounted at a fixed location.  
284 
LoRaWAN networks typically are laid out in a star-of-stars topology in which gateways1 
285 
relay messages between end-devices2 and a central Network Server  the Network Server 
286 
routes the packets from each device of the network to the associated Application Server. 
287 
To secure radio transmissions the LoRaWAN protocol relies on symmetric cryptography 
288 
using session keys derived from the device’s root keys. In the backend the storage of the 
289 
device’s root keys and the associated key derivation operations are insured by a Join 
290 
Server. 
291 
This specification treats the Network Server, Application Server, and Join Server as if they 
292 
are always co-located. Hosting these functionalities across multiple disjoint network nodes is 
293 
outside the scope of this specification but is covered by [BACKEND]. 
294 
 Gateways are connected to the Network Server via secured standard IP connections while 
295 
end-devices use single-hop LoRa™ or FSK communication to one or many gateways.3  All 
296 
communication is generally bi-directional, although uplink communication from an end-
297 
device to the Network Server is expected to be the predominant traffic. 
298 
Communication between end-devices and gateways is spread out on different frequency 
299 
channels and data rates. The selection of the data rate is a trade-off between 
300 
communication range and message duration, communications with different data rates do 
301 
not interfere with each other.  LoRa data rates range from 0.3 kbps to 50 kbps.  To maximize 
302 
both battery life of the end-devices and overall network capacity, the LoRa network 
303 
infrastructure can manage the data rate and RF output for each end-device individually by 
304 
means of an adaptive data rate (ADR) scheme. 
305 
End-devices may transmit on any channel available at any time, using any available data 
306 
rate, as long as the following rules are respected: 
307 
 
The end-device changes channel in a pseudo-random fashion for every 
308 
transmission. The resulting frequency diversity makes the system more robust to 
309 
interferences. 
310 
 
The end-device respects the maximum transmit duty cycle relative to the sub-band 
311 
used and local regulations. 
312 
 
The end-device respects the maximum transmit duration (or dwell time) relative to 
313 
the sub-band used and local regulations. 
314 
Note: Maximum transmit duty-cycle and dwell time per sub-band are 
315 
region specific and are defined in [PHY] 
316 
1.1 LoRaWAN Classes 
317 
All LoRaWAN devices MUST implement at least the Class A functionality as described in 
318 
this document. In addition they MAY implement options named Class B or Class C as also 
319 
                                                
1 Gateways are also known as concentrators or base stations. 
2 End-devices are also known as motes. 
3 Support for intermediate elements – repeaters – is not described in the document, however payload 
restrictions for encapsulation overhead are included in this specification. A repeater is defined as 
using LoRaWAN as its backhaul mechanism.

## Page 9

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 9 of 101 
The authors reserve the right to change 
specifications without notice. 
 
described in this document or others to be defined. In all cases, they MUST remain 
320 
compatible with Class A. 
321 
1.2 Conventions 
322 
 
323 
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", 
324 
"SHOULD NOT", "RECOMMENDED",  "MAY", and  "OPTIONAL" in this document are to be 
325 
interpreted as described in RFC 2119. 
326 
MAC commands are written LinkCheckReq, bits and bit fields are written FRMPayload, 
327 
constants are written RECEIVE_DELAY1, variables are written N. 
328 
In this document, 
329 
 
The over-the-air octet order for all multi-octet fields is little endian  
330 
 
EUI are 8 bytes multi-octet fields and are transmitted as little endian. 
331 
 
By default, RFU bits SHALL be set to zero by the transmitter of the message and 
332 
SHALL be ignored by the receiver  
333

## Page 10

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 10 of 101 
The authors reserve the right to change 
specifications without notice. 
 
2 Introduction on LoRaWAN options 
334 
LoRa™ is a wireless modulation for long-range low-power low-data-rate applications 
335 
developed by Semtech.  Devices implementing more than Class A are generally named 
336 
“higher Class end-devices” in this document. 
337 
2.1 LoRaWAN Classes 
338 
A LoRa network distinguishes between a basic LoRaWAN (named Class A) and optional 
339 
features (Class B, Class C): 
340 
Application
LoRa MAC
LoRa Modulation
EU
868
EU
433
US
915
AS
430
…
Class B 
(beacon)
Class C 
(Continuous)
Application
MAC
MAC options
Modulation
Regional ISM band
Class A 
(baseline)
 
341 
Figure 1: LoRaWAN Classes 
342 
 
Bi-directional end-devices (Class A): End-devices of Class A allow for bi-
343 
directional communications whereby each end-device’s uplink transmission is 
344 
followed by two short downlink receive windows. The transmission slot scheduled by 
345 
the end-device is based on its own communication needs with a small variation 
346 
based on a random time basis (ALOHA-type of protocol). This Class A operation is 
347 
the lowest power end-device system for applications that only require downlink 
348 
communication from the server shortly after the end-device has sent an uplink 
349 
transmission. Downlink communications from the server at any other time will have to 
350 
wait until the next scheduled uplink. 
351 
 
Bi-directional end-devices with scheduled receive slots (Class B): End-devices 
352 
of Class B allow for more receive slots. In addition to the Class A random receive 
353 
windows, Class B devices open extra receive windows at scheduled times. In order 
354 
for the End-device to open its receive window at the scheduled time, it receives a 
355 
time synchronized Beacon from the gateway.  
356 
 
Bi-directional end-devices with maximal receive slots (Class C): End-devices of 
357 
Class C have nearly continuously open receive windows, only closed when 
358 
transmitting. Class C end-device will use more power to operate than Class A or 
359 
Class B but they offer the lowest latency for server to end-device communication. 
360

## Page 11

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 11 of 101 
The authors reserve the right to change 
specifications without notice. 
 
CLASS A – ALL END-DEVICES 
361 
All LoRaWAN end-devices MUST implement Class A features. 
362

## Page 12

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 12 of 101 
The authors reserve the right to change 
specifications without notice. 
 
3 Physical Message Formats 
363 
The LoRa terminology distinguishes between uplink and downlink messages. 
364 
3.1 Uplink Messages 
365 
Uplink messages are sent by end-devices to the Network Server relayed by one or many 
366 
gateways. 
367 
Uplink messages use the LoRa radio packet explicit mode in which the LoRa physical 
368 
header (PHDR) plus a header CRC (PHDR_CRC) are included.1 The integrity of the payload 
369 
is protected by a CRC.  
370 
The PHDR, PHDR_CRC and payload CRC fields are inserted by the radio transceiver. 
371 
Uplink PHY: 
372 
Preamble 
PHDR 
PHDR_CRC 
PHYPayload 
CRC 
Figure 2: Uplink PHY structure 
373 
3.2 Downlink Messages 
374 
Each downlink message is sent by the Network Server to only one end-device and is 
375 
relayed by a single gateway.2  
376 
Downlink messages use the radio packet explicit mode in which the LoRa physical header 
377 
(PHDR) and a header CRC (PHDR_CRC) are included.3 
378 
Downlink PHY: 
379 
Preamble 
PHDR 
PHDR_CRC 
PHYPayload 
Figure 3: Downlink PHY structure 
380 
                                                
1 See the LoRa radio transceiver datasheet for a description of LoRa radio packet implicit/explicit 
modes. 
2 This specification does not describe the transmission of multicast messages from a network server 
to many end-devices. 
3 No payload integrity check is done at this level to keep messages as short as possible with minimum 
impact on any duty-cycle limitations of the ISM bands used.

## Page 13

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 13 of 101 
The authors reserve the right to change 
specifications without notice. 
 
3.3 Receive Windows 
381 
Following each uplink transmission the end-device MUST open two short receive windows. 
382 
The receive window start times are defined using the end of the transmission as a reference. 
383 
 
384 
 
385 
Figure 4: End-device receive slot timing. 
386

## Page 14

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 14 of 101 
The authors reserve the right to change 
specifications without notice. 
 
3.3.1 
First receive window channel, data rate, and start 
387 
The first receive window RX1 uses a frequency that is a function of the uplink frequency and 
388 
a data rate that is a function of the data rate used for the uplink. RX1 opens 
389 
RECEIVE_DELAY11 seconds (+/- 20 microseconds) after the end of the uplink modulation. 
390 
The relationship between uplink and RX1 slot downlink data rate is region specific and 
391 
detailed in [PHY]. By default, the first receive window datarate is identical to the datarate of 
392 
the last uplink. 
393 
3.3.2 
Second receive window channel, data rate, and start 
394 
The second receive window RX2 uses a fixed configurable frequency and data rate and 
395 
opens RECEIVE_DELAY21 seconds (+/- 20 microseconds) after the end of the uplink 
396 
modulation. The frequency and data rate used can be modified through MAC commands 
397 
(see Section 5). The default frequency and data rate to use are region specific and detailed 
398 
in [PHY]. 
399 
3.3.3 
Receive window duration 
400 
The length of a receive window MUST be at least the time required by the end-device’s radio 
401 
transceiver to effectively detect a downlink preamble.  
402 
3.3.4 
Receiver activity during the receive windows 
403 
If a preamble is detected during one of the receive windows, the radio receiver stays active 
404 
until the downlink frame is demodulated. If a frame was detected and subsequently 
405 
demodulated during the first receive window and the frame was intended for this end-device 
406 
after address and MIC (message integrity code) checks, the end-device MUST not open the 
407 
second receive window. 
408 
3.3.5 
Network sending a message to an end-device 
409 
If the network intends to transmit a downlink to an end-device, it MUST initiate the 
410 
transmission precisely at the beginning of at least one of the two receive windows. If a 
411 
downlink is transmitted during both windows, identical frames MUST be transmitted during 
412 
each window. 
413 
3.3.6 
Important notice on receive windows 
414 
An end-device SHALL NOT transmit another uplink message before it either has received a 
415 
downlink message in the first or second receive window of the previous transmission, or the 
416 
second receive window of the previous transmission is expired.  
417 
                                                
1 RECEIVE_DELAY1 and RECEIVE_DELAY2 are described in Chapter 6.

## Page 15

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 15 of 101 
The authors reserve the right to change 
specifications without notice. 
 
3.3.7 
Receiving or transmitting other protocols 
418 
The node MAY listen or transmit other protocols or do any radio transactions between the 
419 
LoRaWAN transmission and reception windows, as long as the end-device remains 
420 
compatible with the local regulation and compliant with the LoRaWAN specification. 
421

## Page 16

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 16 of 101 
The authors reserve the right to change 
specifications without notice. 
 
4 MAC Message Formats 
422 
All LoRa uplink and downlink messages carry a PHY payload (Payload) starting with a 
423 
single-octet MAC header (MHDR), followed by a MAC payload (MACPayload)1, and ending 
424 
with a 4-octet message integrity code (MIC).  
425 
 
426 
 
Radio PHY layer: 
427 
Preamble 
PHDR 
PHDR_CRC 
PHYPayload 
CRC* 
Figure 5: Radio PHY structure (CRC* is only available on uplink messages) 
428 
PHYPayload: 
429 
MHDR 
MACPayload 
MIC 
or 
430 
MHDR 
Join-Request or 
Rejoin-Request 
MIC 
or 
431 
MHDR 
Join-Accept2 
Figure 6: PHY payload structure 
432 
MACPayload: 
433 
FHDR 
FPort 
FRMPayload 
Figure 7: MAC payload structure 
434 
FHDR: 
435 
DevAddr 
FCtrl 
FCnt 
FOpts 
Figure 8: Frame header structure 
436 
 
4.1 MAC Layer (PHYPayload) 
437 
 
438 
Size (bytes) 
1 
7..M 
4 
PHYPayload 
MHDR 
MACPayload 
MIC 
Figure 9: PHY paylod format 
439 
                                                
1 Maximum payload size is detailed in the Chapter 6. 
2 For Join-Accept frame, the MIC field is encrypted with the payload and is not a separate field

## Page 17

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 17 of 101 
The authors reserve the right to change 
specifications without notice. 
 
The maximum length (M) of the MACPayload field is region specific and is specified in 
440 
Chapter 6. 
441 
 
442 
 
443 
4.2 MAC Header (MHDR field) 
444 
Bit# 
7..5 
4..2 
1..0 
MHDR bits 
MType 
RFU 
Major 
 
Figure 10: MAC header field content 
445 
 
446 
The MAC header specifies the message type (MType) and according to which major version 
447 
(Major) of the frame format of the LoRaWAN layer specification the frame has been 
448 
encoded. 
449 
4.2.1 
Message type (MType bit field) 
450 
The LoRaWAN distinguishes between 8 different MAC message types: Join-request, 
451 
Rejoin-request, Join-accept, unconfirmed data up/down, and confirmed data up/down 
452 
and proprietary protocol messages.  
453 
MType 
Description 
000 
Join-request 
001 
Join-accept 
010 
Unconfirmed Data Up 
011 
Unconfirmed Data Down 
100 
Confirmed Data Up 
101 
Confirmed Data Down 
110 
Rejoin-request 
111 
Proprietary 
Table 1: MAC message types 
454 
4.2.1.1 Join-request and join-accept messages 
455 
The join-request, Rejoin-request and join-accept messages are used by the over-the-air 
456 
activation procedure described in Chapter 6.2 and for roaming purposes. 
457 
4.2.1.2 Data messages 
458 
Data messages are used to transfer both MAC commands and application data, which can 
459 
be combined together in a single message.  A confirmed-data message MUST be 
460 
acknowledged by the receiver, whereas an unconfirmed-data message does not require 
461 
an acknowledgment.1 Proprietary messages can be used to implement non-standard 
462 
message formats that are not interoperable with standard messages but must only be used 
463 
                                                
1 A detailed timing diagram of the acknowledge mechanism is given in Section 19.

## Page 18

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 18 of 101 
The authors reserve the right to change 
specifications without notice. 
 
among devices that have a common understanding of the proprietary extensions. When an 
464 
end-device or a Network Server receives an unknown proprietary message, it SHALL silently 
465 
drop it. 
466 
Message integrity is ensured in different ways for different message types and is described 
467 
per message type below. 
468 
4.2.2 
Major version of data message (Major bit field) 
469 
Major bits 
Description 
00 
LoRaWAN R1 
01..11 
RFU 
Table 2: Major list 
470 
Note: The Major version specifies the format of the messages 
471 
exchanged in the join procedure (see Chapter 6.2) and the first four 
472 
bytes of the MAC Payload as described in Chapter 4. For each major 
473 
version, end-devices may implement different minor versions of the 
474 
frame format.  The minor version used by an end-device must be made 
475 
known to the Network Server beforehand using out of band messages 
476 
(e.g., as part of the device personalization information). When a device 
477 
or a Network Server receives a frame carrying an unknown or 
478 
unsupported version of LoRaWAN, it SHALL silently drop it. 
479 
 
480 
4.3 MAC Payload of Data Messages (MACPayload) 
481 
The MAC payload of the data messages, contains a frame header (FHDR) followed by an 
482 
optional port field (FPort) and an optional frame payload field (FRMPayload).  
483 
A frame with a valid FHDR, no Fopts (FoptsLen = 0), no Fport and no FRMPayload is a valid 
484 
frame. 
485 
 
486 
4.3.1 
Frame header (FHDR) 
487 
The FHDR contains the short device address of the end-device (DevAddr), a frame control 
488 
octet (FCtrl), a 2-octets frame counter (FCnt), and up to 15 octets of frame options (FOpts) 
489 
used to transport MAC commands. . If present, the FOpts field shall be encrypted using the 
490 
NwkSEncKey as described in section 4.3.1.6. 
491 
 
492 
 
493 
 Size (bytes) 
4 
1 
2 
0..15 
FHDR 
DevAddr 
FCtrl 
FCnt 
FOpts 
Figure 11 : Frame header format 
494 
 
495 
For downlink frames the FCtrl content of the frame header is: 
496 
 Bit# 
7 
6 
5 
4 
[3..0]

## Page 19

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 19 of 101 
The authors reserve the right to change 
specifications without notice. 
 
FCtrl bits 
ADR 
RFU 
ACK 
FPending 
FOptsLen 
Figure 12 : downlink FCtrl fields 
497 
For uplink frames the FCtrl content of the frame header is: 
498 
Bit# 
7 
6 
5 
4 
[3..0] 
FCtrl bits 
ADR 
ADRACKReq 
ACK 
ClassB 
FOptsLen 
Figure 13 : uplink FCtrl fields 
499 
 
500 
4.3.1.1 Adaptive data rate control in frame header (ADR, ADRACKReq in FCtrl) 
501 
LoRa network allows the end-devices to individually use any of the possible data rates and 
502 
Tx power. This feature is used by the LoRaWAN to adapt and optimize the data rate and Tx 
503 
power of static end-devices. This is referred to as Adaptive Data Rate (ADR) and when this 
504 
is enabled the network will be optimized to use the fastest data rate possible. 
505 
Adaptive Data Rate control may not be possible when the radio channel attenuation 
506 
changes fast and constantly. When the Network Server is unable to control the data rate of a 
507 
device, the device’s application layer should control it. It is recommended to use a variety of 
508 
different data rates in this case. The application layer SHOULD always try to minimize the 
509 
aggregated air time used given the network conditions. 
510 
If the uplink ADR bit is set, the network will control the data rate and Tx power of the end-
511 
device through the appropriate MAC commands. If the ADR bit is not set, the network will 
512 
not attempt to control the data rate nor the transmit power of the end-device regardless of 
513 
the received signal quality. The network MAY still send commands to change the Channel 
514 
mask or the frame repetition parameters.  
515 
When the downlink ADR bit is set, it informs the end-device that the Network Server is in a 
516 
position to send ADR commands. The device MAY set/unset the uplink ADR bit. 
517 
When the downlink ADR bit is unset, it signals the end-device that due to rapid changes of 
518 
the radio channel, the network temporarily cannot estimate the best data rate. In that case 
519 
the device has the choice to either  
520 
 
unset the ADR uplink bit, and control its uplink data rate following its own strategy. 
521 
This SHOULD be the typical strategy for a mobile end-device. 
522 
 
Ignore it (keep the uplink ADR bit set) and apply the normal data rate decay in the 
523 
absence of ADR downlink commands. This SHOULD be the typical strategy for a 
524 
stationary end-device. 
525 
 
526 
 
527 
The ADR bit may be set and unset by the end-device or the Network on demand. However, 
528 
whenever possible, the ADR scheme SHOULD be enabled to increase the battery life of the 
529 
end-device and maximize the network capacity.  
530 
Note: Even mobile end-devices are actually immobile most of the time. 
531 
So depending on its state of mobility, an end-device can request the 
532 
network to optimize its data rate using the ADR uplink bit. 
533

## Page 20

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 20 of 101 
The authors reserve the right to change 
specifications without notice. 
 
Default Tx Power is the maximum transmission power allowed for the device considering 
534 
device capabilities and regional regulatory constraints. Device shall use this power level, 
535 
until the network asks for less, through the LinkADRReq MAC command. 
536 
If an end-device’s data rate is optimized by the network to use a data rate higher than its 
537 
default data rate, or a TXPower lower than its default TXPower, it periodically needs to 
538 
validate that the network still receives the uplink frames. Each time the uplink frame counter 
539 
is incremented (for each new uplink, repeated transmissions do not increase the counter), 
540 
the device increments an ADR_ACK_CNT counter. After ADR_ACK_LIMIT uplinks 
541 
(ADR_ACK_CNT >= ADR_ACK_LIMIT) without any downlink response, it sets the ADR 
542 
acknowledgment request bit (ADRACKReq).  The network is required to respond with a 
543 
downlink frame within the next ADR_ACK_DELAY frames, any received downlink frame 
544 
following an uplink frame resets the ADR_ACK_CNT counter. The downlink ACK bit does 
545 
not need to be set as any response during the receive slot of the end-device indicates that 
546 
the gateway has still received the uplinks from this device. If no reply is received within the 
547 
next 
ADR_ACK_DELAY 
uplinks 
(i.e., 
after 
a 
total 
of 
ADR_ACK_LIMIT 
+ 
548 
ADR_ACK_DELAY), the end-device MUST try to regain connectivity by first stepping up the 
549 
transmit power to default power if possible then switching to the next lower data rate that 
550 
provides a longer radio range. The end-device MUST further lower its data rate step by step 
551 
every time ADR_ACK_DELAY is reached. Once the device has reached the lowest data 
552 
rate, it MUST re-enable all default uplink frequency channels.   
553 
The ADRACKReq SHALL not be set if the device uses its default data rate and transmit 
554 
power because in that case no action can be taken to improve the link range. 
555 
Note: 
Not 
requesting 
an 
immediate 
response 
to 
an 
ADR 
556 
acknowledgement request provides flexibility to the network to 
557 
optimally schedule its downlinks. 
558 
 
559 
Note: In uplink transmissions the ADRACKReq bit is set if 
560 
ADR_ACK_CNT >= ADR_ACK_LIMIT and the current data-rate is 
561 
greater than the device defined minimum data rate or its transmit 
562 
power is lower than the default, or the current channel mask only 
563 
uses a subset of all the default channels. It is cleared in other 
564 
conditions. 
565 
 
566 
The following table provides an example of data rate back-off sequence assuming 
567 
ADR_ACK_LIMIT and ADR_ACK_DELAY constants are both equal to 32. 
568 
 
569 
ADR_ACK_CNT 
ADRACKReq bit 
Data Rate 
TX power 
Channel Mask 
0  to 63 
0 
SF11 
Max – 9dBm 
Single channel 
enabled 
64 to 95 
1 
Keep 
Keep 
Keep 
96 to 127 
1 
Keep 
Max 
Keep 
128 to 159 
1 
SF12 
Max 
Keep 
>= 160 
0 
SF12 
MAX 
All channels 
enabled 
Figure 14 : data rate back-off sequence example 
570 
 
571

## Page 21

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 21 of 101 
The authors reserve the right to change 
specifications without notice. 
 
4.3.1.2 Message acknowledge bit and acknowledgement procedure (ACK in FCtrl) 
572 
When receiving a confirmed data message, the receiver SHALL respond with a data frame 
573 
that has the acknowledgment bit (ACK) set. If the sender is an end-device, the network will 
574 
try to send the acknowledgement using one of the receive windows opened by the end-
575 
device after the send operation. If the sender is a gateway, the end-device transmits an 
576 
acknowledgment at its own discretion (see note below). 
577 
An acknowledgement is only sent in response to the latest message received and it is never 
578 
retransmitted. 
579 
 
580 
Note: To allow the end-devices to be as simple as possible and have 
581 
as few states as possible it may transmit an explicit (possibly empty) 
582 
acknowledgement data message immediately after the reception of a 
583 
data message requiring a confirmation. Alternatively the end-device 
584 
may defer the transmission of an acknowledgement to piggyback it 
585 
with its next data message. 
586 
4.3.1.3 Retransmission procedure 
587 
Downlink frames: 
588 
A downlink “confirmed” or “unconfirmed” frame SHALL not be retransmitted using the same 
589 
frame counter value. In the case of a “confirmed” downlink, if the acknowledge is not 
590 
received, the application server is notified and may decide to retransmit a new “confirmed” 
591 
frame.  
592 
 
593 
Uplink frames: 
594 
Uplink “confirmed” & “unconfirmed” frames are transmitted “NbTrans” times (see 5.3) except 
595 
if a valid downlink is received following one of the transmissions. The “NbTrans” parameter 
596 
can be used by the network manager to control the redundancy of the node uplinks to obtain 
597 
a given Quality of Service. The end-device SHALL perform frequency hopping as usual 
598 
between repeated transmissions, It SHALL wait after each repetition until the receive 
599 
windows have expired. The delay between the retransmissions is at the discretion of the 
600 
end-device and MAY be different for each end-device. 
601 
The device SHALL stop any further retransmission of an uplink “confirmed” frame if a 
602 
corresponding downlink acknowledgement frame is received 
603 
Class B&C devices SHALL stop any further retransmission of an uplink “unconfirmed” frame 
604 
whenever a valid unicast downlink message is received during the RX1 slot window.  
605 
Class A devices SHALL stop any further retransmission of an uplink “unconfirmed” frame 
606 
whenever a valid downlink message is received during the RX1 or the RX2 slot window.  
607 
If the network receives more than NbTrans transmissions of the same uplink frame, this may 
608 
be an indication of a replay attack or a malfunctioning device, and therefore the network 
609 
SHALL not process the extra frames. 
610 
NOTE: The network detecting a replay attack may take additional 
611 
measures, such as reducing the NbTrans parameter to 1, or discarding 
612 
uplink frames that are received over a channel that was already used 
613

## Page 22

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 22 of 101 
The authors reserve the right to change 
specifications without notice. 
 
by an earlier transmission of the same frame, or by some other 
614 
unspecified mechanism 
615 
4.3.1.4 Frame pending bit (FPending in FCtrl, downlink only) 
616 
The frame pending bit (FPending) is only used in downlink communication, indicating that 
617 
the network has more data pending to be sent and therefore asking the end-device to open 
618 
another receive window as soon as possible by sending another uplink message. 
619 
The exact use of FPending bit is described in Chapter 19.3.  
620 
4.3.1.5 Frame counter (FCnt) 
621 
Each end-device has three frame counters to keep track of the number of data frames sent 
622 
uplink to the Network Server (FCntUp), and sent downlink from the Network Server to the 
623 
device (FCntDown).  
624 
In the downlink direction two different frame counter scheme exists; a single counter scheme 
625 
in which all ports share the same downlink frame counter FCntDown when the device 
626 
operates as a LoRaWAN1.0 device, and a two-counter scheme in which a separate 
627 
NFCntDown is used for MAC communication on port 0 and when the FPort field is missing, 
628 
and another AFCntDown is used for all other ports when the device operates as a 
629 
LoRaWAN1.1 device. 
630 
In the two counters scheme the NFCntDown is managed by the Network Server, whereas 
631 
the AFCntDown is managed by the application server. 
632 
Note: LoRaWAN v1.0 and earlier support only one FCntDown counter 
633 
(shared across all ports) and the Network Server must take care to 
634 
support this scheme for devices prior to LoRaWAN v1.1. 
635

## Page 23

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 23 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
636 
Whenever an OTAA device successfully processes a Join-accept message, the frame 
637 
counters on the end-device (FCntUp) and the frame counters on the network side 
638 
(NFCntDown  & AFCntDown) for that end-device are reset to 0.  
639 
ABP devices have their Frame Counters initialized to 0 at fabrication. In ABP devices the 
640 
frame counters MUST NEVER be reset during the device’s life time. If the end-device is 
641 
susceptible of losing power during its life time (battery replacement for example), the frame 
642 
counters SHALL persist during such event. 
643 
Subsequently FCntUp is incremented with each uplink. NFCntDown is incremented with 
644 
each downlink on FPort 0 or when the FPort field is missing. AFCntDown is incremented 
645 
with each downlink on a port different than 0.  At the receiver side, the corresponding 
646 
counter is kept in sync with the value received provided the value received has been 
647 
incremented compared to the current counter value and the message MIC field matches the 
648 
MIC value computed locally using the appropriate network session key . The FCnt is not 
649 
incremented in case of multiple transmissions of a confirmed or unconfirmed frame (see 
650 
NbTrans parameter). The Network Server SHALL drop the application payload of the 
651 
retransmitted frames and only forward a single instance to the application server. 
652 
Frame counters are 32 bits wide, The FCnt field corresponds to the least-significant 16 bits 
653 
of the 32-bits frame counter (i.e., FCntUp for data frames sent uplink and 
654 
AFCntDown/NFCntDown for data frames sent downlink). 
655 
The end-device SHALL NEVER reuse the same FCntUp value with the same application or 
656 
network session keys, except for retransmission of the same confirmed or unconfirmed 
657 
frame. 
658 
The end-device SHALL never process any retransmission of the same downlink frame. 
659 
Subsequent retransmissions SHALL be ignored without being processed. 
660 
Note: This means that the device will only acknowledge once the 
661 
reception of a downlink confirmed frame, similarly the device will only 
662 
generate a single uplink following the reception of a frame with the 
663 
FPending bit set. 
664 
 
665 
Note: Since the FCnt field carries only the least-significant 16 bits of 
666 
the 32-bits frame counter, the server must infer the 16 most-significant 
667 
bits of the frame counter from the observation of the traffic.  
668

## Page 24

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 24 of 101 
The authors reserve the right to change 
specifications without notice. 
 
4.3.1.6 Frame options (FOptsLen in FCtrl, FOpts) 
669 
The frame-options length field (FOptsLen) in FCtrl byte denotes the actual length of the 
670 
frame options field (FOpts) included in the frame.   
671 
FOpts transport MAC commands of a maximum length of 15 octets that are piggybacked 
672 
onto data frames; see Chapter 5 for a list of valid MAC commands.   
673 
If FOptsLen is 0, the FOpts field is absent. If FOptsLen is different from 0, i.e. if MAC 
674 
commands are present in the FOpts field, the port 0 cannot be used (FPort must be either 
675 
not present or different from 0).  
676 
MAC commands cannot be simultaneously present in the payload field and the frame 
677 
options field. Should this occur, the device SHALL ignore the frame. 
678 
If a frame header carries FOpts, FOpts MUST be encrypted before the message integrity 
679 
code (MIC) is calculated.  
680 
The encryption scheme used is based on the generic algorithm described in IEEE 
681 
802.15.4/2006 Annex B [IEEE802154] using AES with a key length of 128 bits.  
682 
The key K used is the NwkSEncKey for FOpts field in both the uplink and downlink direction. 
683 
The fields encrypted are: pld = FOpts 
684 
For each message, the algorithm defines a single Block A: 
685 
 
686 
Size (bytes) 
1 
4 
1 
4 
4 
1 
1 
A 
0x01 
4 x 0x00 
Dir 
DevAddr 
FCntUp or 
NFCntDwn  
0x00 
0x00 
Figure 15 : Encryption block format 
687 
The direction field (Dir) is 0 for uplink frames and 1 for downlink frames. 
688 
The block A is encrypted to get a block S: 
689 
 
690 
 
S = aes128_encrypt(K, A)  
691 
Encryption and decryption of the FOpts is done by truncating (pld | pad16) xor S to the first 
692 
len(pld) octets. 
693 
 
694 
4.3.1.7 Class B 
695 
The Class B bit set to 1 in an uplink signals the Network Server that the device as switched 
696 
to Class B mode and is now ready to receive scheduled downlink pings. Please refer to the 
697 
Class B section of the document for the Class B specification. 
698 
 
699 
4.3.2 
Port field (FPort) 
700 
If the frame payload field is not empty, the port field MUST be present. If present, an FPort 
701 
value of 0 indicates that the FRMPayload contains MAC commands only and any received 
702 
frames with such an FPort shall be processed by the LoRaWAN implementation; see 
703

## Page 25

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 25 of 101 
The authors reserve the right to change 
specifications without notice. 
 
Chapter 5 for a list of valid MAC commands.  FPort values 1..223 (0x01..0xDF) are 
704 
application-specific and any received frames with such an FPort SHALL be  made available 
705 
to the application layer by the LoRaWAN implementation. FPort value 224 is dedicated to 
706 
LoRaWAN MAC layer test protocol. LoRaWAN implementation SHALL discard any 
707 
transmission request from the application layer where the FPort value is not in the 1..224 
708 
range. 
709 
 
710 
Note: The purpose of FPort value 224 is to provide a dedicated FPort 
711 
to run MAC compliance test scenarios over-the-air on final versions of 
712 
devices, without having to rely on specific test versions of devices for 
713 
practical aspects. The test is not supposed to be simultaneous with live 
714 
operations, but the MAC layer implementation of the device shall be 
715 
exactly the one used for the normal application. The test protocol is 
716 
normally encrypted using the AppSKey. This ensures that the Network 
717 
Server cannot enable the device’s test mode without involving the 
718 
device’s owner. If the test runs on a live network connected device, the 
719 
way the test application on the network side learns the AppSKey is 
720 
outside of the scope of the LoRaWAN specification. If the test runs 
721 
using OTAA on a dedicated test bench (not a live network), the way 
722 
the AppKey is communicated to the test bench, for secured JOIN 
723 
process, is also outside of the scope of the specification. 
724 
The test protocol, running at application layer, is defined outside of the 
725 
LoRaWAN spec, as it is an application layer protocol. 
726 
 
727 
FPort values 225..255 (0xE1..0xFF) are reserved for future standardized application 
728 
extensions. 
729 
 
730 
Size (bytes) 
7..22 
0..1 
0..N 
MACPayload 
FHDR 
FPort 
FRMPayload 
Figure 16 : MACPayload field size 
731 
 
732 
N is the number of octets of the application payload. The valid range for N is region specific 
733 
and is defined in [PHY]. 
734 
N MUST be equal or smaller than: 
735 
N ≤ M - 1 - (length of FHDR in octets) 
736 
where M is the maximum MAC payload length. 
737 
4.3.3 
MAC Frame Payload Encryption (FRMPayload) 
738 
If a data frame carries a payload, FRMPayload MUST be encrypted before the message 
739 
integrity code (MIC) is calculated.  
740 
The encryption scheme used is based on the generic algorithm described in IEEE 
741 
802.15.4/2006 Annex B [IEEE802154] using AES with a key length of 128 bits.  
742 
The key K used depends on the FPort of the data message: 
743 
 
744 
FPort 
Direction 
K

## Page 26

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 26 of 101 
The authors reserve the right to change 
specifications without notice. 
 
0 
Uplink/downlink 
NwkSEncKey 
1..255 
Uplink/downlink 
AppSKey 
Table 3: FPort list 
745 
The fields encrypted are: 
746 
 
pld = FRMPayload 
747 
For each data message, the algorithm defines a sequence of Blocks Ai for i = 1..k with k = 
748 
ceil(len(pld) / 16): 
749 
 
750 
Size (bytes) 
1 
4 
1 
4 
4 
1 
1 
Ai 
0x01 
4 x 0x00 
Dir 
DevAddr 
FCntUp or 
NFCntDwn 
or 
AFCntDnw 
0x00 
i 
Figure 17 : Encryption block format 
751 
The direction field (Dir) is 0 for uplink frames and 1 for downlink frames. 
752 
The blocks Ai are encrypted to get a sequence S of blocks Si: 
753 
 
754 
 
Si = aes128_encrypt(K, Ai) for i = 1..k 
755 
 
S = S1 | S2 | ..  | Sk 
756 
Encryption and decryption of the payload is done by truncating 
757 
 
758 
 
(pld | pad16) xor S 
759 
to the first len(pld) octets. 
760 
 
761 
4.4 Message Integrity Code (MIC) 
762 
The message integrity code (MIC) is calculated over all the fields in the message. 
763 
 
764 
 
msg = MHDR | FHDR | FPort | FRMPayload 
765 
whereby len(msg) denotes the length of the message in octets.  
766 
4.4.1 
Downlink frames 
767 
The MIC of a downlink frame is calculated as follows [RFC4493]: 
768 
 
769 
 
cmac = aes128_cmac(SNwkSIntKey, B0 | msg) 
770 
 
MIC = cmac[0..3] 
771 
 
 
772

## Page 27

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 27 of 101 
The authors reserve the right to change 
specifications without notice. 
 
whereby the block B0 is defined as follows: 
773 
Size 
(bytes) 
1 
2 
2 
1 
4 
4 
1 
1 
B0 
0x49 
 
ConfFCnt 
2 x 0x00 
Dir = 
0x01 
DevAddr 
 
AFCntDwn 
or 
NFCntDwn 
 
0x00 
len(msg) 
Figure 18 : downlink MIC computation block format 
774 
If the device is connected to a LoRaWAN1.1 Network Server and the ACK bit of the 
775 
downlink frame is set, meaning this frame is acknowledging an uplink “confirmed” frame, 
776 
then ConfFCnt is the frame counter value modulo 2^16 of the “confirmed” uplink frame that 
777 
is being acknowledged. In all other cases ConfFCnt = 0x0000. 
778 
 
779 
4.4.2 
Uplink frames 
780 
The MIC of uplink frames is calculated with the following process: 
781 
 
782 
the block B0 is defined as follows: 
783 
Size (bytes) 
1 
4 
1 
4 
4 
1 
1 
B0 
0x49 
0x0000 
Dir = 0x00 
DevAddr 
FCntUp 
0x00 
len(msg) 
Figure 19 : uplink B0 MIC computation block format 
784 
 
785 
the block B1 is defined as follows: 
786 
Size 
(bytes) 
1 
2 
1 
1 
1 
4 
4 
1 
1 
B1 
0x49 
ConfFCnt 
 
TxDr 
TxCh 
Dir = 
0x00 
DevAddr 
FCntUp 
 
0x00 
len(msg) 
Figure 20 :  uplink B1 MIC computation block format 
787 
Where: 
788 
 
TxDr is the data rate used for the transmission of the uplink  
789 
 
TxCh is the index of the channel used for the transmission. 
790 
 
If the ACK bit of the uplink frame is set, meaning this frame is acknowledging a 
791 
downlink “confirmed” frame, then ConfFCnt is the frame counter value modulo 2^16 
792 
of the “confirmed” downlink frame that is being acknowledged. In all other cases 
793 
ConfFCnt = 0x0000. 
794 
 
795 
 
796 
 
cmacS = aes128_cmac(SNwkSIntKey, B1 | msg) 
797 
 
cmacF = aes128_cmac(FNwkSIntKey, B0 | msg) 
798 
 
799 
If the device is connected to a LoRaWAN1.0 Network Server then: 
800 
MIC = cmacF[0..3] 
801

## Page 28

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 28 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
802 
If the device is connected to a LoRaWAN1.1 Network Server then:   
803 
MIC = cmacS[0..1] | cmacF[0..1] 
804 
 
805 
 
806

## Page 29

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 29 of 101 
The authors reserve the right to change 
specifications without notice. 
 
5 MAC Commands 
807 
For network administration, a set of MAC commands may be exchanged exclusively 
808 
between the Network Server and the MAC layer on an end-device.  MAC layer commands 
809 
are never visible to the application or the application server or the application running on the 
810 
end-device.   
811 
A single data frame can contain any sequence of MAC commands, either piggybacked in the 
812 
FOpts field or, when sent as a separate data frame, in the FRMPayload field with the FPort 
813 
field being set to 0.  Piggybacked MAC commands are always sent encrypted and must not 
814 
exceed 15 octets.  MAC commands sent as FRMPayload are always encrypted and MUST 
815 
NOT exceed the maximum FRMPayload length.   
816 
A MAC command consists of a command identifier (CID) of 1 octet followed by a possibly 
817 
empty command-specific sequence of octets. 
818 
MAC Commands are answered/acknowledged by the receiving end in the same order than 
819 
they are transmitted. The answer to each MAC command is sequentially added to a buffer.  
820 
All MAC commands received in a single frame must be answered in a single frame, which 
821 
means that the buffer containing the answers must be sent in one single frame. If the MAC 
822 
answer’s buffer length is greater than the maximum FOpt field, the device MUST send the 
823 
buffer as FRMPayload on port 0. If the device has both application payload and MAC 
824 
answers to send and both cannot fit in the frame, the MAC answers SHALL be sent in 
825 
priority. If the length of the buffer is greater than the max FRMPayload size usable, the 
826 
device SHALL clip the buffer to the max FRMPayload size before assembling the frame. 
827 
Therefore the last MAC command answers may be truncated.  In all cases the full list of 
828 
MAC command is executed, even if the buffer containing the MAC answers must be clipped.  
829 
The Network Server MUST NOT generate a sequence of MAC commands that may not be 
830 
answered by the end-device in one single uplink. The Network Server SHALL compute the 
831 
max FRMPayload size available for answering MAC commands as follow: 
832 
 
If the latest uplink ADR bit is 0: The max payload size corresponding to the lowest 
833 
data rate MUST be considered 
834 
 
If the latest uplink ADR bit is set to 1: The max payload size corresponding to the 
835 
data rate used for the last uplink of the device MUST be considered 
836 
 
837 
Note: When receiving a clipped MAC answer the Network Server MAY 
838 
retransmit the MAC commands that could not be answered 
 
839

## Page 30

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 30 of 101 
The authors reserve the right to change 
specifications without notice. 
 
CID 
Command 
Transmitted 
by 
Short Description 
 
End-
device 
Gateway 
0x01 
ResetInd 
x 
 
Used by an ABP device to indicate a reset to 
the network and negotiate protocol version 
0x01 
ResetConf 
 
x 
Acknowledges ResetInd command 
0x02 
LinkCheckReq 
x 
 
Used by an end-device to validate its 
connectivity to a network. 
0x02 
LinkCheckAns 
 
x 
Answer to LinkCheckReq command.  
Contains the received signal power 
estimation indicating to the end-device the 
quality of reception (link margin). 
0x03 
LinkADRReq 
 
x 
Requests the end-device to change data 
rate, transmit power, repetition rate or 
channel. 
0x03 
LinkADRAns 
x 
 
Acknowledges the LinkADRReq. 
0x04 
DutyCycleReq 
 
x 
Sets the maximum aggregated transmit 
duty-cycle of a device 
0x04 
DutyCycleAns 
x 
 
Acknowledges a DutyCycleReq command 
0x05 
RXParamSetupReq 
 
x 
Sets the reception slots parameters 
0x05 
RXParamSetupAns 
x 
 
Acknowledges a RXParamSetupReq 
command 
0x06 
DevStatusReq 
 
x 
Requests the status of the end-device 
0x06 
DevStatusAns 
x 
 
Returns the status of the end-device, namely 
its battery level and its demodulation margin 
0x07 
NewChannelReq 
 
x 
Creates or modifies the definition of a radio 
channel 
0x07 
NewChannelAns 
x 
 
Acknowledges a NewChannelReq command 
0x08 
RXTimingSetupReq 
 
x 
Sets the timing of the of the reception slots   
0x08 
RXTimingSetupAns 
x 
 
Acknowledges RXTimingSetupReq 
command 
0x09 
TxParamSetupReq 
 
x 
Used by the Network Server to set the 
maximum allowed dwell time and Max EIRP 
of end-device, based on local regulations 
0x09 
TxParamSetupAns 
x 
 
Acknowledges TxParamSetupReq command 
0x0A 
DlChannelReq 
 
x 
Modifies the definition of a downlink RX1 
radio channel by shifting the downlink 
frequency from the uplink frequencies (i.e. 
creating an asymmetric channel) 
0x0A 
DlChannelAns 
x 
 
Acknowledges DlChannelReq command 
0x0B 
RekeyInd 
x 
 
Used by an OTA device to signal a security 
context update (rekeying) 
0x0B 
RekeyConf 
 
x 
Acknowledges RekeyInd command 
0x0C 
ADRParamSetupReq 
 
x 
Used by the Network Server to set the 
ADR_ACK_LIMT and ADR_ACK_DELAY 
parameters of an end-device 
0x0C 
ADRParamSetupAns 
x 
 
Acknowledges ADRParamSetupReq 
command 
0x0D 
DeviceTimeReq 
x 
 
Used by an end-device to request the 
current date and time 
0x0D 
DeviceTimeAns 
 
x 
Sent by the network, answer to the 
DeviceTimeReq request 
0x0E  
ForceRejoinReq 
 
x 
Sent by the network, ask the device to

## Page 31

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 31 of 101 
The authors reserve the right to change 
specifications without notice. 
 
CID 
Command 
Transmitted 
by 
Short Description 
 
End-
device 
Gateway 
Rejoin immediately with optional periodic 
retries 
0x0F 
RejoinParamSetupReq 
 
x 
Used by the network to set periodic device 
Rejoin messages  
0x0F 
RejoinParamSetupAns 
x 
 
Acknowledges RejoinParamSetupReq  
0x80 
to 
0xFF 
Proprietary 
x 
x 
Reserved for proprietary network command 
extensions 
Table 4: MAC commands 
840 
Note: In general the end device will only reply one time to any Mac 
841 
command received. If the answer is lost, the network has to send the 
842 
command again. The network decides that the command must be 
843 
resent when it receives a new uplink that doesn’t contain the answer. 
844 
Only 
the 
RxParamSetupReq, 
RxTimingSetupReq 
and 
845 
DlChannelReq 
have 
a 
different 
acknowledgment 
mechanism 
846 
described in their relative section, because they impact the downlink 
847 
parameters. 
848 
 
849 
Note: When a MAC command is initiated by the end device, the 
850 
network makes its best effort to send the acknowledgment/answer in 
851 
the RX1/RX2 windows immediately following the request. If the answer 
852 
is not received in that slot, the end device is free to implement any 
853 
retry mechanism it needs. 
854 
 
855 
Note: The length of a MAC command is not explicitly given and must 
856 
be implicitly known by the MAC implementation.  Therefore unknown 
857 
MAC commands cannot be skipped and the first unknown MAC 
858 
command terminates the processing of the MAC command sequence.  
859 
It is therefore advisable to order MAC commands according to the 
860 
version of the LoRaWAN specification which has introduced a MAC 
861 
command for the first time.  This way all MAC commands up to the 
862 
version of the LoRaWAN specification implemented can be processed 
863 
even in the presence of MAC commands specified only in a version of 
864 
the LoRaWAN specification newer than that implemented. 
865 
 
 
866

## Page 32

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 32 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
867 
5.1 Reset indication commands (ResetInd, ResetConf) 
868 
This MAC command is only available to ABP devices activated on a LoRaWAN1.1 
869 
compatible Network Server. LoRaWAN1.0 servers do not implement this MAC command 
870 
OTA devices MUST NOT implement this command. The Network Server SHALL ignore the 
871 
ResetInd command coming from an OTA device. 
872 
With the ResetInd command, an ABP end-device indicates to the network that it has been 
873 
re-initialized and that it has switched back to its default MAC & radio parameters (i.e the 
874 
parameters originally programmed into the device at fabrication except for the three frame 
875 
counters). The ResetInd command MUST be added to the FOpt field of all uplinks until a 
876 
ResetConf is received. 
877 
This command does not signal to the Network Server that the downlink frame counters have 
878 
been reset. The frame counters (both uplink & downlink) SHALL NEVER be reset in ABP 
879 
devices. 
880 
Note: This command is meant for ABP devices whose power might be 
881 
interrupted at some point (example, battery replacement). The device 
882 
might lose the MAC layer context stored in RAM (except the Frame 
883 
Counters that must be stored in an NVM). In that case the device 
884 
needs a way to convey that context loss to the Network Server. In 
885 
future versions of the LoRaWAN protocol, that command may also be 
886 
used to negotiate some protocol options between the device and the 
887 
Network Server. 
888 
The ResetInd command includes the minor of the LoRaWAN version supported by the end 
889 
device. 
890 
 
891 
Size (bytes) 
1 
ResetInd Payload 
Dev LoRaWAN version 
Figure 21 : ResetInd payload format 
892 
Size (bytes) 
7:4 
3:0 
Dev LoRaWAN version 
RFU 
Minor=1 
 
893 
 
894 
The minor field indicates the minor of the LoRaWAN version supported by the end-device. 
895 
Minor version 
Minor 
RFU 
0 
1 (LoRaWAN x.1) 
1 
RFU 
2:15

## Page 33

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 33 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
896 
When a ResetInd is received by the Network Server, it responds with a ResetConf 
897 
command. 
898 
The ResetConf command contains a single byte payload encoding the LoRaWAN version 
899 
supported by the Network Server using the same format than “dev LoRaWAN version”.  
900 
 
901 
 
902 
Size (bytes) 
1 
ResetConf Payload 
Serv LoRaWAN version 
Figure 22 : ResetConf payload format 
903 
The server’s version carried by the ResetConf must be the same than the device’s version. 
904 
Any other value is invalid. 
905 
If the server’s version is invalid the device SHALL discard the ResetConf command and 
906 
retransmit the ResetInd in the next uplink frame 
907 
 
908 
5.2 Link Check commands (LinkCheckReq, LinkCheckAns) 
909 
With the LinkCheckReq command, an end-device may validate its connectivity with the 
910 
network. The command has no payload.  
911 
When a LinkCheckReq is received by the Network Server via one or multiple gateways, it 
912 
responds with a LinkCheckAns command. 
913 
 
914 
Size (bytes) 
1 
1 
LinkCheckAns Payload 
Margin 
GwCnt 
Figure 23: LinkCheckAns payload format 
915 
The demodulation margin (Margin) is an 8-bit unsigned integer in the range of 0..254 
916 
indicating the link margin in dB of the last successfully received LinkCheckReq command.  
917 
A value of “0” means that the frame was received at the demodulation floor (0 dB or no 
918 
margin) while a value of “20”, for example, means that the frame reached the gateway 20 dB 
919 
above the demodulation floor. Value “255” is reserved. 
920 
The gateway count (GwCnt) is the number of gateways that successfully received the last 
921 
LinkCheckReq command. 
922 
5.3 Link ADR commands (LinkADRReq, LinkADRAns) 
923 
With the LinkADRReq command, the Network Server requests an end-device to perform a 
924 
rate adaptation. 
925 
 
926 
Size (bytes) 
1 
2 
1 
LinkADRReq Payload 
DataRate_TXPower 
ChMask 
Redundancy 
Figure 24 : LinkADRReq payload format 
927 
 
928 
Bits 
[7:4] 
[3:0]

## Page 34

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 34 of 101 
The authors reserve the right to change 
specifications without notice. 
 
DataRate_TXPower 
DataRate 
TXPower 
 
929 
The requested date rate (DataRate) and TX output power (TXPower) are region-specific 
930 
and are encoded as indicated in [PHY]. The TX output power indicated in the command is to 
931 
be considered the maximum transmit power the device may operate at.  An end-device will 
932 
acknowledge as successful a command which specifies a higher transmit power than it is 
933 
capable of using and MUST, in that case, operate at its maximum possible power. A value 
934 
0xF (15 in decimal format) of either DataRate or TXPower means that the device MUST 
935 
ignore that field, and keep the current parameter value. The channel mask (ChMask) 
936 
encodes the channels usable for uplink access as follows with bit 0 corresponding to the 
937 
LSB: 
938 
Bit# 
Usable channels 
0 
Channel 1 
1 
Channel 2 
.. 
.. 
15 
Channel 16 
Table 5: Channel state table 
939 
A bit in the ChMask field set to 1 means that the corresponding channel can be used for 
940 
uplink transmissions if this channel allows the data rate currently used by the end-device. A 
941 
bit set to 0 means the corresponding channels should be avoided.  
942 
 
943 
Bits 
7 
[6:4] 
[3:0] 
Redundancy bits 
RFU 
ChMaskCntl 
NbTrans 
In the Redundancy bits the NbTrans field is the number of transmissions for each uplink 
944 
message. This applies to “confirmed” and “unconfirmed” uplink frames. The default value is 
945 
1 corresponding to a single transmission of each frame. The valid range is [1:15]. If 
946 
NbTrans==0 is received the end-device SHALL keep the current NbTrans value unchanged.  
947 
The channel mask control (ChMaskCntl) field controls the interpretation of the previously 
948 
defined ChMask bit mask. It controls the block of 16 channels to which the ChMask applies. 
949 
It can also be used to globally turn on or off all channels using specific modulation. This field 
950 
usage is region specific and is defined in [PHY].  
951 
The Network Server may include multiple contiguous LinkADRReq commands within a 
952 
single downlink message.  For the purpose of configuring the end-device channel mask, the 
953 
end-device MUST process all contiguous LinkADRReq messages, in the order present in 
954 
the downlink message, as a single atomic block command.  The Network Server MUST NOT 
955 
include more than one such atomic block command in a downlink message. The end-device 
956 
MUST send a single LinkADRAns command to accept or reject an entire ADR atomic 
957 
command block. If the downlink message carries more than one ADR atomic command 
958 
block, the end-device SHALL process only the first one and send a NAck (a LinkADRAns 
959 
command with all Status bits set to 0) in response to all other ADR command block.   The 
960 
device MUST only process the DataRate, TXPower and NbTrans from the last LinkADRReq 
961 
command in the contiguous ADR command block, as these settings govern the end-device 
962 
global state for these values.  The Channel mask ACK bit of the response MUST reflect the 
963 
acceptance/rejection of the final channel plan after in-order-processing of all the Channel 
964 
Mask Controls in the contiguous ADR command block.  
965 
The channel frequencies are region-specific and they are defined [PHY]. An end-device 
966 
answers to a LinkADRReq with a LinkADRAns command. 
967 
 
968 
 
969 
Size (bytes) 
1

## Page 35

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 35 of 101 
The authors reserve the right to change 
specifications without notice. 
 
LinkADRAns Payload 
Status 
Figure 25 : LinkADRAns payload format 
970 
 
971 
Bits 
[7:3] 
2 
1 
0 
Status bits 
RFU 
Power ACK 
Data rate ACK 
Channel mask 
ACK 
 
972 
The LinkADRAns Status bits have the following meaning: 
973 
 
974 
 
Bit = 0 
Bit = 1 
Channel mask ACK 
The channel mask sent 
enables a yet undefined 
channel or the channel mask 
required all channels to be 
disabled. The command was 
discarded and the end-
device state was not 
changed. 
The channel mask sent was 
successfully interpreted. All 
currently defined channel 
states were set according to 
the mask. 
Data rate ACK 
The data rate requested is 
unknown to the end-device 
or is not possible given the 
channel mask provided (not 
supported by any of the 
enabled channels). The 
command was discarded and 
the end-device state was not 
changed. 
The data rate was 
successfully set or the 
DataRate field of the request 
was set to 15, meaning it 
was ignored 
Power ACK 
The device is unable to 
operate at or below the 
requested power level. The 
command was discarded and 
the end-device state was not 
changed. 
The device is able to operate 
at or below the requested 
power level, or the TXPower 
field of the request was set to 
15, meaning it shall be 
ignored 
Table 6: LinkADRAns status bits signification 
975 
If any of those three bits equals 0, the command did not succeed and the node has kept the 
976 
previous state. 
977 
5.4 End-Device Transmit Duty Cycle (DutyCycleReq, DutyCycleAns) 
978 
The DutyCycleReq command is used by the network coordinator to limit the maximum 
979 
aggregated transmit duty cycle of an end-device. The aggregated transmit duty cycle 
980 
corresponds to the transmit duty cycle over all sub-bands.  
981 
 
 
982

## Page 36

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 36 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
983 
Size (bytes) 
1 
DutyCycleReq Payload 
DutyCyclePL 
Figure 26 : DutyCycleReq payload format 
984 
Bits 
7:4 
3:0 
DutyCyclePL 
RFU 
MaxDCycle 
 
985 
 
986 
 
987 
The maximum end-device transmit duty cycle allowed is: 
988 
𝑎𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑒𝑑 𝑑𝑢𝑡𝑦 𝑐𝑦𝑐𝑙𝑒= 
1
2MaxDCycle 
989 
The valid range for MaxDutyCycle is [0 : 15]. A value of 0 corresponds to “no duty cycle 
990 
limitation” except the one set by the regional regulation. 
991 
An end-device answers to a DutyCycleReq with a DutyCycleAns command. The 
992 
DutyCycleAns MAC reply does not contain any payload. 
993 
5.5 Receive Windows Parameters (RXParamSetupReq, 
994 
RXParamSetupAns) 
995 
The RXParamSetupReq command allows a change to the frequency and the data rate set 
996 
for the second receive window (RX2) following each uplink. The command also allows to 
997 
program an offset between the uplink and the RX1 slot downlink data rates. 
998 
 
999 
Size (bytes) 
1 
3 
RXParamSetupReq Payload 
DLsettings 
Frequency 
Figure 27 : RXParamSetupReq payload format 
1000 
Bits 
7 
6:4 
3:0 
DLsettings 
RFU 
RX1DRoffset 
RX2DataRate 
 
1001 
The RX1DRoffset field sets the offset between the uplink data rate and the downlink data 
1002 
rate used to communicate with the end-device on the first reception slot (RX1). As a default 
1003 
this offset is 0. The offset is used to take into account maximum power density constraints 
1004 
for base stations in some regions and to balance the uplink and downlink radio link margins. 
1005 
The data rate (RX2DataRate) field defines the data rate of a downlink using the second 
1006 
receive window following the same convention as the LinkADRReq command (0 means 
1007 
DR0/125kHz for example). The frequency (Frequency) field corresponds to the frequency of 
1008 
the channel used for the second receive window, whereby the frequency is coded following 
1009 
the convention defined in the NewChannelReq command. 
1010 
The RXParamSetupAns command is used by the end-device to acknowledge the reception 
1011 
of RXParamSetupReq command. The RXParamSetupAns command MUST be added in 
1012 
the FOpt field of all uplinks until a class A downlink is received by the end-device. This 
1013 
guarantees that even in presence of uplink packet loss, the network is always aware of the 
1014 
downlink parameters used by the end-device. 
1015 
 
 
1016

## Page 37

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 37 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 The payload contains a single status byte. 
1017 
Size (bytes) 
1 
RXParamSetupAns Payload 
Status 
Figure 28 : RXParamSetupAns payload format 
1018 
The status (Status) bits have the following meaning. 
1019 
 Bits 
7:3 
2 
1 
0 
Status 
bits 
RFU 
RX1DRoffset 
ACK 
RX2 Data rate 
ACK 
Channel ACK 
 
1020 
 
Bit = 0 
Bit = 1 
Channel ACK 
The frequency requested is 
not usable by the end-
device.  
RX2 slot channel was 
successfully set 
RX2DataRate ACK 
The data rate requested is 
unknown to the end-device.  
RX2 slot data rate was 
successfully set 
RX1DRoffset ACK 
the uplink/downlink data rate 
offset for RX1 slot is not in 
the allowed range  
RX1DRoffset was 
successfully set 
Table 7: RXParamSetupAns status bits signification 
1021 
If either of the 3 bits is equal to 0, the command did not succeed and the previous 
1022 
parameters MUST be kept. 
1023 
 
1024 
5.6 End-Device Status (DevStatusReq, DevStatusAns) 
1025 
With the DevStatusReq command a Network Server may request status information from 
1026 
an end-device. The command has no payload. If a DevStatusReq is received by an end-
1027 
device, it MUST respond with a DevStatusAns command. 
1028 
 
1029 
Size (bytes) 
1 
1 
DevStatusAns Payload 
Battery 
Margin 
Figure 29 : DevStatusAns payload format 
1030 
The battery level (Battery) reported is encoded as follows: 
1031 
Battery 
Description 
0 
The end-device is connected to an external 
power source. 
1..254 
The battery level, 1 being at minimum and 
254 being at maximum 
255 
The end-device was not able to measure the 
battery level. 
Table 8: Battery level decoding 
1032 
The margin (Margin) is the demodulation signal-to-noise ratio in dB rounded to the nearest 
1033 
integer value for the last successfully received DevStatusReq command.  It is a signed 
1034 
integer of 6 bits with a minimum value of -32 and a maximum value of 31. 
1035 
 Bits 
7:6 
5:0 
Status 
RFU 
Margin

## Page 38

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 38 of 101 
The authors reserve the right to change 
specifications without notice. 
 
5.7 Creation / Modification of a Channel (NewChannelReq, 
1036 
NewChannelAns, DlChannelReq, DlChannelAns) 
1037 
 
1038 
Devices operating in region where a fixed channel plan is defined shall not implement these 
1039 
MAC commands. The commands SHALL not be answered by the device. Please refer to 
1040 
[PHY] for applicable regions. 
1041 
 
1042 
The NewChannelReq command can be used to either modify the parameters of an existing 
1043 
bidirectional channel or to create a new one. The command sets the center frequency of the 
1044 
new channel and the range of uplink data rates usable on this channel: 
1045 
 
1046 
Size (bytes) 
1 
3 
1 
NewChannelReq Payload 
ChIndex 
Freq 
DrRange 
Figure 30 : NewChannelReq payload format 
1047 
The channel index (ChIndex) is the index of the channel being created or modified. 
1048 
Depending on the region and frequency band used, in certain regions ([PHY]) the LoRaWAN 
1049 
specification imposes default channels which must be common to all devices and cannot be 
1050 
modified by the NewChannelReq command .If the number of default channels is N, the 
1051 
default channels go from 0 to N-1, and the acceptable range for ChIndex is N to 15. A 
1052 
device must be able to handle at least 16 different channel definitions. In certain regions the 
1053 
device may have to store more than 16 channel definitions. 
1054 
 
1055 
The frequency (Freq) field is a 24 bits unsigned integer. The actual channel frequency in Hz 
1056 
is 100 x Freq whereby values representing frequencies below 100 MHz are reserved for 
1057 
future use. This allows setting the frequency of a channel anywhere between 100 MHz to 
1058 
1.67 GHz in 100 Hz steps. A Freq value of 0 disables the channel. The end-device MUST 
1059 
check that the frequency is actually allowed by its radio hardware and return an error 
1060 
otherwise. 
1061 
 
1062 
The data-rate range (DrRange) field specifies the uplink data-rate range allowed for this 
1063 
channel. The field is split in two 4-bit indexes: 
1064 
Bits 
7:4 
3:0 
DrRange 
MaxDR 
MinDR 
 
1065 
Following the convention defined in Section 5.3 the minimum data rate (MinDR) subfield 
1066 
designate the lowest uplink data rate allowed on this channel. For example using European 
1067 
regional parameters, 0 designates DR0 / 125 kHz. Similarly, the maximum data rate 
1068 
(MaxDR) designates the highest uplink data rate. For example, DrRange = 0x77 means that 
1069 
only 50 kbps GFSK is allowed on a channel and DrRange = 0x50 means that DR0 / 125 kHz 
1070 
to DR5 / 125 kHz are supported. 
1071 
The newly defined or modified channel is enabled and can immediately be used for 
1072 
communication. The RX1 downlink frequency is set equal to the uplink frequency. 
1073 
The end-device acknowledges the reception of a NewChannelReq by sending back a 
1074 
NewChannelAns command. The payload of this message contains the following 
1075 
information: 
1076 
Size (bytes) 
1 
NewChannelAns Payload 
Status 
Figure 31 : NewChannelAns payload format 
1077

## Page 39

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 39 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
1078 
The status (Status) bits have the following meaning: 
1079 
 
1080 
 Bits 
7:2 
1 
0 
Status 
RFU 
Data rate 
range ok 
Channel 
frequency ok 
 
1081 
 
1082 
 
1083 
 
1084 
 
Bit = 0 
Bit = 1 
Data rate range ok 
The designated data rate 
range exceeds the ones 
currently defined for this end-
device 
The data rate range is 
compatible with the 
possibilities of the end-
device 
Channel frequency 
ok 
The device cannot use this 
frequency 
The device is able to use this 
frequency. 
Table 9: NewChannelAns status bits signification 
1085 
If either of those 2 bits equals 0, the command did not succeed and the new channel has not 
1086 
been created. 
1087 
 
1088 
The DlChannelReq command allows the network to associate a different downlink 
1089 
frequency to the RX1 slot. This command is applicable for all the physical layer 
1090 
specifications supporting the NewChannelReq command (for example EU and China 
1091 
physical layers, but not for US or Australia).  
1092 
The command sets the center frequency used for the downlink RX1 slot, as follows: 
1093 
 
1094 
Size (bytes) 
1 
3 
DlChannelReq Payload 
ChIndex 
Freq 
Figure 32 : DLChannelReq payload format 
1095 
The channel index (ChIndex) is the index of the channel whose downlink frequency is 
1096 
modified 
1097 
The frequency (Freq) field is a 24 bits unsigned integer. The actual downlink frequency in Hz 
1098 
is 100 x Freq whereby values representing frequencies below 100 MHz are reserved for 
1099 
future use. The end-device has to check that the frequency is actually allowed by its radio 
1100 
hardware and return an error otherwise. 
1101 
The end-device acknowledges the reception of a DlChannelReq by sending back a 
1102 
DlChannelAns command. The DlChannelAns command SHALL be added in the FOpt field 
1103 
of all uplinks until a downlink packet is received by the end-device. This guarantees that 
1104 
even in presence of uplink packet loss, the network is always aware of the downlink 
1105 
frequencies used by the end-device. 
1106 
The payload of this message contains the following information: 
1107 
Size (bytes) 
1 
DlChannelAns Payload 
Status 
Figure 33 : DLChannelAns payload format 
1108 
 
 
1109

## Page 40

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 40 of 101 
The authors reserve the right to change 
specifications without notice. 
 
The status (Status) bits have the following meaning: 
1110 
Bits 
7:2 
1 
0 
Status 
RFU 
Uplink frequency 
exists 
Channel 
frequency ok 
 
1111 
 
Bit = 0 
Bit = 1 
Channel 
frequency ok 
The device cannot use this frequency 
The device is able to 
use this frequency. 
 
Uplink 
frequency 
exists 
The uplink frequency is not defined for this 
channel , the downlink frequency can only be 
set for a channel that already has a valid 
uplink frequency 
The uplink frequency 
of the channel is 
valid 
Table 10: DlChannelAns status bits signification 
1112 
 
1113 
5.8 Setting delay between TX and RX (RXTimingSetupReq, 
1114 
RXTimingSetupAns) 
1115 
The RXTimingSetupReq command allows configuring the delay between the end of the TX 
1116 
uplink and the opening of the first reception slot. The second reception slot opens one 
1117 
second after the first reception slot. 
1118 
 
1119 
Size (bytes) 
1 
RXTimingSetupReq Payload 
Settings 
Figure 34 : RXTimingSetupReq payload format 
1120 
 
1121 
The delay (Delay) field specifies the delay. The field is split in two 4-bit indexes: 
1122 
Bits 
7:4 
3:0 
Settings 
RFU 
Del 
 
1123 
The delay is expressed in seconds. Del 0 is mapped on 1 s. 
1124 
 
1125 
Del 
Delay [s] 
0 
1 
1 
1 
2 
2 
3 
3 
.. 
.. 
15 
15 
Table 11: RXTimingSetup Delay mapping table 
1126 
 
1127 
An end device answers RXTimingSetupReq with RXTimingSetupAns with no payload. 
1128 
The RXTimingSetupAns command should be added in the FOpt field of all uplinks until a 
1129 
class A downlink is received by the end-device. This guarantees that even in presence of 
1130

## Page 41

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 41 of 101 
The authors reserve the right to change 
specifications without notice. 
 
uplink packet loss, the network is always aware of the downlink parameters used by the end-
1131 
device. 
1132 
 
1133 
5.9 End-device transmission parameters (TxParamSetupReq, 
1134 
TxParamSetupAns) 
1135 
This MAC command only needs to be implemented for compliance in certain regulatory 
1136 
regions. Please refer to [PHY]. 
1137 
The TxParamSetupReq command can be used to notify the end-device of the maximum 
1138 
allowed dwell time, i.e. the maximum continuous transmission time of a packet over the air, 
1139 
as well as the maximum allowed end-device Effective Isotropic Radiated Power (EIRP). 
1140 
 
1141 
 
1142 
 
1143 
Figure 35 : TxParamSetupReq payload format 
1144 
The structure of EIRP_DwellTime field is described below: 
1145 
Bits 
7:6 
5 
4 
3:0 
MaxDwellTime 
RFU 
DownlinkDwellTime 
UplinkDwellTime 
MaxEIRP 
 
1146 
Bits [0…3] of TxParamSetupReq command are used to encode the Max EIRP value, as per 
1147 
the following table. The EIRP values in this table are chosen in a way that covers a wide 
1148 
range of max EIRP limits imposed by the different regional regulations.  
1149 
 
1150 
Coded Value 
0 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
11 
12 13 
14 
15 
Max EIRP (dBm) 
8 
10 12 
13 
14 
16 
18 
20 
21 
24 
26 
27 
29 30 
33 
36 
Table 12 : TxParamSetup EIRP encoding table 
1151 
The maximum EIRP corresponds to an upper bound on the device’s radio transmit power. 
1152 
The device is not required to transmit at that power, but shall never radiate more that this 
1153 
specified EIRP. 
1154 
Bits 4 and 5 define the maximum uplink and downlink dwell time respectively, which is 
1155 
encoded as per the following table: 
1156 
Coded Value 
Dwell Time 
0 
No Limit 
1 
400 ms 
 
1157 
When this MAC command is implemented (region specific), the end-device acknowledges 
1158 
the TxParamSetupReq command by sending a TxParamSetupAns command. This 
1159 
TxParamSetupAns command doesn’t contain any payload. 
1160 
When this MAC command is used in a region where it is not required, the device does not 
1161 
process it and shall not transmit an acknowledgement. 
1162 
Size (bytes) 
1 
TxParamSetupReq payload 
EIRP_DwellTime

## Page 42

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 42 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
1163 
5.10 Rekey indication commands (RekeyInd, RekeyConf) 
1164 
This MAC command is only available to OTA devices activated on a LoRaWAN1.1 
1165 
compatible Network Server. LoRaWAN1.0 servers do not implement this MAC command. 
1166 
ABP devices MUST NOT implement this command. The Network Server SHALL ignore the 
1167 
RekeyInd command coming from an ABP device. 
1168 
For OTA devices the RekeyInd MAC command is used to confirm security key update and 
1169 
in future versions of LoRaWAN (>1.1) to negotiate the minor LoRaWAN protocol version 
1170 
running between the end-device and the Network Server. The command does not signal a 
1171 
reset of the MAC & radio parameters (see 6.2.3). 
1172 
The RekeyInd command includes the minor of the LoRaWAN version supported by the end 
1173 
device. 
1174 
 
1175 
Size (bytes) 
1 
RekeyInd Payload 
Dev LoRaWAN version 
Figure 36 : RekeyInd payload format 
1176 
 
1177 
Size (bytes) 
7:4 
3:0 
Dev LoRaWAN version 
RFU 
Minor=1 
 
1178 
 
1179 
The minor field indicates the minor of the LoRaWAN version supported by the end-device. 
1180 
 
1181 
Minor version 
Minor 
RFU 
0 
1 (LoRaWAN x.1) 
1 
RFU 
2:15 
 
1182 
OTA devices SHALL send the RekeyInd in all confirmed & unconfirmed uplink frames 
1183 
following the successful processing of a Join-accept (new session keys have been derived) 
1184 
until a RekeyConf is received. If the device has not received a RekeyConf within the first 
1185 
ADR_ACK_LIMIT uplinks it SHALL revert to the Join state. RekeyInd commands sent by 
1186 
such devices at any later time SHALL be discarded by the Network Server. The Network 
1187 
Server SHALL discard any uplink frames protected with the new security context that are 
1188 
received after the transmission of the Join-accept and before the first uplink frame that 
1189 
carries a RekeyInd command.  
1190 
When a RekeyInd is received by the Network Server, it responds with a RekeyConf 
1191 
command. 
1192 
The RekeyConf command contains a single byte payload encoding the LoRaWAN version 
1193 
supported by the Network Server using the same format than “dev LoRaWAN version”.  
1194 
 
 
1195

## Page 43

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 43 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
1196 
Size (bytes) 
1 
RekeyConf Payload 
Serv LoRaWAN version 
Figure 37 : RekeyConf payload format 
1197 
The server version must be greater than 0 (0 is not allowed), and smaller or equal (<=) to the 
1198 
device’s LoRaWAN version. Therefore for a LoRaWAN1.1 device the only valid value is 1. If 
1199 
the server’s version is invalid the device SHALL discard the RekeyConf command and 
1200 
retransmit the RekeyInd in the next uplink frame 
1201 
 
1202 
5.11 ADR parameters (ADRParamSetupReq, ADRParamSetupAns) 
1203 
The ADRParamSetupReq command allows changing the ADR_ACK_LIMIT and 
1204 
ADR_ACK_DELAY 
parameters 
defining 
the 
ADR 
back-off 
algorithm. 
The 
1205 
ADRParamSetupReq command has a single byte payload. 
1206 
 
1207 
Size (bytes) 
1 
ADRParamSetupReq Payload 
ADRparam 
Figure 38 : ADRParamSetupReq payload format 
1208 
Bits 
7:4 
3:0 
ADRparam 
Limit_exp 
Delay_exp 
 
1209 
The Limit_exp field sets the ADR_ACK_LIMIT parameter value:  
1210 
ADR_ACK_LIMIT = 2^Limit_exp 
1211 
 
1212 
The Limit_exp valid range is 0 to 15, corresponding to a range of 1 to 32768 for 
1213 
ADR_ACK_LIMIT 
1214 
 
1215 
The Delay_exp field sets the ADR_ACK_DELAY parameter value.  
1216 
ADR_ACK_ DELAY = 2^Delay_exp 
1217 
 
1218 
The Delay_exp valid range is 0 to 15, corresponding to a range of 1 to 32768 for 
1219 
ADR_ACK_ DELAY 
1220 
 
1221 
The ADRParamSetupAns command is used by the end-device to acknowledge the 
1222 
reception of ADRParamSetupReq command. The ADRParamSetupAns command has no 
1223 
payload field. 
1224 
 
1225

## Page 44

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 44 of 101 
The authors reserve the right to change 
specifications without notice. 
 
5.12 DeviceTime commands (DeviceTimeReq, DeviceTimeAns) 
1226 
This MAC command is only available if the device is activated on a LoRaWAN1.1 
1227 
compatible Network Server. LoRaWAN1.0 servers do not implement this MAC command. 
1228 
With the DeviceTimeReq command, an end-device may request from the network the 
1229 
current network date and time. The request has no payload. 
1230 
With the DeviceTimeAns command, the Network Server provides the network date and 
1231 
time to the end device. The time provided is the network time captured at the end of the 
1232 
uplink transmission. The command has a 5 bytes payload defined as follows: 
1233 
 
1234 
Size (bytes) 
4 
1 
DeviceTimeAns 
Payload 
32-bit unsigned integer : Seconds since 
epoch* 
8bits unsigned integer: fractional-
second 
in ½^8 second steps 
Figure 39 : DeviceTimeAns payload format 
1235 
The time provided by the network MUST have a worst case accuracy of +/-100mSec.  
1236 
 
1237 
(*) The GPS epoch (i.e Sunday January the 6th 1980 at midnight) is used as origin. The 
1238 
“seconds” field is the number of seconds elapsed since the origin. This field is monotonically 
1239 
increasing by 1 every second. To convert this field to UTC time, the leap seconds must be 
1240 
taken into account.  
1241 
Example: Friday 12th of February 2016 at 14:24:31 UTC corresponds 
1242 
to 1139322288 seconds since GPS epoch. As of June 2017, the GPS 
1243 
time is 17seconds ahead of UTC time. 
1244 
 
1245 
5.13 Force Rejoin Command (ForceRejoinReq) 
1246 
With the Force Rejoin command, the network asks a device to immediately transmit a  
1247 
Rejoin-Request Type 0 or type 2 message with a programmable number of retries, 
1248 
periodicity and data rate. This RejoinReq uplink may be used by the network to immediately 
1249 
rekey a device or initiate a handover roaming procedure. 
1250 
The command has two bytes of payload. 
1251 
 
1252 
 
1253 
Bits 
15:14 
13:11 
10:8 
7 
6:4 
3:0 
ForceRejoinReq bits 
RFU 
Period 
Max_Retries 
RFU 
RejoinType 
DR 
Figure 40 : ForceRejoinReq payload format 
1254

## Page 45

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 45 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
1255 
The parameters are encoded as follow: 
1256 
Period:  The delay between retransmissions SHALL be equal to 32 seconds x 2Period + 
1257 
Rand32, where Rand32 is a pseudo-random number in the [0:32] range.   
1258 
Max_Retries: The total number of times the device will retry the Rejoin-request.  
1259 
 
0 : the Rejoin is sent only once (no retry) 
1260 
 
1 : the Rejoin MUST be sent 2 times in total (1 + 1 retry) 
1261 
 
… 
1262 
 
7: the Rejoin MUST be sent 8 times ( 1 + 7 retries) 
1263 
RejoinType: This field specifies the type of Rejoin-request that shall be transmitted by the 
1264 
device. 
1265 
 
0 or 1 : A Rejoin-request type 0 shall be transmitted 
1266 
 
2 : A Rejoin-request type 2 shall be transmitted 
1267 
 
3 to 7 : RFU 
1268 
DR: The Rejoin-request frame SHALL be transmitted using the data rate DR. The 
1269 
correspondence between the actual physical modulation data rate and the DR value follows 
1270 
the same convention as the LinkADRReq command and is defined for each region in [PHY] 
1271 
The command has no answer, as the device MUST send a Rejoin-Request when receiving 
1272 
the command. The first transmission of a RejoinReq message SHALL be done immediately 
1273 
after the reception of the command (but the network may not receive it). If the device 
1274 
receives a new ForceRejoinReq command before it has reached the number of 
1275 
transmission retries, the device SHALL resume transmission of RejoinReq with the new 
1276 
parameters. 
1277 
 
1278 
5.14 RejoinParamSetupReq (RejoinParamSetupAns) 
1279 
With the RejoinParamSetupReq command, the network may request the device to 
1280 
periodically send a RejoinReq Type 0 message with a programmable periodicity defined as 
1281 
a time or a number of uplinks.  
1282 
Both time and count are proposed to cope with devices which may not have time 
1283 
measurement capability. The periodicity specified sets the maximum time or number of 
1284 
uplink between two RejoinReq transmissions. The device MAY send RejoinReq more 
1285 
frequently.  
1286 
  
1287 
The command has a single byte payload. 
1288 
Bits 
7:4 
3:0 
RejoinParamSetupReq bits 
MaxTimeN 
MaxCountN 
Figure 41 : RejoinParamSetupReq payload format 
1289

## Page 46

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 46 of 101 
The authors reserve the right to change 
specifications without notice. 
 
The parameters are defined as follow: 
1290 
 
1291 
MaxCountN = C = 0 to 15. The device MUST send a Rejoin-request type 0 at least every 
1292 
2C+4 uplink messages. 
1293 
MaxTimeN = T = 0 to 15; the device MUST send a Rejoin-request type 0 at least every 2T+10 
1294 
seconds. 
1295 
 
T = 0 corresponds to roughly 17 minutes 
1296 
 
T = 15 is about 1 year 
1297 
 
1298 
A RejoinReq packet is sent every time one of the 2 conditions (frame Count or Time) is met. 
1299 
The device MUST implement the uplink count periodicity. Time based periodicity is 
1300 
OPTIONAL. A device that cannot implement time limitation MUST signal it in the answer  
1301 
The answer has a single byte payload. 
1302 
Bits 
Bits 7:1 
Bit 0 
Status bits 
RFU 
TimeOK 
Figure 42 : RejoinParamSetupAns payload format 
1303 
If Bit 0 = 1, the device has accepted Time and Count limitations, otherwise it only accepts 
1304 
the count limitation. 
1305 
 
1306 
Note:  For devices that have a very low message rate and no time 
1307 
measurement capability, the mechanism to agree on the optimal count 
1308 
limitation is not specified in LoRaWAN.  
1309

## Page 47

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 47 of 101 
The authors reserve the right to change 
specifications without notice. 
 
6 End-Device Activation 
1310 
To participate in a LoRaWAN network, each end-device has to be personalized and 
1311 
activated.  
1312 
Activation of an end-device can be achieved in two ways, either via Over-The-Air 
1313 
Activation (OTAA) or via Activation By Personalization (ABP)  
1314 
6.1 Data Stored in the End-device  
1315 
6.1.1 
Before Activation 
1316 
6.1.1.1 JoinEUI 
1317 
The JoinEUI is a global application ID in IEEE EUI64 address space that uniquely identifies 
1318 
the Join Server that is able to assist in the processing of the Join procedure and the session 
1319 
keys derivation. 
1320 
For OTAA devices, the JoinEUI MUST be stored in the end-device before the Join 
1321 
procedure is executed. The JoinEUI is not required for ABP only end-devices 
1322 
6.1.1.2 DevEUI 
1323 
The DevEUI is a global end-device ID in IEEE EUI64 address space that uniquely identifies 
1324 
the end-device. 
1325 
DevEUI is the recommended unique device identifier by Network Server(s), whatever 
1326 
activation procedure is used, to identify a device roaming across networks.    
1327 
For OTAA devices, the DevEUI MUST be stored in the end-device before the Join 
1328 
procedure is executed. ABP devices do not need the DevEUI to be stored in the device 
1329 
itself, but it is RECOMMENDED to do so. 
1330 
Note: It is a recommended practice that the DevEUI should also be 
1331 
available on a device label, for device administration. 
1332

## Page 48

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 48 of 101 
The authors reserve the right to change 
specifications without notice. 
 
6.1.1.3 Device root keys (AppKey & NwkKey) 
1333 
The NwkKey and AppKey are AES-128 root keys specific to the end-device that are 
1334 
assigned to the end-device during fabrication.1 Whenever an end-device joins a network via 
1335 
over-the-air activation, the NwkKey is used to derive the FNwkSIntKey , SNwkSIntKey and 
1336 
NwkSEncKey session keys, and AppKey is used to derive the AppSKey session key  
1337 
 
1338 
Note: When working with a v1.1 Network Server, the application 
1339 
session key is derived only from the AppKey, therefore the NwkKey 
1340 
may be surrendered to the network operator to manage the JOIN 
1341 
procedure without enabling the operator to eavesdrop on the 
1342 
application payload data. 
1343 
Secure provisioning, storage, and usage of root keys NwkKey and AppKey on the end-
1344 
device and the backend are intrinsic to the overall security of the solution. These are left to 
1345 
implementation and out of scope of this document. However, elements of this solution may 
1346 
include SE (Secure Elements) and HSM (Hardware Security Modules). 
1347 
To ensure backward compatibility with LoraWAN 1.0 and earlier Network Servers that do not 
1348 
support two root keys, the end-device MUST default back to the single root key scheme 
1349 
when joining such a network. In that case only the root NwkKey is used. This condition is 
1350 
signaled to the end-device by the “OptNeg” bit (bit 7) of the DLsetting field of the Join-accept 
1351 
message being zero. The end-device in this case MUST  
1352 
 
Use the NwkKey to derive both the AppSKey and the FNwkSIntKey session keys as 
1353 
in LoRaWAN1.0 specification.  
1354 
 
Set the SNwkSIntKey & NwkSEncKey equal to FNwkSIntKey, the same network 
1355 
session key is effectively used for both uplink and downlink MIC calculation and 
1356 
encryption of MAC payloads according to the LoRaWAN1.0 specification. 
1357 
 
1358 
A NwkKey MUST be stored on an end-device intending to use the OTAA procedure.  
1359 
A NwkKey is not required for ABP only end-devices. 
1360 
An AppKey MUST be stored on an end-device intending to use the OTAA procedure.  
1361 
An Appkey is not required for ABP only end-devices.  
1362 
Both the NwkKey and AppKey SHOULD be stored in a way that prevents extraction and re-
1363 
use by malicious actors. 
1364 
 
1365 
6.1.1.4 JSIntKey and JSEncKey derivation 
1366 
For OTA devices two specific lifetime keys are derived from the NwkKey root key: 
1367 
 
JSIntKey is used to MIC Rejoin-Request type 1 messages and Join-Accept answers 
1368 
 
JSEncKey is used to encrypt the Join-Accept triggered by a Rejoin-Request 
1369 
                                                
1. Since all end-devices are equipped with unique application and network root keys specific for each 
end-device, extracting the AppKey/NwkKey from an end-device only compromises this one end-
device.

## Page 49

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 49 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
1370 
 
1371 
JSIntKey = aes128_encrypt(NwkKey, 0x06 | DevEUI  | pad16) 
1372 
JSEncKey = aes128_encrypt(NwkKey, 0x05  | DevEUI  | pad16) 
1373 
 
1374 
6.1.2 
 After Activation 
1375 
After activation, the following additional informations are stored in the end-device: a device 
1376 
address (DevAddr), a triplet of network session key (NwkSEncKey/ SNwkSIntKey/ 
1377 
FNwkSIntKey), and an application session key (AppSKey). 
1378 
6.1.2.1 End-device address (DevAddr) 
1379 
The DevAddr consists of 32 bits and identifies the end-device within the current network. 
1380 
The DevAddr is allocated by the Network Server of the end-device. 
1381 
Its format is as follows: 
1382 
 
1383 
Bit# 
[31..32-N] 
[31-N..0] 
DevAddr bits 
AddrPrefix 
NwkAddr 
Figure 43 : DevAddr fields 
1384 
 
1385 
Where N is an integer in the [7:24] range. 
1386 
 
1387 
The LoRaWAN protocol supports various network address types with different network 
1388 
address space sizes. The variable size AddrPrefix field is derived from the Network Server’s 
1389 
unique identifier NetID (see 6.2.3) allocated by the LoRa Alliance with the exception of the 
1390 
AddrPrefix values reserved for experimental/private network. The AddrPrefix field enables 
1391 
the discovery of the Network Server currently managing the end-device during roaming. 
1392 
Devices that do not respect this rule cannot roam between two networks because their home 
1393 
Network Server cannot be found. 
1394 
The least significant (32-N) bits, the network address (NwkAddr) of the end-device, can be 
1395 
arbitrarily assigned by the network manager. 
1396 
The following AddrPrefix values may be used by any private/experimental network and will 
1397 
not be allocated by the LoRa Aliance. 
1398 
 
 
1399

## Page 50

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 50 of 101 
The authors reserve the right to change 
specifications without notice. 
 
Private/experimental network reserved AddrPrefix 
N = 7 
AddrPrefix = 7’b0000000 or AddrPrefix = 7’b0000001 
NwkAddr = 25bits freely allocated by the network manager 
 
1400 
Please refer to [BACKEND] for the exact construction of the AddrPrefix field and the 
1401 
definition of the various address classes. 
1402 
 
1403 
6.1.2.2 Forwarding Network session integrity key (FNwkSIntKey) 
1404 
The FNwkSIntKey is a network session key specific for the end-device. It is used by the end-
1405 
device to calculate the MIC or part of the MIC (message integrity code) of all uplink data 
1406 
messages to ensure data integrity as specified in 4.4.  
1407 
The FNwkSIntKey SHOULD be stored in a way that prevents extraction and re-use by 
1408 
malicious actors. 
1409 
 
1410 
6.1.2.3  Serving Network session integrity key (SNwkSIntKey) 
1411 
The SNwkSIntKey is a network session key specific for the end-device. It is used by the 
1412 
end-device to verify the MIC (message integrity code) of all downlink data messages to 
1413 
ensure data integrity and to compute half of the uplink messages MIC.   
1414 
Note: The uplink MIC calculation relies on two keys (FNwkSIntKey and 
1415 
SNwkSIntKey) in order to allow a forwarding Network Server in a 
1416 
roaming setup to be able to verify only half of the MIC field 
1417 
When a device connects to a LoRaWAN1.0 Network Server the same key is used for both 
1418 
uplink & downlink MIC calculation as specified in 4.4. In that case SNwkSIntKey takes the 
1419 
same value than FNwkSIntKey. 
1420 
The SNwkSIntKey SHOULD be stored in a way that prevents extraction and re-use by 
1421 
malicious actors. 
1422 
 
1423 
6.1.2.4 Network session encryption key (NwkSEncKey) 
1424 
The NwkSEncKey is a network session key specific to the end-device. It is used to encrypt & 
1425 
decrypt uplink & downlink MAC commands transmitted as payload on port 0 or in the FOpt 
1426 
field. When a device connects to a LoRaWAN1.0 Network Server the same key is used for 
1427 
both MAC payload encryption and MIC calculation. In that case NwkSEncKey takes the 
1428 
same value than FNwkSIntKey. 
1429

## Page 51

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 51 of 101 
The authors reserve the right to change 
specifications without notice. 
 
The NwkSEncKey SHOULD be stored in a way that prevents extraction and re-use by 
1430 
malicious actors. 
1431 
6.1.2.5 Application session key (AppSKey) 
1432 
The AppSKey is an application session key specific for the end-device. It is used by both 
1433 
the application server and the end-device to encrypt and decrypt the payload field of 
1434 
application-specific data messages. Application payloads are end-to-end encrypted between 
1435 
the end-device and the application server, but they are integrity protected only in a hop-by-
1436 
hop fashion: one hop between the end-device and the Network Server, and the other hop 
1437 
between the Network Server and the application server. That means, a malicious Network 
1438 
Server may be able to alter the content of the data messages in transit, which may even 
1439 
help the Network Server to infer some information about the data by observing the reaction 
1440 
of the application end-points to the altered data. Network Servers are considered as trusted, 
1441 
but applications wishing to implement end-to-end confidentiality and integrity protection MAY 
1442 
use additional end-to-end security solutions, which are beyond the scope of this 
1443 
specification. 
1444 
The AppSKey SHOULD be stored in a way that prevents extraction and re-use by malicious 
1445 
actors. 
1446 
 
1447 
6.1.2.6 Session Context 
1448 
Session Context contains Network Session and Application Session. 
1449 
 
1450 
The Network Session consists of the following state: 
1451 
 
1452 
 
F/SNwkSIntKey 
1453 
 
NwkSEncKey 
1454 
 
FCntUp 
1455 
 
FCntDwn (LW 1.0) or NFCntDwn (LW 1.1) 
1456 
 
DevAddr 
1457 
 
1458 
The Application Session consists of the following state: 
1459 
 
1460 
 
AppSKey 
1461 
 
FCntUp 
1462 
 
FCntDown (LW 1.0) or AFCntDwn (LW 1.1) 
1463 
 
1464 
Network Session state is maintained by the NS and the end-device.  Application Session 
1465 
state is maintained by the AS and the end-device.  
1466 
 
1467 
Upon completion of either the OTAA or ABP procedure, a new security session context has 
1468 
been established between the NS/AS and the end-device. Keys and the end-device address 
1469 
are fixed for the duration of a session (FNwkSIntKey, SNwkSIntKey, AppSKey, DevAddr).  
1470 
Frame counters increment as frame traffic is exchanged during the session (FCntUp, 
1471 
FCntDwn, NFCntDwn, AFCntDwn).   
1472 
 
1473

## Page 52

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 52 of 101 
The authors reserve the right to change 
specifications without notice. 
 
For OTAA devices, Frame counters MUST NOT be re-used for a given key, therefore new 
1474 
Session Context MUST be established well before saturation of a frame counter.   
1475 
 
1476 
It is RECOMMENDED that session state be maintained across power cycling of an end-
1477 
device.  Failure to do so for OTAA devices means the activation procedure will need to be 
1478 
executed on each power cycling of a device. 
1479 
 
1480 
6.2 Over-the-Air Activation 
1481 
For over-the-air activation, end-devices must follow a join procedure prior to participating in 
1482 
data exchanges with the Network Server. An end-device has to go through a new join 
1483 
procedure every time it has lost the session context information. 
1484 
As discussed above, the join procedure requires the end-device to be personalized with the 
1485 
following information before it starts the join procedure: a DevEUI, JoinEUI, NwkKey and 
1486 
AppKey.  
1487 
Note: For over-the-air-activation, end-devices are not personalized 
1488 
with a pair of network session keys.  Instead, whenever an end-device 
1489 
joins a network, network session keys specific for that end-device are 
1490 
derived to encrypt and verify transmissions at the network level.  This 
1491 
way, roaming of end-devices between networks of different providers is 
1492 
facilitated.  Using different network session keys and application 
1493 
session key further allows federated Network Servers in which 
1494 
application data cannot be read by the network provider. 
1495 
 
1496 
6.2.1 
Join procedure 
1497 
From an end-device’s point of view, the join procedure consists of either a join or rejoin-
1498 
request and a Join-accept exchange. 
1499 
6.2.2 
Join-request message 
1500 
The join procedure is always initiated from the end-device by sending a join-request 
1501 
message. 
1502 
 
1503 
Size (bytes) 
8 
8 
2 
Join-request 
JoinEUI 
DevEUI 
DevNonce 
Figure 44 : Join-request message fields 
1504 
The join-request message contains the JoinEUI and DevEUI of the end-device followed by 
1505 
a nonce of 2 octets (DevNonce).   
1506 
DevNonce is a counter starting at 0 when the device is initially powered up and incremented 
1507 
with every Join-request. A DevNonce value SHALL NEVER be reused for a given JoinEUI 
1508 
value.  If the end-device can be power-cycled then DevNonce SHALL be persistent (stored 
1509 
in a non-volatile memory). Resetting DevNonce without changing JoinEUI will cause the 
1510 
Network Server to discard the Join-requests of the device.  For each end-device, the 
1511

## Page 53

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 53 of 101 
The authors reserve the right to change 
specifications without notice. 
 
Network Server keeps track of the last DevNonce value used by the end-device, and 
1512 
ignores Join-requests if DevNonce is not incremented. 
1513 
 
1514 
Note: This mechanism prevents replay attacks by sending previously 
1515 
recorded join-request messages with the intention of disconnecting the 
1516 
respective end-device from the network. Any time the Network Server 
1517 
processes a Join-Request and generates a Join-accept frame, it shall 
1518 
maintain both the old security context (keys and counters, if any) and 
1519 
the new one until it receives the first successful uplink frame containing 
1520 
the RekeyInd command using the new context, after which the old 
1521 
context can be safely removed.  
1522 
The message integrity code (MIC) value (see Chapter 4 for MAC message description) for a 
1523 
join-request message is calculated as follows:1 
1524 
 
1525 
 
cmac = aes128_cmac(NwkKey, MHDR | JoinEUI | DevEUI | DevNonce) 
1526 
 
MIC = cmac[0..3] 
1527 
The join-request message is not encrypted. The join-request message can be transmitted 
1528 
using any data rate and following a random frequency hopping sequence across the 
1529 
specified join channels. It is RECOMMENDED to use a plurality of data rates. The intervals 
1530 
between transmissions of Join-Requests SHALL respect the condition described in chapter 
1531 
7. For each transmission of a Join-request, the end-device SHALL increment the DevNonce 
1532 
value. 
1533 
6.2.3 
Join-accept message 
1534 
The Network Server will respond to the join or rejoin-request message with a join-accept 
1535 
message if the end-device is permitted to join a network.  The join-accept message is sent 
1536 
like 
a 
normal 
downlink 
but 
uses 
delays 
JOIN_ACCEPT_DELAY1 
or 
1537 
JOIN_ACCEPT_DELAY2 
(instead 
of 
RECEIVE_DELAY1 
and 
RECEIVE_DELAY2, 
1538 
respectively). The channel frequency and data rate used for these two receive windows are 
1539 
identical to the one used for the RX1 and RX2 receive windows described in the “receive 
1540 
windows” section of [PHY] 
1541 
No response is given to the end-device if the Join-request is not accepted. 
1542 
The join-accept message contains a server nonce (JoinNonce) of 3 octets, a network 
1543 
identifier (NetID), an end-device address (DevAddr), a (DLSettings) field providing some of 
1544 
the downlink parameters, the delay between TX and RX (RxDelay) and an optional list of 
1545 
network parameters (CFList ) for the network the end-device is joining. The optional CFList 
1546 
field is region specific and is defined in [PHY]. 
1547 
 
1548 
Size (bytes) 
3 
3 
4 
1 
1 
(16) Optional 
Join-accept 
JoinNonce 
Home_NetID 
DevAddr 
DLSettings 
RxDelay 
CFList 
Figure 45 : Join-accept message fields 
1549 
The JoinNonce is a device specific counter value (that never repeats itself) provided by the 
1550 
Join Server and used by the end-device to derive the session keys FNwkSIntKey, 
1551 
                                                
1 [RFC4493]

## Page 54

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 54 of 101 
The authors reserve the right to change 
specifications without notice. 
 
SNwkSIntKey, NwkSEncKey and AppSKey. JoinNonce is incremented with every Join-
1552 
accept message. 
1553 
The device keeps track of the JoinNonce value used in the last successfully processed Join-
1554 
accept (corresponding to the last successful key derivation). The device SHALL accept the 
1555 
Join-accept only if the MIC field is correct and the JoinNonce is strictly greater than the 
1556 
recorded one. In that case the new JoinNonce value replaces the previously stored one.  
1557 
If the device is susceptible of being power cycled the JoinNonce SHALL be persistent 
1558 
(stored in a non-volatile memory). 
1559 
The LoRa Alliance allocates a 24bits unique network identifier (NetID) to all networks with 
1560 
the exception of the following NetID values reserved for experimental/private networks that 
1561 
are left unmanaged. 
1562 
There are 2^15 Private /Experimental network reserved NetID values built as follow:  
1563 
Nb bits 
3 
14 
7 
 
3’b000 
XXXXXXXXXXXXXX 
Arbitrary 14bit value  
7’b0000000 
Or 7’b0000001 
 
1564 
The home_NetID field of the Join-accept frame corresponds to the NetId of the device’s 
1565 
home network.  
1566 
The network that assigns the devAddr and the home network may be different in a roaming 
1567 
scenario. For more precision please refer to [BACKEND]. 
1568 
The DLsettings field contains the downlink configuration: 
1569 
  
1570 
Bits 
7 
6:4 
3:0 
DLsettings 
OptNeg 
RX1DRoffset 
RX2 Data rate 
 
1571 
The OptNeg bit indicates whether the Network Server implements the LoRaWAN1.0 protocol 
1572 
version (unset) or 1.1 and later (set). When the OptNeg bit is set  
1573 
 
The protocol version is further (1.1 or later) negotiated between the end-device and 
1574 
the Network Server through the RekeyInd/RekeyConf  MAC command exchange. 
1575 
 
The device derives FNwkSIntKey & SNwkSIntKey & NwkSEncKey from the 
1576 
NwkKey 
1577 
 
The device derives AppSKey from the AppKey 
1578 
 
1579 
When the OptNeg bit is not set  
1580 
 
The device reverts to LoRaWAN1.0 , no options can be negotiated 
1581 
 
The RekeyInd command is not sent by the device 
1582 
 
The device derives FNwkSIntKey & AppSKey from the NwkKey  
1583 
 
The device sets SNwkSIntKey & NwkSEncKey equal to FNwkSIntKey 
1584 
 
1585 
The 4 session keys FNwkSIntKey, SNwkSIntKey, NwkSEncKey and AppSKey are 
1586 
derived as follows: 
1587 
 
1588

## Page 55

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 55 of 101 
The authors reserve the right to change 
specifications without notice. 
 
If the OptNeg is unset, the session keys are derived from the NwkKey as follow: 
1589 
AppSKey = aes128_encrypt(NwkKey, 0x02 | JoinNonce | NetID | DevNonce | pad161) 
1590 
FNwkSIntKey = aes128_encrypt(NwkKey, 0x01 | JoinNonce | NetID | DevNonce | pad16) 
1591 
SNwkSIntKey = NwkSEncKey = FNwkSIntKey. 
1592 
 
1593 
The MIC value of the join-accept message is calculated as follows:2 
1594 
cmac = aes128_cmac(NwkKey, MHDR |  JoinNonce | NetID | DevAddr | DLSettings | 
1595 
RxDelay | CFList ) 
1596 
MIC = cmac[0..3] 
1597 
 
1598 
 
1599 
Else if the OptNeg is set, the AppSKey is derived from AppKey as follow: 
1600 
AppSKey = aes128_encrypt(AppKey, 0x02 | JoinNonce | JoinEUI | DevNonce | pad16) 
1601 
 
1602 
And the network session keys  are derived from the NwkKey: 
1603 
FNwkSIntKey = aes128_encrypt(NwkKey, 0x01 | JoinNonce | JoinEUI | DevNonce | pad16 ) 
1604 
SNwkSIntKey = aes128_encrypt(NwkKey, 0x03 | JoinNonce | JoinEUI | DevNonce | pad16) 
1605 
NwkSEncKey = aes128_encrypt(NwkKey, 0x04 | JoinNonce | JoinEUI | DevNonce | pad16) 
1606 
 
1607 
In this case the MIC value is calculated as follows:3 
1608 
cmac = aes128_cmac(JSIntKey,  
1609 
JoinReqType | JoinEUI | DevNonce  |  MHDR | JoinNonce | NetID | DevAddr | 
1610 
DLSettings | RxDelay | CFList ) 
1611 
MIC = cmac[0..3] 
1612 
 
1613 
JoinReqType is a single byte field encoding the type of Join-request or Rejoin-request that 
1614 
triggered the Join-accept response. 
1615 
Join-request or Rejoin-request type JoinReqType  
value 
Join-request 
0xFF 
Rejoin-request type 0 
0x00 
Rejoin-request type 1 
0x01 
Rejoin-request type 2 
0x02 
Table 13 : JoinReqType values 
1616 
The key used to encrypt the Join-Accept message is a function of the Join or ReJoin-
1617 
Request message that triggered it. 
1618 
 
1619 
Triggering Join-request or Rejoin-request type Join-accept Encryption Key 
Join-request 
NwkKey 
Rejoin-request type 0 or 1 or 2 
JSEncKey 
Table 14 : Join-Accept encryption key 
1620 
The Join-Accept message is encrypted as follows: 
1621 
aes128_decrypt(NwkKey or JSEncKey, JoinNonce | NetID | DevAddr | DLSettings | 
1622 
RxDelay | CFList  | MIC). 
1623 
 
1624 
                                                
1 The pad16 function appends zero octets so that the length of the data is a multiple of 16 
2 [RFC4493] 
3 [RFC4493]

## Page 56

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 56 of 101 
The authors reserve the right to change 
specifications without notice. 
 
The message is either 16 or 32 bytes long. 
1625 
Note: AES decrypt operation in ECB mode is used to encrypt the join-
1626 
accept message so that the end-device can use an AES encrypt 
1627 
operation to decrypt the message.  This way an end-device only has to 
1628 
implement AES encrypt but not AES decrypt. 
1629 
Note: Establishing these four session keys allows for a federated 
1630 
Network Server infrastructure in which network operators are not able 
1631 
to eavesdrop on application data.  The application provider commits to 
1632 
the network operator that it will take the charges for any traffic incurred 
1633 
by the end-device and retains full control over the AppSKey used for 
1634 
protecting its application data. 
1635 
Note: The device’s protocol version (1.0 or 1.1) is registered on the 
1636 
backend side out-of-band at the same time than the DevEUI and the 
1637 
device’s NwkKey and possibly AppKey 
1638 
 
1639 
The RX1DRoffset field sets the offset between the uplink data rate and the downlink data 
1640 
rate used to communicate with the end-device on the first reception slot (RX1). By default 
1641 
this offset is 0. The offset is used to take into account maximum power density constraints 
1642 
for base stations in some regions and to balance the uplink and downlink radio link margins. 
1643 
The actual relationship between the uplink and downlink data rate is region specific and 
1644 
detailed in [PHY] 
1645 
The delay RxDelay follows the same convention as the Delay field in the 
1646 
RXTimingSetupReq command. 
1647 
If the Join-accept message is received following the transmission of: 
1648 
 
A Join-Request or a Rejoin-request Type 0 or 1 and if the CFlist field is absent, the 
1649 
device SHALL revert to its default channel definition. If the CFlist is present, it 
1650 
overrides all currently defined channels. The MAC layer parameters (except 
1651 
RXdelay1, RX2 data rate, and RX1 DR Offset that are transported by the join-accept 
1652 
message) SHALL all be reset to their default values.  
1653 
 
A Rejoin-request Type 2 and if the CFlist field is absent, the device SHALL keep its 
1654 
current channels definition unchanged. If the CFlist is present, it overrides all 
1655 
currently defined channels. All other MAC parameters (except frame counters which 
1656 
are reset) are kept unchanged.  
1657 
In all cases following the successful processing of a Join-accept message the device SHALL 
1658 
transmit the RekeyInd MAC command until it receives the RekeyConf command (see 5.9). 
1659 
The reception of the RekeyInd uplink command is used by the Network Server as a signal to 
1660 
switch to the new security context. 
1661 
 
1662

## Page 57

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 57 of 101 
The authors reserve the right to change 
specifications without notice. 
 
6.2.4 
ReJoin-request message 
1663 
Once activated a device MAY periodically transmit a Rejoin-request message on top of its 
1664 
normal applicative traffic. This Rejoin-request message periodically gives the backend the 
1665 
opportunity to initialize a new session context for the end-device. For this purpose the 
1666 
network replies with a Join-Accept message. This may be used to hand-over a device 
1667 
between two networks or to rekey and/or change devAddr of a device on a given network. 
1668 
The Network Server may also use the Rejoin-request RX1/RX2 windows to transmit a 
1669 
normal confirmed or unconfirmed downlink frame optionally carrying MAC commands. This 
1670 
possibility is useful to reset the device’s reception parameters in case there is a MAC layer 
1671 
state de-synchronization between the device and the Network Server. 
1672 
Example: This mechanism might be used to change the RX2 window data rate and the RX1 
1673 
window data rate offset for a device that isn’t reachable any more in downlink using the 
1674 
current downlink configuration. 
1675 
The Rejoin procedure is always initiated from the end-device by sending a Rejoin-request 
1676 
message. 
1677 
Note: Any time the network backend processes a ReJoin-Request 
1678 
(type 0,1 or 2) and generates a Join-accept message, it shall maintain 
1679 
both the old security context (keys and counters, if any) and the new 
1680 
one until it receives the first successful uplink frame using the new 
1681 
context, after which the old context may be safely discarded.  In all 
1682 
cases, the processing of the ReJoin-request message by the network 
1683 
backend is similar to the processing of a standard Join-request 
1684 
message, in that the Network Server initially processing the message 
1685 
determines if it should be forwarded to a Join Server to create a Join-
1686 
accept message in response. 
1687 
 
1688 
There are three types of Rejoin-request messages that can be transmitted by an end device 
1689 
and corresponds to three different purposes. The first byte of the Rejoin-request message is 
1690 
called Rejoin Type and is used to encode the type of Rejoin-request. The following table 
1691 
describes the purpose of each Rejoin-Request message type. 
1692 
 
 
1693

## Page 58

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 58 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
1694 
RejoinReq 
type 
Content & Purpose 
0 
Contains NetID+DevEUI. Used to reset a device context including all radio 
parameters (devAddr, session keys, frame counters, radio parameters, ..). This 
message can only be routed to the device’s home Network Server by the 
receiving Network Server, not to the device’s JoinServer The MIC of this 
message can only be verified by the serving or home Network Server. 
1 
Contains JoinEUI+DevEUI. Exactly equivalent to the initial Join-Request 
message but may be transmitted on top of normal applicative traffic without 
disconnecting the device. Can only be routed to the device’s JoinServer by the 
receiving Network Server. Used to restore a lost session context (Example, 
Network Server has lost the session keys and cannot associate the device to a 
JoinServer). Only the JoinServer is able to check the MIC of this message. 
2 
Contains NetID+DevEUI. Used to rekey a device or change its DevAddr 
(DevAddr, session keys, frame counters). Radio parameters are kept 
unchanged.  This message can only be routed to the device’s home Network 
Server by visited networks, not to the device’s Join Server. The MIC of this 
message can only be verified by the serving or home Network Server. 
Table 15 : summary of RejoinReq messages 
1695 
6.2.4.1 ReJoin-request Type 0 or 2 message 
1696 
 
1697 
Size (bytes) 
1 
3 
8 
2 
Rejoin-request 
Rejoin Type = 0 or 2 
NetID 
DevEUI 
RJcount0 
Figure 46: Rejoin-request type 0&2 message fields 
1698 
The Rejoin-request type 0 or 2 message contains the NetID (identifier of the device’s home 
1699 
network) and DevEUI of the end-device followed by a 16 bits counter (RJcount0).   
1700 
RJcount0 is a counter incremented with every Type 0 or 2 Rejoin frame transmitted. 
1701 
RJcount0 is initialized to 0 each time a Join-Accept is successfully processed by the end-
1702 
device.  For each end-device, the Network Server MUST keep track of the last RJcount0 
1703 
value (called RJcount0_last) used by the end-device. It ignores Rejoin-requests if (Rjcount0 
1704 
<= RJcount0_last)  
1705 
RJcount0 SHALL never wrap around. If RJcount0 reaches 2^16-1 the device SHALL stop 
1706 
transmitting ReJoin-request type 0 or 2 frames. The device MAY go back to Join state. 
1707 
 
1708 
 Note: This mechanism prevents replay attacks by sending previously 
1709 
recorded Rejoin-request messages  
1710 
The message integrity code (MIC) value (see Chapter 4 for MAC message description) for a 
1711 
Rejoin-request message is calculated as follows:1 
1712 
 
1713 
 
cmac = aes128_cmac(SNwkSIntKey, MHDR | Rejoin Type | NetID | DevEUI | 
1714 
RJcount0) 
1715 
 
MIC = cmac[0..3] 
1716 
                                                
1 [RFC4493]

## Page 59

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 59 of 101 
The authors reserve the right to change 
specifications without notice. 
 
The Rejoin-request message is not encrypted. 
1717 
The device’s Rejoin-Req type 0 or 2 transmissions duty-cycle SHALL always be <0.1% 
1718 
Note: The Rejoin-Request type 0 message is meant to be transmitted 
1719 
from once per hour to once every few days depending on the device’s 
1720 
use case. This message can also be transmitted following a 
1721 
ForceRejoinReq MAC command. This message may be used to 
1722 
reconnect mobile device to a visited network in roaming situations. It 
1723 
can also be used to rekey or change the devAddr of a static device. 
1724 
Mobile devices expected to roam between networks should transmit 
1725 
this message more frequently than static devices. 
1726 
 
1727 
Note: The Rejoin-Request type 2 message is only meant to enable 
1728 
rekeying of an end-device. This message can only be transmitted 
1729 
following a ForceRejoinReq MAC command.  
1730 
6.2.4.2 ReJoin-request Type 1 message 
1731 
Similarly to the Join-Request, the Rejoin-Request type 1 message contains the JoinEUI and 
1732 
the DevEUI of the end-device. The Rejoin-Request type 1 message can therefore be routed 
1733 
to the Join Server of the end-device by any Network Server receiving it. The Rejoin-request 
1734 
Type 1 may be used to restore connectivity with an end-device in case of complete state 
1735 
loss of the Network Server.  It is recommended to transmit a Rejoin-Request type 1 
1736 
message a least once per month. 
1737 
 
1738 
 
1739 
Size (bytes) 
1 
8 
8 
2 
Rejoin-request ReJoin Type = 1 
JoinEUI 
DevEUI 
RJcount1 
Figure 47: Rejoin-request type 1 message fields 
1740 
The RJcount1 for Rejoin-request Type 1 is a different counter from the RJCount0 used for 
1741 
Rejoin-request type 0. 
1742 
RJcount1 is a counter incremented with every Rejoin-request Type 1 frame transmitted.  
1743 
For each end-device, the Join Server keeps track of the last RJcount1 value (called 
1744 
RJcount1_last) used by the end-device. It ignores Rejoin-requests if (Rjcount1 <= 
1745 
RJcount1_last).  
1746 
RJcount1 SHALL never wrap around for a given JoinEUI. The transmission periodicity of 
1747 
Rejoin-Request type 1 shall be such that this wrap around cannot happen for the lifetime of 
1748 
the device for a given JoinEUI value. 
1749 
 
1750 
Note: This mechanism prevents replay attacks by sending previously 
1751 
recorded Rejoin-request messages  
1752 
The message integrity code (MIC) value (see Chapter 4 for MAC message description) for a 
1753 
Rejoin-request-Type1 message is calculated as follows:1 
1754 
 
1755 
 
cmac = aes128_cmac(JSIntKey, MHDR | RejoinType | JoinEUI| DevEUI | RJcount1) 
1756 
                                                
1 [RFC4493]

## Page 60

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 60 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
MIC = cmac[0..3] 
1757 
The Rejoin-request-type 1 message is not encrypted. 
1758 
 
1759 
The device’s Rejoin-Req type 1 transmissions duty-cycle shall always be <0.01% 
1760 
Note: The Rejoin-Request type 1 message is meant to be transmitted 
1761 
from once a day to once a week. This message is only used in the 
1762 
case of a complete loss of context of the server side. This event being 
1763 
very unlikely a latency of 1 day to 1 week to reconnect the device is 
1764 
considered as appropriate 
1765 
6.2.4.3 Rejoin-Request transmissions 
1766 
 
1767 
The following table summarizes the possible conditions for transmission of each Rejoin-
1768 
request type message. 
1769 
 
1770 
RejoinReq 
type 
Transmitted autonomously & 
periodically by the end-device 
Transmitted following a 
ForceRejoinReq MAC command 
0 
x 
x 
1 
x 
 
2 
 
x 
Table 16 : transmission conditions for RejoinReq messages 
1771 
Rejoin-Request type 0&1 messages SHALL be transmitted on any of the defined Join 
1772 
channels (see [PHY]) following a random frequency hopping sequence. 
1773 
Rejoin-Request type 2 SHALL be transmitted on any of the currently enabled channels 
1774 
following a random frequency hopping sequence. 
1775 
Rejoin-Request type 0 or type 2 transmitted following a ForceRejoinReq command SHALL 
1776 
use the data rate specified in the MAC command. 
1777 
Rejoin-Request type 0 transmitted periodically and autonomously by the end-device (with a 
1778 
maximum periodicity set by the RejoinParamSetupReq command) and Rejoin-Request type 
1779 
1 SHALL use: 
1780 
 
The data rate & TX power currently used to transmit application payloads if ADR is 
1781 
enabled 
1782 
 
Any data rate allowed on the Join Channels and default TX power if ADR is disabled. 
1783 
In that case it is RECOMMENDED to use a plurality of data rates. 
1784

## Page 61

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 61 of 101 
The authors reserve the right to change 
specifications without notice. 
 
6.2.4.4 Rejoin-Request message processing 
1785 
For all 3 Rejoin-Request types the Network Server may respond with: 
1786 
 
A join-accept message (as defined in 6.2.3) if it wants to modify the device’s 
1787 
network identity (roaming or re-keying). In that case RJcount (0 or 1) replaces 
1788 
DevNonce in the key derivation process 
1789 
 
A normal downlink frame optionally containing MAC commands. This downlink 
1790 
SHALL be sent on the same channel, with the same data rate and the same delay 
1791 
that the Join-accept message it replaces.  
1792 
 
1793 
In most cases following a ReJoin-Request type 0 or 1 the network will not respond. 
1794 
 
1795 
6.2.5 
Key derivation diagram 
1796 
The following diagrams summarize the key derivation schemes for the cases where a device 
1797 
connects to a LoRaWAN1.0 or 1.1 Network Server. 
 
1798

## Page 62

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 62 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
1799 
LoRaWAN1.0 network backend: 
1800 
When a LoRaWAN1.1 device is provisioned with a LoRaWAN1.0.X network backend, all 
1801 
keys are derived from the NwkKey root key. The device’s AppKey is not used. 
1802 
 
1803 
Figure 48 : LoRaWAN1.0 key derivation scheme 
 
1804

## Page 63

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 63 of 101 
The authors reserve the right to change 
specifications without notice. 
 
LoRaWAN1.1 network backend: 
1805 
 
1806 
 
1807 
AES
ECB
JSIntKey
JSEncKey
FNwkSIntKey
SNwkSIntKey
NwkSEncKey
AES
CMAC
AES
ECB
Confidentiality 
of Join Accept 
triggered by
Join Request
AES
CMAC
Data up
partial MIC
AES
CMAC
Join Request 
MIC
AES
CMAC
AES 
CCM*
Confidential. 
of data up & 
data down 
on Fport = 0 
and in the 
Fopt field
Rejoin Request 
type 1 MIC
&
Join Accept 
MIC
Data up
partial MIC
&
Data down MIC
&
Rejoin Request 
type 0 & 2 MIC
Confidentiality
of Join Accept 
triggered by 
Rejoin Request 
type 0,1 & 2
AES
ECB
 DevEUI
0x05
0x06
0x01
0x03
0x04
NwkKey
AppKey
Confidential. 
of data up & 
data down 
on Fport > 0
AES
CCM*
AES
ECB
AppSKey
0x02
JoinNonce + JoinEUI + DevNonce 
 
1808 
Figure 49 : LoRaWAN1.1 key derivation scheme 
1809

## Page 64

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 64 of 101 
The authors reserve the right to change 
specifications without notice. 
 
6.3 Activation by Personalization 
1810 
Activation by personalization directly ties an end-device to a specific network by-passing the 
1811 
Join-request - Join-accept procedure.  
1812 
Activating an end-device by personalization means that the DevAddr and the four session 
1813 
keys FNwkSIntKey, SNwkSIntKey, NwkSEncKey and AppSKey are directly stored into 
1814 
the end-device instead of being derived from the DevEUI, JoinEUI, AppKey and NwkKey 
1815 
during the join procedure.  The end-device is equipped with the required information for 
1816 
participating in a specific LoRa network as soon as it is started. 
1817 
Each device SHALL have a unique set of F/SNwkSIntKey, NwkSEncKey and AppSKey. 
1818 
Compromising the keys of one device SHALL NOT compromise the security of the 
1819 
communications of other devices. The process to build those keys SHALL be such that the 
1820 
keys cannot be derived in any way from publicly available information (like the node address 
1821 
or the end-device’s devEUI for example).  
1822 
When a personalized end-device accesses the network for the first time or after a re-
1823 
initialization, it SHALL transmit the ResetInd MAC command in the FOpt field of all uplink 
1824 
messages until it receives a ResetConf command from the network. After a re-initialization 
1825 
the end-device MUST use its default configuration (id the configuration that was used when 
1826 
the device was first connected to the network). 
1827 
Note: Frame counter values SHALL only be used once in all 
1828 
invocations of a same key with the CCM* mode of operation. 
1829 
Therefore, re-initialization of an ABP end-device frame counters is 
1830 
forbidden. ABP devices MUST use a non-volatile memory to store the 
1831 
frame counters. 
1832 
ABP devices use the same session keys throughout their lifetime (i.e., 
1833 
no rekeying is possible. Therefore, it is recommended that OTAA 
1834 
devices are used for higher security applications. 
1835 
 
 
1836

## Page 65

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 65 of 101 
The authors reserve the right to change 
specifications without notice. 
 
7 Retransmissions back-off 
1837 
 
1838 
Uplink frames that: 
1839 
 
Require an acknowledgement or an answer by the network or an application 
1840 
server, and are retransmitted by the device if the acknowledgement or answer is not 
1841 
received. 
1842 
 
And can be triggered by an external event causing synchronization across a large 
1843 
(>100) number of devices (power outage, radio jamming, network outage, 
1844 
earthquake…) 
1845 
can trigger a catastrophic, self-persisting, radio network overload situation. 
1846 
 
1847 
Note: An example of such uplink frame is typically the Join-request if 
1848 
the implementation of a group of end-devices decides to reset the 
1849 
MAC layer in the case of a network outage.  
1850 
The whole group of end-device will start broadcasting Join-request 
1851 
uplinks and will only stops when receiving a JoinResponse from the 
1852 
network. 
1853 
 
1854 
For those frame retransmissions, the interval between the end of the RX2 slot and the next 
1855 
uplink retransmission SHALL be random and follow a different sequence for every device 
1856 
(For example using a pseudo-random generator seeded with the device’s address) .The 
1857 
transmission duty-cycle of such message SHALL respect the local regulation and the 
1858 
following limits, whichever is more constraining: 
1859 
 
1860 
Aggregated during the first hour 
following power-up or reset 
T0<t<T0+1h 
Transmit 
time 
< 
36Sec 
Aggregated during the next 10 hours 
T0+1<t<T0+11h 
Transmit 
time 
< 
36Sec 
After the first 11 hours , aggregated 
over 24h 
T0+11+N<t<T0+35+N 
N>=0 
Transmit 
time 
< 
8.7Sec per 24h 
Table 17 : Join-request dutycycle limitations 
1861 
 
1862

## Page 66

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 66 of 101 
The authors reserve the right to change 
specifications without notice. 
 
CLASS B – BEACON 
1863 
 
1864

## Page 67

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 67 of 101 
The authors reserve the right to change 
specifications without notice. 
 
8 Introduction to Class B 
1865 
This section describes the LoRaWAN Class B layer which is optimized for battery-powered 
1866 
end-devices that may be either mobile or mounted at a fixed location. 
1867 
End-devices should implement Class B operation when there is a requirement to open 
1868 
receive windows at fixed time intervals for the purpose of enabling server initiated downlink 
1869 
messages. 
1870 
LoRaWAN Class B option adds a synchronized reception window on the end-device. 
1871 
One of the limitations of LoRaWAN Class A is the Aloha method of sending data from the 
1872 
end-device; it does not allow for a known reaction time when the customer application or the 
1873 
server wants to address the end-device. The purpose of Class B is to have an end-device 
1874 
available for reception at a predictable time, in addition to the reception windows that follows 
1875 
the random uplink transmission from the end-device of Class A. Class B is achieved by 
1876 
having the gateway sending a beacon on a regular basis to synchronize all end-devices in 
1877 
the network so that the end-device can open a short additional reception window (called 
1878 
“ping slot”) at a predictable time during a periodic time slot. 
1879 
Note: The decision to switch from Class A to Class B comes from the 
1880 
application layer of the end-device. If this class A to Class B switch 
1881 
needs to be controlled from the network side, the customer application 
1882 
must use one of the end-device’s Class A uplinks to send back a 
1883 
downlink to the application layer, and it needs the application layer on 
1884 
the end-device to recognize this request – this process is not managed 
1885 
at the LoRaWAN level. 
1886

## Page 68

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 68 of 101 
The authors reserve the right to change 
specifications without notice. 
 
9 Principle of synchronous network initiated downlink (Class-B 
1887 
option) 
1888 
For a network to support end-devices of Class B, all gateways must synchronously 
1889 
broadcast a beacon providing a timing reference to the end-devices. Based on this timing 
1890 
reference the end-devices can periodically open receive windows, hereafter called “ping 
1891 
slots”, which can be used by the network infrastructure to initiate a downlink communication. 
1892 
A network initiated downlink using one of these ping slots is called a “ping”. The gateway 
1893 
chosen to initiate this downlink communication is selected by the Network Server based on 
1894 
the signal quality indicators of the last uplink of the end-device. For this reason, if an end-
1895 
device moves and detects a change in the identity advertised in the received beacon, it must 
1896 
send an uplink to the Network Server so that the server can update the downlink routing 
1897 
path database. 
1898 
Before a device can operate in Class B mode, the following informations must be made 
1899 
available to the Network Server out-of-band. 
1900 
 
The device’s default ping-slot periodicity 
1901 
 
Default Ping-slot data rate 
1902 
 
Default Ping-slot channel 
1903 
 
1904

## Page 69

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 69 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
1905 
All end-devices start and join the network as end-devices of Class A. The end-device 
1906 
application can then decide to switch to Class B. This is done through the following process: 
1907 
 
The end-device application requests the LoRaWAN layer to switch to Class B mode. 
1908 
The LoRaWAN layer in the end-device searches for a beacon and returns either a 
1909 
BEACON_LOCKED service primitive to the application if a network beacon was 
1910 
found and locked or a BEACON_NOT_FOUND service primitive. To accelerate the 
1911 
beacon discovery the LoRaWAN layer may use the “DeviceTimeReq” MAC 
1912 
command. 
1913 
 
Once in Class B mode, the MAC layer sets to 1 the Class B  bit of the FCTRL field of 
1914 
every uplink frame transmitted. This bit signals to the server that the device has 
1915 
switched to Class B. The MAC layer will autonomously schedule a reception slot for 
1916 
each beacon and each ping slot. When the beacon reception is successful the end-
1917 
device LoRaWAN layer forwards the beacon content to the application together with 
1918 
the measured radio signal strength. The end-device LoRaWAN layer takes into 
1919 
account the maximum possible clock drift in the scheduling of the beacon reception 
1920 
slot and ping slots. When a downlink is successfully demodulated during a ping slot, 
1921 
it is processed similarly to a downlink as described in the LoRaWAN Class A 
1922 
specification.  
1923 
 
A mobile end-device must periodically inform the Network Server of its location to 
1924 
update the downlink route. This is done by transmitting a normal (possibly empty) 
1925 
“unconfirmed” or “confirmed” uplink. The end-device LoRaWAN layer will 
1926 
appropriately set the Class B bit to 1 in the frame’s FCtrl field. Optimally this can be 
1927 
done more efficiently if the application detects that the node is moving by analyzing 
1928 
the beacon content. In that case the end-device must apply a random delay (as 
1929 
defined in Section 15.5 between the beacon reception and the uplink transmission to 
1930 
avoid systematic uplink collisions. 
1931 
 
At any time the Network Server may change the device’s ping-slot downlink 
1932 
frequency or data rate by sending a PingSlotChannelReq MAC command. 
1933 
 
The device may change the periodicity of its ping-slots at any time. To do so, it 
1934 
MUST temporarily stop class B operation (unset classB bit in its uplink frames) and 
1935 
send a PingSlotInfoReq to the Network Server. Once this command is acknowledged 
1936 
the device may restart classB operation with the new ping-slot periodicity 
1937 
 
If no beacon has been received for a given period (as defined in Section 12.2), the 
1938 
synchronization with the network is lost. The MAC layer must inform the application 
1939 
layer that it has switched back to Class A. As a consequence the end-device 
1940 
LoRaWAN layer stops setting the Class B bit in all uplinks and this informs the 
1941 
Network Server that the end-device is no longer in Class B mode. The end-device 
1942 
application can try to switch back to Class B periodically. This will restart this process 
1943 
starting with a beacon search. 
1944 
The following diagram illustrates the concept of beacon reception slots and ping slots. 
1945

## Page 70

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 70 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
1946 
Figure 50: Beacon reception slot and ping slots 
1947 
In this example, given the beacon period is 128 s, the end-device also opens a ping 
1948 
reception slot every 32 s. Most of the time this ping slot is not used by the server and 
1949 
therefore the end-device reception window is closed as soon as the radio transceiver has 
1950 
assessed that no preamble is present on the radio channel. If a preamble is detected the 
1951 
radio transceiver will stay on until the downlink frame is demodulated. The MAC layer will 
1952 
then process the frame, check that its address field matches the end-device address and 
1953 
that the Message Integrity Check is valid before forwarding it to the application layer. 
1954 
gateway
End-device
End-device 
RX windows
Network beacon 
transmission
Network beacon 
transmission
ping
End-device 
response

## Page 71

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 71 of 101 
The authors reserve the right to change 
specifications without notice. 
 
10 Uplink frame in Class B mode 
1955 
The uplink frames in Class B mode are same as the Class A uplinks with the exception of 
1956 
the RFU bit in the FCtrl field in the Frame header. In the Class A uplink this bit is unused 
1957 
(RFU).  This bit is used for Class B uplinks.  
1958 
 
1959 
Bit#
7 
6 
5 
4 
3..0 
FCtrl ADR 
ADRACKReq ACK Class B 
FOptsLen 
Figure 51 : classB FCtrl fields 
1960 
The Class B bit set to 1 in an uplink signals the Network Server that the device as switched 
1961 
to Class B mode and is now ready to receive scheduled downlink pings. 
1962 
 
1963 
The signification of the FPending bit for downlink is unaltered and still signals that one or 
1964 
more downlink frames are queued for this device in the server and that the device should 
1965 
keep is receiver on as described in the Class A specification. 
1966 
 
1967

## Page 72

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 72 of 101 
The authors reserve the right to change 
specifications without notice. 
 
11 Downlink Ping frame format (Class B option) 
1968 
11.1 Physical frame format 
1969 
A downlink Ping uses the same format as a Class A downlink frame but might follow a 
1970 
different channel frequency plan. 
1971 
11.2 Unicast & Multicast MAC messages 
1972 
Messages can be “unicast” or “multicast”. Unicast messages are sent to a single end-device 
1973 
and multicast messages are sent to multiple end-devices. All devices of a multicast group 
1974 
must share the same multicast address and associated encryption keys. The LoRaWAN 
1975 
Class B specification does not specify means to remotely setup such a multicast group or 
1976 
securely distribute the required multicast key material. This must either be performed during 
1977 
the node personalization or through the application layer. 
1978 
11.2.1 Unicast MAC message format 
1979 
The MAC payload of a unicast downlink Ping uses the format defined in the Class A 
1980 
specification. It is processed by the end-device in exactly the same way. The same frame 
1981 
counter is used and incremented whether the downlink uses a Class B ping slot or a Class A 
1982 
“piggy-back” slot. 
1983 
11.2.2 Multicast MAC message format 
1984 
The Multicast frames share most of the unicast frame format with a few exceptions: 
1985 
 
They are not allowed to carry MAC commands, neither in the FOpt field, nor in the 
1986 
payload on port 0 because a multicast downlink does not have the same 
1987 
authentication robustness as a unicast frame. 
1988 
 
The ACK and ADRACKReq bits must be zero. The MType field must carry the value 
1989 
for Unconfirmed Data Down. 
1990 
 
The FPending bit indicates there is  more multicast data to be sent. If it is set the 
1991 
next multicast receive slot will carry a data frame. If it is not set the next slot may or 
1992 
may not carry data. This bit can be used by end-devices to evaluate priorities for 
1993 
conflicting reception slots. 
1994 
 
1995

## Page 73

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 73 of 101 
The authors reserve the right to change 
specifications without notice. 
 
12 Beacon acquisition and tracking 
1996 
Before switching from Class A to Class B, the end-device must first receive one of the 
1997 
network beacons to align his internal timing reference with the network. 
1998 
Once in Class B, the end-device must periodically search and receive a network beacon to 
1999 
cancel any drift of its internal clock time base, relative to the network timing. 
2000 
A Class B device may be temporarily unable to receive beacons (out of range from the 
2001 
network gateways, presence of interference, ..). In this event, the end-device has to 
2002 
gradually widen its beacon and ping slots reception windows to take into account a possible 
2003 
drift of its internal clock. 
2004 
Note: For example, a device which internal clock is defined with a +/-
2005 
10ppm precision may drift by +/-1.3mSec every beacon period.  
2006 
12.1 Minimal beacon-less operation time 
2007 
In the event of beacon loss, a device shall be capable of maintaining Class B operation for 2 
2008 
hours (120 minutes) after it received the last beacon. This temporary Class B operation 
2009 
without beacon is called “beacon-less” operation. It relies on the end-device’s own clock to 
2010 
keep timing. 
2011 
During beacon-less operation, unicast, multicast and beacon reception slots must all be 
2012 
progressively expanded to accommodate the end-device’s possible clock drift. 
2013 
 
2014 
 
2015 
Figure 52 : beacon-less temporary operation 
2016 
12.2 Extension of beacon-less operation upon reception 
2017 
During this 120 minutes time interval the reception of any beacon directed to the end-device, 
2018 
should extend the Class B beacon-less operation further by another 120 minutes as it allows 
2019 
to correct any timing drift and reset the receive slots duration. 
2020 
12.3 Minimizing timing drift 
2021 
The end-devices may use the beacon’s (when available) precise periodicity to calibrate their 
2022 
internal clock and therefore reduce the initial clock frequency imprecision. As the timing 
2023 
oscillator’s exhibit a predictable temperature frequency shift, the use of a temperature 
2024 
sensor could enable further minimization of the timing drift. 
2025 
End-device
End-device 
receives the 
beacon
Beacon reception 
window
End-device 
temporarily stop 
receiving beacon
End-device receives a 
beacon and resets the 
reception window length
Reception window 
enlarges to 
accommodate clock drift

## Page 74

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 74 of 101 
The authors reserve the right to change 
specifications without notice. 
 
13 Class B Downlink slot timing 
2026 
13.1 Definitions 
2027 
To operate successfully in Class B the end-device must open reception slots at precise 
2028 
instants relative to the infrastructure beacon. This section defines the required timing. 
2029 
The interval between the start of two successive beacons is called the beacon period.  The 
2030 
beacon frame transmission is aligned with the beginning of the BEACON_RESERVED 
2031 
interval. Each beacon is preceded by a guard time interval where no ping slot can be placed. 
2032 
The length of the guard interval corresponds to the time on air of the longest allowed frame. 
2033 
This is to insure that a downlink initiated during a ping slot just before the guard time will 
2034 
always have time to complete without colliding with the beacon transmission. The usable 
2035 
time interval for ping slot therefore spans from the end of the beacon reserved time interval 
2036 
to the beginning of the next beacon guard interval. 
2037 
 
2038 
Figure 53: Beacon timing 
2039 
Beacon_period 
128 s 
Beacon_reserved 
2.120 s 
Beacon_guard 
3.000 s 
Beacon-window 
122.880 s 
Table 18: Beacon timing 
2040 
The beacon frame time on air is actually much shorter than the beacon reserved time 
2041 
interval to allow appending network management broadcast frames in the future. 
2042 
The beacon window interval is divided into 212 = 4096 ping slots of 30 ms each numbered 
2043 
from 0 to 4095. 
2044 
An end-device using the slot number N must turn on its receiver exactly Ton seconds after 
2045 
the start of the beacon where: 
2046 
Ton = beacon_reserved + N * 30 ms 
2047

## Page 75

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 75 of 101 
The authors reserve the right to change 
specifications without notice. 
 
N is called the slot index. 
2048 
The latest ping slot starts at beacon_reserved + 4095 * 30 ms = 124 970 ms after the 
2049 
beacon start or 3030 ms before the beginning of the next beacon. 
2050 
13.2 Slot randomization 
2051 
To avoid systematic collisions or over-hearing problems the slot index is randomized and 
2052 
changed at every beacon period. 
2053 
The following parameters are used: 
2054 
 
2055 
DevAddr 
Device 32 bit network unicast or multicast address 
pingNb 
Number of ping slots per beacon period. This must be a power of 2 integer: 
pingNb = 2k where 0 <= k <=7 
 
pingPeriod 
Period of the device receiver wake-up expressed in number of slots: 
pingPeriod = 212 / pingNb 
 
pingOffset 
Randomized offset computed at each beacon period start. Values can range 
from 0 to (pingPeriod-1) 
beaconTime The time carried in the field BCNPayload.Time of the immediately preceding 
beacon frame 
slotLen 
Length of a unit ping slot = 30 ms 
Table 19 : classB slot randomization algorithm parameters 
2056 
At each beacon period the end-device and the server compute a new pseudo-random offset 
2057 
to align the reception slots. An AES encryption with a fixed key of all zeros is used to 
2058 
randomize: 
2059 
 
Key = 16 x 0x00 
2060 
 
Rand = aes128_encrypt(Key, beaconTime | DevAddr | pad16) 
2061 
pingOffset = (Rand[0] + Rand[1]x 256) modulo pingPeriod 
2062 
The slots used for this beacon period will be: 
2063 
pingOffset + N x pingPeriod with N=[0:pingNb-1] 
2064 
The node therefore opens receive slots starting at : 
2065 
First slot 
Beacon_reserved + pingOffset x slotLen 
Slot 2 
Beacon_reserved + (pingOffset + pingPeriod) x slotLen 
Slot 3  
Beacon_reserved + (pingOffset + 2 x pingPeriod) x slotLen 
… 
… 
If the end-device serves simultaneously a unicast and one or more multicast slots this 
2066 
computation is performed multiple times at the beginning of a new beacon period. Once for 
2067 
the unicast address (the node network address) and once for each multicast group address. 
2068 
In the case where a multicast ping slot and a unicast ping slot collide and cannot be served 
2069 
by the end-device receiver then the end-device should preferentially listen to the multicast 
2070 
slot. If there is a collision between multicast reception slots the FPending bit of the previous 
2071 
multicast frame can be used to set a preference.  
2072 
The randomization scheme prevents a systematic collision between unicast and multicast 
2073 
slots. If collisions happen during a beacon period then it is unlikely to occur again during the 
2074 
next beacon period. 
2075

## Page 76

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 76 of 101 
The authors reserve the right to change 
specifications without notice. 
 
14 Class B MAC commands 
2076 
All commands described in the Class A specification shall be implemented in Class B 
2077 
devices. The Class B specification adds the following MAC commands. 
2078 
 
2079 
CID 
Command 
Transmitted by 
Short Description 
End-
device 
Gateway 
0x10 
PingSlotInfoReq 
x 
 
Used by the end-device to communicate 
the ping unicast slot periodicity to the 
Network Server 
0x10 
PingSlotInfoAns 
 
x 
Used by the network to acknowledge a 
PingInfoSlotReq command 
0x11 
PingSlotChannelReq 
 
x 
Used by the Network Server to set the 
unicast ping channel of an end-device 
0x11 
PingSlotChannelAns 
x 
 
Used by the end-device to acknowledge a 
PingSlotChannelReqcommand 
0x12 
BeaconTimingReq 
x 
 
deprecated 
0x12 
BeaconTimingAns 
 
x 
deprecated 
0x13 
BeaconFreqReq 
 
x 
Command used by the Network Server to 
modify the frequency at which the end-
device expects to receive beacon 
broadcast 
0x13 
BeaconFreqAns 
x 
 
Used by the end-device to acknowledge a 
BeaconFreqReq command 
Table 20 : classB MAC command table 
2080 
14.1 PingSlotInfoReq 
2081 
With the PingSlotInfoReq command an end-device informs the server of its unicast ping 
2082 
slot periodicity. This command must only be used to inform the server of the periodicity of a 
2083 
UNICAST ping slot. A multicast slot is entirely defined by the application and should not use 
2084 
this command. 
2085 
 
2086 
Size (bytes) 
1 
PingSlotInfoReq Payload 
PingSlotParam 
Figure 54 : PingSlotInfoReq payload format 
2087 
Bit# 
7:3 
[2:0] 
PingSlotParam 
RFU 
Periodicity 
The Periodicity subfield is an unsigned 3 bits integer encoding the ping slot period currently 
2088 
used by the end-device using the following equation.  
2089 
𝑝𝑖𝑛𝑔𝑁𝑏= 27−𝑃𝑒𝑟𝑖𝑜𝑑𝑖𝑐𝑖𝑡𝑦 𝑎𝑛𝑑 𝑝𝑖𝑛𝑔𝑃𝑒𝑟𝑖𝑜𝑑= 25+𝑃𝑒𝑟𝑖𝑜𝑑𝑖𝑐𝑖𝑡𝑦 
2090 
The actual ping slot periodicity will be equal to 0.96 ×  2𝑃𝑒𝑟𝑖𝑜𝑑𝑖𝑐𝑖𝑡𝑦 in seconds 
2091

## Page 77

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 77 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
Periodicity = 0 means that the end-device opens a ping slot approximately every 
2092 
second during the beacon_window interval 
2093 
 
Periodicity = 7 , every 128 seconds which is the maximum ping period supported by 
2094 
the LoRaWAN Class B specification. 
2095 
To change its ping slot periodicity a device SHALL first revert to Class A , send the new 
2096 
periodicity through a PingSlotInfoReq command and get an acknowledge from the server 
2097 
through a PingSlotInfoAns . It MAY then switch back to Class B with the new periodicity. 
2098 
This command MAY be concatenated with any other MAC command in the FHDRFOpt field 
2099 
as described in the Class A specification frame format. 
2100 
14.2 BeaconFreqReq 
2101 
This command is sent by the server to the end-device to modify the frequency on which this 
2102 
end-device expects the beacon. 
2103 
 
2104 
Octets 
3 
BeaconFreqReq payload 
Frequency 
Figure 55 : BeaconFreqReq payload format 
2105 
The Frequency coding is identical to the NewChannelReq MAC command defined in the 
2106 
Class A. 
2107 
Frequency is a 24bits unsigned integer. The actual beacon channel frequency in Hz is 100 
2108 
x frequ. This allows defining the beacon channel anywhere between 100 MHz to 1.67 GHz 
2109 
by 100 Hz step. The end-device has to check that the frequency is actually allowed by its 
2110 
radio hardware and return an error otherwise. 
2111 
A valid non-zero Frequency will force the device to listen to the beacon on a fixed frequency 
2112 
channel even if the default behavior specifies a frequency hopping beacon (i.e US ISM 
2113 
band). 
2114 
A value of 0 instructs the end-device to use the default beacon frequency plan as defined in 
2115 
the “Beacon physical layer” section. Where applicable the device resumes frequency 
2116 
hopping beacon search. 
2117 
Upon reception of this command the end-device answers with a BeaconFreqAns message. 
2118 
The MAC payload of this message contains the following information: 
2119 
Size (bytes) 
1 
BeaconFreqAns payload 
Status 
Figure 56 : BeaconFreqAns payload format 
2120 
The Status bits have the following meaning: 
2121 
Bits 7:1 
0 
Status RFU 
Beacon frequency ok 
 
2122 
 
Bit = 0 
Bit = 1 
Beacon 
frequency ok 
The device cannot use this frequency, the 
previous beacon frequency is kept 
The beacon frequency 
has been changed

## Page 78

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 78 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
2123 
14.3 PingSlotChannelReq 
2124 
This command is sent by the server to the end-device to modify the frequency and/or the 
2125 
data rate on which the end-device expects the downlink pings. 
2126 
This command can only be sent in a class A receive window (following an uplink). The 
2127 
command SHALL NOT be sent in a class B ping-slot. If the device receives it inside a class 
2128 
B ping-slot, the MAC command SHALL NOT be processed. 
2129 
 
2130 
Octets 
3 
1 
PingSlotChannelReq Payload 
Frequency 
DR 
Figure 57 : PingSlotChannelReq payload format 
2131 
The Frequency coding is identical to the NewChannelReq MAC command defined in the 
2132 
Class A. 
2133 
Frequency is a 24bits unsigned integer. The actual ping channel frequency in Hz is 100 x 
2134 
frequ. This allows defining the ping channel anywhere between 100MHz to 1.67GHz by 
2135 
100Hz step. The end-device has to check that the frequency is actually allowed by its radio 
2136 
hardware and return an error otherwise. 
2137 
A value of 0 instructs the end-device to use the default frequency plan. 
2138 
The DR byte contains the following fields: 
2139 
 
2140 
Bits 
7:4 
3:0 
DR RFU 
data rate 
 
2141 
The “data rate” subfield is the index of the Data Rate used for the ping-slot downlinks. The 
2142 
relationship between the index and the physical data rate is defined in [PHY] for each region. 
2143 
Upon reception of this command the end-device answers with a PingSlotFreqAns 
2144 
message. The MAC payload of this message contains the following information: 
2145 
 
2146 
Size (bytes) 
1 
pingSlotFreqAns Payload 
Status 
Figure 58 : PingSlotFreqAns payload format 
2147 
The Status bits have the following meaning: 
2148 
Bits 7:2 
1 
0 
Status RFU Data rate ok 
Channel frequency ok 
 
2149 
 
Bit = 0 
Bit = 1 
Data rate ok 
The designated data rate is 
not defined for this end 
device, the previous data 
rate is kept 
The data rate is compatible 
with the possibilities of the 
end device 
Channel frequency ok 
The device cannot receive 
on this frequency  
This frequency can be used 
by the end-device 
 
2150

## Page 79

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 79 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
2151 
If either of those 2 bits equals 0, the command did not succeed and the ping-slot parameters 
2152 
have not been modified. 
2153 
 
2154 
14.4 BeaconTimingReq & BeaconTimingAns 
2155 
These MAC commands are deprecated in the LoRaWAN1.1 version. The device may use 
2156 
DeviceTimeReq&Ans commands as a substitute. 
2157 
 
2158

## Page 80

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 80 of 101 
The authors reserve the right to change 
specifications without notice. 
 
15 Beaconing (Class B option) 
2159 
15.1 Beacon physical layer 
2160 
Besides relaying messages between end-devices and Network Servers,  gateways may 
2161 
participate in providing a time-synchronization mechanisms by sending beacons at regular 
2162 
fixed intervals.  All beacons are transmitted in radio packet implicit mode, that is, without a 
2163 
LoRa physical header and with no CRC being appended by the radio. 
2164 
 
2165 
PHY 
Preamble 
BCNPayload 
Figure 59 : beacon physical format 
2166 
The beacon Preamble shall begin with (a longer than default) 10 unmodulated symbols. This 
2167 
allows end-devices to implement a low power duty-cycled beacon search. 
2168 
The beacon frame length is tightly coupled to the operation of the radio Physical layer. 
2169 
Therefore the actual frame length and content might change from one region implementation 
2170 
to another. The beacon content, modulation parameters and frequencies to use are 
2171 
specified in [PHY] for each region. 
2172 
15.2 Beacon frame content 
2173 
The beacon payload BCNPayload consists of a network common part and a gateway-
2174 
specific part. 
2175 
 
2176 
Size (bytes) 
2/3 
4 
2 
7 
0/1 
2 
BCNPayload 
RFU 
Time 
CRC 
GwSpecific 
RFU 
CRC 
Figure 60 : beacon frame content 
2177 
The common part contains an RFU field equal to 0, a timestamp Time in seconds since 
2178 
00:00:00, Sunday 6th of January 1980 (start of the GPS epoch) modulo 2^32.  The integrity 
2179 
of the beacon’s network common part is protected by a 16 bits CRC . The CRC-16 is 
2180 
computed on the RFU+Time fields as defined in the IEEE 802.15.4-2003 section 7.2.1.8. 
2181 
This CRC uses the following polynomial P(x) = x16+ x12+ x5+ x0 . The CRC is calculated on 
2182 
the bytes in the order they are sent over-the-air 
2183 
For example: This is a valid EU868 beacon frame: 
2184 
00 00 | 00 00 02 CC | A2 7E | 00 | 01 20 00 | 00 81 03 | DE 55 
2185 
Bytes are transmitted left to right. The first CRC is calculated on [00 00 00 00 02 CC]. The 
2186 
corresponding field values are: 
2187 
 
2188 
Field 
RFU 
Time 
CRC 
InfoDesc 
lat 
long 
CRC 
Value Hex 
0000 
CC020000 
7EA2 
0 
002001 
038100 
55DE 
Figure 61 : example of beacon CRC calculation (1) 
2189

## Page 81

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 81 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
2190 
The gateway specific part provides additional information regarding the gateway sending a 
2191 
beacon and therefore may differ for each gateway. The RFU field when applicable (region 
2192 
specific) should be equal to 0. The optional part is protected by a CRC-16 computed on the 
2193 
GwSpecific+RFU fields. The CRC-16 definition is the same as for the mandatory part. 
2194 
For example: This is a valid US900 beacon: 
2195 
Field 
RFU 
Time 
CRC 
InfoDesc 
lat 
long 
RFU 
CRC 
Value Hex 
000000 
CC020000 
7E A2 
00 
002001 
038100 
00 
D450 
Figure 62 : example of beacon CRC calculation (2) 
2196 
Over the air the bytes are sent in the following order: 
2197 
00 00 00 | 00 00 02 CC | A2 7E  | 00 | 01 20 00 | 00 81 03 |00 | 50 D4 
2198 
Listening and synchronizing to the network common part is sufficient to operate a stationary 
2199 
end-device in Class B mode. A mobile end-device may also demodulate the gateway 
2200 
specific part of the beacon to be able to signal to the Network Server whenever he is moving 
2201 
from one cell to another. 
2202 
Note: As mentioned before, all gateways participating in the beaconing 
2203 
process send their beacon simultaneously so that for network common 
2204 
part there are no visible on-air collisions for a listening end-device even 
2205 
if the end-device simultaneously receives beacons from several 
2206 
gateways. Not all gateways are required to participate in the beaconing 
2207 
process. The participation of a gateway to a given beacon may be 
2208 
randomized.  With respect to the gateway specific part, collision occurs 
2209 
but an end-device within the proximity of more than one gateway will 
2210 
still be able to decode the strongest beacon with high probability.   
2211 
15.3 Beacon GwSpecific field format 
2212 
The content of the GwSpecific field is as follow: 
2213 
Size (bytes) 
1 
6 
GwSpecific 
InfoDesc 
Info 
Figure 63 : beacon GwSpecific field format 
2214 
The information descriptor InfoDesc describes how the information field Info shall be 
2215 
interpreted.  
2216 
 
2217 
InfoDesc 
Meaning 
0 
GPS coordinate of the gateway first 
antenna 
1 
GPS coordinate of the gateway second 
antenna 
2 
GPS coordinate of the gateway third 
antenna 
3:127 
RFU 
128:255 
Reserved for custom network specific 
broadcasts 
Table 21 : beacon infoDesc index mapping 
2218 
For a single omnidirectional antenna gateway the InfoDesc value is 0 when broadcasting 
2219 
GPS coordinates. For a site featuring 3 sectored antennas for example, the first antenna 
2220

## Page 82

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 82 of 101 
The authors reserve the right to change 
specifications without notice. 
 
broadcasts the beacon with InfoDesc equals 0, the second antenna with InfoDesc field 
2221 
equals 1, etc. 
2222 
15.3.1 Gateway GPS coordinate:InfoDesc = 0, 1 or 2 
2223 
For InfoDesc = 0 ,1 or 2, the content of the Info field encodes the GPS coordinates of the 
2224 
antenna broadcasting the beacon 
2225 
Size (bytes) 
3 
3 
Info 
Lat 
Lng 
Figure 64 : beacon Info field format 
2226 
The latitude and longitude fields (Lat and Lng, respectively) encode the geographical 
2227 
location of the gateway as follows: 
2228 
 
The north-south latitude is encoded using a two’s complement 24 bit word where -223 
2229 
corresponds to 90° south (the South Pole) and 223-1 corresponds to ~90° north (the 
2230 
North Pole).  The Equator corresponds to 0. 
2231 
 
The east-west longitude is encoded using a two’s complement 24 bit word where - 
2232 
223 corresponds to 180° West and 223-1 corresponds to ~180° East.  The Greenwich 
2233 
meridian corresponds to 0. 
2234 
15.4 Beaconing precise timing 
2235 
The beacon is sent every 128 seconds starting at 00:00:00, Sunday 5th – Monday 6th of 
2236 
January 1980 (start of the GPS epoch) plus TBeaconDelay. Therefore the beacon is sent at 
2237 
 
BT = k * 128 + TBeaconDelay 
2238 
seconds after the GPS epoch. 
2239 
wherebyk is the smallest integer for which 
2240 
 
k * 128 >T 
2241 
whereby 
2242 
 
T = seconds since 00:00:00, Sunday 5th of January 1980 (start of the GPS time). 
2243 
Note: T is GPS time and unlike Unix time, T is strictly monotonically 
2244 
increasing and is not influenced by leap seconds. 
2245 
 
2246 
Whereby TBeaconDelay is 1.5 mSec +/- 1uSec delay. 
2247 
TBeaconDelay is meant to allow a slight transmission delay of the gateways required by the 
2248 
radio system to switch from receive to transmit mode. 
2249 
All end-devices ping slots use the beacon transmission start time as a timing reference, 
2250 
therefore the Network Server as to take TBeaconDelay into account when scheduling the 
2251 
class B downlinks. 
2252 
 
2253 
15.5 Network downlink route update requirements 
2254 
When the network attempts to communicate with an end-device using a Class B downlink 
2255 
slot, it transmits the downlink from the gateway which was closest to the end-device when 
2256

## Page 83

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 83 of 101 
The authors reserve the right to change 
specifications without notice. 
 
the last uplink was received. Therefore the Network Server needs to keep track of the rough 
2257 
position of every Class B device. 
2258 
Whenever a Class B device moves and changes cell, it needs to communicate with the 
2259 
Network Server in order to update its downlink route.  This update can be performed simply 
2260 
by sending a “confirmed” or “unconfirmed” uplink, possibly without applicative payload.  
2261 
The end-device has the choice between 2 basic strategies: 
2262 
 
Systematic periodic uplink: simplest method that doesn’t require demodulation of the 
2263 
“gateway specific” field of the beacon. Only applicable to slowly moving or stationery 
2264 
end-devices. There are no requirements on those periodic uplinks. 
2265 
 
Uplink on cell change: The end-device demodulates the “gateway specific” field of 
2266 
the beacon, detects that the ID of the gateway broadcasting the beacon it 
2267 
demodulates has changed, and sends an uplink. In that case the device SHALL 
2268 
respect a pseudo random delay in the [0:120] seconds range between the beacon 
2269 
demodulation and the uplink transmission.  This is required to insure that the uplinks 
2270 
of multiple Class B devices entering or leaving a cell during the same beacon period 
2271 
will not systematically occur at the same time immediately after the beacon 
2272 
broadcast. 
2273 
Failure to report cell change will result in Class B downlink being temporary not operational. 
2274 
The Network Server may have to wait for the next end-device uplink to transmit downlink 
2275 
traffic. 
2276 
 
2277 
 
2278

## Page 84

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 84 of 101 
The authors reserve the right to change 
specifications without notice. 
 
16 Class B unicast & multicast downlink channel frequencies 
2279 
The class B downlink channel selection mechanism depends on the way the class B beacon 
2280 
is being broadcasted. 
2281 
16.1 Single channel beacon transmission 
2282 
In certain regions (ex EU868) the beacon is transmitted on a single channel. In that case,all 
2283 
unicast&multicastClass B downlinks use a single frequency channel defined by the 
2284 
“PingSlotChannelReq” MAC command. The default frequency is defined in  [PHY]. 
2285 
16.2 Frequency-hopping beacon transmission 
2286 
In certain regions (ex US902-928 or CN470-510) the class B beacon is transmitted following 
2287 
a frequency hopping pattern. 
2288 
In that case, by default Class B downlinks use a channel which is a function of the Time field 
2289 
of the last beacon (see Beacon Frame content) and the DevAddr. 
2290 
Class B downlink channel = [DevAddr + floor ( Beacon_Time 
Beacon_period)]  modulo NbChannel 
2291 
 
Whereby Beacon_Time is the 32 bit Time field of the current beacon period 
2292 
 
Beacon_period is the length of the beacon period (defined as 128sec in the 
2293 
specification) 
2294 
 
Floor designates rounding to the immediately lower integer value 
2295 
 
DevAddr is the 32 bits network address of the device 
2296 
 
NbChannel is the number of channel over which the beacon is frequency hopping 
2297 
Class B downlinks therefore hop across NbChannel channels (identical to the beacon 
2298 
transmission channels) in the ISM band and all Class B end-devices are equally spread 
2299 
amongst the NbChannel downlink channels.  
2300 
If the “PingSlotChannelReq” command with a valid non-zero argument is used to set the 
2301 
Class B downlink frequency then all subsequent ping slots should be opened on this single 
2302 
frequency independently of the last beacon frequency. 
2303 
If the “PingSlotChannelReq” command with a zero argument is sent, the end-device 
2304 
should resume the default frequency plan, id Class B ping slots hoping across 8 channels. 
2305 
The underlying idea is to allow network operators to configure end-devices to use a single 
2306 
proprietary dedicated frequency band for the Class B downlinks if available, and to keep as 
2307 
much frequency diversity as possible when the ISM band is used. 
2308 
 
2309

## Page 85

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 85 of 101 
The authors reserve the right to change 
specifications without notice. 
 
CLASS C – CONTINUOUSLY LISTENING 
2310

## Page 86

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 86 of 101 
The authors reserve the right to change 
specifications without notice. 
 
17 Class C: Continuously listening end-device 
2311 
The end-devices implanting the Class C option are used for applications that have sufficient 
2312 
power available and thus do not need to minimize reception time. 
2313 
Class C end-devices SHALL NOT implement Class B option. 
2314 
The Class C end-device will listen with RX2 windows parameters as often as possible. The 
2315 
end-device SHALL listen on RX2 when it is not either (a) sending or (b) receiving on RX1, 
2316 
according to Class A definition. To do so, it MUST open a short window using RX2 
2317 
parameters between the end of the uplink transmission and the beginning of the RX1 
2318 
reception window and MUST switch to RX2 reception parameters as soon as the RX1 
2319 
reception window is closed; the RX2 reception window MUST remain open until the end-
2320 
device has to send another message. 
2321 
Note: If the device is in the process of demodulating a downlink using 
2322 
the RX2 parameters when the RX1 window should be opened, it shall 
2323 
drop the demodulation and switch to the RX1 receive window 
2324 
Note: There is not specific message for a node to tell the server that it 
2325 
is a Class C node. It is up to the application on server side to know that 
2326 
it manages Class C nodes based on the contract passed during the 
2327 
join procedure. 
2328 
In case a message is received by a device in Class C mode requiring an uplink transmission 
2329 
(DL MAC command request or DL message in confirmed mode), the device SHALL answer 
2330 
within a time period known by both the end-device and the Network Server (out-of-band 
2331 
provisioning information). 
2332 
Before this timeout expires, the network SHALL not send any new confirmed message or 
2333 
MAC command to the device. Once this timeout expires or after reception of any uplink 
2334 
message, the network is allowed to send a new DL message. 
2335 
17.1 Second receive window duration for Class C 
2336 
Class C devices implement the same two receive windows as Class A devices, but they do 
2337 
not close RX2 window until they need to send again. Therefore they may receive a downlink 
2338 
in the RX2 window at nearly any time, including downlinks sent for the purpose of MAC 
2339 
command or ACK transmission. A short listening window on RX2 frequency and data rate is 
2340 
also opened between the end of the transmission and the beginning of the RX1 receive 
2341 
window. 
2342 
 
2343 
 
2344

## Page 87

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 87 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
2345 
Figure 65: Class C end-device reception slot timing. 
2346 
17.2 Class C Multicast downlinks 
2347 
Similarly to Class B, Class C devices may receive multicast downlink frames. The multicast 
2348 
address and associated network session key and application session key must come from 
2349 
the application layer. The same limitations apply for Class C multicast downlink frames: 
2350 
 
They SHALL NOT  carry MAC commands, neither in the FOpt field, nor in the 
2351 
payload on port 0 because a multicast downlink does not have the same 
2352 
authentication robustness as a unicast frame. 
2353 
 
The ACK and ADRACKReq bits MUST be zero. The MType field MUST carry the 
2354 
value for Unconfirmed Data Down. 
2355 
 
The FPending bit indicates there is more multicast data to be sent. Given that a 
2356 
Class C device keeps its receiver active most of the time, the FPending bit does not 
2357 
trigger any specific behavior of the end-device. 
2358

## Page 88

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 88 of 101 
The authors reserve the right to change 
specifications without notice. 
 
18 Class C MAC command 
2359 
All commands described in the Class A specification SHALL be implemented in Class C 
2360 
devices. The Class C specification adds the following MAC commands. 
2361 
 
2362 
CID 
Command 
Transmitted by 
Short Description 
End-
device 
Gateway 
0x20 
DeviceModeInd 
x 
 
Used by the end-device to indicate its current 
operating mode (Class A or C) 
0x20 
DeviceModeConf 
 
x 
Used by the network to acknowledge a 
DeviceModeInd command 
Table 22 : Class C MAC command table 
2363 
18.1 Device Mode (DeviceModeInd, DeviceModeConf) 
2364 
With the DeviceModeInd command, an end-device indicates to the network that it wants to 
2365 
operate either in class A or C. The command has a one byte payload defined as follows: 
2366 
 
2367 
Size (bytes) 
1 
DeviceModeInd Payload 
Class 
Figure 66 : DeviceModeInd payload format 
2368 
With the classes defined for the above commands as: 
2369 
  
2370 
Class 
Value 
Class A 
0x00 
RFU 
0x01 
Class C 
0x02 
Table 23 : DeviceModInd class mapping 
2371 
When a DeviceModeInd command is received by the Network Server, it responds with a 
2372 
DeviceModeConf command. The device SHALL include the DeviceModeInd command in 
2373 
all uplinks until the DeviceModeConf command is received.   
2374 
The device SHALL switch mode as soon as the first DeviceModeInd command is 
2375 
transmitted. 
2376 
Note: When transitioning from class A to class C, It is recommended 
2377 
for battery powered devices to implement a time-out mechanism in the 
2378 
application layer to guarantee that it does not stay indefinitely in class 
2379 
C mode if no connection is possible with the network. 
2380 
The DeviceModeConf command has a 1 byte payload. 
2381 
Size (bytes) 
1 
DeviceModeConf Payload 
Class 
 
2382 
With the class parameter defined as for the DeviceModeInd command 
2383 
 
2384 
 
2385 
 
2386

## Page 89

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 89 of 101 
The authors reserve the right to change 
specifications without notice. 
 
SUPPORT INFORMATION 
2387 
This sub-section is only a recommendation. 
2388 
 
2389

## Page 90

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 90 of 101 
The authors reserve the right to change 
specifications without notice. 
 
19 Examples and Application Information 
2390 
Examples are illustrations of the LoRaWAN spec for information, but they are not part of the 
2391 
formal specification. 
2392 
19.1 Uplink Timing Diagram for Confirmed Data Messages 
2393 
The following diagram illustrates the steps followed by an end-device trying to transmit two 
2394 
confirmed data frames (Data0 and Data1). This device’s NbTrans parameter must be 
2395 
greater or equal to 2 for this example to be valid (because the first confirmed frame is 
2396 
transmitted twice) 
2397 
 
2398 
 
2399 
Figure 67: Uplink timing diagram for confirmed data messages 
2400 
The end-device first transmits a confirmed data frame containing the Data0 payload at an 
2401 
arbitrary instant and on an arbitrary channel. The frame counter Cu is simply derived by 
2402 
adding 1 to the previous uplink frame counter. The network receives the frame and 
2403 
generates a downlink frame with the ACK bit set exactly RECEIVE_DELAY1 seconds later, 
2404 
using the first receive window of the end-device. This downlink frame uses the same data 
2405 
rate and the same channel as the Data0 uplink. The downlink frame counter Cd is also 
2406 
derived by adding 1 to the last downlink towards that specific end-device. If there is no 
2407 
downlink payload pending the network shall generate a frame without a payload. In this 
2408 
example the frame carrying the ACK bit is not received. 
2409 
If an end-device does not receive a frame with the ACK bit set in one of the two receive 
2410 
windows immediately following the uplink transmission it may resend the same frame with 
2411 
the same payload and frame counter again at least ACK_TIMEOUT seconds after the 
2412 
second reception window. This resend must be done on another channel and must obey the 
2413 
duty cycle limitation as any other normal transmission.  If this time the end-device receives 
2414 
the ACK downlink during its first receive window, as soon as the ACK frame is demodulated, 
2415 
the end-device is free to transmit a new frame on a new channel. 
2416 
The third ACK frame in this example also carries an application payload. A downlink frame 
2417 
can carry any combination of ACK, MAC control commands and payload.  
2418 
19.2 Downlink Diagram for Confirmed Data Messages 
2419 
The following diagram illustrates the basic sequence of a “confirmed” downlink. 
2420 
 
2421 
 
2422 
gateway
End-point
Confirmed Data0 
{Cu}
ACK 
{Cd}
Confirmed Data0
{Cu}
ACK 
{Cd+1}
Confirmed Data1
{Cu+1}
Data + ACK 
{Cd+2}
ok
ok
ok
ko
ok
ok
Receive slots
(diag 1)

## Page 91

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 91 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
2423 
Figure 68: Downlink timing diagram for confirmed data messages 
2424 
The frame exchange is initiated by the end-device transmitting an “unconfirmed” application 
2425 
payload or any other frame on channel A. The network uses the downlink receive window to 
2426 
transmit a “confirmed” data frame towards the end-device on the same channel A. Upon 
2427 
reception of this data frame requiring an acknowledgement, the end-device transmits a 
2428 
frame with the ACK bit set at its own discretion. This frame might also contain piggybacked 
2429 
data or MAC commands as its payload. This ACK uplink is treated like any standard uplink, 
2430 
and as such is transmitted on a random channel that might be different from channel A. 
2431 
Note: To allow the end-devices to be as simple as possible and have 
2432 
keep as few states as possible it may transmit an explicit (possibly 
2433 
empty) acknowledgement data message immediately after the 
2434 
reception of a data message requiring an acknowledgment. 
2435 
Alternatively the end-device may defer the transmission of an 
2436 
acknowledgement to piggyback it with its next data message. 
2437 
19.3 Downlink Timing for Frame-Pending Messages 
2438 
The next diagram illustrates the use of the frame pending (FPending) bit on a downlink. 
2439 
The FPending bit can only be set on a downlink frame and informs the end-device that the 
2440 
network has several frames pending for him; the bit is ignored for all uplink frames. 
2441 
If a frame with the FPending bit set requires an acknowledgement, the end-device shall do 
2442 
so as described before. If no acknowledgment is required, the end-device may send an 
2443 
empty data message to open additional receive windows at its own discretion, or wait until it 
2444 
has some data to transmit itself and open receive windows as usual. 
2445 
Note: The FPending bit is independent to the acknowledgment 
2446 
scheme. 
2447 
 
2448 
Figure 69: Downlink timing diagram for frame-pending messages, example 1 
2449 
gateway
End-point
Unconfirmed data 
{Cu}
Confirmed Data 
{Cd}
ok
ok
Receive slots
ok
ACK 
{Cu+1}
gateway
End-point
Data uplink
{cu}
Confirmed 
Data0+F_P 
{cd}
ACK 
{cu+1}
Confirmed 
Data1 
{cd+1}
ACK 
{cu+2}
ok
ok
ok
(*) F_P means ‘frame pending’ bit set
Receive slots

## Page 92

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 92 of 101 
The authors reserve the right to change 
specifications without notice. 
 
In this example the network has two confirmed data frames to transmit to the end-device. 
2450 
The frame exchange is initiated by the end-device via a normal “unconfirmed” uplink 
2451 
message on channel A. The network uses the first receive window to transmit the Data0 with 
2452 
the bit FPending set as a confirmed data message. The device acknowledges the reception 
2453 
of the frame by transmitting back an empty frame with the ACK bit set on a new channel B. 
2454 
RECEIVE_DELAY1 seconds later, the network transmits the second frame Data1 on 
2455 
channel B, again using a confirmed data message but with the FPending bit cleared. The 
2456 
end-device acknowledges on channel C.  
2457 
 
2458 
 
2459 
 
2460 
Figure 70: Downlink timing diagram for frame-pending messages, example 2 
2461 
In this example, the downlink frames are “unconfirmed” frames, the end-device does not 
2462 
need to send back and acknowledge. Receiving the Data0 unconfirmed frame with the 
2463 
FPending bit set the end-device sends an empty data frame. This first uplink is not received 
2464 
by the network. If no downlink is received during the two receive windows, the network has 
2465 
to wait for the next spontaneous uplink of the end-device to retry the transfer. The end-
2466 
device can speed up the procedure by sending a new empty data frame. 
2467 
Note: An acknowledgement is never sent twice.  
2468 
 
2469 
The FPending bit, the ACK bit, and payload data can all be present in the same downlink. 
2470 
For example, the following frame exchange is perfectly valid. 
2471 
 
2472 
 
2473 
Figure 71: Downlink timing diagram for frame-pending messages, example 3 
2474 
The end-device sends a “confirmed data” uplink. The network can answer with a confirmed 
2475 
downlink containing Data + ACK + “Frame pending” then the exchange continues as 
2476 
previously described. 
2477 
gateway
End-point
Data uplink
{cu}
Data0+F_P 
{cd}
void
{cu+1}
ok
void
{cu+3}
ok
ok
Data1+F_P
{cd+1}
void 
{cu+2}
gateway
End-point
Confirmed 
Data uplink
{cu}
Confirmed 
Data0+F_P+ACK
{cd}
ACK 
{cu+1}
Confirmed 
Data1+F_P
{cd+2}
ACK 
{cu+3}
ok
void
{cu+2}
Receiving a frame without the ACK bit set , server 
retransmits Data1 , frame counter must be incremented
ok
ok
Confirmed 
Data1+F_P
{cd+1}
(diag 2)

## Page 93

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 93 of 101 
The authors reserve the right to change 
specifications without notice. 
 
20 Recommendation on contract to be provided to the Network 
2478 
Server by the end-device provider at the time of provisioning 
2479 
Configuration data related to the end-device and its characteristics must be known by the 
2480 
Network Server at the time of provisioning. –This provisioned data is called the “contract”. 
2481 
This contract cannot be provided by the end-device and must be supplied by the end-device 
2482 
provider using another channel (out-of-band communication). 
2483 
This end-device contract is stored in the Network Server. It can be used by the Application 
2484 
Server and the network controller to adapt the algorithms. 
2485 
This data will include: 
2486 
 
End-device specific radio parameters (device frequency range, device maximal 
2487 
output power, device communication settings - RECEIVE_DELAY1, 
2488 
RECEIVE_DELAY2) 
2489 
 
Application type (Alarm, Metering, Asset Tracking, Supervision, Network Control) 
2490

## Page 94

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 94 of 101 
The authors reserve the right to change 
specifications without notice. 
 
21 Recommendation on finding the locally used channels 
2491 
End-devices that can be activated in territories that are using different frequencies for 
2492 
LoRaWAN will have to identify what frequencies are supported for join message at their 
2493 
current location before they send any message. The following methods are proposed: 
2494 
 
A GPS enabled end-device can use its GPS location to identify which frequency 
2495 
band to use. 
2496 
 
End-device can search for a class B beacon and use its frequency to identify its 
2497 
region 
2498 
 
End-device can search for a class B beacon and if this one is sending the antenna 
2499 
GPS coordinate, it can use this to identify its region 
2500 
 
End-device can search for a beacon and if this one is sending a list of join 
2501 
frequencies, it can use this to send its join message 
2502

## Page 95

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 95 of 101 
The authors reserve the right to change 
specifications without notice. 
 
22 Revisions  
2503 
22.1 Revision 1.0 
2504 
 
Approved version of LoRaWAN1.0 
2505 
22.2 Revision 1.0.1 
2506 
 
Clarified the RX window start time definition 
2507 
 
Corrected  the maximum payload size for DR2 in the NA section 
2508 
 
Corrected the typo on the downlink data rate range in 7.2.2 
2509 
 
Introduced a requirement for using coding rate 4/5 in 7.2.2 to guarantee a maximum 
2510 
time on air < 400mSec 
2511 
 
Corrected the Join-accept MIC calculation in 6.2.5 
2512 
 
Clarified the NbRep field and renamed it to NbTrans in 5.2 
2513 
 
Removed the possibility to not encrypt the Applicative payload in the MAC layer , 
2514 
removed the paragraph 4.3.3.2. If further security is required by the application , the 
2515 
payload will be encrypted, using any method, at the application layer then re-
2516 
encrypted at the MAC layer using the specified default LoRaWAN encryption 
2517 
 
Corrected FHDR field size typo 
2518 
 
Corrected the channels impacted by ChMask when chMaskCntl equals 6 or 7 in 
2519 
7.2.5 
2520 
 
Clarified 6.2.5 sentence describing the RX1 slot data rate offset in the JoinResp 
2521 
message 
2522 
 
Removed the second half of the DRoffset table in 7.2.7 , as DR>4 will never be used 
2523 
for uplinks by definition 
2524 
 
Removed explicit duty cycle limitation implementation in the EU868Mhz ISM band 
2525 
(chapter7.1) 
2526 
 
Made the RXtimingSetupAns and RXParamSetupAns sticky MAC commands to 
2527 
avoid end-device’s hidden state problem. (in 5.4 and 5.7) 
2528 
 
Added a frequency plan for the Chinese 470-510MHz metering band 
2529 
 
Added a frequency plan for the Australian 915-928MHz ISM band 
2530 
 
2531 
22.3 Revision 1.0.2 
2532 
 
Extracted section 7 “Physical layer” that will now be a separated document 
2533 
“LoRaWAN regional physical layers definition” 
2534 
 
corrected the ADR_backoff  sequence description (ADR_ACK_LIMT was written 
2535 
instead of ADR_ACK_DELAY) paragraph 4.3.1.1 
2536 
 
 Corrected a formatting issue in the title of section 18.2 (previously section 19.2 in the 
2537 
1.0.1 version) 
2538 
 
Added the DlChannelRec MAC command, this command is used to modify the 
2539 
frequency at which an end-device expects a downlink. 
2540 
 
Added the Tx ParamSetupRec MAC command. This command enables to remotely 
2541 
modify the maximum TX dwell time and the maximum  radio transmit power of a 
2542 
device in certain regions 
2543

## Page 96

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 96 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
Added the ability for the end-device to process several ADRreq commands in a 
2544 
single block in 5.2 
2545 
 
Clarified AppKey definitionIntroduced the ResetInd / ResetConf MAC commands 
2546 
 
Split Data rate and txpower table in 7.1.3 for clarity 
2547 
 
Added DeviceTimeReq/Ans MAC command to class A 
2548 
 
Changed Class B time origin to GPS epoch, added BeaconTimingAns description 
2549 
 
Aligned all beacons of class B to the same time slot. Class B beacon is now common 
2550 
to all networks. 
2551 
 
Separated AppKey and NwkKey to independently derive AppSKeys and NetSKeys. 
2552 
 
Separated NetSKeyUp and NetSKeyDnw for roaming 
2553 
 
 
2554 
22.4 Revision 1.1  
2555 
This section provides an overview of the main changes happening between LoRaWAN1.1 
2556 
and LoRaWAN1.0.2. 
2557 
22.4.1 Clarifications 
2558 
o 
Grammatical 
2559 
o 
Normative text used consistently  
2560 
o 
ADR behavior,  
2561 
 
Introduced the concept of ADR command block processing  
2562 
 
TXPower handling 
2563 
 
Default channel re-enabling 
2564 
 
ADR Backoff behavior 
2565 
o 
Default TXPower definition 
2566 
o 
FCnt shall never be reused with the same session keys 
2567 
o 
MAC Commands are discarded if present in both FOpts and Payload 
2568 
o 
Retransmission backoff clarification 
2569 
22.4.2 Functional modifications 
2570 
o 
FCnt changes 
2571 
 
All counters are 32bits wide , 16bits not supported any more 
2572 
 
Separation of FCntDown into AFCntDown and NFCntDown 
2573 
 
Remove state synchronization requirement from NS/AS 
2574 
 
Remove requirement to discard frames if FCnt gap is greater than MAX_FCNT_GAP 
2575 
 
Unnecessary with 32bit counters 
2576 
 
End-device Frame counters are reset upon the successful processing of a Join-Accept 
2577 
 
ABP device must never reset frame counters 
2578 
o 
Retransmission (transmission without incrementing the FCnt) 
2579 
 
Downlink frames are never retransmitted 
2580 
 
Subsequent receptions of a frame with the same FCnt are ignored 
2581 
 
Uplink retransmissions are controlled by NbTrans (this includes both confirmed and 
2582 
unconfirmed frames) 
2583

## Page 97

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 97 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
A retransmission may not occur until both RX1 and RX2 receive windows have 
2584 
expired 
2585 
 
Class B/C devices cease retransmitting a frame upon the reception of a frame in the 
2586 
RX1 window 
2587 
 
Class A device cease retransmitting a frame upon the reception of a frame in either 
2588 
the RX1 or RX2 window 
2589 
o 
Key changes 
2590 
 
Added one new root key (separation of cipher function) 
2591 
 
NwkKey and AppKey 
2592 
 
Added new session keys 
2593 
 
NwkSEncKey encrypts payloads where Fport = 0 (MAC command payload) 
2594 
 
AppSKey encrypts payloads where Fport != 0 (Application payloads) 
2595 
 
NwkSIntKey is used to MIC downlink frames 
2596 
 
For downlinks with the ACK bit set, the 2 LSBs of the AFCntUp of the 
2597 
confirmed uplink which generated the ACK are added to the MIC 
2598 
calculation 
2599 
 
SNwkSIntKey and FNwkSIntKey are used to MIC uplink frames 
2600 
 
Each is used to calculate 2 separate 16 bit MICs which are combined to a 
2601 
single 32 bit MIC 
2602 
 
The SNwkSIntKey portion is considered "private" and not shared with a 
2603 
roaming fNs 
2604 
 
The FNwkSIntKey portion is considered "public" and may be shared with 
2605 
a roaming fNs 
2606 
 
The private MIC portion now uses the TxDr, TxCh 
2607 
 
For uplinks with the ACK bit set, the 2 LSBs of the FCntDown of the 
2608 
confirmed downlink which generated the ACK are added to the private 
2609 
MIC calculation 
2610 
 
Keys fully defined later (section 6) 
2611 
 
Associated MIC and Encrypt changes using new keys 
2612 
o 
MAC Commands introduced 
2613 
 
TxParamSetupReq/Ans 
2614 
 
DlChannelReq/Ans 
2615 
 
ResetInd/Conf 
2616 
 
ADRParamSetupReq/Ans 
2617 
 
DeviceTimeReq/Ans 
2618 
 
ForceRejoinReq 
2619 
 
RejoinParamSetupReq/Ans 
2620 
 
For the linkADRReq command 
2621 
 
Value of 0xF is to be ignored for DR or TXPower 
2622 
 
Value of 0 is to be ignored for NbTrans 
2623 
o 
Activation 
2624 
 
JoinEUI replaces AppEUI (clarification) 
2625 
 
EUI's fully defined 
2626 
 
Root keys defined 
2627 
 
NwkKey 
2628 
 
AppKey 
2629 
 
Additional session keys added (split MIC/Encrypt keys) 
2630 
 
SNwkSIntKeyUp and FNwkSIntKeyUp (split-MIC uplink) 
2631 
 
NwkSIntKeyDown (MIC downlink) 
2632 
 
NwkSEncKey (Encrypt up/down) 
2633

## Page 98

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 98 of 101 
The authors reserve the right to change 
specifications without notice. 
 
 
JSIntKey (Rejoin-Request and related Join-Accept) 
2634 
 
JSencKey (Join-Accepts in response to Rejoin-Request) 
2635 
 
Session context defined 
2636 
o 
OTAA 
2637 
 
JoinAccept MIC modified to prevent replay attack 
2638 
 
Session key derivation defined 
2639 
 
ReJoin-Request messages defined (one new LoRaWAN Message type [MType] 
2640 
 
0 - Handover roaming assist 
2641 
 
1 - Backend state recovery assist 
2642 
 
2 - Rekey session keys 
2643 
 
All Nonces are now counters (not random any more) 
2644 
 
NetId clarified (association with Home Network) 
2645 
 
OptNeg bit defined in Join-Accept to identify 1.0 or 1.1+ operational version of 
2646 
network backend 
2647 
 
1.0 operation reversion by a 1.1 device defined 
2648 
o 
ABP 
2649 
 
Additional Session key requirement described 
2650 
o 
Class B 
2651 
 
Network now controls the device’s DR 
2652 
 
Beacon definition moved to Regional document 
2653 
 
Clarifications 
2654 
 
Deprecated the BeaconTimingReq/Ans (replaced by the standard MAC command 
2655 
DeviceTimeReq/Ans) 
2656 
o 
Class C 
2657 
 
Clarify requirement for a DL timeout 
2658 
 
Add Class C MAC Commands 
2659 
 
DeviceModeInd/Conf 
2660 
22.4.3 Examples 
2661 
 
Removed aggressive data-rate backoff example during retransmission 
2662 
 
2663

## Page 99

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 99 of 101 
The authors reserve the right to change 
specifications without notice. 
 
23 Glossary 
2664 
 
2665 
ADR 
Adaptive Data Rate 
2666 
AES 
Advanced Encryption Standard 
2667 
AFA 
Adaptive Frequency Agility 
2668 
AR 
Acknowledgement Request 
2669 
CBC 
Cipher Block Chaining 
2670 
CMAC 
Cipher-based Message Authentication Code 
2671 
CR 
Coding Rate 
2672 
CRC 
Cyclic Redundancy Check 
2673 
DR 
Data Rate 
2674 
ECB 
Electronic Code Book 
2675 
ETSI 
European Telecommunications Standards Institute 
2676 
EIRP 
Equivalent Isotropically Radiated Power 
2677 
FSK 
Frequency Shift Keying modulation technique 
2678 
GPRS 
General Packet Radio Service 
2679 
HAL 
Hardware Abstraction Layer 
2680 
IP 
Internet Protocol 
2681 
LBT 
Listen Before Talk 
2682 
LoRa™ 
Long Range modulation technique 
2683 
LoRaWAN™ 
Long Range Network protocol 
2684 
MAC 
Medium Access Control 
2685 
MIC 
Message Integrity Code 
2686 
RF 
Radio Frequency 
2687 
RFU 
Reserved for Future Usage 
2688 
Rx 
Receiver 
2689 
RSSI 
Received Signal Strength Indicator 
2690 
SF 
Spreading Factor 
2691 
SNR 
Signal Noise Ratio 
2692 
SPI 
Serial Peripheral Interface 
2693 
SSL 
Secure Socket Layer 
2694 
Tx 
Transmitter 
2695 
USB 
Universal Serial Bus 
2696

## Page 100

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 100 of 101 
The authors reserve the right to change 
specifications without notice. 
 
24 Bibliography 
2697 
24.1 References 
2698 
[IEEE802154]: IEEE Standard for Local and Metropolitan Area Networks—Part 15.4: Low-
2699 
Rate Wireless Personal Area Networks (LR-WPANs), IEEE Std 802.15.4TM-2011 (Revision 
2700 
of IEEE Std 802.15.4-2006), September 2011. 
2701 
[RFC4493]: The AES-CMAC Algorithm, June 2006. 
2702 
[PHY]:  LoRaWAN Regional parameters v1.1, LoRa Alliance  
2703 
[BACKEND]:  LoRaWAN backend Interfaces specification v1.0, LoRa Alliance 
2704

## Page 101

LoRaWAN 1.1 Specification 
 
©2017 LoRa Alliance™ 
Page 101 of 101 
The authors reserve the right to change 
specifications without notice. 
 
25 NOTICE OF USE AND DISCLOSURE 
2705 
Copyright © LoRa Alliance, Inc. (2017). All Rights Reserved.  
2706 
The information within this document is the property of the LoRa Alliance (“The Alliance”) 
2707 
and its use and disclosure are subject to LoRa Alliance Corporate Bylaws, Intellectual 
2708 
Property Rights (IPR) Policy and Membership Agreements. 
2709 
Elements of LoRa Alliance specifications may be subject to third party intellectual property 
2710 
rights, including without limitation, patent, copyright or trademark rights (such a third party 
2711 
may or may not be a member of LoRa Alliance). The Alliance is not responsible and shall 
2712 
not be held responsible in any manner for identifying or failing to identify any or all such third 
2713 
party intellectual property rights. 
2714 
This document and the information contained herein are provided on an “AS IS” basis and 
2715 
THE ALLIANCE DISCLAIMS ALL WARRANTIES EXPRESS OR IMPLIED, INCLUDING 
2716 
BUT NOT LIMITED TO (A) ANY WARRANTY THAT THE USE OF THE INFORMATION 
2717 
HEREIN WILL NOT INFRINGE ANY RIGHTS OF THIRD PARTIES (INCLUDING WITHOUT 
2718 
LIMITATION 
ANY 
INTELLECTUAL 
PROPERTY 
RIGHTS 
INCLUDING 
PATENT, 
2719 
COPYRIGHT OR TRADEMARK RIGHTS) OR (B) ANY IMPLIED WARRANTIES OF 
2720 
MERCHANTABILITY, 
FITNESS 
FOR 
A 
PARTICULAR 
PURPOSE, 
TITLE 
OR 
2721 
NONINFRINGEMENT. 
2722 
IN NO EVENT WILL THE ALLIANCE BE LIABLE FOR ANY LOSS OF PROFITS, LOSS OF 
2723 
BUSINESS, LOSS OF USE OF DATA, INTERRUPTION OFBUSINESS, OR FOR ANY 
2724 
OTHER DIRECT, INDIRECT, SPECIAL OR EXEMPLARY, INCIDENTIAL, PUNITIVE OR 
2725 
CONSEQUENTIAL DAMAGES OF ANY KIND, IN CONTRACT OR IN TORT, IN 
2726 
CONNECTION WITH THIS DOCUMENT OR THE INFORMATION CONTAINED HEREIN, 
2727 
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH LOSS OR DAMAGE.  
2728 
The above notice and this paragraph must be included on all copies of this document that 
2729 
are made. 
2730 
LoRa Alliance, Inc. 
2731 
3855 SW 153rd Drive 
2732 
Beaverton, OR  97007 
2733 
Note: All Company, brand and product names may be trademarks that are the sole property 
2734 
of their respective owners. 
2735
