/**Created by sparky on 3/21/15.*/

module.exports = function(grunt) {

    //noinspection GjsLint
    grunt.initConfig({
        less: {
            app: {
                files: { "css/main.css": "less/main.less" }
            }
        },
        qunit: {
            all: ['form_validation/js/tests/*.html']
        }
    });
    grunt.loadNpmTasks("grunt-contrib-less");
    grunt.loadNpmTasks('grunt-contrib-qunit');
};
