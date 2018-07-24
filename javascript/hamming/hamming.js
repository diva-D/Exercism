let Hamming = function() {
};

Hamming.prototype.compute = function (strandA, strandB) {
    let hammingDistance = 0;
    let strandLength = strandA.length;
    if (strandA.length !== strandB.length) {
        throw new Error("DNA strands must be of equal length.")
    } else {
        for (let i = 0; i < strandLength; i++) {
            if (strandA[i] !== strandB[i]) {
                hammingDistance++;
            }
        }
    }
    return hammingDistance;
};

module.exports = Hamming;