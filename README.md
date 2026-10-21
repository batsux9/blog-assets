# little world of batsu

A Sims 2–inspired Tumblr theme with a desktop-style layout, muted colors, and a little nostalgia.

## File structure

```text
src/
  template.html        Tumblr markup
  theme.css            Styles
  theme.js             UI interactions

dist/
  theme.html           Built Tumblr theme
  local-preview.html   Static preview

assets/
  icons/               Theme icons
  images/              Images
  legacy/              Older assets

asset-map.json         Asset URLs
build.py               Theme builder
make_preview.py        Preview updater
```

Edit the files in `src/`, then run `python build.py` to generate the Tumblr-ready `dist/theme.html`.

## Icons

The theme uses [Tabler Icons](https://tabler.io/icons), with filled icons for navigation and player controls, and outline icons for other interface elements. A few small controls also use inline SVGs.

## Terms of use

Do whatever you want with the theme. Use it, modify it, share it, remix it. No permission or credit required.

Third-party assets and icon libraries retain their own licenses.
