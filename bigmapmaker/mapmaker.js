// https://www.google.co.il/maps/@32.083,34.8,16z
var WebPage = require('webpage');
var page = WebPage.create();
page.viewportSize = { width: 1200, height: 800 };

/*
Some Notes:
	2500 X 5000 px is equal to 82x170 cm
	30 px is roughly equal to 1 cm
	30 px ~= 1 cm
	500px ~= 16.666 cm
*/
zoomParams = {
	14: { x: 0.043, y: 0.0365 },
	15: { x: 0.02148, y: 0.0182 },
	16: { x: 0.01075, y: 0.00908 },
	17: { x: 0.00537, y: 0.00454 },
	18: { x: 0.00268, y: 0.00227 },
}

function handle_page(y, x, zoom){
	yCoord = baseY - zoomParams[zoom]['y']*row;
	xCoord = baseX + zoomParams[zoom]['x']*column;
    page.open('https://maps.google.co.il/maps?t=m&ll='+yCoord+','+xCoord+'&z='+zoom+'&output=classic&dg=opt&hl=en',function(){
    	page.clipRect = { top: 100, left: 500, width: 500, height: 500 };
        page.render('images/map_('+pad(y)+","+pad(x)+').png', {format: 'png', quality: 100});
        setTimeout(next_page,100);
    });
}

function next_page(){
	// Exit Condition
    if(column == nX){phantom.exit(0);}

    // Log to console
    console.log("Processing map segment ("+row+","+column+")");

    // Handle page
    handle_page(row, column, zoom);
    // Set up new parameters
    row++;
    if (row == nY) { row = 0; column++; }
}

points = {
	'TLV Port Store 17': {'y': 32.102981, 'x': 34.768329},
	'TLV Port Store 18': {'y': 32.101109, 'x': 34.770003},
	'Tel Aviv': {'y': 32.1, 'x': 34.763},
	'Tel Aviv East': {'y': 32.1, 'x': 34.806},
	'Tel Aviv South': {'y': 32.04552, 'x': 34.763},
	'Petach Tikva': {'y': 32.099015, 'x': 34.847034},
	'Holon Bat Yam': {'y': 32.031553, 'x': 34.738268},
};

// Set up the first page (and parameters)
nY = 5, nX = 5;
baseY = points['TLV Port Store 18']['y'], baseX = points['TLV Port Store 18']['x'];
// baseY = 32.1388052, baseX = 34.8236558;
zoom = 18;
row = 0, column = 0;
setTimeout(next_page,100);

// Aux Functions
function pad(n, width) {
	width = width || 3;
	n = n + '';
	return n.length >= width ? n : new Array(width - n.length + 1).join('0') + n;
}
