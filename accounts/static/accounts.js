var initialize = function(navigator, user, token, urls) {	
    $('#id_login').on('click', function(){
	    navigator.id.request();
	});
    var watch_args = {
	loggedInUser: user, 
	onlogin: function (assertion){
	    $.post(urls.login, {
		    assertion: assertion, 
		    csrfmiddlewaretoken: token
		}).fail(function(){navigator.id.logout();}).done(function(){window.location.reload();});
	},
	onlogout: function(){},
    };
    navigator.id.watch(watch_args);
};

window.Superlists = {
    Accounts: {
	initialize: initialize,
    }
};