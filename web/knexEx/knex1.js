const knexConfig = {
    client: 'mysql',
    connection: {
        host: '35.221.77.159',
        user: 'nodejs9',
        password: 'nodejs9',
        database: 'nodejs9',
        charset: 'utf8'
    },
    debug: true,
    pool: {
        max: 10
    },
    acquireConnectionTimeout: 60000
};

const knex = require('knex')(knexConfig);

knex.raw('select * from domains').then((resp) => {
    console.log(resp);
}
).catch((err) => {
    console.log(err);
}
);