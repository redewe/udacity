<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />
<title>Data Wrangling - Final Project</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.2.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.2.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.2.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.2.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.2.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.2.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
@media (max-width: 991px) {
  #ipython_notebook {
    margin-left: 10px;
  }
}
[dir="rtl"] #ipython_notebook {
  float: right !important;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#login_widget {
  float: right;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  text-align: center;
  vertical-align: middle;
  display: inline;
  opacity: 0;
  z-index: 2;
  width: 12ex;
  margin-right: -12ex;
}
.alternate_upload .btn-upload {
  height: 22px;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
[dir="rtl"] #tabs li {
  float: right;
}
ul#tabs {
  margin-bottom: 4px;
}
[dir="rtl"] ul#tabs {
  margin-right: 0px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons {
  float: left !important;
}
[dir="rtl"] .list_toolbar .pull-right {
  padding-top: 1px;
  float: left !important;
}
[dir="rtl"] .list_toolbar .pull-left {
  float: right !important;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: baseline;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
#tree-selector {
  padding-right: 0px;
}
[dir="rtl"] #tree-selector a {
  float: right;
}
#button-select-all {
  min-width: 50px;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
[dir="rtl"] #new-menu {
  text-align: right;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
[dir="rtl"] #running .col-sm-8 {
  float: right !important;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI colors. */
