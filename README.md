# little world of batsu ✦

A personal **Sims 2–inspired Tumblr theme**, with a quiet nighttime neighborhood, desktop-window layout, blue-gray panels, isometric icons, and a decorative *on rotation* music widget.

**Status:** v0.1 boilerplate; Tumblr integration has not yet been live-tested.

## Layout

```text
src/
  template.html     Tumblr theme markup
  theme.css         Canonical styling
  theme.js          UI behavior
dist/
  theme.html        Generated single-file theme for Tumblr
assets/
  legacy/           All original repo assets (preserved intact)
  icons/            Current theme SVGs — upload pending
  images/           Current theme images — upload pending
asset-map.json      Public GitHub Pages asset URLs
build.py            Single-file theme builder (Python 3)
```

## Work locally

1. Edit files under `src/`; don't edit generated `dist/theme.html`.
2. Run `python build.py` from the repository root.
3. Copy `dist/theme.html` to Tumblr's **Edit HTML** and use **Update Preview**. Tumblr must render real posts, NPF, reblogs, notes and pagination.

## Assets

The previous repository's avatar, wallpapers, PNG icons, and GIF have all been preserved, byte-for-byte, under `assets/legacy/`. None were discarded.

**Still to upload from the previously shared `batsu-tumblr-boilerplate-v0.1.zip`:**

- `assets/images/neighborhood-night.webp`
- `assets/images/avatar.png`
- `assets/images/sims-ui.webp`
- `assets/icons/plumbob.svg`, `home.svg`, `ask.svg`, `downloads.svg`, `resources.svg`, `archive.svg`

The URL map assumes GitHub Pages on `https://batsux9.github.io/blog-assets/`. Enable Pages at **Settings → Pages → Deploy from branch → main / root**. Until images/icons exist and Pages is active, deployed imagery will be missing. These pending files must be added before deploying.

## Next steps

- Upload the current media and icons
- Confirm Pages asset URLs
- Test the rendered theme with real Tumblr posts, NPF photosets and reblog trails
- Build custom-layout Downloads and Resources pages

[Theme documentation](https://www.tumblr.com/docs/en/custom_themes) · [NPF specification](https://github.com/tumblr/docs/blob/master/npf-spec.md)
