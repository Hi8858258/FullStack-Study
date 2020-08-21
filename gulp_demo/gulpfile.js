var gulp = require("gulp");
var cssnano = require("gulp-cssnano");
var rename = require("gulp-rename");
var uglify = require("gulp-uglify");

//定义一个处理css文件改动的任务
gulp.task("css",function(){
    gulp.src("./css/*.css")
    .pipe(cssnano())
    .pipe(rename({"suffix":".min"}))
    .pipe(gulp.dest("./dist/css/"))
});

gulp.task("script",function(){
    gulp.src("./js/*.js")
    .pipe(uglify())
    .pipe(rename({"suffix":".min"}))
    .pipe(gulp.dest("./dist/js/"))
})