const gulp = require('gulp');
const del = require('del');
const config = require('../config');

function cleanDest() {
  return del([config.dest + "/css"]);
}

gulp.task('clean', cleanDest);
module.exports = cleanDest;
