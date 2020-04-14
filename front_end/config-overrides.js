const BundleTracker = require('webpack-bundle-tracker');
const path = require('path');
const webpack = require('webpack');

if (process.env.NODE_ENV !== "development") {
  module.exports = {
    webpack: (config, env) => {
      config.plugins.push(
          new BundleTracker({
            path: __dirname,
            filename: './config/webpack-stats.json',
          })
      );
      config.output["publicPath"] = process.env.PUBLIC_PATH;
      config.optimization.splitChunks.name = 'vendors';

      return config;
    },
  }
} else {
  module.exports = {
    webpack: (config, env) => {
      config.plugins.push(
          new BundleTracker({
            path: __dirname,
            filename: './config/webpack-stats.json',
          }),
      );
      config.entry = [
        'webpack-dev-server/client?' + process.env.PUBLIC_PATH,
        'webpack/hot/dev-server',
        './src/index'
      ];
      config.output["publicPath"] = process.env.PUBLIC_PATH;
      config.optimization.splitChunks.name = 'vendors';

      return config;
    },
    devServer: function (configFunction) {
      return function (proxy, allowedHost) {
        const config = configFunction(proxy, allowedHost);
        config.headers = {
          'Access-Control-Allow-Origin': '*'
        };
        config.hot = true;
        config.public = process.env.PUBLIC_PATH;

        return config;
      };
    },
    paths: function (paths, env) {
      console.log(path.resolve(__dirname, 'src'));
      paths.appIndexJs = path.resolve(__dirname, 'src/index.js');
      paths.appSrc = path.resolve(__dirname, 'src');
      return paths;
    },
  };
}
// ' + paths.serverHostname + '