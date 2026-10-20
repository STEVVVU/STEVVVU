from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    'dark': {'bg': '#0b1214', 'panel': '#101d20', 'line': '#284247', 'text': '#eff8f3', 'muted': '#b2c8c4', 'accent': '#a8f0c6', 'warm': '#ffbc80', 'blue': '#88cce8'},
    'light': {'bg': '#f2f7f4', 'panel': '#e8f0eb', 'line': '#b4cbc0', 'text': '#152f29', 'muted': '#42675b', 'accent': '#207956', 'warm': '#a44c17', 'blue': '#226c8e'},
}
PROJECTS = [
    {'slug': 'stratadb', 'title': 'StrataDB', 'category': '01 / STORAGE', 'stack': 'RUST', 'lines': ['Crash-safe storage.', 'WAL, snapshots, compaction.'], 'detail': 'Checksummed WAL, atomic batches, snapshots, and crash recovery.', 'diagram': 'storage'},
    {'slug': 'edgeproxy', 'title': 'EdgeProxy', 'category': '02 / NETWORKING', 'stack': 'RUST', 'lines': ['HTTP/1.1 routing.', 'Health checks and circuit breakers.'], 'detail': 'HTTP/1.1 proxy with bounded concurrency, health checks, circuit breakers, and phase-aware retries.', 'diagram': 'network'},
    {'slug': 'durableflow', 'title': 'DurableFlow', 'category': '03 / DISTRIBUTED WORK', 'stack': 'PYTHON', 'lines': ['Durable jobs and fenced leases.', 'Retries and worker recovery.'], 'detail': 'Durable job queue with fenced leases, retries, and recovery tests.', 'diagram': 'queue'},
    {'slug': 'warpforge-mlir', 'title': 'WarpForge', 'category': '04 / COMPILERS', 'stack': 'C++ / MLIR', 'lines': ['Graph fusion and vectorization.', 'LLVM / MLIR compiler passes.'], 'detail': 'LLVM/MLIR optimization with graph fusion, tiling, vectorization, and progressive lowering.', 'diagram': 'compiler'},
    {'slug': 'chainindex', 'title': 'ChainIndex', 'category': '05 / EVENT SYSTEMS', 'stack': 'TYPESCRIPT / SOLIDITY', 'lines': ['Reorg-aware event indexing.', 'Solidity escrow and deterministic tests.'], 'detail': 'Reorg-aware EVM event indexing with a Solidity escrow contract and deterministic tests.', 'diagram': 'chain'},
    {'slug': 'lumenforge-webgl', 'title': 'LumenForge', 'category': '06 / GRAPHICS', 'stack': 'TYPESCRIPT / WEBGL2', 'lines': ['Deferred PBR rendering.', 'glTF inspection and frame diagnostics.'], 'detail': 'glTF inspection, deferred PBR lighting, object picking, and frame diagnostics.', 'diagram': 'graphics'},
]


def svg_document(width, height, title, description, body, theme):
    colors = THEMES[theme]
    style = '''text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif}.mono{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}.trace{stroke-dasharray:1600;animation:draw 4.6s ease-out both}.arrive{animation:arrive 1.2s ease-out both}.orbit{transform-origin:770px 174px;animation:orbit 4.6s ease-out both}.spark{animation:spark 4.6s ease-out both}@keyframes draw{from{stroke-dashoffset:1600;opacity:.1}to{stroke-dashoffset:0;opacity:1}}@keyframes arrive{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}@keyframes orbit{from{transform:rotate(-32deg);opacity:.2}to{transform:rotate(0);opacity:1}}@keyframes spark{0%,100%{opacity:.5}35%,70%{opacity:1}}@media(prefers-reduced-motion:reduce){.trace,.arrive,.orbit,.spark{animation:none}}'''
    doc = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">\n<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>\n<style>{style}</style>\n{body}\n</svg>\n'
    for key, value in colors.items():
        doc = doc.replace('{' + key + '}', value)
    return doc


