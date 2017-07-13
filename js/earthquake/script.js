/**
* Created by tanktankette on 6/28/17.
*/
const map = new ol.Map({
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

const col = new ol.Collection();

function read(){
    col.clear();
    $.ajax({
        url: "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson",
        success: function (data) {
            for (i in data.features) {
                if (data.features[i].properties.mag > 0) {
                    const opac = (data.features.length - i) * .9 / data.features.length;
                    const size = data.features[i].properties.mag * 20000;
                    const lon = data.features[i].geometry.coordinates[0];
                    const lat = data.features[i].geometry.coordinates[1];
                    const feature = new ol.Feature(new ol.geom.Circle(ol.proj.fromLonLat([lon, lat]), size, "XY"));

                    feature.setStyle(new ol.style.Style({
                        fill: new ol.style.Fill({color: [200, 200, 255, opac]}),
                        stroke: new ol.style.Stroke({
                            color: [50, 50, 100, opac],
                            width: 2
                        })
                    }));
                    col.push(feature);
                }
            }
        }
    });
}
read();
setInterval(read, 300000);
 const vecSource = new ol.source.Vector({
     features: col
 });
 const vecLayer = new ol.layer.Vector({
     source: vecSource
 });
map.addLayer(vecLayer);