module.exports = function(app) {

    app.get('*', function(req, res) {
        res.sendfile('./client/pages/index.html'); // load our index page
    });

};