def hero(theme):
    body = '''<defs>
      <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M30 0H0V30" fill="none" stroke="{line}" stroke-width=".6"/></pattern>
      <radialGradient id="halo"><stop stop-color="{accent}" stop-opacity=".13"/><stop offset="1" stop-color="{bg}" stop-opacity="0"/></radialGradient>
    </defs>
    <rect x="1" y="1" width="958" height="358" rx="16" fill="{bg}" stroke="{line}"/>
    <path d="M1 39H959" stroke="{line}"/>
    <circle cx="23" cy="20" r="4" fill="{warm}"/><circle cx="39" cy="20" r="4" fill="{accent}"/><circle cx="55" cy="20" r="4" fill="{blue}"/>
    <text x="80" y="24" font-size="11" class="mono" letter-spacing="1.3" fill="{muted}">STEVVVU / ENGINEERING WORKBENCH</text>
    <rect x="575" y="40" width="383" height="318" fill="url(#grid)"/>
    <circle cx="770" cy="174" r="166" fill="url(#halo)"/>
    <g>
      <text x="40" y="94" class="mono" font-size="14" letter-spacing="3" fill="{accent}">SOFTWARE / SYSTEMS / EXPERIMENTS</text>
      <text x="34" y="184" font-size="88" font-weight="700" letter-spacing="-4" fill="{text}">Steven Vu<tspan fill="{accent}">.</tspan></text>
      <text x="40" y="234" font-size="30" font-weight="500" letter-spacing="-.5" fill="{text}">Systems in motion.</text>
      <text x="40" y="270" font-size="19" fill="{muted}">Storage, compilers, and graphics.</text>
    </g>
    <path class="trace" d="M40 305H112L124 293H202L214 305H322L334 293H460" stroke="{accent}" stroke-width="1.5" fill="none"/>
    <g class="mono" font-size="12" letter-spacing="1.3" fill="{muted}">
      <text x="40" y="333">RUST</text><text x="131" y="333">PYTHON</text><text x="242" y="333">TYPESCRIPT</text><text x="390" y="333">CUDA</text>
    </g>
    <g class="orbit" fill="none" stroke="{line}" stroke-width="1">
      <circle cx="770" cy="174" r="119"/><ellipse cx="770" cy="174" rx="72" ry="119"/>
      <ellipse cx="770" cy="174" rx="119" ry="45"/><ellipse cx="770" cy="174" rx="119" ry="88"/>
      <path d="M651 174H889M770 55V293"/>
      <ellipse class="trace" cx="770" cy="174" rx="144" ry="52" transform="rotate(-33 770 174)" stroke="{accent}" stroke-width="1.2"/>
    </g>
    <g class="arrive" stroke="{accent}" stroke-linejoin="round" stroke-width="1.4">
      <path d="M715 108L748 142L793 142L824 108L813 205L770 237L727 205Z" fill="{panel}"/>
      <path d="M715 108L748 142L727 205Z" fill="{accent}" fill-opacity=".14"/>
      <path d="M824 108L793 142L813 205Z" fill="{blue}" fill-opacity=".16"/>
      <path d="M748 142L770 206L793 142M727 205L770 206L813 205M770 206V237" fill="none"/>
      <path d="M737 172L751 177M790 177L803 172" stroke="{text}" stroke-width="3"/>
      <path d="M764 204H777L770 212Z" fill="{warm}" stroke="{warm}"/>
    </g>
    <g class="spark" fill="{warm}"><circle cx="651" cy="174" r="4"/><circle cx="857" cy="112" r="4"/></g>
    <g fill="{accent}"><circle cx="770" cy="55" r="3"/><circle cx="833" cy="275" r="3"/></g>
    <g class="mono" font-size="10" letter-spacing="1.4" fill="{muted}">
      <text x="628" y="316">PERSIST</text><text x="740" y="316">COMPUTE</text><text x="855" y="316">RENDER</text>
    </g>'''
    return svg_document(960, 360, 'Steven Vu. Systems in motion.', 'A geometric arctic fox sits inside a wireframe globe. Orbit lines draw in and settle. Software, systems, and experiments in Rust, Python, TypeScript, and CUDA.', body, theme)


