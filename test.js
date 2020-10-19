const { gostCrypto, gostEngine } = require('node-gost-crypto');
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

const key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';

const b_key = Buffer.from(key);

const ciph = gostEngine.getGostCipher({name: 'GOST R 34.13', block: 'ECB'});


console.log('----------------')
var s = hex2buf('85e9ca7a6a71001c');
console.log('mensaje encriptado:' + buf2hex(s));
dt = ciph.decrypt(b_key, s);
console.log('mensaje desencriptado:' + buf2hex(dt));
