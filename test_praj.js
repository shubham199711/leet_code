// function aa() {
//     let totalPair = 0
//     let pairs = {}
//     const input_array = [1, 1, 1, 3, 3, 6, 1]
//     input_array.forEach((item) => {
//         if (pairs[`${item}`] == undefined || pairs[`${item}`] == 0) {
//             pairs[`${item}`] = 1;
//         } else {
//             pairs[`${item}`] += 1;
//             if (pairs[`${item}`] == 2) {
//                 totalPair += 1
//                 pairs[`${item}`] = 0;
//             }
//         }
//     })
//     return totalPair
// }


function getCombn(arr) {
    if (arr.length == 1) {
        return arr[0];
    } else {
        var ans = [];
        var otherCases = getCombn(arr.slice(1));
        for (var i = 0; i < otherCases.length; i++) {
            for (var j = 0; j < arr[0].length; j++) {
                ans.push(arr[0][j] + otherCases[i]);
            }
        }
        return ans;
    }
}

function aa(input_num) {
    const keypadMap = {
        1: ["1"],
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
        0: ["0"]
    };

    const digits = input_num.toString()
    if (digits.length === 1) {
        return keypadMap[digits];
    }
    const words = [];
    for (const digit of digits) {
        const letters = keypadMap[digit];
        words.push(letters);
    }
    return [...new Set(getCombn(words))].sort();
}


// assertArrayEquality(keypadWords('79'),
//     ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"])
// console.log(aa(79))
// console.log(aa(234))
// console.log(aa(2))


function king(n) {
    var a = new Array(n);
    var position = 0;
    if (n === 1) return 1
    for (let i = 0; i < n; i++) {
        a[i] = i + 1;
    }
    while (a.length > 1) {
        position++;
        position = position % (a.length);
        a.splice(position, 1);
    }
    return a[0];
}
// console.log(king(1));
// console.log(king(2));
// console.log(king(3));
// console.log(king(4));
console.log(king(5));


// assert(king(1), 1);
// assert(king(2), 1);
// assert(king(3), 3);
// assert(king(4), 1);
// assert(king(5), 3);