DIAGRAMS = {
    'storage': '<path d="M28 159H360"/><g fill="{panel}"><rect x="32" y="145" width="58" height="28" rx="5"/><rect x="112" y="145" width="58" height="28" rx="5"/><rect x="192" y="145" width="58" height="28" rx="5"/><path d="M292 145L320 133L348 145V173L320 185L292 173Z"/></g><path d="M43 159L49 165L61 153M123 159L129 165L141 153M203 159L209 165L221 153" stroke="{accent}"/><path d="M292 145L320 158L348 145M320 158V185"/>',
    'network': '<path d="M37 159H123M152 159H215L244 133H351M215 159L244 185H351M215 159H351"/><circle cx="137" cy="159" r="15" fill="{panel}" stroke="{accent}"/><g fill="{panel}"><rect x="307" y="120" width="50" height="25" rx="4"/><rect x="307" y="147" width="50" height="25" rx="4"/><rect x="307" y="174" width="50" height="25" rx="4"/></g><circle cx="37" cy="159" r="4" fill="{accent}"/>',
    'queue': '<path d="M35 153H358M333 153L345 141M333 153L345 165M280 165V188H130V165"/><g fill="{panel}"><rect x="42" y="139" width="38" height="28" rx="4"/><rect x="92" y="139" width="38" height="28" rx="4"/><rect x="169" y="133" width="68" height="40" rx="6"/><circle cx="291" cy="153" r="18"/></g><path d="M283 153L289 159L300 147" stroke="{accent}"/><path d="M130 188L142 181M130 188L142 195" stroke="{warm}"/>',
    'compiler': '<path d="M32 153H363"/><g fill="{panel}"><rect x="38" y="136" width="70" height="34" rx="5"/><rect x="157" y="130" width="80" height="46" rx="5"/><rect x="286" y="136" width="70" height="34" rx="5"/></g><g stroke="{accent}"><path d="M49 147H95M49 158H82M168 142H224M168 153H214M168 164H198M297 147H345M297 158H332"/></g><path d="M124 146L131 153L124 160M254 146L261 153L254 160" stroke="{warm}"/>',
    'chain': '<path d="M34 151H356M171 151L219 186H309"/><g fill="{panel}"><rect x="40" y="137" width="43" height="28" rx="4"/><rect x="112" y="137" width="43" height="28" rx="4"/><rect x="184" y="137" width="43" height="28" rx="4"/><rect x="256" y="137" width="43" height="28" rx="4"/><rect x="328" y="137" width="29" height="28" rx="4"/></g><g stroke="{warm}" fill="{panel}"><rect x="215" y="174" width="43" height="25" rx="4"/><rect x="282" y="174" width="43" height="25" rx="4"/></g>',
    'graphics': '<path d="M40 145L68 130L97 145V177L68 193L40 177ZM40 145L68 162L97 145M68 162V193M121 161H165M215 161H259M309 161H359"/><circle cx="190" cy="161" r="24" fill="{panel}" stroke="{accent}"/><path d="M175 146L205 176M174 174L204 147" stroke="{accent}"/><rect x="263" y="137" width="45" height="47" rx="4" fill="{panel}"/><path d="M275 149H296M275 160H296M275 171H289" stroke="{warm}"/>',
}


def project_card(project, theme):
    title = escape(project['title'])
    line_one, line_two = map(escape, project['lines'])
    body = f'''<rect x="1" y="1" width="398" height="218" rx="12" fill="{{bg}}" stroke="{{line}}"/>
    <text x="24" y="29" class="mono" font-size="11" letter-spacing="1.2" fill="{{accent}}">{project['category']}</text>
    <text x="24" y="65" font-size="28" font-weight="650" letter-spacing="-.6" fill="{{text}}">{title}</text>
    <path d="M360 42H374V56M374 42L357 59" fill="none" stroke="{{accent}}" stroke-width="1.5"/>
    <text x="24" y="94" font-size="16" fill="{{muted}}">{line_one}</text>
    <text x="24" y="116" font-size="16" fill="{{muted}}">{line_two}</text>
    <g fill="none" stroke="{{line}}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round">{DIAGRAMS[project['diagram']]}</g>
    <text x="24" y="209" class="mono" font-size="10" letter-spacing="1" fill="{{muted}}">{project['stack']}</text>'''
    return svg_document(400, 220, project['title'], project['detail'], body, theme)


