/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
    // for keeping track of the open parentheses
    openParens = [];

    // iterate through each character of the string
    for(let i = 0; i < str.length; i++) {
        // push open parentheses found to array
        if(str[i] == '(') { openParens.push(str[i]); }
        
        // if a closing parens is encountered before an opening parens, it auto fails
        else if(str[i] == ')' && openParens.length == 0) { return false; }

        // for each close, pop an open parens from the array
        else if(str[i] == ')') { openParens.pop(); }

    }

    // if any open parens remain after for loop executes, string is invalid
    if (openParens.length != 0) {
        return false
    }

    // if it made it this far, it's valid!
    return true;
}

/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const b_str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const b_expected1 = true;

const b_str2 = "D(i{a}l[ t]o)n{e";
const b_expected2 = false;

const b_str3 = "A(1)s[O (n]0{t) 0}k";
const b_expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
// for keeping track of the open parentheses
    openParens = [];
    openSquares = [];
    openCurlies = [];

    console.log(str);

    // iterate through each character of the string
    for(let i = 0; i < str.length; i++) {
        // push open parentheses found to array
        if(str[i] == '(') { openParens.push(str[i]); }
        if(str[i] == '[') { openSquares.push(str[i]); }
        if(str[i] == '{') { openCurlies.push(str[i]); }
        
        // if a closing parens is encountered before an opening parens, it auto fails
        else if(str[i] == ')' && openParens.length == 0) { return false; }
        else if(str[i] == ']' && openSquares.length == 0) { return false; }
        else if(str[i] == '}' && openCurlies.length == 0) { return false; }

        // for each close, pop an open parens from the array
        else if(str[i] == ')') { openParens.pop(); }
        else if(str[i] == ']') { openSquares.pop(); }
        else if(str[i] == '}') { openCurlies.pop(); }

        // Print working status of arrays
        console.log(`openParens: ${openParens}\nopenSquares: ${openSquares}\nopenCurlies: ${openCurlies}`)
    }

    // if any open parens remain after for loop executes, string is invalid
    if (openParens.length != 0 || openSquares != 0 || openCurlies != 0) {
        return false
    }

    // if it made it this far, it's valid!
    return true;
}

console.log(bracesValid(b_str1));
console.log(bracesValid(b_str2));
console.log(bracesValid(b_str3));