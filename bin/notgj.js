const osmtogeojson = require("osmtogeojson");
const DOMParser = require("xmldom").DOMParser;
const path = require("path");
const fs = require("fs");

var ready,
  filePath,
  flatProperties,
  outputPath;

try {
  filePath = process.argv[2];
  outputPath = process.argv[3];
  flatProperties = Boolean(process.argv[4] === "True");
  console.log('flatProperties: ', flatProperties);
  ready = true;
} catch (err) {
  console.error(err);
  console.log('Not enough arguments declared');
}

if (ready) {
  const polygonsConfig = require(path.resolve(__dirname, ".polygonFeatures.config.json"));
  const uninterestingTags = require(path.resolve(__dirname, ".uninterestingTags.config.json"));
  fs.readFile(filePath, "utf-8", (err, data) => {
      if (err) throw err;
      console.log('xml input file readed');
      const geojson = osmtogeojson(new DOMParser().parseFromString(data, 'text/xml'), {
        polygonFeatures: polygonsConfig,
        flatProperties: flatProperties,
        uninterestingTags: uninterestingTags
      });
      console.log('geojson data generated');
      fs.writeFile(outputPath, JSON.stringify(geojson), (err) => {
          if (err) throw er;
          console.log(outputPath + ' created with exit');
      });
  });  
}