// node dependency
const path = require('path');

// gulp dependency
const gulp = require('gulp');
const watch = require('gulp-watch');

// other tasks
const sassTask = require('./sass');

// config
const config = require('../config');

function watchTask() {
  watch(config.sass.src, function () {
    sassTask();
  })
  // gulp.watch(config.sass.src, ['sass']);
    // .pipe(sassTasks.dev());
  // gulp.watch(`${paths.root}/**/*.html`, ['html']);
  // gulp.watch(`${paths.data}/**/*`, ['html']);
}

gulp.task('watch', watchTask);
module.exports = watchTask;
