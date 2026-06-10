# CyberQuest Camp — Content Expansion Plan
## Textbook Chapter Mapping, Content Gaps, and GitHub Pages Setup

**Camp repo:** https://github.com/devharsh/cyberquest-camp  
**Textbook repo:** https://github.com/devharsh/cybersec-textbook  
**Textbook live:** https://book.com.puter.tips  
**Proposed camp URL:** https://camp.com.puter.tips  

---

## 1. Textbook Chapter Mapping by Day

### Day 1 — Python and the Linux Command Line

**Current content:** Python variables, networking basics, HTTP vs HTTPS, Linux CLI intro, CodeCombat, OverTheWire Bandit.

**Primary textbook chapters:**

| Section | Title | Relevance |
|---|---|---|
| Ch3 §3.1 | Why Networking Is the Battleground | motivates the whole day |
| Ch3 §3.2–3.3 | OSI Model, TCP/IP Model and Encapsulation | visual model for packets |
| Ch3 §3.4–3.5 | IP Addressing, Ports and Common Protocols | HTTP=80, HTTPS=443 etc. |
| Ch3 §3.6 | TCP, UDP, ICMP headers | `socket` Python examples |
| Ch1 §1.10 | Security Mindset, Ethics, and the Law | ground rules from day 1 |

**Content gaps to fill:**

- Python: data types, `for` loops, `while`, functions, `open()` for file I/O — students need this to run Day3 and Day5 notebooks. Add a 4-slide Python primer with runnable code cells.
- Linux: explain the filesystem tree (`/`, `/etc`, `/home`, `/tmp`), `man` pages, pipes (`|`), redirection (`>`, `>>`), and `grep`. OverTheWire Bandit levels 0–5 each need a specific command; map those commands to the slides so students know what they are learning.
- Networking visual: draw the OSI stack as a labeled box diagram (can be inline SVG). Show where each protocol sits. Map to Ch3 Fig 3.1.
- Add a numeric example: compute how many IPv4 addresses exist in a /24 subnet (256 − 2 = 254 usable hosts). This is tractable arithmetic and introduces subnetting without full CIDR notation.
- Add knowledge-check questions from Ch3 Review Questions set (10 MCQ per chapter in the textbook — you can quote or rephrase 3–4 for the slides).

**Suggested new slides (Day1_slides.html):**

1. Python data types with live demo (int, str, list, dict)  
2. Python functions — define, call, return  
3. File I/O in Python — `open()`, `read()`, `write()`  
4. OSI model — 7-layer visual with one example protocol per layer  
5. What happens when you type a URL — DNS → TCP → HTTP request/response  
6. Linux filesystem tree and key directories  
7. Pipes and redirection — `cat /etc/passwd | grep root`  
8. Numeric example: IPv4 address space, subnet sizing  
9. Knowledge check (4 MCQ from Ch3 concepts)  

---

### Day 2 — Security Foundations and Strong Passwords

**Current content:** CIA triad, risk/threat/vulnerability, hacker profiles, CFAA, brute force, DDoS.

**Primary textbook chapters:**

| Section | Title | Relevance |
|---|---|---|
| Ch1 §1.1 | What Is Cybersecurity? | definition, scope |
| Ch1 §1.2 | The CIA Triad and Its Extensions | AAA, DAD, Parkerian model |
| Ch1 §1.3 | The Anatomy of an Attack | threat, vuln, attack surface, exploitation |
| Ch1 §1.4 | Threat Actors and the Adversary Model | script kiddies to APTs |
| Ch1 §1.8 | Quantifying Risk in Monetary Terms | SLE, ARO, ALE, ROSI formulas |
| Ch4 §4.1–4.4 | Why People Are the Weakest Link, Psychology of Influence | human factor |
| Ch4 §4.6 | Recognizing and Analyzing Phishing | spam, spear-phishing, indicators |
| Ch4 §4.8 | Authentication Factors | MFA categories |
| Ch5 §5.1–5.2 | Risk as the Organizing Principle, Vocabulary of Risk | threat vs. vulnerability |
| Ch5 §5.5–5.6 | Qualitative and Quantitative Risk Assessment | high/medium/low matrix; ALE |

**Content gaps to fill:**

