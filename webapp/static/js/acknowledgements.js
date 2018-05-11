$(document).ready(function(){
	// register our custom symbols to nvd3
	// make sure your path is valid given any size because size scales if the chart scales.
	//console.log("NODES "+nodes["nodes"])
	console.log(randomData(4,40))
	nv.utils.symbolMap.set('thin-x', function(size) {
		size = Math.sqrt(size);
		return 'M' + (-size/2) + ',' + (-size/2) +
				'l' + size + ',' + size +
				'm0,' + -(size) +
				'l' + (-size) + ',' + size;
	});
	// create the chart
	var chart;
	nv.addGraph(function() {
		chart = nv.models.scatterChart()
			.showDistX(true)
			.showDistY(true)
			.useVoronoi(true)
			.color(d3.scale.category10().range())
			.duration(300)
		;
		chart.dispatch.on('renderEnd', function(){
			console.log('render complete');
		});
		chart.xAxis.tickFormat(d3.format('d'));
		chart.yAxis.tickFormat(d3.format('d'));
		d3.select('#test1 svg')
			.datum(nodes)
			.call(chart);
		nv.utils.windowResize(chart.update);
		chart.dispatch.on('stateChange', function(e) { ('New State:', JSON.stringify(e)); });
		return chart;
	});
})


function randomData(groups, points) { //# groups,# points per group
	// smiley and thin-x are our custom symbols!
	var data = [],
		shapes = [ 'circle'],
		random = d3.random.normal();
	for (i = 0; i < groups; i++) {
		data.push({
			key: 'Group ' + i,
			values: []
		});
		for (j = 0; j < points; j++) {
			data[i].values.push({
				x: random(),
				y: random(),
				size: Math.round(Math.random() * 100) / 100,
				shape: shapes[j % shapes.length]
			});
		}
	}
	//console.log(data)
	return data;
}
