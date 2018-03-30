# Bolder client-side contributing guide #

These contribution guidelines are specific to the client-side part of the style.

## Colours

The colours used are those of the [freecolour.org](https://freecolour.org/) system. Each colour has a name of the form `H###_L##_C###` where the digits after H, L, and C are the hue, lightness, and chroma respectively. For greys with 0 chroma and pastels with 5 chroma, L is a multiple of 5 and H a multiple of 30. For brighter colours, H is a multiple of 10, L is 15, 25, etc, 85, or 90, and chroma is a multiple of 10. A PDF showing all the colours [can be downloaded](https://www.freiefarbe.de/en/thema-farbe/software/).

The colours are defined as globals in [`freecolour.yaml`](freecolour.yaml) and details of the colour conversion can be found there. For pure white and black the CSS colour names of `white` and `black` should be used.

**TODO: Decide on greys**

## Code style guidelines

### YAML

- Two spaces per indent. No tabs
- Widths and other measurements in px, not meters. E.g. `width: 2px`, not `width: 200`
- When using stops, define them on even zooms unless it is essential for the cartography. E.g. ``width: [[10,0px], [12, 1px], [14, 3px]]``, not ``width: [[10,0px], [13, 1px], [14, 3px]]`` unless it is essential.
- Omit unnecessary stops unless it significantly aids clarity. E.g. the zoom 12 stop can normally be omitted from ``width: [[10,0px], [12, 2px], [14, 4px]]`` and the output won't change.
- When defining a line with a fill plus casing using stops, match stop positions on both, even if it isn't necessary. E.g.

  ```yaml
  lines:
    width: [[10,0px], [12, 1px], [14, 3px]]
    outline:
      width: [[10, 0px], [12, 1px], [14, 2px]]
  ```
  not

  ```yaml
  lines:
    width: [[10,0px], [12, 1px], [14, 3px]]
    outline:
      width: [[10, 0px], [14, 2px]]
  ```
