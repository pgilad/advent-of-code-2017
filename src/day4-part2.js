const fs = require('fs');

const input = fs.readFileSync('./day4.txt', { encoding: 'utf8' });
const lines = input.split('\n');

const total_valid = lines.reduce((total, line) => {
    if (!line) {
        return total;
    }
    const words = line.split(' ');
    if (!words || words.length === 0) {
        return total;
    }
    const sorted = words.map(word => word.split('').sort().join(''));

    const dict = sorted.reduce((map, word) => {
        map[word] = (map[word] || 0) + 1
        return map;
    }, {});
    const is_invalid = Object.keys(dict).some(word => dict[word] > 1);
    const value = is_invalid ? 0 : 1
    return total + value;
}, 0);

console.log(total_valid);
