import re, sys, json, os as _os

# ---------------------------------------------------------------------------
# Module-level figure / table counters  (reset via reset_counters())
# ---------------------------------------------------------------------------
_fig_counter = [0]
_tab_counter = [0]

_CAPTIONS_FILE = ('/sessions/optimistic-dazzling-cerf/mnt/Cybersecurity'
                  '/Bowie/cyberquest-camp/book/figs/captions.json')
try:
    with open(_CAPTIONS_FILE) as _f:
        _FIG_CAPTIONS = {int(k): v for k, v in json.load(_f).items()}
except (FileNotFoundError, Exception):
    _FIG_CAPTIONS = {}

_FIGS_DIR = ('/sessions/optimistic-dazzling-cerf/mnt/Cybersecurity'
             '/Bowie/cyberquest-camp/book/figs')

def reset_counters():
    """Call once before starting a new build to reset figure/table numbering."""
    _fig_counter[0] = 0
    _tab_counter[0] = 0

# ---------------------------------------------------------------------------
# Basic helpers
# ---------------------------------------------------------------------------

def esc(s):
    """Escape LaTeX special characters in plain text."""
    return (s.replace('\\', r'\textbackslash{}')
             .replace('#', r'\#').replace('$', r'\$').replace('%', r'\%')
             .replace('&', r'\&').replace('_', r'\_').replace('^', r'\^{}')
             .replace('{', r'\{').replace('}', r'\}')
             .replace('<', r'\textless{}').replace('>', r'\textgreater{}')
             # Unicode chars that must map to ASCII for T1/lmodern
             .replace('✓', r'\checkmark{}')      # checkmark
             .replace('✗', r'$\times$')          # ballot x
             .replace('≡', r'$\equiv$')          # triple bar
             .replace('≈', r'$\approx$')         # almost equal
             .replace('≤', r'$\leq$')            # less or equal
             .replace('≥', r'$\geq$')            # greater or equal
             .replace('≠', r'$\neq$')            # not equal
             .replace('→', r'$\rightarrow$')     # right arrow
             .replace('←', r'$\leftarrow$')      # left arrow
             .replace('×', r'$\times$')          # multiplication sign
             .replace('•', r'\textbullet{}')     # bullet
             .replace('’', r"'")                 # right single quote
             .replace('‘', r"'")                 # left single quote
             .replace('“', r"``")                # left double quote
             .replace('”', r"''")                # right double quote
             .replace('–', '--')                 # en dash
             .replace('—', '---'))               # em dash

def strip_tags(html):
    return re.sub(r'<(?:[a-zA-Z/!?][^>]*|)>', '', html)

def unescape(s):
    return (s.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
             .replace('&nbsp;', ' ').replace('&#39;', "'").replace('&quot;', '"')
             .replace('&mdash;', '---').replace('&ndash;', '--'))

def clean_js(html):
    # JS template literal: \$ is a literal dollar (not a template placeholder start)
    html = html.replace('\\$', '$')
    # Stray backslash before an HTML tag (e.g. \<span> used as prefix in slide sources)
    html = re.sub(r'\\(</?[a-zA-Z])', r'\1', html)
    # Remove ${...} template expressions (8 passes handles nesting up to depth 8)
    for _ in range(8):
        html = re.sub(r'\$\{[^{}]*\}', '', html)
    # Remove lines that are just JS punctuation
    html = re.sub(r'(?m)^[ \t]*[\'\")(}{]+[ \t]*$', '', html)
    return html

# ---------------------------------------------------------------------------
# Pre-escaper: apply esc(unescape()) to text nodes only, leaving tags intact
# ---------------------------------------------------------------------------

def _esc_text_nodes(html):
    """Escape LaTeX special chars in all text nodes (between HTML tags)."""
    result = []
    pos = 0
    for m in re.finditer(r'<(?:[a-zA-Z/!?][^>]*|)>', html):
        if m.start() > pos:
            result.append(esc(unescape(html[pos:m.start()])))
        result.append(m.group(0))   # tag kept verbatim
        pos = m.end()
    if pos < len(html):
        result.append(esc(unescape(html[pos:])))
    return ''.join(result)

# ---------------------------------------------------------------------------
# Post-processor: convert escaped exponents to readable superscripts
# ---------------------------------------------------------------------------

def _fix_exponents(tex):
    """Convert X\^\{\}Y -> X\textsuperscript{Y} for alphanumeric X and Y.

    esc() converts '^' to r'\^{}', but then the sequential replacements also
    escape the '{' and '}', producing '\^\{\}' in the output.  We convert any
    alphanumeric-caret-alphanumeric sequence (digits or letters) to a proper
    text superscript.  This covers both digit exponents (26^5, 2^256) and RSA
    variable exponents (m^e, c^d, n^e).

    Pattern matches: backslash + caret + backslash + { + backslash + }
    between two runs of alphanumeric characters.
    """
    return re.sub(r'([a-zA-Z0-9]+)\\\^\\\{\\\}([a-zA-Z0-9]+)',
                  r'\1\\textsuperscript{\2}', tex)

