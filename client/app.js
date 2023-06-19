 


function onPageLoad(){
    console.log("document loaded");
    var url ="http://127.0.0.1:5000/get_state_names";
    $.get(url,function(data,status){
        console.log("got response for get_state_names request");
        if(data){
            var States=data.state;
            var uiStates=document.getElementById("uiState");
            $('#uiStates').empty();
            for(var i in States){
                var opt=new Option(States[i]);
                $('#uiState').append(opt);

            }
        
                
        }                       
        
    });

    
    
    

    /*console.log("document loaded");
    var url ="http://127.0.0.1:5000/get_soil_names";
    $.get(url,function(data,status){
        console.log("got response for get_state_names request");
        if(data){
            var Soil=data.soil;
            var uiSoil=document.getElementById("uiSoil");
            $('#uiSoil').empty();
            for(var i in Soil){
                var opt=new Option(Soil[i]);
                $('#uiSoil').append(opt);

            }
        
                
        }
        
    });*/
    
    
}
    function onClickedPredictCrop() {                                                     
        console.log("Predict Crop button Pressed");
        var State=document.getElementById('uiState');
        var Rainfall=document.getElementById('uiRainfall');
        var Season=document.getElementById('uiSeason');
        var Soil=document.getElementById('uiSoil');
        var Precrop=document.getElementById('uiPredictCrop');

        var url="https//127.0.0.1:5000/predict_crop";
    

        $.post(url,{
            State: State.value,
            Rainfall: parseInt(Rainfall.value),
            Season: Season.value,
            Soil: Soil.value
        
    },  function(data,status){
        console.log("Predict Crop button Pressed222")
            console.log(data.predict_crop);
            Precrop.innerHTML="<h2>" + data.predict_crop.toString() + "</h2>";
            console.log(status);
    })
}


window.onload = onPageLoad; 

