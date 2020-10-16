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
const str = 'cacaaaaacacaaaaa';
const key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';
const buffer = Buffer.from(str);
const b_key = Buffer.from(key);
//console.log(buf2hex(buffer));
//console.log(buf2hex(b_key));
const ciph = gostEngine.getGostCipher({name: 'GOST R 34.13', block: 'ECB'});
//console.log(ciph);
//const buffer2 = ;
let buffArr = ciph.encrypt(b_key, buffer);
console.log(buf2hex(buffArr));
buffArr = ciph.decrypt(b_key, buffArr);
console.log(buf2hex(buffArr));

console.log('----------------')
var s = hex2buf('54e1b572408a705054e1b572408a7050');
console.log(buf2hex(s));
dt = ciph.decrypt(b_key, s);
console.log(buf2hex(dt));







//console.log(gostEngine.getGostCipher);
//gostCrypto.subtle.decrypt('GOST R 34.12', buffer, key).then((arrayBuffer) => {
//    console.log(Buffer.from(arrayBuffer).toString('hex'));
//});