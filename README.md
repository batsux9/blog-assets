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

## Tumblr custom pages

**Downloads** and **Resources** are Tumblr **Standard Layout** pages, rather
than independent HTML documents. In the Tumblr page editor, use URLs
`/downloads` and `/resources` and paste `pages/downloads.html` or
`pages/resources.html` into the corresponding page content editor.

Their page titles use **Sora**, while the category names, body text and link
cards continue to use **Inter**.

`pages/resources.html` intentionally has no real links yet: it displays a
small empty state and includes a commented example of the reusable resource
section/card markup. Add only verified, useful links when ready.

To publish changes to the theme stylesheet, run `python build.py` and copy
`dist/theme.html` into Tumblr's **Edit HTML** editor. Changes to page content
must be pasted separately into that page's editor.
