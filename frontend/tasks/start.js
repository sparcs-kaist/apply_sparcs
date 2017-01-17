const gulp = require('gulp');
const runSequence = require('run-sequence');

gulp.task('start', ['start:UI'])
gulp.task('start:UI', () => {
  runSequence(
    'runserver', // 서버가 먼저 켜져야 뒤의 browserSync가 바로 잘 작동한다.
    'clean',
    'build', [
      'browserSync',
      'watch',
    ])
})
