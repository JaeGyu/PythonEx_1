module.exports = (sequelize, DataType) => {
    return sequelize.define('comment', {
        comment: {
            type: DataType.STRING(100),
            allowNull: false,
        },
        created_at: {
            type: DataType.DATE,
            allowNull: true,
            defaultValue: sequelize.literal('now()'),
        }
    }, {
            timestamps: false
        });
};