function getOverallHeight() {

  var uiheight = document.getElementsByName("uiheight");
  for(var i in uiheight) {

    if(uiheight[i].checked) {

      return parseFloat(uiheight[i].value);
    }
  }
  return -1; // Invalid Value
}
  
function getOrientation() {
  var uiOrient = document.getElementsByName("uiOrient");
  for(var i in uiOrient) {
    if(uiOrient[i].checked) {

      return parseInt(i)+2;
    }
  }
  return -1; // Invalid Value
}

function getGlazingAreaDistribution() {
  var uiGlazingAreaDist = document.getElementsByName("uiGlazingAreaDist");
  for(var i in uiGlazingAreaDist) {
    if(uiGlazingAreaDist[i].checked) {
      return parseInt(i);
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimateHeatingLoad() {
  console.log("Estimate Heating Load clicked");
  var relcomp = document.getElementById("uiRelComp");
  console.log(relcomp.value);
  var wallarea = document.getElementById("uiWallArea");
  var roofarea = document.getElementById("uiRoofArea");
  var height = getOverallHeight();
  console.log(height);
  var orientation = getOrientation();
  var glazingarea = document.getElementById("uiGlazingArea");
  var glazingareadist = getGlazingAreaDistribution();
  var estHL = document.getElementById("uiEstimatedHeatingLoad");
  console.log(estHL);

  var url = "http://127.0.0.1:5000/predict_heating_load"; //Use this if you are NOT using nginx which is first 7 tutorials
  
  $.post(url, {

    relative_compactness: parseFloat(relcomp.value),
    wall_area: parseFloat(wallarea.value),
    roof_area: parseFloat(roofarea.value),
    overall_height: height,
    orientation: orientation,
    glazing_area: parseFloat(glazingarea),
    glazing_area_distribution: glazingareadist
        
  },function(data, status) {
    console.log(data.estimated_heating_load);
    estHL.innerHTML = "<h2>" + data.estimated_heating_load.toString() + "</h2>";;
    console.log(status);
  });
}

function onClickedEstimateCoolingLoad() {
  console.log("Estimate Cooling Load clicked");
  var relcomp = document.getElementById("uiRelComp");
  console.log("Estimate Cooling Load clicked");

  var wallarea = document.getElementById("uiWallArea");
  var roofarea = document.getElementById("uiRoofArea");
  var height = getOverallHeight();

  var orientation = getOrientation();
  var glazingarea = document.getElementById("uiGlazingArea");
  var glazingareadist = getGlazingAreaDistribution();
  var estCL = document.getElementById("uiEstimatedCoolingLoad");

  var url2 = "http://127.0.0.1:5000/predict_cooling_load"; //Use this if you are NOT using nginx which is first 7 tutorials
  
  $.post(url2, {

    relative_compactness: parseFloat(relcomp.value),
    wall_area: parseFloat(wallarea.value),
    roof_area: parseFloat(roofarea.value),
    overall_height: height,
    orientation: orientation,
    glazing_area: parseFloat(glazingarea),
    glazing_area_distribution: glazingareadist
        
  },function(data, status) {

    console.log(data.estimated_cooling_load);
    estCL.innerHTML = "<h2>" + data.estimated_cooling_load.toString() + "</h2>";
    console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/hello";
}

window.onload= onPageLoad;




