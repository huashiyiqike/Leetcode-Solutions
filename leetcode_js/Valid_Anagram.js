/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    return s.split('').sort().toString() === t.split('').sort().toString();
//    var sortfun = function (item1, item2) {
//        if (item1.attr < item2.attr)
//            return -1;
//        if (item1.attr > item2.attr)
//            return 1;
//        return 0;
//    }
//    s.split('').sort(sortfun).join();
//    t.split('').sort(sortfun).join();
//    return s == t;
};
console.log(isAnagram("abc", "cba"));
console.log(isAnagram("abc", "cbae"));

function isAnagram(s, t) {
    const map = {};
    s.split('').map(c => map[c] = map[c] ? map[c] + 1 : 1);
    t.split('').map(c => map[c] = map[c] ? map[c] - 1 : -1);
    return Object.keys(map).every(k => map[k] === 0);
}