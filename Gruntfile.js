/**Created by sparky on 3/21/15.*/

module.exports = function(grunt) {

    grunt.initConfig({
        less: {
            app: {
                files: { "css/main.css": "less/main.less" }
            }
        },
        qunit: {
            // configuration here
        }

    });
    grunt.loadNpmTasks("grunt-contrib-less");
};
