/**
 * Created by tanktankette on 6/28/17.
 */
var map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          })
        ],
        view: new ol.View({
          center: ol.proj.fromLonLat([37.41, 8.82]),
          zoom: 4
        })
      });

var col = new ol.Collection();
$.ajax({
        url: "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson",
        success: function(data){
            for (i in data.features){
                if (data.features[i].properties.mag > 0) {
                    var opac = (data.features.length - i) / data.features.length;
                    var size = data.features[i].properties.mag * 10;
                    var lon = data.features[i].geometry.coordinates[0];
                    var lat = data.features[i].geometry.coordinates[1];
                    var color = "#000000";
                    console.log(color);
                    var feature = new ol.Feature({
                        geometry: new ol.geom.Point(ol.proj.fromLonLat([lon, lat]), "XY"),
                        style: new ol.style.Circle({
                            radius: size,
                            // fill: new ol.style.Fill([0,9,9,1])
                        })
                    });
                    col.push(feature);
                }
            }
        }
    });
console.log(col);
 var vecSource = new ol.source.Vector({
     features: col
 });
console.log("help");
 var vecLayer = new ol.layer.Vector({
     source: vecSource
 });
console.log("help");
map.addLayer(vecLayer);
console.log("help");