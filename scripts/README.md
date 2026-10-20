# Profile source

These optional contribution-calendar, portrait, and info-card generators are copied from [navi3582/animated-github-profile](https://github.com/navi3582/animated-github-profile/tree/2623020d4279dc4dfbae967795e865d784031b98), commit `2623020d4279dc4dfbae967795e865d784031b98`. The original [MIT license](../LICENSE) is retained unchanged. The upstream template credits [Avi Vashishta's write-up](https://www.avivashishta.com/blog/build-animated-github-profile-readme.html). The current README follows osu's highlights, badge groups, and project-table layout and does not display these optional assets.

The portrait and heatmap renderers are unchanged. The info-card renderer changes only `TITLE` and `ROWS` to Steven Vu's public details. The input image is the public STEVVVU arctic fox avatar, saved unchanged as `source-prepped.png`. No background-removal model or photo preprocessing is required.

The contribution fetcher defaults to STEVVVU and requires an exact tooltip count for every day instead of estimating a missing count from its color. Dependency pins are updated from upstream for Python 3.11 compatibility and current package releases. Only Pillow and NumPy are needed for the portrait.

## Regenerate

Run from the repository root with Python 3.11 or newer. Create a virtual environment with `python -m venv .venv`. Activate it with `.venv\Scripts\Activate.ps1` in PowerShell or `source .venv/bin/activate` in Bash. Then install the two requirement files:

```sh
python -m pip install -r scripts/requirements.txt -r scripts/requirements-portrait.txt
python scripts/make_ascii_svg.py
python scripts/make_info_card.py
python scripts/fetch_contributions.py
python scripts/render_heatmap_svg.py
```

In PowerShell, set `$env:PYTHONUTF8='1'` before running the scripts. In Bash, use `export PYTHONUTF8=1`. The calendar defaults to STEVVVU; set the `GITHUB_USERNAME` environment variable only to override it. Update the snapshot date in the README when refreshing the calendar.

The optional calendar is a public contribution snapshot, not live telemetry. Its SVG contains no external resources. No scheduled workflow, secret, or token is used. The current README loads static technology badges from Shields.io.
