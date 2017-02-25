const gulp = require('gulp');
const run = require('run-sequence');

function build(done) {
  run('clean', ['sass'], done);
}

gulp.task('build', build);
module.export = build;
