
    function predictObesity() {
        var formData = {
            "Gender": document.getElementById("gender").value,
            "Height": parseFloat(document.getElementById("height").value),
            "Weight": parseFloat(document.getElementById("weight").value),
            "family_history_with_overweight": document.getElementById("family-obesity-history").value,
            "FAVC": document.getElementById("favc").value,
            "FCVC": parseFloat(document.getElementById("fcvc").value),
            "NCP": parseFloat(document.getElementById("ncp").value),
            "CAEC": document.getElementById("caec").value,
            "SMOKE": document.getElementById("smoke").value,
            "CH2O": parseFloat(document.getElementById("ch2o").value),
            "FAF": parseFloat(document.getElementById("faf").value),
            "TUE": parseFloat(document.getElementById("tue").value),
            "MTRANS": document.getElementById("mtrans").value
        };

    
        fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerHTML = "Predicted obesity level: " + data.prediction;
        })
        .catch(error => console.error('Error:', error));
    }

