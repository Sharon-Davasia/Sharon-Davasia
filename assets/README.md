# Profile artwork

Original SVG assets for the Sharon-Davasia GitHub profile.

- `header-light.svg`, `header-dark.svg` — restrained personal banner.
- `divider.svg` — transparent decorative separator.
- `projects/` — four consistent 720 × 240 project illustrations, each in light and dark variants. These are conceptual artwork, not screenshots.
- `contact/` — small light/dark contact badges used in the closing section.
- `icons/` — vendored, sage-normalized technology marks; see its README for sources and licenses.

Edit the shared palettes and geometry in `tools/build_graphics.py`, then run:

```bash
python3 tools/build_graphics.py
```

The README references these files relatively, so keep the directory structure intact when copying the profile to another repository.
