#!/usr/bin/node

exports.addMeMaybe = function (number, thefunction) {
  const nb = number + 1;
  thefunction(nb);
};
