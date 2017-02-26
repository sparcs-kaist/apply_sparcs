const gulp = require('gulp');
const watch = require('gulp-watch');
const browserSync = require('browser-sync');
const reload = browserSync.reload;
const path = require('path');
const config = require('../config');

function browserSyncTask () {
  browserSync.init({
    open: false,
    port: config.browserSync.port,
    proxy: 'localhost:8000',
    browser: 'google chrome',
    notify: {
      styles: {
        left: 0,
        right: "auto",
        bottom: 0,
        top: "auto"
      }
    },
  })
  // gulp.watch(paths.copy, ['copy']);
  gulp.watch(path.join(config.src, '/**/*.html')).on('change', reload);
}

gulp.task('browserSync', browserSyncTask);
module.exports = browserSyncTask;
