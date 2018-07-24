var RLE = new Object();

RLE.encode = function (str) {
    let count = 1;
    let encoded = "";
    let currentLetter = str[0];
    for (let i = 1; i < str.length; i++) {
        if (str[i] === currentLetter) {
            count++;
        } else {
            if (count > 1) {
                encoded += count + currentLetter;
                currentLetter = str[i];
                count = 1;
            } else {
                encoded += currentLetter;
                currentLetter = str[i];
            }
        }
    }
    if (encoded !== "") {
        if (count > 1) {
            encoded += count + currentLetter;
        } else {
            encoded += currentLetter;
        }
    }
    return encoded;
};

RLE.decode = function (str) {
    let decoded = "";
    if (str === "") {
        return decoded;
    }
    // if num then repeat letter next to it, num times 
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        if (!isNaN(str[i])) {
            count = Number(str[i]);
            for (let j = 0; j < count; j++) {
                decoded += str[i+1];
            }
        } else if (isNaN(str[i-1])) {
            decoded += str[i];
        }
    }
    return decoded;
};

module.exports = RLE;