# Case Study: Target Data Breach (2013)

**One-line:** Attackers got into a giant retailer through a small heating-and-cooling vendor, then stole 40 million payment cards.

## What was the asset
Customer payment-card data (about 40 million cards) and personal information for about 70 million more customers.

## The vulnerability
Two big weaknesses: a third-party vendor with network access, and no separation between that vendor's access and Target's payment systems.

## The threat (what happened)
Attackers sent a phishing email to Fazio Mechanical Services, an HVAC contractor. Stolen vendor credentials let the attackers into Target's network in November 2013. Because the network was not segmented, they reached the point-of-sale systems and installed card-stealing malware that ran from November 27 to December 15, 2013. Target's security tools flagged the malware, but the alerts were not acted on.

## Which CIA pillar broke
**Confidentiality**: payment-card and personal data were stolen.

## Controls that could have prevented or limited it
- Network segmentation so a vendor account cannot reach payment systems.
- Strong vendor access controls and multi-factor authentication.
- Acting on security alerts (the warnings were there).
- Phishing awareness training for partners.

## Impact
About 40 million cards and 70 million customer records. Total costs exceeded 200 million dollars; Target agreed to an 18.5 million dollar multistate settlement in 2017.

## Sources (authoritative)
- Krebs on Security (broke the story): https://krebsonsecurity.com/2014/02/target-hackers-broke-in-via-hvac-company/
- CSO Online analysis: https://www.csoonline.com/article/548244/security0-11-steps-attackers-took-to-crack-target.html
