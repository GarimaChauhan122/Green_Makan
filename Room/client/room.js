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
  var wallarea = document.getElementById("uiWallArea");
  var roofarea = document.getElementById("uiRoofArea");
  var height = getOverallHeight();
  var orientation = getOrientation();
  var glazingarea = document.getElementById("uiGlazingArea");
  var glazingareadist = getGlazingAreaDistribution();
  var estHL = document.getElementById("uiEstimatedHeatingLoad");

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
    if (data && data.estimated_heating_load !== undefined && data.estimated_heating_load !== null) {
      estHL.innerHTML = "<h2>" + data.estimated_heating_load.toString() + "yay</h2>";
    } else {
      // Use a default value when data.estimated_heating_load is null
      var defaultValue = "24.5";
      estHL.innerHTML = "<h2>" + defaultValue + "</h2>";
    }
    
    console.log(status);
  });
}

function onClickedEstimateCoolingLoad() {
  console.log("Estimate Cooling Load clicked");
  var relcomp = document.getElementById("uiRelComp");
  var wallarea = document.getElementById("uiWallArea");
  var roofarea = document.getElementById("uiRoofArea");
  var height = getOverallHeight();
  var orientation = getOrientation();
  var glazingarea = document.getElementById("uiGlazingArea");
  var glazingareadist = getGlazingAreaDistribution();
  var estCL = document.getElementById("uiEstimatedCoolingLoad");

  var url = "http://127.0.0.1:5000/predict_cooling_load"; //Use this if you are NOT using nginx which is first 7 tutorials
  
  $.post(url, {

    relative_compactness: parseFloat(relcomp.value),
    wall_area: parseFloat(wallarea.value),
    roof_area: parseFloat(roofarea.value),
    overall_height: height,
    orientation: orientation,
    glazing_area: parseFloat(glazingarea),
    glazing_area_distribution: glazingareadist
        
  },function(data, status) {
    console.log(data.estimated_cooling_load);

    if (data && data.estimated_cooling_load !== undefined && data.estimated_cooling_load !== null) {
      estCL.innerHTML = "<h2>" + data.estimated_cooling_load.toString() + "yay</h2>";
    } else {
      // Use a default value when data.estimated_heating_load is null
      var defaultValue = "20.5";
      estCL.innerHTML = "<h2>" + defaultValue + "</h2>";
    }
    console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/hello";
}

window.onload= onPageLoad;




