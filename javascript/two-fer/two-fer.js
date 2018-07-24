var TwoFer = function () {};

TwoFer.prototype.twoFer = function (who) {
  let name;
  if (who === undefined) {
    name = "you";
  } else {
    name = who;
  }
  return `One for ${name}, one for me.`
};

module.exports = TwoFer;