# ---------------------------------------------------------------------------
# Main converter
# ---------------------------------------------------------------------------

def html_to_tex(html):
    if not html or not html.strip():
        return ''
    html = clean_js(html)

    html = re.sub(r'<div[^>]*class=["\']feedback[^>]*>.*?</div>', '', html, flags=re.DOTALL)

    # ── Placeholder pools ────────────────────────────────────────────────────
    # Items saved here bypass _esc_text_nodes entirely.
    # CRITICAL: SVG replacement must go into latex_blocks BEFORE _esc_text_nodes
    # so the LaTeX commands in the replacement string are not double-escaped.

    latex_blocks = []   # pre-formed LaTeX snippets (SVG, etc.)
    code_blocks  = []   # verbatim code listings

    def save_latex(content):
        """Return a placeholder token for a pre-formed LaTeX string."""
        ph = 'LATEXBLOCK{}ENDLATEX'.format(len(latex_blocks))
        latex_blocks.append(content)
        return ph

    # ── Box-drawing character map (for lstlisting) ───────────────────────────
    BOX_ASCII = str.maketrans({
        '─': '-',  '━': '-',  '│': '|',  '┃': '|',
        '┌': '+',  '┐': '+',  '└': '+',  '┘': '+',
        '├': '|',  '┤': '|',  '┬': '+',  '┴': '+',
        '┼': '+',  '═': '-',  '║': '|',  '╠': '+',
        '╣': '+',  '╦': '+',  '╩': '+',  '╬': '+',
        '╴': '-',  '╵': '|',  '╶': '-',  '╷': '|',
        '╸': '-',  '╹': '|',  '╺': '-',  '╻': '|',
    })

    def save_code(m):
        raw = unescape(m.group(1) if m.lastindex else m.group(0))
        raw = raw.translate(BOX_ASCII)
        ph = 'CODEBLOCK{}ENDCODE'.format(len(code_blocks))
        code_blocks.append(raw)
        return ph

    # ── Replace SVG with a figure environment BEFORE _esc_text_nodes ─────────
    # Each SVG maps to a pre-generated PDF in figs/.  The module-level counter
    # increments in the same order as make_figs.py traversed the slides.
    def _svg_to_figure(_m):
        _fig_counter[0] += 1
        n   = _fig_counter[0]
        pdf = f'{_FIGS_DIR}/fig{n:03d}.pdf'
        cap = esc(_FIG_CAPTIONS.get(n, f'Figure {n}'))
        if not _os.path.exists(pdf):
            # Fallback: text placeholder if PDF missing
            return save_latex(
                '\n' + r'\begin{center}\small\textit{[Diagram ' + str(n) +
                r' --- view at \mbox{\url{https://camp.com.puter.tips}}]}\end{center}' + '\n'
            )
        return save_latex(
            f'\n\\begin{{figure}}[H]\n'
            f'\\centering\n'
            f'\\includegraphics[width=0.88\\linewidth]{{{pdf}}}\n'
            f'\\caption{{{cap}}}\n'
            f'\\label{{fig:{n:03d}}}\n'
            f'\\end{{figure}}\n'
        )
    html = re.sub(r'<svg[^>]*>.*?</svg>', _svg_to_figure, html, flags=re.DOTALL)

    # ── MCQ: convert knowledge-check buttons into a formatted answer list ─────
    # Must run after save_latex is defined so the LaTeX output is protected from
    # _esc_text_nodes.  Correct answer = onclick contains choose(this,true,...).
    def _convert_mcq_block(m):
        block = m.group(0)
        buttons = re.findall(
            r'<button[^>]*onclick=["\']choose\(this,(true|false),\'([^\']*)\'[^>]*>(.*?)</button>',
            block, re.DOTALL)
        if not buttons:
            return ''
        lines = []
        labels = ['A', 'B', 'C', 'D', 'E']
        correct_explanation = ''
        for i, (correct, explanation, text) in enumerate(buttons):
            label = labels[i] if i < len(labels) else str(i + 1)
            text_clean = strip_tags(text).strip()
            if correct == 'true':
                lines.append(
                    r'\item[\textbf{' + label + r'.}] \textbf{' +
                    esc(text_clean) + r'} $\checkmark$')
                correct_explanation = strip_tags(explanation).strip()
            else:
                lines.append(r'\item[' + label + r'.] ' + esc(text_clean))
        result = ('\n\\begin{itemize}[leftmargin=2em,label={}]\n' +
                  '\n'.join(lines) + '\n\\end{itemize}\n')
        if correct_explanation:
            result += (r'{\small\itshape\color{gray}' +
                       esc(correct_explanation) + '}\n\n')
        return save_latex(result)

    html = re.sub(
        r'(?:<button[^>]*class=["\']opt["\'][^>]*>.*?</button>\s*)+',
        _convert_mcq_block, html, flags=re.DOTALL)

    # ── Save code blocks BEFORE _esc_text_nodes ──────────────────────────────
    html = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', save_code, html, flags=re.DOTALL)
    html = re.sub(r'<pre[^>]*>(.*?)</pre>',                  save_code, html, flags=re.DOTALL)

    # ── PRE-ESCAPE: all remaining text nodes are now LaTeX-safe ──────────────
    html = _esc_text_nodes(html)

    # ── Restore SVG (and any other pre-formed LaTeX) placeholder content ──────
    # These tokens are not inside any HTML tag so _esc_text_nodes left them alone.
    for idx, block in enumerate(latex_blocks):
        html = html.replace('LATEXBLOCK{}ENDLATEX'.format(idx), block)

    # From here: all text is pre-escaped; handlers just use strip_tags() on cell
    # content which is already safe.

    # ── Inline code — content pre-escaped, just wrap ─────────────────────────
    html = re.sub(r'<code>(.*?)</code>',
        lambda m: r'\texttt{' + strip_tags(m.group(1)) + '}',
        html, flags=re.DOTALL)

    # ── Headings ─────────────────────────────────────────────────────────────
    def _sec(cmd):
        return lambda m: '\n' + cmd + '{' + strip_tags(m.group(1)) + '}\n'
    html = re.sub(r'<h1[^>]*>(.*?)</h1>', _sec(r'\section*'),       html, flags=re.DOTALL)
    html = re.sub(r'<h2[^>]*>(.*?)</h2>', _sec(r'\subsection*'),    html, flags=re.DOTALL)
    html = re.sub(r'<h3[^>]*>(.*?)</h3>', _sec(r'\subsubsection*'), html, flags=re.DOTALL)

    # ── Strip slide-navigation-only muted paragraphs (PDF-irrelevant) ────────
    # e.g. "This part is 4 slides. Press Next to begin."
    #      "6 parts. Press Next to move in order."
    html = re.sub(
        r"<p[^>]*class=['\"]muted['\"][^>]*>[^<]*Press Next[^<]*</p>",
        '', html, flags=re.DOTALL | re.IGNORECASE)

    # ── Strip keyword chip/pill divs (PDF-irrelevant UI decorations) ──────────
    # e.g. <div class="chips"><span class="pill">Encoding</span>...</div>
    # These produce stray lines like "Encoding Caesar Hashing RSA CyberChef"
    html = re.sub(r'<div[^>]*class=["\']chips["\'][^>]*>.*?</div>', '', html,
                  flags=re.DOTALL | re.IGNORECASE)

    # ── Special paragraph classes ─────────────────────────────────────────────
    html = re.sub(r"<p[^>]*class=['\"]partbadge['\"][^>]*>(.*?)</p>",
        lambda m: '\n' + r'\vspace{4pt}\noindent\textsc{' + strip_tags(m.group(1)) + '}\n\n',
        html, flags=re.DOTALL)
    html = re.sub(r'<p[^>]*class=["\']muted["\'][^>]*>(.*?)</p>',
        lambda m: r'{\small\itshape\color{gray}' + strip_tags(m.group(1)) + '}\n\n',
        html, flags=re.DOTALL)

    # ── Inline formatting ────────────────────────────────────────────────────
    html = re.sub(r'<(?:strong|b)>(.*?)</(?:strong|b)>',
        lambda m: r'\textbf{' + strip_tags(m.group(1)) + '}', html, flags=re.DOTALL)
    html = re.sub(r'<(?:em|i)>(.*?)</(?:em|i)>',
        lambda m: r'\textit{' + strip_tags(m.group(1)) + '}', html, flags=re.DOTALL)
    # Superscripts and subscripts (e.g. 26<sup>5</sup> in keyspace formulas)
    html = re.sub(r'<sup[^>]*>(.*?)</sup>',
        lambda m: r'\textsuperscript{' + strip_tags(m.group(1)) + '}', html, flags=re.DOTALL)
    html = re.sub(r'<sub[^>]*>(.*?)</sub>',
        lambda m: r'\textsubscript{' + strip_tags(m.group(1)) + '}', html, flags=re.DOTALL)

    # ── Tables ───────────────────────────────────────────────────────────────
    def convert_table(m):
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', m.group(1), re.DOTALL)
        if not rows:
            return ''
        tex_rows, ncols, header_cap = [], 0, ''
        for i, row in enumerate(rows):
            cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, re.DOTALL)
            ct = [strip_tags(c).strip() for c in cells]
            if not ct:
                continue
            if i == 0:
                ncols = len(ct)
                # Use first 3 header columns joined as the caption
                header_cap = ', '.join(ct[:3])
                tex_rows.append(r'\textbf{' + r'} & \textbf{'.join(ct) + r'} \\ \midrule')
            else:
                tex_rows.append(' & '.join(ct) + r' \\')
        if not ncols:
            return ''
        w = str(round(14.5 / ncols, 1))
        spec = ('p{' + w + 'cm}') * ncols
        _tab_counter[0] += 1
        tn = _tab_counter[0]
        return ('\n\\begin{table}[H]\n'
                '\\centering\\small\n'
                '\\begin{tabular}{' + spec + '}\\toprule\n'
                + '\n'.join(tex_rows) + '\n'
                + '\\bottomrule\\end{tabular}\n'
                + '\\caption{' + header_cap + '}\n'
                + '\\label{tab:' + f'{tn:03d}' + '}\n'
                + '\\end{table}\n')
    html = re.sub(r'<table[^>]*>(.*?)</table>', convert_table, html, flags=re.DOTALL)

    # ── Lists ────────────────────────────────────────────────────────────────
    def cvt_list(tag, env, h):
        def _outer(m):
            items = re.sub(r'<li[^>]*>(.*?)</li>',
                lambda x: '  ' + r'\item ' + strip_tags(x.group(1)).strip() + '\n',
                m.group(1), flags=re.DOTALL)
            return '\n' + r'\begin{' + env + '}\n' + items + r'\end{' + env + '}' + '\n'
        return re.sub(r'<' + tag + r'[^>]*>(.*?)</' + tag + r'>', _outer, h, flags=re.DOTALL)
    html = cvt_list('ul', 'itemize', html)
    html = cvt_list('ol', 'enumerate', html)

    # ── HR ───────────────────────────────────────────────────────────────────
    HR = '\n' + r'\medskip\noindent\rule{\linewidth}{0.4pt}\medskip' + '\n'
    html = re.sub(r'<hr\s*/?>', lambda _: HR, html)

    # ── Strip remaining block wrappers ────────────────────────────────────────
    html = re.sub(r'<p[^>]*>(.*?)</p>',    lambda m: '\n' + m.group(1) + '\n', html, flags=re.DOTALL)
    html = re.sub(r'<div[^>]*>(.*?)</div>', lambda m: '\n' + m.group(1) + '\n', html, flags=re.DOTALL)
    # Add space between adjacent spans to prevent text fusion (e.g. "AttackersDay")
    html = re.sub(r'</span>\s*<span', '</span> <span', html)
    html = re.sub(r'<span[^>]*>(.*?)</span>', lambda m: m.group(1),             html, flags=re.DOTALL)
    html = re.sub(r'<(?:[a-zA-Z/!?][^>]*|)>', '', html)

    # ── Restore code blocks ───────────────────────────────────────────────────
    for idx, code in enumerate(code_blocks):
        html = html.replace('CODEBLOCK{}ENDCODE'.format(idx),
            '\n' + r'\begin{lstlisting}' + '\n' + code + r'\end{lstlisting}' + '\n')

    # ── Post-process: digit exponents -> \textsuperscript ────────────────────
    html = _fix_exponents(html)

    html = re.sub(r'\n{4,}', '\n\n', html)
    return html.strip()

