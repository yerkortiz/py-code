// ==UserScript==
// @name    tarea3Cripto
// @author  Yerko Ortiz
// @version 0.1
// @descripcion buenas noches, cómo le va
// @match       https://yerkortiz.github.io/py-code/index
// @require     https://raw.githubusercontent.com/rudonick/crypto/master/gostDigest.js
// @require     https://raw.githubusercontent.com/rudonick/crypto/master/gostRandom.js
// @require     https://raw.githubusercontent.com/rudonick/crypto/master/gostKeys.js
// @require     https://raw.githubusercontent.com/rudonick/crypto/master/gostSign.js
// @require     https://raw.githubusercontent.com/rudonick/crypto/master/gostCipher.js
// @require     https://raw.githubusercontent.com/rudonick/crypto/master/gostEngine.js
// @require     https://raw.githubusercontent.com/rudonick/crypto/master/gostCoding.js

// ==/UserScript==

(function decryp() {
    'use strict';
    function buf2hex(buffer) { // buffer is an ArrayBuffer
        return Array.prototype.map.call(new Uint8Array(buffer), x => ('00' + x.toString(16)).slice(-2)).join('');
    }
    function hex2buf(hex) {
        var buffer = new ArrayBuffer(hex.length / 2);
        var array = new Uint8Array(buffer);
        var k = 0;
        for (var i = 0; i < hex.length; i +=2 ) {
            array[k] = parseInt(hex[i] + hex[i+1], 16);
            k++;
        }
        return buffer;
    }
    function toHex(str) {
    var hex = '';
    var i = 0;
    while(str.length > i) {
        hex += ''+str.charCodeAt(i).toString(16);
        i++;
    }
    return hex;
    }

    var key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';
    var ct = document.getElementsByClassName("kuznyechik")[0].id;
    var aux = document.getElementsByClassName("kuznyechik");
    //const ciph = gostEngine.getGostCipher({name: 'GOST R 34.13', block: 'ECB'})
    const b_key = hex2buf(toHex(key));
    const b_ct = hex2buf(ct);
    const dt = decryptECB(b_key, b_ct);
    const dt = b_ct
    aux[0].innerHTML = 'mensaje cifrado: ' + buf2hex(dt);
})();