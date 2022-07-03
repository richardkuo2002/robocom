function check(location){
    Swal.fire({
        title: "操作確認",
        text: "是否前往"+location,
        showCancelButton: true
    }).then(function(result) {
        if (result.value) {
            window.location = "sign.html";
        }
        else {
            window.location = "choose.html";
        }
    });
};
