/**
 * django 실행의 간단한 gulp wrapping 입니다.
 */

const gulp = require('gulp');
const spawn = require('child_process').spawn;

function runserver(cb) {
  // var run = exec('python ../manage.py runserver --settings=apply_sparcs.ui_dev.settings');
  var run = spawn('python', [
    "../manage.py",
    "runserver",
    "--settings=apply_sparcs.ui_dev.settings"
  ], {stdio: 'inherit' });

  // run.stdout.on('data', (data) => {
  //   console.log(`stdout: ${data}`);
  // });
  //
  // run.stderr.on('data', (data) => {
  //   console.log(`django log: ${data}`);
  // });

  run.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });

  cb() // django가 완전히 실행됐는지를 체크할 방법을 찾지 못했다. 비동기로 실행시킨후 적당히 딜레이 후에 browsersync를 실행하도록한다.
}

gulp.task('runserver', runserver);

module.exports = runserver;
