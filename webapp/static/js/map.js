$('document').ready(function(){

    console.log('inside map js')

    var m_width = $('#map').width(),
    width = 938,
    height = 500,
    country,
    state;

    var projection = d3.geo.mercator()
        .scale(150)
        .translate([width / 2, height / 1.5]);

    var path = d3.geo.path()
        .projection(projection);

    var svg = d3.select('#map').append('svg')
        .attr('preserveAspectRatio', 'xMidYMid')
        .attr('viewBox', '0 0 ' + width + " " + height)
        .attr('width', m_width)
        .attr('height', m_width * height / width);

    svg.append('rect')
        .attr('class', 'background')
        .attr('width', width)
        .attr('height', height)
    //.on('click', country_clicked);

    var g = svg.append('g');

    load_country(g,path);

    g.selectAll(["#states", "#cities"]).remove();
    state = null;

    var xyz = get_xyz(d);
    country = d;

      //load states
    load_city(g,path);

    $(window).resize(function() {
        var w = $("#map").width();
        svg.attr("width", w);
        svg.attr("height", w * height / width);
    });

});

function load_country(g,path) {
    //setup country
    d3.json('/static/maps/countries.topo.json', function(error, topology) {
    g.append('g')
      .attr('id', 'countries')
      .selectAll('path')
      .data(topology.features)
      .enter()
      .append('path')
      .attr('id', function(d) { return d.id; })
      .attr('d', path)
    });
}//end load country

function load_state(g, path) {

      d3.json('/static/maps/states.topo.json', function(error, topology) {
        g.append('g')
          .attr('id', 'states')
          .selectAll('path')
          .data(topology.features)
          .enter()
          .append('path')
          .attr('id', function(d) { return d.id; })
          .attr('class', 'active')
          .attr('d', path)

        zoom(xyz);
        g.selectAll('#' + d.id).style('display', 'none');
      });

}

function load_city() {
  d3.json("/static/maps/cities.topo.json", function(error, topology) {
      g.append("g")
        .attr("id", "cities")
        .selectAll("path")
        .data(topology.features.filter(function(d) { return state_name == d.properties.state; }))
        .enter()
        .append("path")
        .attr("id", function(d) { return d.properties.name; })
        .attr("class", "city")
        .attr("d", path.pointRaditopology(20 / xyz[2]));

      zoom(xyz);
}
