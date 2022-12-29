#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  function occurs (count, current) {
    return (current === searchElement ? count + 1 : count);
  }
  return list.reduce(occurs, 0);
};
/* alternatively in one line of code
 *
 * return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
 *  };
 */
