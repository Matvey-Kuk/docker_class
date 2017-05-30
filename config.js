// # Ghost Configuration
// Setup your Ghost install for various [environments](http://support.ghost.org/config/#about-environments).

// Ghost runs in `development` mode by default. Full documentation can be found at http://support.ghost.org/config/

var path = require('path'),
    config;

config = {
    production: {
        url: 'http://0.0.0.0:8080',
        database: {
            client: 'mysql',
            connection: {
                host     : 'blog_mysql',
                user     : 'myuser',
                password : 'secret',
                database : 'blog',
                charset  : 'utf8'
            },
            debug: false
        },
        server: {
            host: '0.0.0.0',
            port: '2368'
        },
        logging: false,
        paths: {
            contentPath: path.join(process.env.GHOST_CONTENT, '/')
        }
    },

};

module.exports = config;
