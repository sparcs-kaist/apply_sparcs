const gulp = require('gulp');
const sass        = require('gulp-sass');
const rename      = require('gulp-rename');
const browserSync = require('browser-sync');

const config = require('../config');
//const tasks = require('./lib/sassPipes');
// TODO: 폴더에 빌드할 sass들

function compileSass() {
  return gulp
    .src(config.sass.src)
    // .pipe(tasks.dev());
    .pipe(sass().on('error', sass.logError))
    // .pipe(rename({
    //   dirname: '.'
    // }))
    .pipe(gulp.dest(config.sass.dest))
    .pipe(browserSync.stream())
}

gulp.task('sass', compileSass)
module.exports = compileSass;
