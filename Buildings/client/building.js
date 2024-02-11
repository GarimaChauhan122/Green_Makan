function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_facility_type";
    $.get(url,function(data, status) {
        console.log("got response for get_facility_type request");
        if(data) {
            var facility_type = data.facility_type;
            var uifacilitytype = document.getElementById("uifacilitytype");
            $('#uifacilitytype').empty();
            for(var i in facility_type) {
                var opt = new Option(facility_type[i]);
                $('#uifacilitytype').append(opt);
            }
        }
    });
  }

window.onload= onPageLoad;