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

**Asset hosting:** The current `asset-map.json` uses direct public GitHub **raw file URLs** for the six temporary SVGs, so GitHub Pages is **not required for the first Tumblr test**. We can switch to Pages or Tabler later. Older assets (21 original files) remain byte-for-byte under `assets/legacy/`.

## Next steps

- Choose the final navigation icons (legacy PNG or Tabler) and check their loading
- Upload a Wallpaper in Tumblr's Theme Options (and optionally Featured Screenshot)
- Test the rendered theme with real Tumblr posts, NPF photosets and reblog trails
- Build custom-layout Downloads and Resources pages

[Theme documentation](https://www.tumblr.com/docs/en/custom_themes) · [NPF specification](https://github.com/tumblr/docs/blob/master/npf-spec.md)

## Customizer controls — v0.2

The theme follows the free-text icon-field pattern used by [Seyche's Lilac theme](https://github.com/seyche/tumblr-themes/blob/master/theme%20nine%3A%20lilac), adapted to the [Tabler webfont](https://tabler.io/icons) (3.49.0 via jsDelivr): enter icon **names** such as `home`, `books`, `download` without any prefix. No dropdown or icon asset is needed for the navigation.

- **Profile Heading**, **Profile Bio**, **Profile Interests**: three independent text fields. Tumblr provides the profile picture.
- **Show Message** (also requires Ask enabled in the blog) and **Show Archive**: separate toggles.
- **Home/Message/Archive Label + Icon**: text inputs for default navigation links.
- **Custom Link 1/2/3**: each has a link title, URL and icon input. Like Lilac, clearing the title hides its slot. The first two default to Downloads and Resources; the third starts empty. Create target Tumblr pages separately.
- **Show Needs** plus **Need Hunger/Energy/Nicotine**: compact decorative Sims-like meters between the profile and the navigation. Text values from 0 to 100; non-interactive.
- **Show Music Widget**, **Music Track**, **Music Artist**: decorative right-rail track card replacing the formerly hardcoded "Browse Posts" tags.

**Working process:** after editing source in GitHub, rerun `python build.py` and paste the newly generated `dist/theme.html` into Tumblr's HTML editor. A repository change does not automatically update the live blog. Note: `dist/local-preview.html` is a static snapshot, not a Tumblr renderer.

The preview helper `make_preview.py` refreshes the **CSS and JS inside the checked-in visual snapshot**. It does not automatically re-render changing Tumblr page markup; verify layout changes in Tumblr's own preview.

## UI polish (October 2026)

- Flat, **decorative** music player with shared titlebar/card design; its transport and volume controls intentionally do not play audio. The plumbob is centered on the slider.
- Sidebar navigation uses **filled Tabler webfont icons** (`.nav-filled`), while the rest of the UI retains outline Tabler. Player transport controls use the same filled font. The optional third custom link still accepts an outline Tabler icon name.
- Sticky desktop sidebars have viewport-height **footer zones**; at very short screen heights, normal browser scrolling takes over. Vertical separators are drawn by `.main-panel`, not by sticky sidebars.
- The right-side plumbob + **theme info** is one link to this GitHub repository.
- Tumblr Theme Options → **Main Font Size**: `13`, `13.5`, `14`, `14.5` (default), `15`. This scales primary body/post/sidebar text and related metadata while leaving decorative titlebar and control icon sizes stable.
- The source stylesheet contains a Tumblr customizer token; run `python build.py` for Tumblr, or `python make_preview.py` to replace it with `14.5` in the static fixture.
