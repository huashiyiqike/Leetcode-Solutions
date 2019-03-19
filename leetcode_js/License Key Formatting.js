/**
 * @param {string} S
 * @param {number} K
 * @return {string}
 */
var licenseKeyFormatting = function(S, K) {
  s = S.split('-').join('');
  let j = s.length % K;
  let res = [];
  if (j !== 0)    res = [s.slice(0, j)];
  
  for (let i = j; i <= s.length - K; i += K) {
      res.push(s.slice(i, i+K));
  }
  return res.join('-').toUpperCase();
};