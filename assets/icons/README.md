# Technology icons

These are local, transparent SVG marks, normalized to a single sage fill (`#819889`) so they stay cohesive in GitHub light and dark themes. They are not proficiency ratings.

## Sources

- **Devicon v2.18.0** — most technology marks, plus the LinkedIn mark used by the contact-badge generator. Release: <https://github.com/devicons/devicon/releases/tag/v2.18.0>. License: `LICENSE-devicon.txt` (MIT).
- **Devicon master, commit `32fe1d3b3f36ad11f90ab94f7db59738139c2bf6`** — `mysql-original.svg`, which is not present in the v2.18.0 release under the plain-icon filename.
- **Simple Icons v13.21.0** — Flask and OpenAI marks, which were not available in the selected Devicon source. Package: <https://www.npmjs.com/package/simple-icons/v/13.21.0>. License: `LICENSE-simple-icons.md` (CC0-1.0).

`sources.json` records the source used for each file. Original brand colors, unnecessary dimensions, and presentation attributes were removed; the geometry was retained. Trademarks remain the property of their respective owners.

## Editing

The README uses one `<img>` line per technology. Copy, remove, or reorder those lines to edit a group. Keep `width="26" height="26"` and a meaningful `alt` value for consistency. The LinkedIn file is also consumed by `tools/build_graphics.py` to build the local contact badges.
