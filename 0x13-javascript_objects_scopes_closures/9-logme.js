#!/usr/bin/node

let numOfArgsPrinted = 0;

exports.logMe = function (item) {
  console.log(`${numOfArgsPrinted}:`, item);
  numOfArgsPrinted += 1;
};
