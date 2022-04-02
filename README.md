# [Instruction available in English below] - Overlay do r/brasil no r/place 2022

O overlay aqui usa o mesmo overlay do r/Superstonk: https://github.com/rplacesuperstonk/rplace-image, com pequenas modificações nossas e de outros brazucas.

### INSTRUÇÕES:

- Instale o TamperMonkey no Chrome ou o seu equivalente do Firefox, o ViolentMonkey
  - TamperMonkey p/ Chrome https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en
  - OPERA - https://addons.opera.com/en/extensions/details/tampermonkey-beta/
  - ViolenyMonkey p/ Firefox - https://addons.mozilla.org/en-US/firefox/addon/violentmonkey/

- Na aba extensões, ative a extensão TamperMonkey, deixe-a sempre visível, e vá em "Userscripts instalados"

- Clique no símbolo de + (mais) e copie o seguinte texto:

```
// ==UserScript==
// @name         Brasil r/place Template
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  try to take over the canvas!
// @author       oralekin, LittleEndu
// @match        https://hot-potato.reddit.com/embed*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=reddit.com
// @grant        none
// ==/UserScript==
if (window.top !== window.self) {
    window.addEventListener('load', () => {
        document.getElementsByTagName("mona-lisa-embed")[0].shadowRoot.children[0].getElementsByTagName("mona-lisa-canvas")[0].shadowRoot.children[0].appendChild(
            (function () {
                const i = document.createElement("img");
                i.src = "https://raw.githubusercontent.com/Tetizera/place-rbrasil2022/main/image.png";
                i.onload = () => {
                    if (i.width === i.height) {
                        i.style = "position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 1000px;height: 1000px;";
                    } else {
                        i.style = "position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 2000px;height: 1000px;";
                    }
                };
                return i;
            })())
    }, false);
}
```
Note que o script pode ser atualizado por vários motivos, então pra garantir, entre no Discord e veja TUDO no #rplace-anúncios. Aliás, procure um emoji de bandeira do Brasil e clique nele para receber anúncios dos mods e responsáveis.

- Se tiver dúvidas, pingue @Tet#0001

---

This is a simple overlay made by r/brasil Discord users to make our life easier when coordinating actions.

### INSTRUCTIONS:

- Install TamperMonkey on Chrome or ViolentMonkey on Firefox
  - TamperMonkey for Chrome https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en
  - OPERA - https://addons.opera.com/en/extensions/details/tampermonkey-beta/
  - ViolenyMonkey for Firefox - https://addons.mozilla.org/en-US/firefox/addon/violentmonkey/

- Go to your Extension tab, activate it and allow it to be always visible, and go to "Installed Usercripts"

- Click on the + symbol on the right corner and copy the following code:

```
// ==UserScript==
// @name         Brasil r/place Template
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  try to take over the canvas!
// @author       oralekin, LittleEndu
// @match        https://hot-potato.reddit.com/embed*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=reddit.com
// @grant        none
// ==/UserScript==
if (window.top !== window.self) {
    window.addEventListener('load', () => {
        document.getElementsByTagName("mona-lisa-embed")[0].shadowRoot.children[0].getElementsByTagName("mona-lisa-canvas")[0].shadowRoot.children[0].appendChild(
            (function () {
                const i = document.createElement("img");
                i.src = "https://raw.githubusercontent.com/Tetizera/place-rbrasil2022/main/image.png";
                i.onload = () => {
                    if (i.width === i.height) {
                        i.style = "position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 1000px;height: 1000px;";
                    } else {
                        i.style = "position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 2000px;height: 1000px;";
                    }
                };
                return i;
            })())
    }, false);
}
```

FYI: The script's code may be changed for a variety of reasons. Because of that, our "diplomats" (Mostly Tet#0001), will contact people on their Discords and subreddits in necessary. Feel free to ping me if I'm in your subreddit's server.

---

# r/place 2022 color HEX codes (as seen on Wikipedia and r/place HTML code)

[image on Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Place_2022_swatches.svg/662px-Place_2022_swatches.svg.png)

red - #FF4500

orange - #FFA800

yellow - #FFD635

dark green - #00A368

light green - #7EED56

dark blue - #2450A4

blue - #36980EA

light blue - #51E9F4

dark purple - #811E9F

purple - #B44AC0

light link - #FF99AA

brown - #9C6926

black - #000000

dark gray - #898D90

light gray - #D4D7D9

white - #FFFFFF
