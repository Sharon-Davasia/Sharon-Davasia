# Profile notes

A short maintenance record for `README.md`. The README itself is the deliverable; this file keeps provenance and unfinished personal details out of the public profile.

## Finish these placeholders before publishing

- Replace the four `[ADD CREDENTIAL URL]` placeholders in **Certifications** with public certificate links, or remove the placeholder text.
- Confirm the experience and recognition entries transcribed from the published résumé. Dates were deliberately omitted because “present” in a résumé can become stale.
- Review the public email, LinkedIn URL, and portfolio URL. Remove any contact detail you do not want displayed.
- Add a featured-project demo link only when a real deployment or demo is verified. The corresponding README comments are marked `[ADD VERIFIED URL WHEN AVAILABLE]`.
- Review the skill inventory. FastAPI, Flask, Hugging Face, Supabase, Redis, RAG, and prompt engineering were retained from the supplied request; they were not all independently demonstrated in the public repositories inspected. Remove anything that is no longer part of your experience.

## Content provenance

| Content | Source | Treatment |
| --- | --- | --- |
| Name, degree, specialization, university | Public portfolio and résumé in `dispensable_portfolio1` | Used without invented grades or dates. |
| Email, LinkedIn, portfolio | Public GitHub profile, résumé, and portfolio | Portfolio page was reachable during the check. LinkedIn returned 403 to the automated fetch, so its URL is sourced but not independently opened. |
| RecallPad | `Google-Chrome-Built-in-AI-Challenge` README, manifest, and services | Description kept to implemented capture, summarization, and search; no performance or privacy guarantee claimed. |
| IdeaForge | `ideaforge-hackathon` README | Presented as a hackathon exploration, not a deployed product. |
| CertifyPro | `Cathedral` README and client/server manifests | Repository name and project name differ; the README links to the real repository. |
| Vision experiments | `Uptoskills_Output_Repo` task READMEs and notebooks | Explicitly labeled a shared/team internship repository; no individual attribution or benchmark numbers invented. |
| Downloads Folder Organizer | `Kiro-week2` README | Included as a small optional experiment. |
| PyTorch | Computer-vision notebooks importing/using `torch` and YOLO | Retained. |
| TensorFlow | Published résumé and portfolio project stack | Retained without an expertise claim. |
| Experience, award, leadership, certifications | Published résumé | Transcribed conservatively; credential proof links remain placeholders. |
| Open-source contributions | No merged contribution was verified | No contribution claim added; a fork alone was not treated as a contribution. |

Résumé source: <https://github.com/Sharon-Davasia/dispensable_portfolio1/blob/main/SHARON_RESUME_LATEST.pdf>

## External-service check — 2026-11-06

- **GitHub Readme Stats:** the public Vercel endpoint returned `503 DEPLOYMENT_PAUSED`. Omitted.
- **GitHub Readme Activity Graph:** the canonical public Vercel endpoint reported a paused deployment. Omitted.
- **GitHub Readme Streak Stats:** the project is actively maintained, and its JSON endpoint returned live contribution data for `Sharon-Davasia`. The README uses the documented SVG endpoint with the same palette and a visible native GitHub activity fallback. The text-fetch tool could not render the SVG response, and browser egress to that host was blocked in the build sandbox; spot-check the final card on GitHub after publishing.
- **Badges:** remote badge candidates were replaced with local, theme-aware SVG contact badges, so the closing section has no badge-service dependency.

No statistics are hard-coded in the README. Language-percentage and rank cards were intentionally omitted: repository byte counts and gamified ranks would add clutter without reliably describing ability.

## Design and compatibility

- Palette: `#FCFCFB`, `#F5F7F5`, `#202722`, `#747C76`, `#819889`, `#A8B9AC`, `#E5EAE5`. Dark-mode artwork uses a coordinated deep-green neutral palette.
- Original header, project artwork, divider, and contact badges are separate SVG files. Project artwork is decorative, not a screenshot.
- `picture` elements provide light/dark artwork. GitHub controls page fonts and native link colors; no custom CSS or JavaScript is required by the README.
- Projects use full-width editorial rows rather than a fixed desktop-only card grid. Tables and images were checked at a 390 px viewport with GitHub-style Markdown CSS; no horizontal page overflow was observed.
- The README was rendered through GitHub’s Markdown API to check supported HTML and image handling. Meaningful images have alt text; decorative dividers use empty alt text.
- Local assets avoid dependence on an icon CDN. If the live streak service fails, its short alt text and the native activity link remain.

## Maintenance

- Edit skills directly in the README’s grouped `<img>` rows.
- Edit project copy and links in the four `<tr>` blocks under **Selected work**.
- Regenerate original graphics with `python3 tools/build_graphics.py` from the repository root. The script uses only the Python standard library and the vendored GitHub/LinkedIn marks.
- Icon provenance and licenses are in `assets/icons/`.
