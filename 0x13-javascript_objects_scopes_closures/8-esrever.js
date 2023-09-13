exports.esrever = function (list) {
  const reversedList = [];
  for (const element of list) {
    reversedList.unshift(element);
  }
  return reversedList;
}