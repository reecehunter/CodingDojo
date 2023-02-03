function flatten(arr2d) {
    var flat = [];

    for(var row = 0; row < arr2d.length; row++) {
        for(var x = 0; x < arr2d[row].length; x++) {
            flat.push(arr2d[row][x]);
        }
    }

    return flat;
}
    
var result = flatten( [ [2, 5, 8], [3, 6, 1], [5, 7, 7] ] );

// we expect to get back [2, 5, 8, 3, 6, 1, 5, 7, 7]
console.log(result);

