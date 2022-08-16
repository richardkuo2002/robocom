function check(location){
    Swal.fire({
        title: "操作確認",
        text: "是否前往 輸送帶"+location,
        showCancelButton: true
    }).then(function(result) {
        if (result.value) {
            window.location = "../move/"+location;
        }
        else {
            window.location = "../choose";
        }
    });
};

function checkDock(){
    Swal.fire({
        title: "操作確認",
        text: "是否回送",
        showCancelButton: true
    }).then(function(result) {
        if (result.value) {
            window.location = "../move/"+"回送";
        }
        else {
            window.location = "../choose";
        }
    });
};

function report(){
    Swal.fire({
        title: "操作確認",
        text: "是否回報問題",
        showCancelButton: true
    }).then(function(result) {
        if (result.value) {
            window.location = "../report";
        }
        else {
            window.location.reload();
        }
    });
}
