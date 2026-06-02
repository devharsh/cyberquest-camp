# Case Study: Yahoo Data Breaches (2013, disclosed 2016 to 2017)

**One-line:** The largest known breach by user count: every Yahoo account, about 3 billion, was compromised, and the company did not tell users for years.

## What was the asset
Yahoo user account data: names, email addresses, telephone numbers, dates of birth, hashed passwords, and security questions and answers.

## The vulnerability
A combination of weak protections and slow disclosure. Passwords were protected with the outdated MD5 hashing function, which is easy to crack, and some security answers were stored unencrypted.

## The threat (what happened)
A breach in August 2013 affected all 3 billion Yahoo accounts. A separate 2014 breach affected at least 500 million accounts and was attributed to a state-sponsored actor. Yahoo first disclosed the 2013 incident in December 2016 (estimating 1 billion accounts), then revised it in October 2017 to all 3 billion.

## Which CIA pillar broke
**Confidentiality**: account data and credentials were exposed. The slow disclosure also harmed user trust.

## Controls that could have prevented or limited it
- Strong, salted password hashing (not MD5).
- Encrypting security questions and answers.
- Faster detection and honest, prompt disclosure to users.
- Multi-factor authentication so stolen passwords alone are not enough.

## Impact
About 3 billion accounts. The disclosures happened during Yahoo's sale to Verizon and reduced the purchase price by about 350 million dollars.

## Sources (authoritative)
- Overview and timeline: https://en.wikipedia.org/wiki/Yahoo_data_breaches
- Yahoo SEC 8-K filing (2016): https://www.sec.gov/Archives/edgar/data/0001011006/000119312516793106/d305610dex991.htm
