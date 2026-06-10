import re, sys
sys.path.insert(0, '/sessions/optimistic-dazzling-cerf/mnt/outputs/cyberquest-pdf')
from extract import html_to_tex, extract_s_calls, get_prop, esc, strip_tags

# ── Paths ──────────────────────────────────────────────────────────────────
BASE = '/sessions/optimistic-dazzling-cerf/mnt/Cybersecurity'
MAIN = '/sessions/optimistic-dazzling-cerf/mnt/Cybersecurity/Interactive_Slides.html'

DAY_TITLES = {
    1: ("Python and the Linux Terminal",
        "Day 1 equips students with the foundational technical skills needed throughout the week: "
        "basic Python programming (variables, loops, functions, file I/O), navigation of the Linux "
        "command line, the OSI seven-layer model, IPv4 addressing, and URL anatomy."),
    2: ("Threats, Risk, and the CIA Triad",
        "Day 2 covers the strategic side of security: the CIA and DAD triads, the Parkerian Hexad, "
        "threat actor taxonomy (script kiddies through nation-state APTs), quantitative risk analysis "
        "using ALE, password entropy, and the legal framework of the Computer Fraud and Abuse Act."),
    3: ("Cryptography and TLS",
        "Day 3 explores how mathematics protects information: classical ciphers and frequency analysis, "
        "the one-time pad, AES block cipher modes (ECB vs CBC), hash functions and the birthday paradox, "
        "RSA public-key cryptography worked numerically, digital signatures, and the TLS handshake."),
    4: ("Web Security and AI Attacks",
        "Day 4 examines how web applications are attacked and defended: raw HTTP, the OWASP Top 10, "
        "SQL injection, cross-site scripting, session hijacking, CSRF, and emerging AI attack vectors "
        "including prompt injection, data poisoning, and deepfake social engineering."),
    5: ("CTF Competitions and Career Roadmap",
        "Day 5 ties the week together with Capture the Flag competitions: CTF category taxonomy, "
        "OSINT methodology, Google dorks, EXIF metadata analysis, cryptographic CTF demos, "
        "and a certification and career roadmap mapping skills to professional roles."),
}

# ── Read main deck ─────────────────────────────────────────────────────────
try:
    with open(MAIN) as f:
        main_content = f.read()
    main_script = re.search(r'<script[^>]*>(.*?)</script>', main_content, re.DOTALL).group(1)
    main_slides = extract_s_calls(main_script)
    print(f"Main deck: {len(main_slides)} slides", file=sys.stderr)
except Exception as e:
    print(f"Could not read main deck: {e}", file=sys.stderr)
    main_slides = []

# ── Read day decks ─────────────────────────────────────────────────────────
day_slides = {}
for day in [1,2,3,4,5]:
    path = f'{BASE}/Day{day}_slides.html'
    try:
        with open(path) as f:
            c = f.read()
    except FileNotFoundError:
        path = f'/sessions/optimistic-dazzling-cerf/mnt/Users/devharsh/Documents/cyberquest-camp/Day{day}/Day{day}_slides.html'
        with open(path) as f:
            c = f.read()
    chunks = []
    for m in re.finditer(r"<div class='slide'>(.*?)(?=<div class='slide'>|</div>\s*<div class=\"progress\">|$)", c, re.DOTALL):
        inner = m.group(1).strip()
        text = re.sub(r'<[^>]+>','', inner).strip()
        if len(text) > 4:
            chunks.append(inner)
    day_slides[day] = chunks
    print(f"Day {day}: {len(chunks)} slides", file=sys.stderr)

# ── Main deck → chapter sections ──────────────────────────────────────────
def main_deck_section(section_name, slides):
    lines = []
    for obj in slides:
        sec_m = re.search(r"sec\s*:\s*['\"]([^'\"]+)['\"]", obj)
        if not sec_m or sec_m.group(1) != section_name:
            continue
        html = get_prop(obj, 'html')
        title = get_prop(obj, 'title') or get_prop(obj, 'kick') or ''
        slide_type = get_prop(obj, 't') or ''

        if slide_type in ('cover', 'divider', 'toc'):
            tex = html_to_tex(html)
            if tex:
                lines.append(tex + '\n')
        else:
            if title:
                lines.append('\\subsubsection*{' + esc(strip_tags(title)) + '}\n')
            tex = html_to_tex(html)
            if tex:
                lines.append(tex + '\n')
        lines.append('\n')
    return '\n'.join(lines)

# ── Day deck → section ────────────────────────────────────────────────────
def day_deck_section(chunks):
    lines = []
    for chunk in chunks:
        tex = html_to_tex(chunk)
        if tex.strip():
            lines.append(tex)
            lines.append('\n\\medskip\n')
    return '\n'.join(lines)