def picture(asset, alt, width):
    return f'''<picture><source media="(prefers-color-scheme: dark)" srcset="assets/{asset}-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/{asset}-light.svg"><img src="assets/{asset}-light.svg" alt="{escape(alt, quote=True)}" width="{width}"></picture>'''


def readme():
    cards = []
    for project in PROJECTS:
        alt = project['title'] + '. ' + project['detail'] + ' Open repository.'
        cards.append(f'<a href="https://github.com/STEVVVU/{project["slug"]}">{picture(project["slug"], alt, 400)}</a>')
    rows = [' '.join(cards[i:i + 2]) for i in range(0, len(cards), 2)]
    gallery = '\n\n'.join(rows)
    return f'''{picture('hero', 'Steven Vu. Systems in motion. Storage, compilers, and graphics.', '100%')}

[Explore the work](#selected-work) · [Inside the projects](#inside-the-projects) · [All repositories](https://github.com/STEVVVU?tab=repositories)

I build systems software, developer tools, and graphics. I'm interested in what happens inside: the write that survives a crash, the worker that recovers, and the frame that reaches the screen.

### Selected work

Select a project to inspect the code.

{gallery}

### Inside the projects

<details>
<summary>Read the architecture and failure models</summary>

- [StrataDB storage architecture](https://github.com/STEVVVU/stratadb/blob/main/docs/architecture.md) and [failure model](https://github.com/STEVVVU/stratadb/blob/main/docs/failure-model.md)
- [EdgeProxy protocol and failure model](https://github.com/STEVVVU/edgeproxy/blob/main/docs/protocol-and-failure-model.md)
- [DurableFlow delivery and recovery guarantees](https://github.com/STEVVVU/durableflow/blob/main/docs/failure-model.md)
- [LumenForge rendering architecture](https://github.com/STEVVVU/lumenforge-webgl/blob/main/docs/ARCHITECTURE.md)

</details>

<details>
<summary>More experiments in languages, compute, and tooling</summary>

- [EmberLang](https://github.com/STEVVVU/emberlang-vm): a Rust compiler and bytecode VM.
- [KernelForge](https://github.com/STEVVVU/kernelforge-gpu): CUDA kernel fusion and correctness checks.
- [Traceframe](https://github.com/STEVVVU/traceframe): a Python execution visualizer.
- [SRE Observatory](https://github.com/STEVVVU/sre-observatory): an infrastructure and observability reference.
- [Microbook](https://github.com/STEVVVU/microbook-quant): market-data ingestion and order-book replay.

</details>

<details>
<summary>See a frame from the LumenForge renderer</summary>

[![LumenForge material-grid scene with deferred lighting, object inspection, and frame diagnostics](https://raw.githubusercontent.com/STEVVVU/lumenforge-webgl/main/artifacts/browser-desktop.png)](https://github.com/STEVVVU/lumenforge-webgl)

</details>

<sub>Original SVG artwork, generated from [source](scripts/render_profile.py). The header settles after 4.6 seconds and respects reduced-motion preferences.</sub>
'''


if __name__ == '__main__':
    assets = ROOT / 'assets'
    assets.mkdir(exist_ok=True)
    for theme in THEMES:
        (assets / f'hero-{theme}.svg').write_text(hero(theme), encoding='utf-8')
        for project in PROJECTS:
            (assets / f'{project["slug"]}-{theme}.svg').write_text(project_card(project, theme), encoding='utf-8')
    (ROOT / 'README.md').write_text(readme(), encoding='utf-8')
