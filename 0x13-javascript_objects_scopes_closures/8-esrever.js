#!/usr/bin/node

// we are instructed not to use the built-in reverse method
exports.esrever = function (list) {
  const lastIndex = list.length - 1;
  const revList = [];
  let index = 0;
  for (let i = lastIndex; i >= 0; i--) {
    revList[index] = list[i];
    index += 1;
  }
  return revList;
};
