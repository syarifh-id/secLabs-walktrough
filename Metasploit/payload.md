# Payloads
A Payload in Metasploit refers to a module that aids the exploit module in (typically) returning a shell to the attacker.
 *_note :_*
>
The Payload in cybersecurity is the malicious code that cyberattackers use to harm computers and networks.


*There are three different types of payload modules in the Metasploit Framework:*
1. Singles
2. Stagers
3. Stages

## Singles

A Single payload contains the exploit and the entire shellcode for the selected task. Inline payloads are by design more stable than their counterparts because they contain everything all-in-one. However, some exploits will not support the resulting size of these payloads as they can get quite large. Singles are self-contained payloads. They are the sole object sent and executed on the target system, getting us a result immediately after running. A Single payload can be as simple as adding a user to the target system or booting up a process.

## Stagers
Stager payloads work with Stage payloads to perform a specific task. A Stager is waiting on the attacker machine, ready to establish a connection to the victim host once the stage completes its run on the remote host. Stagers are typically used to set up a network connection between the attacker and victim and are designed to be small and reliable. Metasploit will use the best one and fall back to a less-preferred one when necessary.

Windows NX vs. NO-NX Stagers

Reliability issue for NX CPUs and DEP
NX stagers are bigger (VirtualAlloc memory)
Default is now NX + Win7 compatible

## Stages
Stages are payload components that are downloaded by stager's modules. The various payload Stages provide advanced features with no size limits, such as Meterpreter, VNC Injection, and others. Payload stages automatically use middle stagers:

A single recv() fails with large payloads
The Stager receives the middle stager
The middle Stager then performs a full download
Also better for RWX

## Staged Payloads
A staged payload is, simply put, an exploitation process that is modularized and functionally separated to help segregate the different functions it accomplishes into different code blocks, each completing its objective individually but working on chaining the attack together. This will ultimately grant an attacker remote access to the target machine if all the stages work correctly.

The scope of this payload, as with any others, besides granting shell access to the target system, is to be as compact and inconspicuous as possible to aid with the Antivirus (AV) / Intrusion Prevention System (IPS) evasion as much as possible.

Stage0 of a staged payload represents the initial shellcode sent over the network to the target machine's vulnerable service, which has the sole purpose of initializing a connection back to the attacker machine. This is what is known as a reverse connection. As a Metasploit user, we will meet these under the common names reverse_tcp, reverse_https, and bind_tcp. For example, under the show payloads command, you can look for the payloads that look like the following:

```
msf6 > show payloads
```

Reverse connections are less likely to trigger prevention systems like the one initializing the connection is the victim host, which most of the time resides in what is known as a security trust zone. However, of course, this trust policy is not blindly followed by the security devices and personnel of a network, so the attacker must tread carefully even with this step.

Stage0 code also aims to read a larger, subsequent payload into memory once it arrives. After the stable communication channel is established between the attacker and the victim, the attacker machine will most likely send an even bigger payload stage which should grant them shell access. This larger payload would be the Stage1 payload. We will go into more detail in the later sections.
