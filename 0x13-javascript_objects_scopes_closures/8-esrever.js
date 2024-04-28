#!/usr/bin/node
exports.esrever = function (list) {
  const copy = list.slice(0, list.length);
  for (let i = 0; i < list.length; i++) {
    list[i] = copy[(list.length - 1) - i];
  }
  return list;
};
