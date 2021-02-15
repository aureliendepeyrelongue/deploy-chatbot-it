// requires Jquery

function targetIsSameLocation(targetLocation) {
    if (targetLocation == null) throw "Error null location passed in parameters";
    return targetLocation.split("#")[0] == window.location.href.split("#")[0];
}
document.addEventListener("DOMContentLoaded", function() {
    var destination = "";
    var preventDepartureModal = M.Modal.getInstance(
        document.getElementById("modal-prevent-departure")
    );
    document
        .getElementById("modal-quit-chatbot-button")
        .addEventListener("click", function(e) {
            try {
                var sameLocationTest = targetIsSameLocation(destination);
                if (destination != "" && !sameLocationTest) {
                    e.stopPropagation();
                    e.preventDefault();
                    axios
                        .get("/chatbot/end_chat?was_helpfull=no")
                        .then((response) => {
                            window.location.assign(destination);
                        })
                        .catch((err) => {
                            alert("Error no internet connexion");
                        });
                } else if (sameLocationTest) {
                    destination = "";
                }
            } catch (err) {
                console.trace(err);
            }
        });

    document
        .getElementById("modal-cancel-chatbot-button")
        .addEventListener("click", function() {
            destination = "";
        });

    var links = document.querySelectorAll("a:not(.modal-link-click-exception)");
    links.forEach((link) => {
        link.addEventListener("click", function(e) {
            e.preventDefault();
            destination = e.target.href;
            preventDepartureModal.open();
        });
    });
});