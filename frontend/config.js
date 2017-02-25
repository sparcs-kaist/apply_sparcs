const path = require('path');

const config = {
  'src': 'web',
  'dest': 'dist'
}

config['sass'] = {
  src : path.join(config.src, '**/*.{scss,sass,css}'),
  dest: path.join(config.dest, 'css'),
  folders: {
    vendor: './web/index.scss'
  },
}

config['browserSync'] = {
  port: 3000,
}

module.exports = config;