- The CIA triad is mentioned but not deep enough. Add the DAD triad (Disclosure, Alteration, Destruction) and the Parkerian Hexad. Each property should have a real-world breach example. Maps to Ch1 §1.2.
- Threat actors need more specificity: nation-states (APTs), hacktivists, insiders, cybercriminals. Tie to the adversary model (Ch1 §1.4). Add a matching quiz: match actor type to a real incident.
- Add the risk formula: `Risk = Threat × Vulnerability × Impact`. Then walk through a quantitative example using ALE = SLE × ARO. Example: a $50,000 server breached once every 2 years → ALE = $25,000. This is a direct numeric example from Ch1 §1.8.
- Password strength: add a brute-force time estimate calculation. A lowercase 8-char password: 26^8 ≈ 2×10^11 combinations. At 10^10 guesses/sec → 20 seconds. A 12-char alphanumeric+symbol: 94^12 ≈ 4×10^23 → impossible. Show this in Python.
- CFAA is mentioned; add a short side-by-side of legal vs. illegal actions (port scanning your own machine = legal, port scanning a bank = illegal). Maps to Ch1 §1.10.

**Suggested new slides:**

1. CIA vs. DAD triads — side-by-side with breach examples  
2. Parkerian Hexad — add Authenticity, Utility, Possession  
3. Threat actor taxonomy — table: type, motivation, typical TTP  
4. The risk equation with SLE/ARO/ALE worked example  
5. How brute force works — Python loop counting guesses, time estimate  
6. Password entropy calculation — numeric walkthrough  
7. MFA factors — something you know / have / are, with examples  
8. CFAA: legal vs. illegal — scenario cards for discussion  
9. Knowledge check (5 MCQ from Ch1 and Ch4 concepts)  

---

### Day 3 — Cryptography: Codes and Ciphers

**Current content:** encoding, encryption, hashing, digital signatures, phishing, MFA.

**Primary textbook chapters:**

| Section | Title | Relevance |
|---|---|---|
| Ch2 §2.1 | What Cryptography Is and What It Promises | goals: confidentiality, integrity, auth |
| Ch2 §2.2 | Classical Ciphers and Why They Fall | Caesar, Vigenere, frequency analysis |
| Ch2 §2.3 | Perfect Secrecy and the One-Time Pad | why it works; why it is impractical |
| Ch2 §2.4 | Randomness: True, Pseudo, and Cryptographically Secure | `random` vs `secrets` in Python |
| Ch2 §2.5–2.6 | Symmetric Encryption: Stream and Block Ciphers; Modes | AES, ECB vs. CBC visual |
| Ch2 §2.7 | Cryptographic Hash Functions | SHA-256, MD5 weaknesses, SHA-1 |
| Ch2 §2.8–2.9 | MACs and Authenticated Encryption; Key Derivation | HMAC, PBKDF2, salting |
| Ch2 §2.10 | Public-Key Cryptography and RSA | modular arithmetic, key pair |
| Ch2 §2.13 | Digital Signatures, Certificates, and PKI | signing, verification, CA chain |
| Ch2 §2.14 | Putting It Together: The TLS Handshake | ties Day1 HTTP/HTTPS back in |

**Content gaps to fill:**

- Caesar cipher: currently shown as encryption but should also show frequency analysis to break it. Add a Python frequency analysis code cell that plots letter frequency (or just prints a sorted table) and automatically finds the key. Maps to Ch2 §2.2.
- Vigenere cipher: add the index of coincidence calculation for key-length detection. Show why repeating keys leak information.
- Hash functions: add collision resistance explanation with the birthday paradox. For SHA-256 (256-bit), the collision space is 2^128. For MD5 (128-bit), it is 2^64 — feasible. Show real MD5 collision example (the 2004 Wang attack produced two different files with the same hash).
- RSA numeric example from the textbook (Ch2 §2.10) — work through p=17, q=23, n=391, phi=352, e=3, d=235. Show encryption of m=5: c = 5^3 mod 391 = 125. Show decryption: 125^235 mod 391 = 5. This is already in the Python notebooks — integrate slide explanation directly.
- TLS handshake: add a 5-step visual diagram showing client hello, server hello, certificate, key exchange, and finished. Ties to Ch2 §2.14 and makes HTTPS concrete for students.
- Digital signatures: add a practical Python example using `hashlib` + a simulated sign/verify with RSA parameters. Show how a tampered message changes the hash and fails verification.

**Suggested new slides:**

