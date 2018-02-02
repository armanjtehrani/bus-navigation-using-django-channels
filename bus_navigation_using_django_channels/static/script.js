var myCenter = new google.maps.LatLng(35.746031, 51.513406);


var mapProp = {
   center:myCenter,
   zoom:13,
   mapTypeId:google.maps.MapTypeId.ROADMAP
};


var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);

main_dict = {
	"Resalat": [],
	"Hengam": [],
	"Bagheri": [],
	"EmamAliHW": [],
};

 // show station
function show_station(x_pos, y_pos, line_name, station_info){
	console.log("line: in show", line_name);
	var color ;
	if (line_name =="Resalat"){
			color = "#000000";
		}
	if (line_name == "Bagheri"){
			color = "#fa7921";
		}
	if (line_name == "Hengam"){
			color = "#2900ff"
		}




	//map = loadMap();

	var station = new google.maps.LatLng(x_pos, y_pos);


	var marker = new google.maps.Circle({
	   center:station,
	   radius:40,

	   strokeColor:color,
	   strokeOpacity:1,
	   strokeWeight:5,

	   fillColor:color,
	   fillOpacity:0

	});

	marker.setMap(map);
	main_dict[line_name].push(marker);
	var infowindow = new google.maps.InfoWindow({
	   content: station_info,
	   position : station

	});


	google.maps.event.addListener(marker, 'click', function() {
	   infowindow.open(map,marker);
	});
	}


//Show Buses

function show_buses(x_pos, y_pos, line_name, station_info){
	var color ;
	if (line_name =="Resalat"){
			color = "#000000";
		}
	if (line_name == "Bagheri"){
			color = "#fa7921";
		}
	if (line_name == "Hengam"){
			color = "#2900ff"
		}




	//map = loadMap();

	var station = new google.maps.LatLng(x_pos, y_pos);


	var marker = new google.maps.Circle({
	   center:station,
	   radius:30,

	   strokeColor:color,
	   strokeOpacity:1,
	   strokeWeight:1,

	   fillColor:color,
	   fillOpacity:1

	});

	marker.setMap(map);
	main_dict[line_name].push(marker);
	var infowindow = new google.maps.InfoWindow({
	   content: station_info,
	   position : station

	});


	google.maps.event.addListener(marker, 'click', function() {
	   infowindow.open(map,marker);
	});
	}



var added = {Resalat : undefined,Bagheri : false,EmamAliHW : false,Hengam: false };
function toggleCheckbox(toggle){
	var isChecked ;// $(toggle).is(':checked');
	var req_obj = {"add":[],"discard":[]};

	//console.log(toggle.value, toggle.checked);
	if (toggle.value == "Resalat"){
		if (toggle.checked == false){
				added[Resalat] = false;
				req_obj["discard"].push("Resalat");
			}

		else {
			added[Resalat] = true;
			req_obj["add"].push("Resalat");

			console.log(req_obj);
			}
		console.log("Resalat", added[Resalat]);
	}

	if (toggle.value == "Bagheri"){
		if (toggle.checked == false){
				added[Bagheri] = false;
				req_obj["discard"].push("Bagheri");
			}
		else {
			added[Bagheri] = true;
			req_obj["add"].push("Bagheri");
			}
		console.log("Bagheri", added[Bagheri]);
		}

	if (toggle.value == "Hengam"){
		if (toggle.checked == false){
				added[Hengam] = false;
				req_obj["discard"].push("Hengam");
			}
		else {
			added[Hengam] = true;
			req_obj["add"].push("Hengam");

			}
		console.log("Hengam", added[Hengam]);
		}
	if (toggle.value == "EmamAliHW"){
		if (toggle.checked == false){
				added[EmamAliHW] = false;
				req_obj["discard"].push("EmamAliHW");
			}
		else {
			added[EmamAliHW] = true;
			req_obj["add"].push("EmamAliHW");
			}
		console.log("EmamAliHW", added[EmamAliHW]);
		}

	ws.send(JSON.stringify(req_obj));


}

//WS REQ

var ws = new WebSocket("ws://127.0.0.1:8000/customers/");
ws.onmessage = function(e){
	//console.log(JSON.parse(e.data));
	var resp_lines = JSON.parse(e.data);
	var added_lines = resp_lines["add"];
	var dis_lines = resp_lines["discard"];
	dis_recv_line__(dis_lines);
	show_recv_stations__(added_lines);
	show_recv_buses__(added_lines);

};



function dis_recv_line__(dis_list){
	console.log("dis list", dis_list);
	var stations ;
	for(i=0; i<dis_list.length ; i++){
		var line_name = dis_list[i]["name"];
		var markers = main_dict[line_name];
		for(var i = 0;i < markers.length; i++){
			marker = markers[i]
			marker.setMap(null);
		}
		main_dict[line_name] = [];
	}

}


function show_recv_stations__(add_list){
		for(var i = 0; i < add_list.length; i++)
			add_list[i]["name"] = add_list[i]["line"]["name"];
		dis_recv_line__(add_list);
		var stations ;
		for(i=0; i<add_list.length ; i++){
			console.log("i");

			var line_name = add_list[i]["line"]["name"];
			var line_id	=   add_list[i]["line"]["id"];


					for(k=0; k<add_list[i]["stations"].length ; k++){
						console.log("k")

						var station_name = add_list[i]["stations"][k]["name"];
						var station_line = add_list[i]["stations"][k]["line"];
						var y_pos = add_list[i]["stations"][k]["y_pos"];
						var x_pos = add_list[i]["stations"][k]["x_pos"];


						show_station(x_pos, y_pos, line_name, station_name+"\n"+line_name );


					}
			}
	}



function show_recv_buses__(add_list){
	var stations ;
	for(i=0; i<add_list.length ; i++){
		console.log("i");

		var line_name = add_list[i]["line"]["name"];
		var line_id	=   add_list[i]["line"]["id"];


		for(k=0; k<add_list[i]["buses"].length ; k++){
			var y_pos = add_list[i]["buses"][k]["y_pos"];
			var x_pos = add_list[i]["buses"][k]["x_pos"];

			show_buses(x_pos, y_pos, line_name, "line: " + line_name );


		}
	}
}




