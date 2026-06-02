# Case Study: SolarWinds Supply-Chain Attack (2020)

**One-line:** Attackers hid a backdoor inside a trusted software update, so thousands of organizations infected themselves by installing it.

## What was the asset
The integrity of SolarWinds Orion, network-management software used by about 300,000 customers, including U.S. government agencies and large companies.

## The vulnerability
A software supply chain weakness. Attackers compromised SolarWinds' build system and inserted malicious code into legitimate, digitally signed Orion updates.

## The threat (what happened)
Starting in early 2020, attackers (attributed to a Russian state intelligence service) injected a backdoor known as SUNBURST into Orion updates. When customers installed the normal update, they installed the backdoor too. About 18,000 of 300,000 customers received the trojanized version. It was publicly disclosed in December 2020.

## Which CIA pillar broke
**Integrity** first (a trusted update was secretly altered), leading to loss of **Confidentiality** as attackers accessed victim networks.

## Controls that could have prevented or limited it
- Securing the software build pipeline and verifying what gets shipped.
- Zero-trust and least-privilege so one tool cannot reach everything.
- Network monitoring for unusual outbound traffic from trusted software.

## Impact
About 18,000 organizations downloaded the malicious update, including multiple U.S. federal agencies. It is considered one of the most significant supply-chain attacks to date and prompted a major government response.

## Sources (authoritative)
- CISA advisory AA20-352A: https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a
- U.S. GAO overview: https://www.gao.gov/blog/solarwinds-cyberattack-demands-significant-federal-and-private-sector-response-infographic