1. Cryptography goals — confidentiality, integrity, authentication, non-repudiation  
2. Caesar cipher + frequency analysis attack in Python  
3. Vigenere cipher + key-length detection concept  
4. One-time pad — perfect secrecy and why it is impractical  
5. Randomness quality — `random` vs `secrets`; why the difference matters for keys  
6. AES block cipher — ECB penguin diagram (identical blocks → identical ciphertext)  
7. Hash functions — SHA-256 properties: one-way, deterministic, avalanche  
8. Birthday paradox — why MD5 is broken; numeric calculation  
9. RSA step-by-step: choose p and q, compute n, phi, e, d; encrypt/decrypt m=5  
10. Digital signatures — sign, transmit, verify; tamper detection demo  
11. TLS handshake — 5-step diagram  
12. Knowledge check (5 MCQ from Ch2 concepts)  

---

### Day 4 — Web Security and AI Security

**Current content:** SQL injection, prompt engineering, prompt injection, AI hallucinations, steganography.

**Primary textbook chapters:**

| Section | Title | Relevance |
|---|---|---|
| Ch10 §10.1 | How the Web Works: HTTP, Sessions, Same-Origin Policy | foundation |
| Ch10 §10.2 | The OWASP Top 10 | landmark vulnerability list |
| Ch10 §10.3–10.4 | Injection Attacks; SQL Injection in Depth | SQLi mechanics |
| Ch10 §10.5 | Cross-Site Scripting (XSS) | reflected, stored, DOM |
| Ch10 §10.6 | Broken Access Control, CSRF, SSRF | high-impact flaws |
| Ch10 §10.7 | Authentication and Session Management | cookie theft, session fixation |
| Ch4 §4.10–4.11 | Social Engineering in the Age of AI; Deepfakes, Voice Cloning | AI-enabled social eng. |
| Ch17 §17.2 | AI-Enabled Attacks and Defenses | adversarial ML, evasion |
| Ch17 §17.12 | Securing AI Systems: Agentic AI, Red Teaming, Model Supply Chain | prompt injection, RLHF poisoning |
| Ch6 §6.9 | Ethics and Professional Conduct | grounds the ethical hacking framing |

**Content gaps to fill:**

- OWASP Top 10 is the anchor for professional web security discourse. Summarize all 10 items in a quick-reference slide with one-line descriptions. Maps to Ch10 §10.2.
- XSS is completely missing from current content. Add reflected XSS with a simple `<script>alert(1)</script>` demo (explain why `alert(1)` is the classic proof-of-concept). Add stored XSS scenario: attacker posts malicious script in a forum comment. Maps to Ch10 §10.5.
- Session management: show how cookies work, what `HttpOnly` and `Secure` flags do, and what happens when they are absent. Add a session hijacking scenario. Maps to Ch10 §10.7.
- AI security content is strong on prompt injection but light on the threat model. Add: adversarial examples (an image that fools a classifier), data poisoning (training data manipulation), model inversion (recovering training data from model outputs). Maps to Ch17 §17.2.
- Add the AI security taxonomy from Ch17 §17.12: prompt injection vs. jailbreaking vs. model poisoning vs. supply chain attack on model weights. Each term needs a one-sentence definition and a real example.
- Steganography: integrate the CTF forensics framing — steganography is a CTF forensics technique, not just a creative tool. Show `exiftool` metadata reading concept and the LSB (least significant bit) technique in Python. Maps to Ch16 §16.2 (forensics).

**Suggested new slides:**

1. How HTTP requests and responses work — method, headers, body, status codes  
2. Same-origin policy — what it prevents and why  
3. OWASP Top 10 — one slide, 10 items, 10 one-liners  
4. SQL injection mechanics — the query, the injection, the fix (parameterized queries)  
5. SQL injection demo — `' OR 1=1 --` walkthrough  
6. XSS: reflected vs. stored — attack flow diagrams  
7. Session hijacking — cookie theft scenario; HttpOnly flag defense  
8. CSRF — cross-site request forgery scenario  
9. AI attack taxonomy — prompt injection, jailbreaking, data poisoning, model inversion  
10. Adversarial examples — image classifier fooling (conceptual, no code required)  
11. AI-powered phishing — deepfake voice cloning, spear-phishing at scale  
12. Lakera Gandalf walkthrough — what prompt injection is and why it works  
13. Knowledge check (5 MCQ from Ch10 and Ch17 concepts)  

---

### Day 5 — Capstone: CTF and OSINT

**Current content:** CTF mechanics, OSINT framework, careers.

**Primary textbook chapters:**

| Section | Title | Relevance |
|---|---|---|
| Ch16 §16.1 | What Is a CTF? | full mechanics |
| Ch16 §16.2 | Category Deep Dives | web, forensics, crypto, pwn, reversing |
| Ch16 §16.4 | CTF Platforms | picoCTF, TryHackMe, HTB, OverTheWire |
| Ch16 §16.5 | CTF Skills and Professional Mapping | each category → job role |
| Ch16 §16.9 | picoCTF, CyberPatriot, CCDC | accessible competitions |
| Ch7 §7.x | Recon (OSINT chapter) | passive recon, OSINT tools |
| Ch6 §6.1–6.5 | Penetration Testing Methodology, Phases | frames ethical hacking |
| App. C | Certification Mapping | Security+, CEH, path forward |

