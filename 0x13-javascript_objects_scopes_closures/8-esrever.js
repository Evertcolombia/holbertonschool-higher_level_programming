#!/usr/bin/node

exports.esrever = function (list) {
  const reverse = [];
  let i = list.length - 1;
  for (; i >= 0; i--) {
    reverse.push(list[i]);
  }
  return (reverse);
};
