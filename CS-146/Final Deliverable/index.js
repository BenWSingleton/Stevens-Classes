
var imgSrc = ["Images/checkout.png","Images/coolers.png","Images/seating.png"];
var imgIndex = -1;
$(document).ready(docEvents());

//primary function
function docEvents(){
    navbarHoverHandler();
    window.setInterval(dynamicImage,7000);
    grubhubHandler();
    formHandler();
    miniMenuHandler();
    $(window).resize(menuExpansionFix());
}

//Deselects the active menu button when the menu is hovered over
function navbarHoverHandler(){
    $('.nav_btn').hover(function(){
        $('#active').removeClass("active");
    },function() {
        $('#active').addClass("active");
    });
}

//Handles the fading between images on index.html
function dynamicImage(){
    if(imgIndex === 2){
        imgIndex = -1
    }
    $('.index_img').fadeTo(1000,0, function(){
       $(this).attr('src', imgSrc[imgIndex]);
       $(this).on('load', function(){
           $(this).fadeTo(1000,1);
       })
    });
    imgIndex++;
}

//Redirects to grubhub.com when grubhub image is pressed
function grubhubHandler(){
    $('#grubhub').click(function(){
        window.location.href = 'https://grubhub.com';
    });
    $('#grubhubApp').click(function(){
        window.location.href = 'https://grubhub.com/mobile_home';
    });
}

//Makes the submit button on contact.html do something
function formHandler(){
    $('#submit').click(function(){
       $('#form_head').text("Thanks for the feedback!");
    });
}

//Handles the collapsing of the menu in the phone view
function miniMenuHandler(){

        $('.menu_head').click(function () {
            if($('.padding').css("height") === "10px") {
                if ($('#' + $(this).text().replace(/\s/g, '').replace(/\?/g, '')).css("display") === "none") {
                    $('#' + $(this).text().replace(/\s/g, '').replace(/\?/g, '')).css("display", "table-row-group");
                } else {
                    $('#' + $(this).text().replace(/\s/g, '').replace(/\?/g, '')).css("display", "none");
                }
            }
        });
}
//Fixes display css on menu when you expand from phone to tablet
function menuExpansionFix(){
    if(window.innerWidth > 502){
        $('.menu_fold').forEach($(this).css("display", "table-row-group"));
    }
}