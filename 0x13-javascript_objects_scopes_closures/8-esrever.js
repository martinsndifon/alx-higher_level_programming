#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length - 1;
  const newlist = [];
  let j = 0;

  for (let i = len; i >= 0; i--) {
    newlist[j] = list[i];
    j++;
  }
  return (newlist);
};
