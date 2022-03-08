//  William Sigala
//  3/9/22
//  ID# 0022

//  CSE 3302
//  Lab 2

//  1
let inputtable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; //  array with numbers between 1 and 10

//  2
//  a
let fiveTable = inputtable.map((val) => {
  return val * 5 <= 51 ? val * 5 : null;
}); //  Uses values in inputtable to create a set of multiples of 5 between 1 and 51
//  b
let thirteenTable = inputtable.map((val) => {
  return val * 13 <= 131 ? val * 13 : null;
}); //  Uses values in inputtable to create a set of multiples of 13 between 13 and 131
//  c
let squaresTable = inputtable.map((val) => val * val);
//  Uses values in inputtable to create a set of squares from each value

//  3
function oddFives(it = 5, vals = []) {
  return vals.push(it) < 10 ? oddFives(it + 10, vals) : vals;
} //  Recursively gets all the values that are multiples of 5 and odd and returns the set

//  4
function sumEvenSevens(it = 14, sum = 0) {
  return it <= 100 ? sumEvenSevens(it + 14, sum + it) : sum;
} //  Sums multiples of 7 that are even between 1 and 100 recursively

//console.log(sumEvenSevens());
//  5
let cylinder_volume = (r) => (h) => {
  return 3.14 * r * r * h;
}; // Uses the radius as a parameter and returns a function that uses height as a parameter.

//  a
let volume = cylinder_volume(5); //  Setting radius to 5 for cylinder volume
volume(10); //  Uses function above and passes height = 10 as arg
//  b
volume(17); //  Uses volume function and passes height = 17 as arg
//  c
volume(11); //  Uses volume function and passes height = 11 as arg

//  6
let makeTag = function (beginTag, endTag) {
  return function (textcontent) {
    return beginTag + textcontent + endTag;
  };
};

let table = makeTag("<table>\n", "</table>\n"); //  generates table outer tag
let tableRow = makeTag(" <tr>\n", " </tr>\n"); //  inner row tag
let content1 = makeTag("  <th>", "</th>\n"); // row content tag
let content2 = makeTag("  <td>", "</td>\n"); // row content tag

console.log(
  table(
    tableRow(content1("hi")) +
      tableRow(content2("William") + content2("Sigala") + content2("CSE3302"))
  )
); //  Passes two content tags to oddFives row tags. Puts both in table tag

//  8
function even_odd(even) {
  let curried_func = (multiple, it = 0, vals = []) => {
    if (!it) it = even ? multiple * 2 : multiple;
    if (it <= 100) vals.push(it);
    else return vals;
    return curried_func(multiple, it + 2 * multiple, vals);
  };
  return curried_func;
} //  First pass even = true or even = false, then returns function that takes multiple as argument.
//  That function returns the set of even/odd multiples between 1 and 100

let multiple = even_odd(true);
let even_fives = multiple(5);
console.log(even_fives);
