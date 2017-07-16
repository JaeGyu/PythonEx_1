function findAndSaveUser(Users) {
    Users.findOne({}, (err, user) => {
        if (err) {
            return console.error(err);
        }
    });
}