let DnaTranscriber = function() {
};

DnaTranscriber.prototype.toRna = function (dna) {
    const dnaRna = {
        G: "C",
        C: "G",
        T: "A",
        A: "U"
    };
    let rna = "";
    for (let i = 0; i < dna.length; i++) {
        if (!dnaRna.hasOwnProperty(dna[i])){
                throw new Error("Invalid input");
        } else {
            rna += dnaRna[dna[i]];
        }
    }
    return rna;
};

module.exports = DnaTranscriber;