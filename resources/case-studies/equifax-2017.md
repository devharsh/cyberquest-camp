# Case Study: Equifax Data Breach (2017)

**One-line:** A credit bureau left a known web-server flaw unpatched, and attackers stole the personal data of about 147 million people.

## What was the asset
Highly sensitive personal records held by Equifax: names, Social Security numbers, birth dates, addresses, and some driver's license and credit-card numbers.

## The vulnerability
A critical flaw in the Apache Struts web framework, tracked as CVE-2017-5638, which allowed remote code execution through a crafted HTTP request. A patch was released on March 7, 2017. Equifax did not apply it to all systems.

## The threat (what happened)
Around March 10, 2017, attackers exploited the unpatched flaw on Equifax's online dispute portal. From May to July 2017 they quietly moved through the network and exfiltrated data on about 147 million people. Weak internal controls (poor network segmentation and an expired certificate on a monitoring tool) let the intrusion go unnoticed for about 76 days.

## Which CIA pillar broke
Mainly **Confidentiality**: private data was exposed to people who had no right to see it.

## Controls that could have prevented or limited it
- Patch management: apply critical security updates quickly.
- Network segmentation so one server cannot reach the whole database.
- Working monitoring and certificate management to detect exfiltration.

## Impact
About 147 million people affected. Equifax agreed to a settlement of at least 575 million dollars (potentially up to 700 million) with the U.S. Federal Trade Commission, the Consumer Financial Protection Bureau, and the states in 2019.

## Sources (authoritative)
- U.S. Federal Trade Commission settlement: https://www.ftc.gov/news-events/press-releases/2019/07/equifax-pay-575-million-part-settlement-ftc-cfpb-states-related
- U.S. House Oversight Committee report (PDF): https://oversight.house.gov/wp-content/uploads/2018/12/Equifax-Report.pdf
- CVE-2017-5638 record: https://nvd.nist.gov/vuln/detail/CVE-2017-5638
- Overview: https://en.wikipedia.org/wiki/2017_Equifax_data_breach