# ── Assemble LaTeX ─────────────────────────────────────────────────────────
PREAMBLE = r"""\documentclass[12pt,openany]{book}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in,top=1.1in,bottom=1.1in]{geometry}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage{amssymb}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{array}
\usepackage{longtable}
\usepackage{listings}
\usepackage{enumitem}
\usepackage{parskip}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{hyperref}
\usepackage{url}
\usepackage{graphicx}
\usepackage{tcolorbox}
\usepackage{setspace}
\usepackage{accsupp}

\setlength{\headheight}{14.5pt}

\definecolor{accent}{HTML}{2563EB}
\definecolor{accent2}{HTML}{7C3AED}
\definecolor{codebg}{HTML}{F1F5FF}
\definecolor{gray}{HTML}{5A6B8C}

\hypersetup{
  unicode=true, colorlinks=true, linkcolor=accent, urlcolor=accent, citecolor=accent2,
  pdfcreator={pdfLaTeX}, pdfproducer={TeX Live 2022},
  pdfdisplaydoctitle=true,
  pdflang={en-US}, pdftitle={CyberQuest Summer Camp 2026},
  pdfauthor={Devharsh Trivedi},
  pdfsubject={Cybersecurity Education},
  pdfkeywords={cybersecurity, CTF, cryptography, web security, AI security, Python}
}

\lstset{
  basicstyle=\ttfamily\small,
  backgroundcolor=\color{codebg},
  frame=single, framerule=0.4pt, rulecolor=\color{accent!40},
  breaklines=true, breakatwhitespace=true,
  keepspaces=true, columns=flexible,
  showstringspaces=false,
  xleftmargin=6pt, xrightmargin=6pt,
  aboveskip=8pt, belowskip=8pt
}

\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\color{accent}}
  {\chaptertitlename\ \thechapter}{18pt}{\Huge}
\titleformat{\section}{\normalfont\Large\bfseries\color{accent2}}{}{0pt}{}
\titleformat{\subsection}{\normalfont\large\bfseries\color{accent}}{}{0pt}{}
\titleformat{\subsubsection}{\normalfont\normalsize\bfseries}{}{0pt}{}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\textit{\leftmark}}
\fancyhead[LO]{\textit{\rightmark}}
\renewcommand{\headrulewidth}{0.4pt}

\setlist[itemize]{noitemsep, topsep=4pt}
\setlist[enumerate]{noitemsep, topsep=4pt}
\onehalfspacing
"""

TITLE_PAGE = r"""
\begin{titlepage}
\centering
\vspace*{2cm}
{\large\textsc{Bowie State University --- Department of Computer Science}\par}
\vspace{1.5cm}
{\Huge\bfseries\color{accent} CyberQuest Summer Camp\par}
\vspace{0.5cm}
{\LARGE\color{accent2} 2026 Curriculum Book\par}
\vspace{0.8cm}
\noindent\rule{0.6\linewidth}{1.2pt}\par
\vspace{0.8cm}
{\large A five-day cybersecurity course for middle and high school students.\par
Learn how attacks work, how to stop them, basic Python, ethical hacking,\par
and the new world of AI security --- all hands-on.\par}
\vspace{1.5cm}
{\large\textbf{Devharsh Trivedi, Ph.D., CISSP}\par}
{\normalsize Department of Computer Science, Bowie State University\par
Computer Science Building, Room 221\par
Washington D.C., 20003\par
\texttt{devharsh.1592@gmail.com}\par}
\vspace{1.5cm}
{\normalsize\color{gray}
Interactive version: \url{https://camp.com.puter.tips}\par
Source: \url{https://github.com/devharsh/cyberquest-camp}\par}
\vspace{2cm}
{\normalsize\today\par}
\end{titlepage}
"""

DEDICATION = r"""
\frontmatter
\chapter*{Preface}
\addcontentsline{toc}{chapter}{Preface}
This curriculum book is the companion document to the CyberQuest Summer Camp interactive
slide decks, available at \url{https://camp.com.puter.tips}. It is structured in two parts:

\textbf{Part~I} reproduces the main course deck (\textit{Interactive Slides}), which is the
primary teaching vehicle presented to students during each day's opening session.
Each of its six chapters corresponds to a thematic section of the week.

\textbf{Part~II} contains the five daily companion decks. These slides are used during
teaching sessions, labs, and review periods. They expand on the main deck with worked
examples, Python code, mathematical derivations, and knowledge checks drawn from
\textit{Introduction to Cybersecurity} (Trivedi), cited by chapter and section throughout.

All diagrams marked \textit{[Interactive diagram]} are rendered in the browser;
the interactive versions can be accessed at the URL above.

\vspace{1em}
\noindent\textbf{License.} This work is released under CC~BY~4.0. You may reproduce,
adapt, and redistribute it with attribution.

\vspace{1em}
\noindent\textbf{Citation.} See the \texttt{CITATION.cff} file in the repository or
the Zenodo record for the preferred citation format.
"""

def build():
    out = [PREAMBLE, r'\begin{document}', TITLE_PAGE, DEDICATION, r'\tableofcontents', r'\mainmatter']

    # PART I — Main Deck
    out.append(r'\part{Main Course Deck}')
    out.append(r'\chapter{Welcome and Course Overview}')
    out.append(main_deck_section('Welcome', main_slides))

    for day in [1,2,3,4,5]:
        title, _ = DAY_TITLES[day]
        out.append(f'\\chapter{{Day {day}: {esc(title)}}}')
        out.append(main_deck_section(f'Day {day}', main_slides))

    # PART II — Daily Companion Decks
    out.append(r'\part{Daily Companion Decks}')
    for day in [1,2,3,4,5]:
        title, intro = DAY_TITLES[day]
        out.append(f'\\chapter{{Day {day} Companion: {esc(title)}}}')
        out.append(esc(intro) + '\n')
        out.append(day_deck_section(day_slides[day]))

    out.append(r'\end{document}')
    return '\n'.join(out)

tex = build()
with open('/sessions/optimistic-dazzling-cerf/mnt/outputs/cyberquest-pdf/main.tex', 'w') as f:
    f.write(tex)
print(f"Wrote main.tex ({len(tex)} bytes, ~{len(tex.split(chr(10)))} lines)", file=sys.stderr)