# ---------------------------------------------------------------------------
# JS slide object extraction helpers
# ---------------------------------------------------------------------------

def get_prop(js_obj, key):
    pattern = re.compile(r'\b' + re.escape(key) + r'\s*:\s*`')
    m = pattern.search(js_obj)
    if not m:
        return None
    start = m.end()
    i, depth = start, 0
    while i < len(js_obj):
        ch = js_obj[i]
        if ch == '\\':
            i += 2
            continue
        if ch == '$' and i + 1 < len(js_obj) and js_obj[i + 1] == '{':
            depth += 1
            i += 2
            continue
        if ch == '}' and depth > 0:
            depth -= 1
            i += 1
            continue
        if ch == '`' and depth == 0:
            return js_obj[start:i]
        i += 1
    return None

def extract_s_calls(js):
    calls = []
    i = 0
    while i < len(js):
        idx = js.find('S({', i)
        if idx == -1:
            break
        brace_depth, backtick, j = 0, False, idx + 2
        while j < len(js):
            ch = js[j]
            if ch == '\\' and backtick:
                j += 2
                continue
            if ch == '`':
                backtick = not backtick
            if not backtick:
                if ch == '{':
                    brace_depth += 1
                elif ch == '}':
                    brace_depth -= 1
                    if brace_depth == 0:
                        calls.append(js[idx + 2:j + 1])
                        i = j + 1
                        break
            j += 1
        else:
            break
    return calls