**Content gaps to fill:**

- CTF category table is in the textbook (Ch16 §16.1, Table 16.1). Add it verbatim (or adapted) to the slides: Web, Forensics, Cryptography, Pwn, Reversing, OSINT, Misc — with the skill tested and a beginner challenge example for each.
- OSINT methodology needs structure. Walk through a 5-step OSINT process: 1) define the target, 2) passive sources (Google dorks, Shodan, WHOIS), 3) social media search, 4) metadata analysis (`exiftool` on images), 5) compile and verify. Maps to Ch7 (recon).
- Google dorking: teach at least 4 operators — `site:`, `filetype:`, `inurl:`, `"exact phrase"`. These are safe to teach and widely used in recon.
- Career slide: the textbook Appendix C maps certifications. Add a clear progression: CompTIA Security+ → CEH → OSCP, with the approximate cost and experience level for each. This motivates students to continue beyond camp.
- CTF worked example from Ch16 §16.6: the Caesar cipher brute-force Python snippet is perfect for a live demo in the closing session. It encapsulates day 3 crypto + day 5 CTF in one.
- Add picoCTF walkthrough of one actual beginner challenge (e.g., the classic base64 decode challenge) to show the end-to-end experience. Maps to Ch16 §16.9.

**Suggested new slides:**

1. CTF category table — Web / Forensics / Crypto / Pwn / Rev / OSINT with example challenges  
2. Jeopardy vs. Attack-Defense vs. King-of-the-Hill formats  
3. OSINT 5-step methodology  
4. Google dorks — 4 operators with live-demo-safe examples  
5. Metadata analysis — exiftool concept; image metadata contains GPS coordinates  
6. Base64 decode CTF demo in Python (3 lines)  
7. Caesar brute-force CTF demo in Python (from Ch16 §16.6 worked example)  
8. XOR known-plaintext CTF demo in Python  
9. CTF skills → job role mapping table (from Ch16 §16.5)  
10. Certification roadmap — Security+, CEH, OSCP, college programs  
11. Capstone briefing structure — what each team presents on Day 5  
12. Knowledge check (5 MCQ from Ch16 concepts)  

---

## 2. Content Depth Summary — Gaps by Priority

| Gap | Affects | Effort | Maps to |
|---|---|---|---|
| Python primer (types, loops, functions, file I/O) | Day1 notebook + all days | Medium | Ch3 lab |
| Risk quantification: SLE/ARO/ALE worked example | Day2 slides | Low | Ch1 §1.8 |
| CIA/DAD/Parkerian Hexad | Day2 slides | Low | Ch1 §1.2 |
| Frequency analysis attack on Caesar cipher | Day3 slides + notebook | Low | Ch2 §2.2 |
| RSA step-by-step numeric example | Day3 slides + notebook | Low | Ch2 §2.10 |
| TLS handshake 5-step diagram | Day3 slides | Low | Ch2 §2.14 |
| OWASP Top 10 summary slide | Day4 slides | Low | Ch10 §10.2 |
| XSS (reflected and stored) | Day4 slides | Medium | Ch10 §10.5 |
| Session management and cookie flags | Day4 slides | Low | Ch10 §10.7 |
| AI attack taxonomy (prompt injection, poisoning) | Day4 slides | Medium | Ch17 §17.12 |
| Google dorks and OSINT methodology | Day5 slides | Low | Ch7 |
| CTF category table with beginner examples | Day5 slides | Low | Ch16 §16.2 |
| Certification roadmap | Day5 slides | Low | App. C |
| LSB steganography in Python | Day4 notebook | Medium | Ch16 §16.2 |

---

## 3. GitHub Pages + camp.com.puter.tips Setup

### Why this is a good idea

Your textbook is already live at `book.com.puter.tips` via GitHub Pages and a CNAME file in the repo root. The exact same pattern works for the camp: add a `CNAME` file to `cyberquest-camp` and point a DNS record at GitHub Pages. Students and instructors then access the slides at a memorable URL without needing to download anything.

### Step-by-step setup

**Step 1 — Enable GitHub Pages on the camp repo**

