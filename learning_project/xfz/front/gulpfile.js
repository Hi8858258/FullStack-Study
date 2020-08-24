var gulp = require("gulp");
var cssnano = require("gulp-cssnano");
var rename = require("gulp-rename");
var uglify = require("gulp-uglify");
var concat = require("gulp-concat");
var imagemin = require("gulp-imagemin");
// var watch = require("gulp-watch");
var bs = require("browser-sync").create();
//var watch = require("gulp-watch");
//先定义常用的路径
var path = {
    'html':'./templates/**/',
    'css':'./src/css/',
    'js':'./src/js/',
    'images':'./src/images/',
    'css_dist':'./dist/css/',
    'js_dist':'./dist/js/',
    'images_dist':'./dist/images/',
};

//定义css压缩任务
gulp.task('css',function(done){
    gulp.src(path.css+'*.css')
        .pipe(cssnano())
        .pipe(rename({"suffix":".min"}))
        .pipe(gulp.dest(path.css_dist))
        .pipe(bs.stream());
    done();
});

//定义js压缩任务
gulp.task('js',function(done){
    gulp.src(path.js+"*.js")
        .pipe(uglify())
        .pipe(rename({"suffix":".min"}))
        .pipe(gulp.dest(path.js_dist))
        .pipe(bs.stream());
    done();
});

//定义处理图片的任务
gulp.task('images',function(done){
    gulp.src(path.images+"*.*")
        .pipe(cache(imagemin()))
        .pipe(gulp.dest(path.images_dist))
        .pipe(bs.stream());
    done();
});

//处理html文件的任务
gulp.task("html",function(done){
    gulp.src(path.html+"*.html")
        .pipe(bs.stream());
    done();
});

//定义监听文件的修改
gulp.task("watched",function(){
    gulp.watch(path.html+"*.html",gulp.series('html'));
    gulp.watch(path.css+"*.css",gulp.series('css'));
    gulp.watch(path.js+"*.js",gulp.series('js'));
    gulp.watch(path.images+"*.*",gulp.series('images'));
});

//初始监听浏览器任务
gulp.task("bs",function(){
    bs.init({
        'server':{
            'baseDir':'./'
        }
    });
});

//创建一个默认的任务，在cmd中的命令只需要输入gulp，就会执行bs和watch
gulp.task("default",gulp.parallel('bs','watched'));