/**
 * Created by tanktankette on 6/27/17.
 */
function encrypt(str, key){
    str = str.toLowerCase();
    let encode = "";
    for(c in str){
        let temp = str.charCodeAt(c);
        if(temp !== 32) {
            temp += key;
            if (temp > 122) {
                temp = temp - 26;
            } else if (temp < 97) {
                temp = temp + 26;
            }
        }
        encode = encode.concat(String.fromCharCode(temp));
    }
    return encode;
}

function decrypt(str, key){
    return encrypt(str, -key);
}

let code = encrypt("Hello how have you been", 5);
console.log(code);
code = decrypt(code, 5);
console.log(code);