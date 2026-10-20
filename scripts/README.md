# Profile artwork

Run from the repository root with Python 3.11 or newer:

```sh
python scripts/render_profile.py
```

The generator uses the Python standard library. Edit `PROJECTS` for the six linked projects and `THEMES` for the light and dark palettes. It writes `README.md` and fourteen SVG files in `assets/`.

The header animation ends after 4.6 seconds. Its reduced-motion media rule disables the nonessential animation. The diagrams are illustrations of each project's subject, rather than live telemetry.