.ansibold {
  font-weight: bold;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  border-left-width: 1px;
  padding-left: 5px;
  background: linear-gradient(to right, transparent -40px, transparent 1px, transparent 1px, transparent 100%);
}
div.cell.jupyter-soft-selected {
  border-left-color: #90CAF9;
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected {
  border-color: #ababab;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 5px, transparent 5px, transparent 100%);
}
@media print {
  div.cell.selected {
    border-color: transparent;
  }
}
div.cell.selected.jupyter-soft-selected {
  border-left-width: 0;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 7px, #E3F2FD 7px, #E3F2FD 100%);
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #66BB6A -40px, #66BB6A 5px, transparent 5px, transparent 100%);
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  padding: 0.4em;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. We need the 0 value because of how we size */
  /* .CodeMirror-lines */
  padding: 0;
  border: 0;
  border-radius: 0;
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul {
  list-style: disc;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ul ul {
  list-style: square;
  margin: 0em 2em;
}
.rendered_html ul ul ul {
  list-style: circle;
  margin: 0em 2em;
}
.rendered_html ol {
  list-style: decimal;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
  margin: 0em 2em;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  background-color: #fff;
  color: #000;
  font-size: 100%;
  padding: 0px;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: 1px solid black;
  border-collapse: collapse;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  border: 1px solid black;
  border-collapse: collapse;
  margin: 1em 2em;
}
.rendered_html td,
.rendered_html th {
  text-align: left;
  vertical-align: middle;
  padding: 4px;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget {
  float: right !important;
  float: right;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  margin-top: 6px;
}
span.save_widget span.filename {
  height: 1em;
  line-height: 1em;
  padding: 3px;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  display: none;
}
.command-shortcut:before {
  content: "(command)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Open-Street-Map-Data-Case-Study">Open Street Map Data Case Study<a class="anchor-link" href="#Open-Street-Map-Data-Case-Study">&#182;</a></h1><p>By Rachel Foong</p>
<p><strong>Map Area:</strong> Singapore
Chosen mainly due to its friendly size. One of the smallest countries I could think of and it's close to the country of my origin - Singapore.</p>
<p><strong>Data Sources:</strong></p>
<ul>
<li>OpenStreetMap Relation: <a href="https://www.openstreetmap.org/relation/536780#map=9/1.3218/104.0687">https://www.openstreetmap.org/relation/536780#map=9/1.3218/104.0687</a></li>
<li>Metro Extract: <a href="https://mapzen.com/data/metro-extracts/metro/singapore/">https://mapzen.com/data/metro-extracts/metro/singapore/</a></li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Data-Overview">Data Overview<a class="anchor-link" href="#Data-Overview">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#declare all variables</span>
<span class="kn">import</span> <span class="nn">sqlite3</span>
<span class="kn">import</span> <span class="nn">pprint</span><span class="o">,</span> <span class="nn">os</span>

<span class="n">folder_PATH</span><span class="o">=</span><span class="s2">&quot;data_input_output&quot;</span>
<span class="n">file_PATH</span><span class="o">=</span><span class="n">folder_PATH</span><span class="o">+</span><span class="s2">&quot;/singapore.db&quot;</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Function to display readable filesize</span>
<span class="k">def</span> <span class="nf">GetHumanReadable</span><span class="p">(</span><span class="n">size</span><span class="p">,</span><span class="n">precision</span><span class="o">=</span><span class="mi">2</span><span class="p">):</span>
    <span class="n">suffixes</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39; B&#39;</span><span class="p">,</span><span class="s1">&#39; KB&#39;</span><span class="p">,</span><span class="s1">&#39; MB&#39;</span><span class="p">,</span><span class="s1">&#39; GB&#39;</span><span class="p">,</span><span class="s1">&#39; TB&#39;</span><span class="p">]</span>
    <span class="n">suffixIndex</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">while</span> <span class="n">size</span> <span class="o">&gt;</span> <span class="mi">1024</span> <span class="ow">and</span> <span class="n">suffixIndex</span> <span class="o">&lt;</span> <span class="mi">4</span><span class="p">:</span>
        <span class="n">suffixIndex</span> <span class="o">+=</span> <span class="mi">1</span> <span class="c1">#increment the index of the suffix</span>
        <span class="n">size</span> <span class="o">=</span> <span class="n">size</span><span class="o">/</span><span class="mf">1024.0</span> <span class="c1">#apply the division</span>
    <span class="k">return</span> <span class="s2">&quot;</span><span class="si">%.*f%s</span><span class="s2">&quot;</span><span class="o">%</span><span class="p">(</span><span class="n">precision</span><span class="p">,</span><span class="n">size</span><span class="p">,</span><span class="n">suffixes</span><span class="p">[</span><span class="n">suffixIndex</span><span class="p">])</span>

<span class="n">theFiles</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">folder_PATH</span><span class="p">))</span>

<span class="c1">#Calculate size for all files here. </span>
<span class="n">theDict</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
<span class="k">for</span> <span class="n">something</span> <span class="ow">in</span> <span class="n">theFiles</span><span class="p">:</span> 
    <span class="k">try</span><span class="p">:</span>
        <span class="n">new_path</span> <span class="o">=</span> <span class="n">folder_PATH</span><span class="o">+</span><span class="s2">&quot;</span><span class="se">\\</span><span class="s2">&quot;</span><span class="o">+</span><span class="n">something</span>
        <span class="n">theStats</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="n">new_path</span><span class="p">)</span>
        <span class="n">theDict</span><span class="p">[</span><span class="n">something</span><span class="p">]</span> <span class="o">=</span> <span class="n">theStats</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>

<span class="c1">#Display list of files and filesize</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File Names and Sizes&quot;</span><span class="p">,</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">++++++++++++++++++++++++&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">theDict</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="si">{:30s}</span><span class="s2"> </span><span class="si">{:s}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">item</span><span class="p">,</span><span class="n">GetHumanReadable</span><span class="p">(</span><span class="n">theDict</span><span class="p">[</span><span class="n">item</span><span class="p">]</span><span class="o">.</span><span class="n">st_size</span><span class="p">)))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>File Names and Sizes 
++++++++++++++++++++++++
nodes.csv                      118.59 MB
nodes_tags.csv                 4.90 MB
sample.osm                     9.24 MB
singapore.db                   255.52 MB
singapore.osm                  328.98 MB
ways.csv                       13.55 MB
ways_nodes.csv                 43.46 MB
ways_tags.csv                  21.44 MB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<ul>
<li>Number of nodes: 1,517,456</li>
<li>Number of ways: 237,891</li>
<li>Number of unique users: 2,178</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Enquire database</span>
<span class="n">db</span> <span class="o">=</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">file_PATH</span><span class="p">)</span>
<span class="n">c</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
<span class="n">c</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="s2">&quot;SELECT e.user, COUNT(*) as num FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e GROUP BY e.user ORDER BY num DESC LIMIT 10;&quot;</span><span class="p">)</span>
<span class="n">rows</span> <span class="o">=</span> <span class="n">c</span><span class="o">.</span><span class="n">fetchall</span><span class="p">()</span>

<span class="c1">#Print results</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Top 10 contributing users&quot;</span><span class="p">,</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">++++++++++++++++++++++++&quot;</span><span class="p">)</span>
<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="n">rows</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Top 10 contributing users 
++++++++++++++++++++++++
[(&#39;JaLooNz&#39;, 404899),
 (&#39;berjaya&#39;, 117377),
 (&#39;rene78&#39;, 77581),
 (&#39;cboothroyd&#39;, 72204),
 (&#39;lmum&#39;, 51342),
 (&#39;kingrollo&#39;, 39063),
 (&#39;Luis36995&#39;, 38821),
 (&#39;ridixcr&#39;, 38239),
 (&#39;Sihabul Milah&#39;, 37160),
 (&#39;calfarome&#39;, 32945)]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Problems-Encountered-with-Data">Problems Encountered with Data<a class="anchor-link" href="#Problems-Encountered-with-Data">&#182;</a></h3><h4 id="Cultural-issues">Cultural issues<a class="anchor-link" href="#Cultural-issues">&#182;</a></h4><ul>
<li>Language Inconsistency - some were in English, others in Chinese</li>
<li>Street names were a mixture of Malay and English e.g. <em>Jalan</em> is Malay for road. I've included a list of other Malay names into the expected list of words during the audit process in the Python File <a href="https://github.com/redewe/udacity/blob/master/python%20files/XML%20file%20to%20CSV%20files.ipynb">https://github.com/redewe/udacity/blob/master/python%20files/XML%20file%20to%20CSV%20files.ipynb</a></li>
</ul>
<h4 id="User-entry-issues">User entry issues<a class="anchor-link" href="#User-entry-issues">&#182;</a></h4><ul>
<li>Alternative keys for the same value were discovered e.g. name_1, name_2, building_1 Full list as below taken from the Python file mentioned above</li>
<li>Some of the keys were also tagged as "FIXME" which meant that the data was incomplete</li>
<li>While there was a tag for address, the keys like <em>Jalan</em> which is Malay for road was also used as a tag on its own</li>
</ul>

</div>
</div>
</div>Other k values (Unique: 48 ) 
++++++++++++++++++++++++
[('Datafile', 62),
 ('Data_Dicti', 62),
 ('source_1', 37),
 ('FIXME', 12),
 ('name_1', 11),
 ('name_2', 5),
 ('building_1', 5),
 ('leisure_1', 4),
 ('name_3', 3),
 ('description2', 3),
 ('landuse_1', 3),
 ('amenity_1', 2),
 ('name_4', 2),
 ('Id', 2),
 ('Jalan', 2),
 ('naptan:Bearing', 1),
 ('country_code_iso3166_1_alpha_2', 1),
 ('SMA', 1),
 ('SPI', 1),
 ('LT5A', 1),
 ('LT5B', 1),
 ('MLT1', 1),
 ('LT 7', 1),
 ('Singapore Poly', 1),
 ('TODO', 1),
 ('DateTimeS', 1),
 ('website_1', 1),
 ('race course', 1),
 ('alt_name2', 1),
 ('maxspeed_1', 1),
 ('Type', 1),
 ('tourism_1', 1),
 ('fuel:GTL_diesel', 1),
 ('Name', 1),
 ('FolderPath', 1),
 ('Shape_Area', 1),
 ('Shape_Leng', 1),
 ('SHAPE_Leng', 1),
 ('Line_ID', 1),
 ('Avg_Horz_P', 1),
 ('Avg_Vert_P', 1),
 ('Worst_Horz', 1),
 ('Worst_Vert', 1),
 ('Bandar', 1),
 ('highway_1', 1),
 ('fuel:RON_92', 1),
 ('fuel:RON_97', 1),
 ('fuel:Diesel_Euro_5', 1)]
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Map-boundary-issues">Map boundary issues<a class="anchor-link" href="#Map-boundary-issues">&#182;</a></h4><ul>
<li>More than 50% of points includes places outside the country boundary of Singapore</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%</span><span class="k">matplotlib</span> inline
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">from</span> <span class="nn">pandas</span> <span class="k">import</span> <span class="n">DataFrame</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">from</span> <span class="nn">IPython.display</span> <span class="k">import</span> <span class="n">Image</span>

<span class="c1">#Find nodes where they are beyond singapore&#39;s borders using https://gps-coordinates.org/singapore-latitude.php</span>
<span class="n">c</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="s2">&quot;SELECT lat As Latitude, lon as Longitude FROM nodes;&quot;</span><span class="p">)</span>

<span class="n">party</span> <span class="o">=</span> <span class="n">DataFrame</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">fetchall</span><span class="p">())</span>
<span class="n">party</span><span class="o">.</span><span class="n">columns</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">c</span><span class="o">.</span><span class="n">description</span><span class="p">)</span>

<span class="c1">#names = list(map(lambda x: x[0], c.description))</span>

<span class="c1">#Code taken from https://www.kaggle.com/somesnm/new-york-parties-eda </span>
<span class="n">city_long_border</span> <span class="o">=</span> <span class="p">(</span><span class="o">-</span><span class="mf">74.03</span><span class="p">,</span> <span class="o">-</span><span class="mf">73.75</span><span class="p">)</span>
<span class="n">city_lat_border</span> <span class="o">=</span> <span class="p">(</span><span class="mf">40.63</span><span class="p">,</span> <span class="mf">40.85</span><span class="p">)</span>

<span class="c1">#fig, ax = plt.subplots(ncols=1, sharex=True, sharey=True)</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">party</span><span class="p">[</span><span class="s1">&#39;Longitude&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span> <span class="n">party</span><span class="p">[</span><span class="s1">&#39;Latitude&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span>
              <span class="n">color</span><span class="o">=</span><span class="s1">&#39;black&#39;</span><span class="p">,</span> <span class="n">s</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">&#39;train&#39;</span><span class="p">,</span> <span class="n">alpha</span><span class="o">=</span><span class="mf">0.1</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">axes</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Coordinates of the points in the dataset&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Longitude&#39;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">18</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Latitude&#39;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">16</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">figure</span><span class="o">.</span><span class="n">set_size_inches</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span><span class="mi">5</span><span class="p">)</span>
<span class="c1">#plt.ylim(city_lat_border)</span>
<span class="c1">#plt.xlim(city_long_border)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="c1">#taken from http://labs.strava.com/heatmap/#10/103.51044/1.55232/blue/bike</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Map of Singapore for comparison - boundary is grey line&quot;</span><span class="p">)</span>
<span class="n">Image</span><span class="p">(</span><span class="s2">&quot;singaporeheatmap.PNG&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
Wq2W4nR0dJCdnU1HRwcAra2t/PDDDzel1VcYQGlpKTNmzODxxx+nuLiYzs5OysvLqaysJDk5mccf
f5wjR46Qk5PDmjVrqKur67WeekIURRobGzlz5gxFRUXU1tb22l47Ozs5fvw48+fPZ8KECUycOJGs
rCzS09Opr68nKSkJlUr1k/I3cpcgiuJ//RETEyP+0rS2toqXLl0Sr1y5IiYmJop1dXXS9cuXL4ut
ra2iVqsVVSqVqNVq+0xPpVKJeXl5okql6lf+169fF3fv3i2mpKSIarW6x/Lt3LlT3Llzp3jt2jWx
rq5OrK2tFffu3Svu2bNHbGpqkuK2tLSIaWlpYnp6unjmzBmxtbW1X89veM6eSE1NFX19fUU7OzsR
6HbI5XJxxIgR4sGDB8WOjo5e009OThbXr18vZmVliRqNptey7Nq1S/Tz8xOHDBki7t+/X7x27Zp4
4MAB8fr161Kczs5Ocfjw4VL+p06dEjdt2iS+9tprYn5+fo/pajQacfXq1aJSqRTHjBkjZmdnS2Ff
f/21aGVlJT2TlZWV+NZbb4kFBQViZ2dnt3QqKirEt99+W3ziiSe61cP+/fu7xTt16pQ4efJkcezY
seInn3wi7tq1S4yKihJ37dolajQasaOjQzx06JD44osvileuXBFFURT37NkjRkREiGvWrBEPHz4s
qlQqsaOjQ7x06ZL40ksviYGBgeLOnTt7fL65c+dKZVm8eLGYlZUlrl27VnzvvfdEf39/ERCDg4PF
efPmiQqFQly1alWv76AnVCqVuGvXLnHu3LniX/7yF/F///d/xdra2h7j5uXlieHh4d3qJzg4WFy4
cKG4Zs0aMSoqSty3b99Pyt/Izwc4Lf7M/vf/hAPGn0NbWxunT59m6NChyOVy6bpGo6GoqAhRFAkP
D0epVN50r1qtpqysDE9Pz2739oSFhQWenp5YWFj0q1wWFhZcu3aNd999l5UrVxIXFyeFiaLIwYMH
Wb58OY8//jjDhw8nOzubwYMH4+Xlxb59+/D29iYiIgJRFCkpKaG2tpbg4GBqampuObsx0NnZSWlp
Kc7OzsjlcgRB6Bb+9ttvU1zcs++2trY2Tp48yR/+8Ae2bdtGZGTkTXFEUcTKyoqYmBhKSkqwtbXF
1dX1pnwAJk2axMqVKxEEgYKCApqamvD29u5WlxUVFdJ5W1sbixcv5vvvv5dmYBqNBlNTU0A3cygu
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
E2JjY4mLi8PFxQUTExM8PDx47LHHWLFiBfHx8RQXF7Nq1SqOHz9OW1sboaGhvPHGGyxevJjAwEDa
29tJSkriyJEj+Pr6cs899zBgwAAGDRpERUUFzc3NPPnkkzz99NOEhYVhYmKCXC6X1CAmJibY29sz
fvx4qZMXRZH6+np+/PFHioqKiI2NZdmyZfj6+vL3v/+dpKQkAA4fPkx6ejr29vb4+vrS1NTE4cOH
OXDgAEVFRXzxxRf861//4osvvmDIkCHk5+f36z0Z9iLMnDkT0M00w8LCpE2C48aNY8uWLajVaszM
zCgsLKSjo4OHHnqI4cOH8+233/L666+zYcMGioqK0Gg0mJiY4O3tzX333SdZFW3YsKHb5sv+YGtr
yxtvvMEf//hHmpqaUCgUODk53TQo0Wq1mJiYoNVqqaio4MMPPyQpKYmKigrs7e3ZunUrGRkZkscF
w6zWoNZ88803Wbt2LaGhodI6lmGzaF1dHXK5nIaGBiIjI/H09MTS0pKtW7eSk5MjlaGjo4Pz58/T
1NSEIAjEx8czf/78m4xPDF4TkpKSMDU1Zfr06QwZMgQzMzPpfY0cOZJ169YxbNgwTExMaG1tpbi4
mKSkJAoLC3+yrzojvx6/eSECuj0gOTk52Nra9rj2YGdnx9ixY7vNTn4NHB0dCQgI6GZ+3BsmJiYo
lUrs7OwkPXlmZiY2NjbMnj0bR0dHqqur+ctf/kJdXR2hoaFERkbi7OyMi4sL2dnZnD59mmPHjmFr
a4udnR1arVZyy3Hu3DmmTZuGVqvl2LFjXLlyhfz8fEJCQhgzZgwymYzU1FQOHjzYzUjBoH4yNzen
o6MDURQpKipiwYIFTJ06lTlz5lBcXIy7uzvffPMNZ86cke41rMVYWFhgaWmJra0tBw4cYOfOnWzb
tk2ascD/70KjP5vlXFxcmD17Np9//jlPPvkkSqWS/fv389577wFw/fp1nnnmGc6cOYOvry/BwcH4
+/vj5eXF/PnzeeqppwgLC+Pf//43q1evJjU1lY6ODqqrq3n//ff561//KuX1+uuv9+tdi6JIdXU1
+fn5hIeHM3PmTJqbm0lOTqa6urpb3M7OTiorKzE3N8fExISqqioqKytxcHAgKCiIU6dOsXHjRkpL
S2ltbWXixIm8/fbb3VRrZ8+eJSMjg8jIyG7uSDo7O3FyciIrK4stW7aQm5vLyZMn8fX15cqVK92E
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
8NMtAAAAAElFTkSuQmCC
"
>
</div>

</div>

<div class="output_area">

<div class="prompt output_prompt">Out[27]:</div>




<div class="output_png output_subarea output_execute_result">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Other-ideas-about-the-dataset">Other ideas about the dataset<a class="anchor-link" href="#Other-ideas-about-the-dataset">&#182;</a></h2><ul>
<li><p>To improve the dataset, it's best if the OSM data automatically filters for points outside the boundaries of any given country/city. As proven above, it's problematic for many when trying to validate the data.</p>
</li>
<li><p>While the OSM data may be useful for those who would like to look beyond just Singapore in mapping routes, the data can be in a supplementary file than combined into the main file.</p>
</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">db</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

</div>
</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>
