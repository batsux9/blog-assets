# little world of batsu ✦

A personal **Sims 2–inspired Tumblr theme**, with a quiet nighttime neighborhood, desktop-window layout, blue-gray panels, isometric icons, and a decorative *on rotation* music widget.

**Asset approach:** Tumblr's own avatar (`{PortraitURL-128}`) and Theme Options image uploads are the source of truth for the profile photo, wallpaper, and optional featured screenshot. GitHub stores backups and the few assets that need a public URL.

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
  icons/            Current placeholder SVG navigation icons (may change)
  images/           Optional image backups (night wallpaper currently stored)
asset-map.json      Public GitHub Pages asset URLs
build.py            Single-file theme builder (Python 3)
```

## Work locally

1. Edit files under `src/`; don't edit generated `dist/theme.html`.
2. Run `python build.py` from the repository root.
3. Copy `dist/theme.html` to Tumblr's **Edit HTML** and use **Update Preview**. Tumblr must render real posts, NPF, reblogs, notes and pagination.

## Images and icons

**Profile photo:** taken directly from the Tumblr blog using `{PortraitURL-128}`. No `avatar.png` file is necessary.

**Wallpaper:** Tumblr **Customize → Theme Options → Wallpaper** is created with `<meta name="image:Wallpaper" content="">`. Choose an image there. The copy at `assets/images/neighborhood-night.webp` is kept as a backup and optional direct URL, **not** hardwired into the live theme. If no wallpaper is chosen, the solid background color remains.

**From my game:** an optional Tumblr image upload named **Featured Screenshot**. The whole panel is omitted when no image is selected; `sims-ui.webp` is not required.

**Navigation icons:** The 6 present `assets/icons/*.svg` files are temporary. We may later switch to the preserved PNGs in `assets/legacy/icons/` or Tabler Icons. No new custom SVG drawing is required now. Small interface controls already use inline stroke icons.

**Asset hosting:** The current `asset-map.json` contains only those six active navigation-icon URLs. If using them from GitHub Pages, enable Pages on **main / root** and verify the URLs. Older assets (21 original files) remain byte-for-byte under `assets/legacy/`.

## Next steps

- Choose the final navigation icons (legacy PNG or Tabler) and check their loading
- Upload a Wallpaper in Tumblr's Theme Options (and optionally Featured Screenshot)
- Test the rendered theme with real Tumblr posts, NPF photosets and reblog trails
- Build custom-layout Downloads and Resources pages

[Theme documentation](https://www.tumblr.com/docs/en/custom_themes) · [NPF specification](https://github.com/tumblr/docs/blob/master/npf-spec.md)