In the `cyberquest-camp` repo, go to Settings → Pages. Under Source, select Deploy from branch → `main` → `/ (root)`. Click Save. GitHub will serve the repo at `devharsh.github.io/cyberquest-camp` until you add the custom domain.

**Step 2 — Add the CNAME file to the repo**

Create a file named `CNAME` (no extension) in the root of the `cyberquest-camp` repo containing exactly one line:

```
camp.com.puter.tips
```

Push this to `main`. GitHub Pages reads this file and enforces the custom domain.

**Step 3 — Add a DNS record at your registrar**

At whatever DNS provider controls `com.puter.tips`, add:

```
Type:  CNAME
Name:  camp
Value: devharsh.github.io
TTL:   3600
```

(Some providers use `@` for the apex domain. `camp` here is the subdomain label.)

**Step 4 — Enforce HTTPS**

After DNS propagates (usually 5–30 minutes), GitHub will issue a Let's Encrypt certificate. In Settings → Pages, check "Enforce HTTPS". After this, `http://camp.com.puter.tips` redirects to `https://camp.com.puter.tips`.

**Step 5 — Make the root URL serve the main slide deck**

Currently the repo has `Interactive_Slides.html` at the root. GitHub Pages serves `index.html` by default. Either rename `Interactive_Slides.html` to `index.html`, or add an `index.html` that redirects:

```html
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="0; url=Interactive_Slides.html">
</head>
<body>
<a href="Interactive_Slides.html">Click here to open the slides.</a>
</body>
</html>
```

Then `https://camp.com.puter.tips` loads the full deck immediately, and `https://camp.com.puter.tips/Day1/Day1_slides.html` etc. work as deep links from the day menu.

### Cross-linking with the textbook

Each day's slides can add a "Read more" footer pointing to the relevant textbook chapter at `book.com.puter.tips`. For example, Day 3 slides can link:

```
Further reading: book.com.puter.tips/chapters/02_cryptography/chapter02.html
```

This is a clean, free alternative to a proprietary LMS and puts your own open educational resource directly in front of students.

---

## 4. Recommended File Changes in the Repo

| File | Change |
|---|---|
| `CNAME` | Create with content `camp.com.puter.tips` |
| `index.html` | Create redirect to `Interactive_Slides.html`, or rename the slides file |
| `Day1/Day1_slides.html` | Add 9 new slides (Python primer, OSI, Linux filesystem, subnetting) |
| `Day1/Day1.ipynb` | Add Python primer exercises (loops, functions, file I/O) |
| `Day2/Day2_slides.html` | Add CIA/DAD/Parkerian, threat actors, ALE calculation, password entropy |
| `Day2/Day2.ipynb` | Add brute-force time estimate calculation in Python |
| `Day3/Day3_slides.html` | Add frequency analysis, RSA walkthrough, TLS handshake diagram |
| `Day3/Day3.ipynb` | Frequency analysis code, RSA p=17 q=23 numeric example |
| `Day4/Day4_slides.html` | Add OWASP Top 10, XSS, session management, AI taxonomy |
| `Day4/Day4.ipynb` | Add LSB steganography demo, XOR CTF challenge |
| `Day5/Day5_slides.html` | Add CTF category table, OSINT methodology, Google dorks, cert roadmap |
| `Day5/Day5.ipynb` | Add Caesar brute-force, base64 decode, XOR known-plaintext CTF demos |
| `README.md` | Add "Textbook" section linking to book.com.puter.tips with per-day chapter refs |

---

## 5. README Textbook Section (paste-ready)

```markdown
## Companion textbook

The slides reference *Cybersecurity: Theory, Practice, and Ethics* by Devharsh Trivedi, Ph.D., CISSP.  
The textbook is free and open-source, published at [book.com.puter.tips](https://book.com.puter.tips).

| Day | Topic | Textbook chapters |
|---|---|---|
| 1 | Python and Linux CLI | Ch 3 §3.1–3.6 (Networking) |
| 2 | Security foundations | Ch 1 §1.1–1.8 (Intro), Ch 4 §4.1–4.6 (Social Eng.), Ch 5 §5.1–5.6 (Risk) |
| 3 | Cryptography | Ch 2 §2.1–2.14 (Cryptography) |
| 4 | Web and AI security | Ch 10 §10.1–10.7 (Web), Ch 17 §17.2, 17.12 (Emerging/AI) |
| 5 | CTF and OSINT | Ch 16 (CTF), Ch 7 (Recon/OSINT), App. C (Certifications) |
```

---

*Document prepared 2026-06-09. Author: Devharsh Trivedi, Bowie State University.*
