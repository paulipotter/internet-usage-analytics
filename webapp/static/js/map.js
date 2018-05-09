$('document').ready(function(){

    console.log('map')

    var width = 900;
    var height = 600;

    var projection = d3.geo.mercator();

    var svg = d3.select("#map").append("svg")
      .attr("width", width)
      .attr("height", height);
    var path = d3.geo.path()
      .projection(projection);
    var g = svg.append("g");


    //create variables
    // console.log("before");
    var m_width = $("#map").width(),
        country,
        state;
        // console.log("w");

    var svg = d3.select("#map").append("svg")
        .attr("preserveAspectRatio", "xMidYMid")
        .attr("viewBox", "0 0 " + width + " " + height)
        .attr("width", m_width)
        .attr("height", m_width * height / width);

    svg.append("rect")
        .attr("class", "background")
        .attr("width", width)
        .attr("height", height)
// console.log("svg");
    var g = svg.append("g");

    d3.json("/static/maps/countries.topo.json", function(error, topology) {
      g.append("g")
        .attr("id", "countries")
        .selectAll("path")
        .data(topology.features)
        .enter()
        .append("path")
        .attr("id", function(d) { return d.id; })
        .attr("d", path)
    });
});
    /*
console.log("d3 json");
    d3.json("/static/maps/states.topo.json", function(error, topology) {
      g.append("g")
        .attr("id", "states")
        .selectAll("path")
        .data(topology.features)
        .enter()
        .append("path")
        .attr("id", function(d) { return d.id; })
        .attr("class", "active")
        .attr("d", path)
      });

     //zoom(xyz,g,path);

     country_code = "PRY"
     //state_name = state.properties.name;

     d3.json("/static/maps/cities.topo.json", function(error, topology) {
       g.append("g")
         .attr("id", "cities")
         .selectAll("path")
         .data(topology.features)
         .enter()
         .append("path")
         .attr("id", function(d) { return d.properties.name; })
         .attr("class", "city")
         .attr("d", path.pointRadius(20 / xyz[2]));

         });



    $(window).resize(function() {
      var w = $("#map").width();
      svg.attr("width", w);
      svg.attr("height", w * height / width);
    });

});
function zoom(xyz,g,path) {
  g.transition()
    .duration(750)
    .attr("transform", "translate(" + projection.translate() + ")scale(" + xyz[2] + ")translate(-" + xyz[0] + ",-" + xyz[1] + ")")
    .selectAll(["#countries", "#states", "#cities"])
    .style("stroke-width", 1.0 / xyz[2] + "px")
    .selectAll(".city")
    .attr("d", path.pointRadius(20.0 / xyz[2]));
}

function get_xyz(d,path) {
  var bounds = path.bounds(d);
  var w_scale = (bounds[1][0] - bounds[0][0]) / width;
  var h_scale = (bounds[1][1] - bounds[0][1]) / height;
  var z = .96 / Math.max(w_scale, h_scale);
  var x = (bounds[1][0] + bounds[0][0]) / 2;
  var y = (bounds[1][1] + bounds[0][1]) / 2 + (height / z / 6);
  return [x, y, z];
}*/
