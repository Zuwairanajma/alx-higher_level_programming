#!/usr/bin/node

const dict = require('./101-data.js').dict;

const dict1 = Object.entries(dict);
const uniqID = [...new Set(Object.values(dict))];
const newDict = {};

for (const ID in uniqID) {
  const idList = [];
  for (const i in dict1) {
    if (dict1[i][1] === uniqID[ID]) {
      idList.unshift(dict1[i][0]);
    }
  }
  newDict[uniqID[ID]] = idList;
}

console.log(newDict);
